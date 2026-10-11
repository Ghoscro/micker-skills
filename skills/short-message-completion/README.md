# Short Request Completion / 短请求补全

Carry forward the current object when a user says “shorter,” “use that one,” or
“finish the rest,” then deliver the requested revision with fewer repeated questions.

[Skill entry](SKILL.md) · [Positive and boundary cases](references/examples.md) · [All skills](../../README.md)

## Try it

Copy this directory to your host's documented skill location, retaining
`references/`, and verify discovery. Or supply `SKILL.md` and the examples directly:

> Use short-message-completion for the next request. Carry forward the current
> draft, preserve its facts, and deliver the requested wording.

Then provide a draft and brief feedback:

> Draft: “The meetup begins at 14:00 on Friday in Room 3. Please bring a laptop.”
> Feedback: “Shorter. Ready to use.”

**Mock revision:** “Friday, 14:00, Room 3. Bring a laptop.”

The object and requested change are already clear. Names, dates, approved choices,
and other facts remain intact.

## Workflow and input

Use the recent conversation and relevant artifact to identify the object, change,
constraints, and requested completion level. Do the work when they are clear.
For a reversible style choice, choose a reasonable default. When interpretations
would lead to materially different work, ask one separating question.

An isolated “continue” with several possible tasks needs clarification. A greeting
or a complete factual question needs ordinary handling. A request to revise a
draft calls for the revised draft. Drafting a message does not authorize sending
it. Context supplies meaning; spending, sending, and irreversible operations need
the appropriate authorization.

No runtime tool is bundled. Text revision needs a text-capable agent and the
relevant context. File-edit requests additionally need file tools and a relevant
check; essential missing material should be requested rather than invented.

## 中文快速使用

用户在刚看过的草稿后说“短点”“就这个”“给成品”，就接着当前对象修改，保留事实。
例如“周五 14:00，3 号会议室，请带电脑”可缩成“周五 14:00，3 号会议室，带电脑”。
对象清楚就交付；如果“继续”对应多个任务，用一个问题确认。文案请求交完整文字，
文件修改请求完成授权的修改和检查，计划请求交计划。对发送、花钱等操作按实际授权执行。

## Verification, credit, and license

Public format/reference checks and independent mock-case review were performed.
Host discovery, long-context behavior, and reductions in clarification frequency
have not been measured in this public edition.

Interaction workflow maintained by Micker / Ghoscro with AI collaborators;
context-aware conversation is an established practice. [MIT License](../../LICENSE).
