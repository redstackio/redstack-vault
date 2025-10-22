---
id: 2f70dfbb-ac45-47ee-b814-8e99496e33e0
name: Open PowerShell
type: command
executor: bash
data: 'Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"

  Set SW = GetObject("new:" & ShellWindows).Item()

  SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32",
  Null, 0'
output: null
created_at: '2023-04-06T03:56:23.581507+00:00'
updated_at: '2023-04-10T20:36:53.437030+00:00'
---

# Open PowerShell

```bash
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```
