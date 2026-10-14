# Keep the record

Copyright Seampoint, LLC. Licensed under the Apache License 2.0; see [LICENSE.txt](../LICENSE.txt).

Never edit, rename or delete an entry file, yours or anyone's. To close, correct or withdraw something, create a new entry.

To add an entry, create a new file in the unit's `record/` folder:

- File name: `YYYY-MM-DD-<writer>-<short-slug>.md`, where `<writer>` is your own assistant name in lower case, or the person's name if you are recording something a person did on their instruction and they asked you to. The slug is two to five words from the Object. If a file with that name exists, add `-2`, `-3`.
- Content: these lines, in this order, one per line:

```
Date: YYYY-MM-DD HH:MM
Kind: commitment | decision | done | correction | proposal | change | pending | note
Actor: the named person, or your own assistant name if you did it
Object: what was acted on, in a few words, the same wording each time it is mentioned
Label: a short stable name for the thing this entry is about, lower case with hyphens, such as renewal-proposal-draft
Authority: the named person who approved it, or none
Due: YYYY-MM-DD for a commitment, otherwise -
Source: the file, meeting, email or conversation it came from, in words a person can follow
Method: every method in force on the path to this work, nearest first, each with its version and separated by semicolons, such as harbor-renewal v6; clients v3, or none if you found no method
```

Record extensions: if a method in force declares a record extension (a line such as `Record extension: <name>` in its "The record" section), add the fields that extension requires, where it says to put them. If another installed skill defines that extension, follow it. If you do not know the extension, write the lines above, and tell the user which extension's fields you could not add.

Rules for entries:

- Read the clock before you write the Date. Write it in local time on a 24-hour clock, for example `2026-10-06 14:20`, with nothing after it. If you do not know the user's time zone, ask.
- The first entry about a commitment, decision, proposal or correction sets its Label. Every later entry about the same thing (its `done`, a `change`, a further correction) reuses that Label exactly, so readers can join them.
- Before adding, list the `record/` folder and read the entries. If an entry already records the same act (same Kind and Label, same Actor, same thing done), do not add another. A later act about the same thing, such as a second decision, a further correction or a change, is a new entry with the same Label. If an entry describes the same thing under a different Label, reuse its Label rather than inventing a new one.
- Record who actually did the thing. If you drafted or sent something, you are the Actor, and the person who approved it is the Authority.
- Only a person decides. When you bring a decision to a person, record their answer as a `decision` entry: that person as Actor and Authority, the decision in the Object, and in Source who asked them, where and when. Record it whether they approve, change or refuse. Then record the act itself with that person as the Authority.
- Write Source so a person can find it: the file name, meeting, email subject or conversation and its date. Never use internal message, session or tool identifiers.
- Record a commitment only in the name of the person who made it, or in your own name for what you will do. When work waits on someone who has not agreed to do it, add a `pending` entry instead: the person waiting is the Actor, and the Object says whom they wait on, for what, and by when. If that person agrees, record their commitment then.
- A `done` entry repeats the Label of the commitment or pending entry it closes.
- When the user changes something you drafted, add a `change` entry: the user as Actor, what changed as Object, the reason in Source if given. A `change` entry about a commitment gives in Due the commitment's due date after the change; `-` means it no longer has one.
- When anyone tells you how work is done here (a correction, "always", "never"), add a `correction` entry in the unit you are working in, naming in the Object which method it concerns. Do not save it to your own memory. Tell the user the method's owner decides whether it becomes part of the method.
- New commitments and decisions from notes or conversation go in the record, not only in what you write for the user.
- If you cannot create files in the folder, say so and give the user the exact entry text.
