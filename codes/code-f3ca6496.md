---
id: f3ca6496-d1eb-4cf4-ac5e-1d268b391a4f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:18.515434+00:00'
updated_at: '2023-04-10T20:34:33.397879+00:00'
---

# Code Snippet f3ca6496

**Language**: Powershell

```powershell
find / -mmin -10 2>/dev/null | grep -Ev "^/proc"
```
