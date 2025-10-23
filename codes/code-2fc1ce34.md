---
id: 2fc1ce34-11bf-4884-ae5f-e39d7e1b10b1
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.581409+00:00'
updated_at: '2023-04-10T20:36:53.438562+00:00'
---

# Code Snippet 2fc1ce34

**Language**: ps1

```ps1
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```


