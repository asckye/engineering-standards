---
type: llm
focus:
  source: file
  path: tool-spec.md
---

PASS if the spec requires approval by a human in a window the server owns or a dialog inside the target software, and says a parameter from the caller (such as confirm=true) or a form shown by the client cannot replace it. FAIL if approval can come from a parameter or the client alone, or if there is no approval.
