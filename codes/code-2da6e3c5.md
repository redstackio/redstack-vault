---
id: 2da6e3c5-7bd8-417f-b612-ffe5f6375c3e
type: code
language: ''
verified: false
created_at: '2023-06-06T03:13:11.590351+00:00'
updated_at: '2023-06-06T16:19:30.736264+00:00'
---

# Code Snippet 2da6e3c5

```
#Background Window
proc Stealth() =
  var Stealth: HWND
  discard AllocConsole()
  Stealth = FindWindowA("ConsoleWindowClass", nil);
  discard ShowWindow(Stealth,0)
  
Stealth()
```


