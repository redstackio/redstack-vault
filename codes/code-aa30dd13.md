---
id: aa30dd13-e570-4243-85df-18388600838a
type: code
language: ''
verified: false
created_at: '2023-06-06T03:12:44.555297+00:00'
updated_at: '2023-06-06T03:13:11.599411+00:00'
---

# Code Snippet aa30dd13

```
#Background Window
proc Stealth() =
  var Stealth: HWND
  discard AllocConsole()
  Stealth = FindWindowA("ConsoleWindowClass", nil);
  discard ShowWindow(Stealth,0)
  
Stealth()
```


