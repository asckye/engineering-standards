---
type: llm
focus: last_message
---

PASS if the reply says resending after a timeout is wrong because the first command may already have reached the device, so the outcome is unknown. FAIL if it only suggests backoff or a better retry.
