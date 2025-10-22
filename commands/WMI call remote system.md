---
id: fb57cd12-7c77-4c6a-85c9-46f542ef76a7
name: WMI call remote system
type: command
executor: bash
data: 'wmic /node:remote_computer process call create "netstat.exe -ano > C:\output.txt"

  '
output: null
created_at: '2020-07-14T18:21:27.746213+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# WMI call remote system

```bash
wmic /node:remote_computer process call create "netstat.exe -ano > C:\output.txt"

```
