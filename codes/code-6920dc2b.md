---
id: 6920dc2b-4cee-4b26-80aa-515d758560cc
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.986322+00:00'
updated_at: '2023-04-10T20:37:53.846607+00:00'
---

# Code Snippet 6920dc2b

**Language**: Powershell

```powershell
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*
where /R C:\ user.txt
where /R C:\ *.ini
```
