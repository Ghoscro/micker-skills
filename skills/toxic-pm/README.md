# Toxic-PM / 麦式毒舌自检

Before saying “done,” compare the claim with what the user can actually use.
Return the strongest supported claim and the smallest repair that improves delivery.

[Skill entry](SKILL.md) · [Evidence-level examples](references/examples.md) · [All skills](../../README.md)

## Try it

Copy this directory to your agent host's documented skill location, keeping
`references/` with the entry, and verify discovery. Or give the agent `SKILL.md`
and the example file explicitly:

> Use toxic-pm to review this claim: “The dashboard is deployed and ready.”
> Original goal: users can open it and filter their records. Available evidence:
> a successful local build and a screenshot from a local preview. Inspect any
> available relevant evidence and return a verdict, supported claim, and next check.

## Mock result

> **Verdict:** narrow the claim.
> **Evidence:** the build completed and the sampled local screen rendered.
> **Supported claim:** “The dashboard builds locally; its sampled screen renders.”
> **Next check:** open the production URL with the intended account and exercise
> the filter on representative records, including an empty result.

The local progress is real; production access and the interaction still need evidence.
If the original request was only a plan, a delivered plan can satisfy it.

## What the skill reviews

| Angle | Useful question |
|---|---|
| Goal | Does the artifact solve the requested problem for the intended user? |
| Usability | Was the relevant real path actually exercised? |
| Evidence | Which environment, time, input, and coverage support this claim? |
| Complexity | Which cost can be removed without losing a required behavior? |
| Honest wording | Accept, narrow, repair, or reject this delivery claim? |

Provide the original request, proposed claim, artifact, checks, and material risks.
The agent needs access to relevant files, screenshots, logs, or the application
to verify more than the supplied prose. This package contains a review workflow
and mock cases; it bundles no deployment, browser, or test runner.

## 中文快速使用

适合交付前检查“做好了”“能用”“已上线”的依据。把原始目标、成品和实际检查结果
交给 Agent：

> 用麦式毒舌自检看这次交付：我的目标是什么，现有证据支持哪种完成程度，最小
> 的补修或下一步实测是什么？先查手头证据，再给结论。

结果包括判断、关键依据、能支持的表述和最小下一步。批评对象是作品与宣称，
已验证的进展保留。自检属于同一 Agent 的复核；需要独立审核的发布应另设审核者。

## Verification, sources, and license

Local format/reference checks and independent mock-case review were performed.
No measured improvement in model reliability or delivery speed is claimed.

This public edition is authored and maintained by Micker / Ghoscro with AI
collaborators. General QA and evidence-based review are established practices.
The internal workflow acknowledges Grill / grill-me's single-unresolved-branch
questioning pattern as conceptual inspiration; no upstream implementation or
source text is shipped in this edition. [MIT License](../../LICENSE).
