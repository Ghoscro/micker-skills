---
name: windows-utf8-mojibake-guard
description: Diagnose UTF-8, BOM, JSON parsing, and possible mojibake in Windows text files before editing. Use when Chinese text looks corrupted or patch anchors fail around non-ASCII text; distinguish file damage from terminal display problems.
license: MIT
metadata:
  version: "1.0.0"
  author: "Micker / Ghoscro and AI collaborators"
---

# Windows UTF-8 Guard

Inspect bytes before rewriting text that looks garbled. Terminal rendering, file encoding, and already-corrupted content are different problems.

Run the bundled read-only inspector from this skill directory:

```powershell
python -X utf8 scripts/inspect_text_encoding.py "path/to/document.json" --json
```

The script needs Python 3 and only its standard library. It prints encoding status, BOM, NUL-byte count, possible mojibake markers, a short content sample, and JSON parse results where relevant. Use local files appropriate to inspect; its output contains file paths and the first 240 characters. Review that output before sharing it elsewhere.

Its exit code describes command execution, not a pass/fail encoding verdict. Inspect the returned fields. Marker hits are clues: ordinary Chinese characters can match. Valid UTF-8 bytes can still encode already-garbled text.

Choose the next action from the evidence:

- If exact Unicode strings and file bytes are correct but the terminal is garbled, fix the display environment and leave the file intact.
- If a UTF-8 BOM is present, keep it unless the consuming format or tool requires otherwise. JSON inspection tolerates the BOM; actual consumers can differ.
- If UTF-8 decoding fails, identify the intended source encoding from project evidence. Do not guess a whole-file conversion from appearance alone.
- If text is already garbled, restore from a verified source or backup. Test any reversible transformation on a copy and a known sample first.

For an authorized repair, preserve the original, make the smallest edit, and force the intended encoding. PowerShell 7 supports UTF-8 without BOM; Windows PowerShell 5.1's `-Encoding utf8` writes a BOM. Python's `write_text(..., encoding="utf-8")` writes UTF-8 without BOM.

Verify the real consumer: parse JSON, compare known Unicode strings, or inspect the affected browser text. A successful decode alone proves only the byte encoding.

See [examples](references/examples.md) for diagnostic cases.

Created by Micker / Ghoscro as part of the Micker Method. Encoding concepts are standard knowledge; this package contributes a diagnostic workflow and a read-only inspector.

This is a public-safe version. Examples use mock data; private memory, user data, credentials, deployment details, and full automation loops are intentionally excluded.
