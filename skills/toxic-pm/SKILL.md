---
name: toxic-pm
description: Audit a delivery claim against the original goal, actual artifact, and fresh evidence before calling work finished, usable, or deployed. Use for self-review of completed work; assess the work and the claim, not the person's character.
license: MIT
metadata:
  version: "1.0.0"
  author: "Micker / Ghoscro and AI collaborators"
---

# Toxic-PM: Evidence Before “Done”

Find the strongest honest delivery claim and the smallest repair that would improve it.

Start with the proposed claim, the user's original goal, the artifact, fresh verification evidence, and material risks. Retrieve available evidence before asking the user. If no claim exists, draft the narrowest candidate supported by the work.

Use only the review angles that can change the verdict:

1. Goal: does this artifact solve the requested problem for the intended user? File counts and test counts can describe effort while leaving the goal unresolved.
2. Usability: inspect the affected real path. A build supports a build claim; a rendered screen supports appearance; a tested interaction supports that interaction; production access needs production evidence.
3. Evidence: bind each claim to its environment, time, and coverage. Keep local runs, mock data, sampled checks, and deployment distinct.
4. Complexity: identify maintenance cost with no current user benefit. Prefer a smaller repair or a standard capability when it meets the requirement. Preserve error handling and actual user requirements.
5. Honest wording: accept, narrow the claim, repair then deliver, or reject the current delivery. Explain the next observable check.

For a small reversible artifact, a short paragraph is enough. For a multi-part delivery, identify the few issues that block the user's result, then repair within the authorized scope. Self-review is not independent review; consequential releases may need a separate reviewer under the host's rules.

Credit verified progress explicitly. A missing production check does not erase a successful local implementation. Criticism targets a claim or artifact; sharp language is optional and never supplies evidence. Do not invent a finding to look strict or add another protocol merely to document the audit.

Default output: verdict, decisive evidence or gap, strongest supported claim, and smallest next repair. The request's completion level determines when to stop.

See [examples](references/examples.md) for contrasting evidence levels.

Created by Micker / Ghoscro as part of the Micker Method. This public edition summarizes the team's delivery self-review workflow. General quality assurance and evidence-based review are established practices. The internal workflow also notes the single-unresolved-branch questioning pattern of Grill / grill-me; this edition ships no upstream implementation or source text.

This is a public-safe version. Examples use mock data; private memory, user data, credentials, deployment details, and full automation loops are intentionally excluded.
