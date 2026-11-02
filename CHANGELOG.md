# Changes

## 1.2.0 working-draft rules (proposed)

- Number rules and keep each number for as long as the rule exists, so overrides, entries and reviews can cite `<method name> rule <n>` reliably.
- Let a rule carry its reason (`Because:`) and what it rests on (`Rests on:`). A reason helps a person apply a rule to a case it did not foresee; it never sets the rule aside. A good reason names what goes wrong if the rule is not followed: the work fails, someone is harmed, or the work gets harder.
- Add fixed rules (`Fixed:`). Methods below may add to a fixed rule or make it stricter, never replace or loosen it. A reader that finds a conflict follows the fixed rule and tells the user. This narrows the nearest-method-wins rule for thresholds and limits that a team or project must not relax.
- Add an optional `Rule` field naming the rule an entry applied or departed from, written only when the act clearly turned on that rule.
- Add rule reviews to the applications in section 7.
- Readers that ignore `Rule` still read every entry. `Fixed:` changes precedence: a reader that does not know it applies nearest-method-wins and follows a nearer rule that loosens a fixed rule. A method owner cannot rely on a fixed rule until the assistants reading that tree implement this draft.
- A nearer rule counts as stricter only when every act it allows, the fixed rule also allows. Following a fixed rule over a conflicting nearer rule is recorded as a note, not as a departure.
- A removed rule keeps its line as `Removed in v<number>.` Skipping the number is not allowed, because rendered Markdown renumbers the list.
- Package version numbers are unchanged until release.

## 1.1.1 working-draft alignment patch

- Label the format the WORKMETHOD.md 1.1 working draft, since 1.1.0 added the optional Window, Resurface and Same as fields.
- Bring the open-items procedure into line with the specification on joins: a join is one step, a join to a label not in the folder or to the entry's own label is ignored and reported, and chains and loops are never followed.
- Say in the skill that only the method's owner or a person the method names closes a proposal or correction.
- Say where optional fields go: after Method, in the order Window, Resurface, Same as, then any extension fields.
- When a declared record extension is unknown and the method asks for it, add a note entry saying so.
- The specification's fields and rules, the entry format and the examples are unchanged.

## 1.1.0 working-draft record fields

- Add optional Window, Resurface, and Same as fields so a span, a raise day, and a second label can be recorded without editing an earlier entry.
- A decision closes a proposal or correction only when it is dated at or after that entry.
- Teach readers and the open-items procedure to use the fields. This package does not define an attention product.
- A Same as join is one step: chains, loops and joins to a label not in the folder are ignored and reported.
- A writer never gives a proposal or correction the same Date as a decision it follows.
- Minor version: new optional record fields are a format addition. Readers that ignore them still read every entry.

## 1.0.2 working-draft packaging patch

- Rename the standalone attribution file to NOTICE.txt without changing its contents, and reject unsupported or hidden resource filenames in source checks.
- Package the standalone skill inside one workmethod-md folder for native Claude uploads.
- Keep instruction behavior and the WORKMETHOD.md working-draft format unchanged. Claude web native import, file operations and the independent snapshot audit completed in one isolated trial; behavioral gaps remain as documented in docs/qualification.md. Previously released assets remain unchanged.

## 1.0.1 publication candidate

- Distinguish package version from working-draft format status and remove the universal vendor-retention assurance.
- Align reader recognition with compatible two-line headers while requiring all three header lines for newly written methods.
- Align owner-controlled method changes: no autonomous edits, exact confirmation, versioning, readback and recording.
- Clarify item-level labels, the Due exception for changed commitments, coverage disclosures, canonical destinations, host-memory conflicts and unavailable practices.
- Include standalone NOTICE attribution and explicit qualification/known-limit documentation.
- Preserve the example method and record contents. No new Resurface field, cross-tree join or automatic CRM activation is introduced.

## 1.0.0 private draft

Initial specification, standalone skill, starter template, fictional examples and plugin manifests. Subsequent private refactoring split procedure references and clarified when record rules must be loaded.
