# Progressive Video Review / 视频渐进精读

Find the relevant moment in a video, then read the detail from the original frame.
Start with a numbered overview; spend image-reading effort where the question needs it.

[Skill entry](SKILL.md) · [Worked examples](references/examples.md) · [All skills](../../README.md)

## Try it

Copy this whole directory to your agent host's documented skill location, keeping
`references/` beside `SKILL.md`. Verify discovery in that host. For a first trial,
give the agent [SKILL.md](SKILL.md), the example file, and an accessible local video:

> Use video-progressive-review to find when the settings language changes in this
> recording. Start with a numbered contact sheet and timestamp mapping. Open it,
> inspect the relevant original frames, and report what changed and when.

## What happens

1. Build or reuse roughly 12 numbered overview frames with timestamps and a sheet ID.
2. Open the sheet through a real image-reading tool and select relevant tiles.
3. Extract 1–3 original-resolution frames; crop small text from those originals.
4. Inspect a denser interval if a click, transition, or brief event matters.
5. Return a timestamped answer with the inspected coverage and remaining gaps.

**Mock example:** tile 5 maps to 20 s and tile 6 to 25 s. Original frames show an
English settings screen at 20 s and Chinese at 25 s. These observations support
“changed between 20 and 25 s.” They leave the exact click time unresolved; a dense
sequence within that interval can narrow it.

## Inputs, tools, and limits

Provide the question, video or existing sheet, and access to the relevant images.
Your host needs extraction, contact-sheet assembly, and image-reading tools;
FFmpeg plus an image compositor is one possible setup. Tool commands depend on
your environment. This package includes a workflow and examples; it includes no
video CLI, downloader, or transcription service.

Sparse sampling leaves unsampled events unknown. Spoken words need a transcript
or audio; rhythm and music need audio evidence. Measure host usage before claiming
a percentage of token savings. The public package has local format/link checks and
independent mock-case review; automatic discovery and media execution in your host
need a real trial.

## 中文快速使用

适合长视频分析、录屏检查和小字读取。把本目录完整安装到宿主的技能目录，或将
入口与示例显式交给 Agent，再提供本地视频和问题：

> 用视频渐进精读看这段录屏：语言设置何时改变？先给编号拼图和时间映射，实际
> 打开拼图，再看相关原始高清帧，给出时间范围和依据。

顺序是总览拼图 → 定位编号 → 原视频高清帧 → 必要时密集帧 → 带时间的结论。
例如 20 秒为英文、25 秒为中文，只能先定位到这五秒范围。抽帧、拼图、看图工具
由使用者环境提供；本包附方法与虚构示例。音频结论需要音频证据，节省比例需要实测。

## Credit and license

Workflow designed and maintained by Micker / Ghoscro with AI collaborators.
Frame extraction and contact sheets are established techniques. Released under
the [MIT License](../../LICENSE); retain its notice when redistributing.
