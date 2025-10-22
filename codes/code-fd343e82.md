---
id: fd343e82-4b92-4b0d-a26e-2b1dbb5903b2
type: code
language: ''
verified: false
created_at: '2023-06-06T03:07:45.871280+00:00'
updated_at: '2023-06-06T03:09:03.665803+00:00'
---

# Code Snippet fd343e82

```
#Background Window
proc Stealth() =
  var Stealth: HWND
  discard AllocConsole()
  Stealth = FindWindowA("ConsoleWindowClass", nil);
  discard ShowWindow(Stealth,0)

Stealth()
```
