---
id: 5b0f54fb-bc8f-43a6-8cd4-0d5af16cc354
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.290845+00:00'
updated_at: '2023-04-10T20:37:49.693666+00:00'
---

# Code Snippet 5b0f54fb

**Language**: Powershell

```powershell
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type C:\Users\swissky\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
cat (Get-PSReadlineOption).HistorySavePath
cat (Get-PSReadlineOption).HistorySavePath | sls passw
```
