---
name: short-message-completion
description: Complete context-dependent action requests such as “shorter”, “use that one”, or “finish the rest” by carrying forward the known object and goal. Use when recent context resolves an underspecified task, not for every short message or an isolated “continue”.
license: MIT
metadata:
  version: "1.0.0"
  author: "Micker / Ghoscro and AI collaborators"
---

# Short Request Completion

Turn an abbreviated request into the requested deliverable with minimal user effort.

Use this workflow when there is both an action intent and useful context to carry forward. A greeting, acknowledgement, factual question, or complete instruction usually needs ordinary handling.

Identify the current object, requested change, preserved constraints, and intended delivery level. Use the recent conversation and relevant artifacts; do not pull an unrelated old task into an ambiguous “continue”.

- When the object and change are clear, do the work immediately.
- For low-cost reversible style choices, pick a reasonable default and deliver it. Preserve facts, names, dates, and user-approved choices.
- When plausible interpretations yield materially different work, ask one question that separates them. Continue independent preparation where useful.
- When essential source material, a recipient, or authorization is absent, prepare the grounded portion and request the missing item. A timeout is not an answer.

Complete the intended level: a writing request receives finished wording, an authorized file change receives an actual edit and a relevant check, and a plan request receives a plan. Brief feedback on a draft calls for a revision of that draft. Avoid expanding the task into deployment, redesign, or external communication.

Existing authorization remains usable when its object, scope, and risk are unchanged. Context completion supplies missing meaning, not missing permission. Sending, spending, and irreversible changes continue to require the appropriate authorization.

Respond with the result first. Explain only assumptions that change use or genuine blocking items. Mark placeholders clearly; a template with placeholders is a draft.

See [examples](references/examples.md) for positive and negative cases.

Created by Micker / Ghoscro as part of the Micker Method. This is a maintained interaction workflow; it makes no claim of inventing context-aware conversation.

This is a public-safe version. Examples use mock data; private memory, user data, credentials, deployment details, and full automation loops are intentionally excluded.
