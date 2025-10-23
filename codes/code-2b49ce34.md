---
id: 2b49ce34-83ab-48ba-894b-77bf606228ee
type: code
language: ''
verified: false
created_at: '2023-06-06T03:09:03.652005+00:00'
updated_at: '2023-06-06T03:12:18.192813+00:00'
---

# Code Snippet 2b49ce34

```
#Background Window
proc Stealth() =
  var Stealth: HWND
  discard AllocConsole()
  Stealth = FindWindowA("ConsoleWindowClass", nil);
  discard ShowWindow(Stealth,0)
  
Stealth()
```


