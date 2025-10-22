---
id: 634ace15-f203-4c85-96fb-fe9455bea4e3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.377887+00:00'
updated_at: '2023-04-10T20:37:39.718796+00:00'
---

# Code Snippet 634ace15

**Language**: Powershell

```powershell
schtasks /query /fo LIST 2>nul | findstr TaskName
schtasks /query /fo LIST /v > schtasks.txt; cat schtask.txt | grep "SYSTEM\|Task To Run" | grep -B 1 SYSTEM
Get-ScheduledTask | where {$_.TaskPath -notlike "\Microsoft*"} | ft TaskName,TaskPath,State
```
