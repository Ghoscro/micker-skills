# Diagnostic cases

| Input | Observation | Appropriate conclusion |
|---|---|---|
| UTF-8 JSON containing `{"title":"你好，世界"}` | `utf8: true`, `json_parse: ok` | The bytes and JSON structure are valid; compare the expected string or real display if corruption is reported. |
| The same JSON with a UTF-8 BOM | `bom_utf8: true`, JSON inspection succeeds | BOM is present; compatibility depends on the actual consumer. |
| GBK bytes containing `中文` | UTF-8 decode error | This input is not valid UTF-8; confirm intended encoding before converting a copy. |
| UTF-8 text `她娴熟地弹琴` | A marker may match `娴` | A marker alone does not establish corruption. |
| Malformed UTF-8 JSON `{"title":}` | Decode succeeds; JSON parse reports an error | The JSON syntax needs attention; encoding is a separate finding. |

The inspector leaves every input file unchanged. An omitted or missing input file produces an execution error; that is a failed inspection, not a healthy result.
