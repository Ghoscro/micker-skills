# Micker Skills

Small, inspectable agent workflows for fewer premature “done” claims, less irrelevant video input, and less friction with real user requests.

[中文说明](README.zh-CN.md) · [MIT License](LICENSE) · [Candidate catalog](CATALOG.md) · [Release status](RELEASE_STATUS.md)

| Skill | A task to try | What is included |
|---|---|---|
| [Progressive Video Review](skills/video-progressive-review/README.md) | “Find the changed setting in this UI recording.” | Numbered overview → original frames → timestamped conclusion; method only. |
| [Windows UTF-8 Guard](skills/windows-utf8-mojibake-guard/README.md) | “Chinese text looks broken; check the bytes before rewriting.” | Read-only Python inspector and a diagnostic workflow. |
| [Toxic-PM](skills/toxic-pm/README.md) | “Can the evidence support calling this deployed?” | Claim-to-evidence self-review and the smallest useful repair. |
| [Short Request Completion](skills/short-message-completion/README.md) | After a draft: “Shorter. Ready to use.” | Carry forward the known object, facts, and requested delivery level. |

## Try a skill

Clone this repository, then choose a folder inside `skills/`:

```sh
git clone https://github.com/Ghoscro/micker-skills.git
```

Place the selected folder in your agent host's documented skill location. Each folder has a bilingual README, a `SKILL.md` entry and local references. Keep its subfolders intact and retain the repository's license notice when distributing copies. These use the [Agent Skills format](https://agentskills.io/specification); host discovery and behavior still require verification in that host.

Alternatively, give an agent the selected `SKILL.md` and its example file for an explicit trial. Prompt-only workflows require suitable image/audio tools or execution permissions for the task; they do not install those capabilities.

For the included read-only tool, from this repository's root:

```powershell
python -X utf8 skills/windows-utf8-mojibake-guard/scripts/inspect_text_encoding.py "sample.json" --json
```

The inspector prints a short content sample. Inspect suitable local files and review its output before sharing it. It reports findings in JSON; exit code 0 alone is not an encoding verdict.

## Contribution and evidence

Created by Micker / Ghoscro with AI collaborators, as part of the Micker Method. Our contribution is the maintained workflow design, integration, and selected tools. Encoding rules, frame extraction, contact sheets, context-aware dialogue, and quality assurance are established practices.

This bundle contains compact public editions, not the complete internal agent system. Known inspiration is documented in the relevant entry. Local structure/tool checks and independent case review do not establish performance gains, host-wide compatibility, market demand, or future stars.

This is a public-safe version. Examples use mock data; private memory, user data, credentials, deployment details, and full automation loops are intentionally excluded.

## Status and feedback

Version 1.0.0 is released under the [MIT License](LICENSE), including commercial use. Retain the copyright and permission notice when redistributing copies or substantial portions. See [release status](RELEASE_STATUS.md) for the package's verified scope.

Useful feedback is a concrete input, the behavior you expected, the observed result, and the host/tools used. Sanitize examples before submitting them. If this work saves you time, a star helps you find it again and helps others discover it.
