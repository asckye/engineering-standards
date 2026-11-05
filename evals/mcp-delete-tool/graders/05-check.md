---
type: llm
focus:
  source: file
  path: tool-spec.md
---

PASS if the spec says that when the outcome of the delete is unknown (for example a timeout or lost connection after sending) the call is not retried automatically and a human has to check. FAIL if it retries, or does not address an unknown outcome.
