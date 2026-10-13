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

**With a skill.** Install `skills/workmethod-md` in your assistant:

- Claude Code: `/plugin marketplace add seampoint/workmethod.md`, then `/plugin install workmethod-md@workmethod-md`.
- Claude apps: upload the `skills/workmethod-md` folder as a zip under Customize, then Skills.
- Microsoft 365 Copilot Cowork: upload the zip under Customize, then Skills.
- Codex and ChatGPT: install the skill folder, or the plugin from this repository's marketplace.

**With AGENTS.md.** A tool that reads AGENTS.md can follow the same rules with one line:

```
Follow WORKMETHOD.md files as described at https://github.com/seampoint/workmethod.md/blob/main/spec/workmethod.md
```

Then copy the template into the folder it governs, name the copy `WORKMETHOD.md`, and fill it in.

## Applications

Anything that reads the files can build on them: a view of what needs one person's attention, a review of whether reserved decisions reached the right people, a comparison of assistants working under the same methods. [Seampoint Workbench](https://seampoint.com) is one.

## Versions

The specification and the skill share a version, in [`VERSION`](VERSION). This is 1.0.0, a working draft.

## License

Apache License 2.0; see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). The template is CC0. Method files and records you write are yours. See [`TRADEMARKS.md`](TRADEMARKS.md) for names.
