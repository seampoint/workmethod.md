# WORKMETHOD.md

A team's working rules, and its record of what it decided and promised, in plain files the team owns and any AI assistant can follow.

- **`WORKMETHOD.md`** sits in a folder and says how work is done there: who owns the rules, what the rules are, and which decisions belong to which people. It applies to that folder and everything below it. The nearest one wins, as with AGENTS.md.
- **`record/`** sits beside it and holds one small file per commitment, decision, correction, proposal, completion or hand-off. Entries are written once and never edited.

The assistant reads the methods from the top of the tree down, follows them, brings reserved decisions to the named person instead of making them, and writes the record. Change assistants and the rules and the record stay with you.

## What is here

| Path | What it is | License |
|---|---|---|
| [`spec/workmethod.md`](spec/workmethod.md) | The specification | Apache 2.0 |
| [`skills/workmethod-md/`](skills/workmethod-md/SKILL.md) | A skill that teaches an assistant to follow the specification | Apache 2.0 |
| [`templates/WORKMETHOD-template.md`](templates/WORKMETHOD-template.md) | A starting point for your first method | CC0 (public domain) |
| [`examples/`](examples/README.md) | A small working tree | Apache 2.0 |

## Use it

**With a skill.** The standalone package includes only workmethod-md. It does not install Workbench, its accelerator or checkpoint delivery.

For tested local source-bound use in Codex, explicitly ask it to read and apply `skills/workmethod-md/SKILL.md` from this checkout for the work folder you name. This direct-file route was checked in a fresh consumer task; it does not install a native plugin or qualify a marketplace. See the [qualification record](docs/qualification.md) for scope and limits.

Claude Code recognized the candidate plugin through its local loader, but its execution test was blocked by expired authentication. To load a local preview, start a new session from the folder holding the work:

```sh
claude --plugin-dir /absolute/path/to/workmethod.md
```

Invoke `/workmethod-md:workmethod-md` and ask it to read the selected work folder. This loads the plugin directly from its source directory; it does not install a marketplace copy. See [first use and test scope](docs/first-use.md) and the [qualification record](docs/qualification.md) before relying on a route.

After public-source installation has been verified, the intended marketplace route is:

```text
/plugin marketplace add seampoint/workmethod.md
/plugin install workmethod-md@workmethod-md
```

Other hosts may accept the standalone skill-folder ZIP. Those routes are unqualified here; this repository does not claim that uploading a skill proves its instruction-following, saves or updates. See [known limits](docs/known-limits.md).

**With AGENTS.md.** A tool that reads AGENTS.md can follow the same rules with one line:

```
Follow WORKMETHOD.md files as described at https://github.com/seampoint/workmethod.md/blob/main/spec/workmethod.md
```

Then copy the template into the folder it governs, name the copy `WORKMETHOD.md`, and fill it in.

## Applications

Anything that reads the files can build on them: a view of what needs one person's attention, a review of whether reserved decisions reached the right people, a comparison of assistants working under the same methods. [Seampoint Workbench](https://seampoint.com) is one.

## Versions

[`VERSION`](VERSION) identifies the skill package: 1.0.3. It implements the WORKMETHOD.md 1.0 working draft, which has not been ratified as stable. Package versioning does not promise stable format compatibility. See [changes](CHANGELOG.md) and [known limits](docs/known-limits.md). Pin the reviewed release or commit when using it as an engagement reference.

## License

Apache License 2.0; see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). The template is CC0. Method files and records you write are yours. See [`TRADEMARKS.md`](TRADEMARKS.md) for names.

## Maintainer and feedback

Seampoint, LLC maintains this draft. Report fictional minimal reproductions through [GitHub issues](https://github.com/seampoint/workmethod.md/issues); do not include private work files, personal data or credentials. Maintainer responsibility does not confer authority over a user's methods or create a support entitlement. Use a separately agreed service arrangement for paid assistance.

The standalone ZIP contains one `workmethod-md/` folder with `SKILL.md`, Markdown references, `LICENSE.txt` and `NOTICE.txt`. Use the standalone ZIP for a native skill uploader; the Claude plugin ZIP is a separate plugin layout. Native installation and behavioral qualification are distinct; see the qualification record before treating a host as supported.
