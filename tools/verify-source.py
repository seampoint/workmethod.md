"""Read-only packaging/reference checks, not a semantic or host-conformance validator."""
from pathlib import Path
from urllib.parse import unquote
import hashlib,json,re,subprocess

ROOT=Path(__file__).resolve().parents[1]
version=(ROOT/'VERSION').read_text().strip()
assert re.fullmatch(r'\d+\.\d+\.\d+',version)
versions=[json.loads((ROOT/p).read_text())['version']
          for p in ['plugin.json','.claude-plugin/plugin.json']]
skill=(ROOT/'skills/workmethod-md/SKILL.md').read_text()
versions.append(re.search(r'version: "([^"]+)"',skill).group(1))
assert all(v==version for v in versions)
assert json.loads((ROOT/'plugin.json').read_text())['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
links=[]
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts or 'dist' in p.parts:continue
    text=p.read_text()
    for match in re.finditer(r'\[[^\]\n]*\]\(([^)]+)\)',text):
        value=match.group(1).strip('<>')
        if value.startswith(('http:','https:','mailto:','#')):continue
        target=p.parent/unquote(value.split('#')[0])
        assert target.exists(),f'{p}: {value}'
        links.append({'source':str(p.relative_to(ROOT)),'target':value})
for p in ROOT.rglob('*.json'):
    if '.git' not in p.parts and 'dist' not in p.parts:json.loads(p.read_text())
assert (ROOT/'LICENSE').read_bytes()==(ROOT/'skills/workmethod-md/LICENSE.txt').read_bytes()
assert (ROOT/'skills/workmethod-md/NOTICE.txt').is_file()
# The standalone upload contains only supported Markdown/plain-text resources.
# This is a packaging contract, not a claim that every host accepts the package.
skill_files=[p for p in (ROOT/'skills/workmethod-md').rglob('*') if p.is_file()]
for p in skill_files:
    relative=p.relative_to(ROOT/'skills/workmethod-md')
    assert all(not part.startswith('.') for part in relative.parts),f'Hidden skill path: {relative}'
    assert p.suffix.lower() in {'.md','.txt'},f'Unsupported standalone skill file type: {relative}'
    p.read_text(encoding='utf-8')
example_files=[]
for p in (ROOT/'examples').rglob('*'):
    if not p.is_file():continue
    path=str(p.relative_to(ROOT))
    original=subprocess.check_output(['git','show','8e5b23f:'+path],cwd=ROOT)
    assert p.read_bytes()==original,f'Example changed: {path}'
    example_files.append(path)
records=list((ROOT/'examples').glob('**/record/*.md'))
for p in records:
    lines=p.read_text().splitlines()
    assert len(lines)==9 and [l.split(':',1)[0] for l in lines]==[
        'Date','Kind','Actor','Object','Label','Authority','Due','Source','Method']
assert 'the only copy an assistant vendor holds' not in (ROOT/'spec/workmethod.md').read_text().lower()
print(json.dumps({'version':version,'relative_links':len(links),'links':links,
                  'example_files_unchanged':len(example_files),'example_records':len(records),
                  'skill_notice_present':True,'scope':'Static source/reference/byte checks only; no method example executed.'}))
