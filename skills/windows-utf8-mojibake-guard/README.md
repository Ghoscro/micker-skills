# Windows UTF-8 Guard / Windows 防乱码

Check the bytes before rewriting Chinese text that merely looks broken in a terminal.
Includes a read-only Python inspector and an agent diagnostic workflow.

[Skill entry](SKILL.md) · [Diagnostic examples](references/examples.md) · [All skills](../../README.md)

## Run the tool

Requires Python 3.10+ for this release's tested syntax; uses only the standard
library, with no extra packages. From this skill directory:

```powershell
python -X utf8 scripts/inspect_text_encoding.py "sample.json" --json
```

From the repository root:

```powershell
python -X utf8 skills/windows-utf8-mojibake-guard/scripts/inspect_text_encoding.py "sample.json" --json
```

You can pass several file paths before `--json`. Relative input paths are resolved
from your current working directory. Existing files are required; a missing or
unreadable file fails the invocation. Inspection leaves the inputs unchanged.

## Read the result

For a UTF-8 file containing `{"title":"你好，世界"}`, the relevant JSON fields are:

```json
{"utf8": true, "bom_utf8": false, "nul_bytes": 0, "markers": {}, "json_parse": "ok"}
```

This is an excerpt of one row; `--json` returns an array. Each full row also
contains `path`, `bytes`, `exists`, `sample`, and `error`.

| Field | Meaning |
|---|---|
| `utf8` / `error` | Whether the original bytes decode strictly as UTF-8, and a decode error if they fail |
| `bom_utf8` | Whether the file begins with the UTF-8 BOM |
| `nul_bytes` | Count of zero bytes; investigate whether the format expects them |
| `markers` | Heuristic character counts; ordinary Chinese can match |
| `json_parse` | Present for a UTF-8 `.json` file; inspection tolerates a leading BOM |
| `sample` | First 240 decoded characters, with newlines escaped; failed decoding uses replacement characters |

Exit code 0 means the command completed. A malformed JSON file or failed UTF-8
decode can still yield exit 0; inspect the fields. Valid UTF-8 can contain text
that was already corrupted earlier. Marker matches are clues, not a damage verdict.
The output reveals file paths and a short content sample; review it before sharing.

## Use the agent workflow

Copy this whole directory to your host's documented skill location, preserving
`scripts/` and `references/`, then verify discovery. Or provide the entry explicitly:

> Use windows-utf8-mojibake-guard to inspect sample.json. Compare the original bytes,
> known Chinese strings, and the actual consuming app. Explain the cause before
> making any edit; preserve an original copy for an authorized repair.

The workflow distinguishes display trouble, wrong source encoding, and existing
text damage. It checks the real consumer after a repair. It performs no automatic
conversion or recovery. PowerShell 5.1 and 7 differ in their UTF-8 BOM defaults.

## 中文快速使用

看到乱码先查字节，再查终端和实际应用。运行上面的命令即可，不需要额外依赖。
关注 `utf8`、BOM、零字节、JSON 解析和样本文字；退出码 0 只说明检查命令执行完成。
正常汉字也会命中启发式标记。工具只读输入，输出包含路径和前 240 个解码字符。
需要修复时保留原文件，先在副本验证转换，最后确认真实应用中的中文显示。

## Verification, credit, and license

Local black-box fixtures cover UTF-8 Chinese JSON, BOM JSON, GBK bytes, malformed
JSON, a legitimate Chinese marker match, empty text, NUL bytes, missing files,
and preservation of input bytes. Host-wide discovery and repair behavior depend
on your environment and need separate verification.

Diagnostic workflow and inspector by Micker / Ghoscro with AI collaborators;
encoding concepts are standard knowledge. [MIT License](../../LICENSE).
