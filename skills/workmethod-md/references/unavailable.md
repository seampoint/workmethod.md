# When you can't do it from here

Copyright Seampoint, LLC. Licensed under the Apache License 2.0; see [LICENSE.txt](../LICENSE.txt).

When you cannot do the whole job:

1. Say in one sentence what you cannot do from here and why.
2. Offer the most useful step you can take that keeps the work moving, and wait for the user's yes before taking it, even when it seems the obvious next step.
3. Leave a trail. If part of the job has to wait for another place (the desktop app, Word, Excel, a person), add a `pending` entry: you are the Actor, the Object says exactly what is waiting and where any draft is saved, and the Label is set as usual. Whoever completes it adds a `done` entry with the same Label.

Typical cases:

- You cannot change an existing Word, Excel or PowerPoint file without losing its formatting: write the change as a new file beside it named `<file name>-pending-<label>.md`, saying exactly what to change and where, and add a `pending` entry so an assistant in Word or Excel, or a person, can apply it.
- You cannot find the folder: ask where the file is saved.
- You cannot reach the methods: offer to go ahead with the work marked "not checked against the method", or to wait.
- You cannot create files in the record: give the user the exact entry text.

A connector that cannot update a file in place is also a capability gap. Do not silently archive and recreate files. Use an applicable, explicitly approved method procedure or disclose the limitation and obtain authorization for the proposed fallback. Immutable record entries are never archive-and-replace candidates.

When an applicable method requires a missing skill or practice, identify the exact unavailable step. Use a permitted manual procedure only when one is available and authorized. Follow this handoff procedure for the rest; never claim the missing maintenance ran. A successfully saved canonical entry remains saved even if later derived maintenance fails. Report that distinction and any stale derived file.

## When no one can answer

If no person can answer during this run, directly or through the assistant that asked for the work, as in a scheduled run, the steps above do not apply and you make no offer. If you cannot tell whether a person can answer, treat the run this way until one does.

- Take no fallback step of the kind step 2 describes, and no step that this skill, a method or the person who set up the run reserves for a person or says to confirm first. The exception is a step that the person it is reserved for, or where it names no one the person who set up the run, has already said yes to, in instructions that person gave the run or in a `decision` entry you can read; the yes covers the step as written there and no wider: a yes to one act covers it once, and a yes to a recurring act covers each time it names. If you cannot tell whether a step is one of these, whether a yes covers it, or whether a yes to one act has already been used, do not take the step.
- If you cannot read a method on the path to the work, or cannot list a folder on that path, do not do the work on that path.
- Write no entry, in `record/` or in a system a method designates in its place, and no `-pending-` file, because an unattended run must not write to a person's record without the person. The one exception: a method in force may allow an entry by a rule that says it applies to such runs. Name yourself as Actor, that method's owner as Authority and that rule in `Rule`, say in Source that a run with no one present wrote it, or carry the same facts in a system a method designates, and never write a `decision` or a withdrawal.
- In the run's own output, say what cannot be done and why, name exactly what waits and where, including any open `pending` entry about the work, and say what you did and anything else you would have recorded. If a method names a folder outside `record/` for that output, add a new file there for each run.

If you set up such a run, first say where its output will be kept and who will see it, or that the host keeps none, or that you cannot tell.

When you start work on a file and a method names such a folder, look there for reports about the file. When you read a run's report with a person present, in that folder or where the host keeps it, offer once to record what the person confirms. Date the entry when you write it, and name the run and when it acted in Source.
