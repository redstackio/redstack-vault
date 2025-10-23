---
id: 9724aaee-65d9-4531-bf1b-70750f789b3c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:31.141002+00:00'
updated_at: '2023-04-10T20:37:59.144920+00:00'
---

# Code Snippet 9724aaee

**Language**: Powershell

```powershell
PS> Invoke-Command -ComputerName DC -Credential $cred -ScriptBlock { whoami }
PS> Invoke-Command -computername DC01,CLIENT1 -scriptBlock { Get-Service }
PS> Invoke-Command -computername DC01,CLIENT1 -filePath c:\Scripts\Task.ps1
```


