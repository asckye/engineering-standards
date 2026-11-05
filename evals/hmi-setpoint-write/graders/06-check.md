---
type: llm
focus:
  source: file
  path: design.md
---

PASS if the design says a write whose outcome is unknown (timeout or lost connection after sending) is not retried automatically and the operator has to check the actual value first. FAIL if it retries, or does not address this case.
