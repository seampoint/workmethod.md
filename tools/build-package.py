"""Build reproducible standalone skill and Claude plugin ZIPs; never install or send."""
from pathlib import Path
import hashlib, json, zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT/'VERSION').read_text().strip()
OUT = ROOT/'dist'
OUT.mkdir(exist_ok=True)
skill = ROOT/'skills/workmethod-md'
skill_files = sorted(p for p in skill.rglob('*') if p.is_file())
plugin_files = [ROOT/p for p in [
    '.claude-plugin/plugin.json', 'plugin.json', 'VERSION', 'LICENSE', 'NOTICE']]+skill_files

def make(name, files, base):
    path=OUT/name
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(files):
            info=zipfile.ZipInfo(str(p.relative_to(base)),date_time=(2026,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644 << 16
            z.writestr(info,p.read_bytes())
    with zipfile.ZipFile(path) as z:
        for p in files:assert z.read(str(p.relative_to(base)))==p.read_bytes()
    return {'file':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'bytes':path.stat().st_size,'entries':len(files)}

result={'package_version':VERSION,'format_status':'WORKMETHOD.md 1.0 working draft',
        'artifacts':[make(f'workmethod-md-{VERSION}-skill.zip',skill_files,skill.parent),
                     make(f'workmethod-md-{VERSION}-claude.zip',plugin_files,ROOT)]}
(OUT/'checksums.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
