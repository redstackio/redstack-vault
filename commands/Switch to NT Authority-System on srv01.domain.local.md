---
id: d5b41f8a-fe05-435d-999d-ae74d1bbecb9
name: Switch to NT Authority/System on srv01.domain.local
type: command
executor: bash
data: PsExec.exe \\srv01.domain.local -u DOMAIN\username -p password cmd.exe -s
output: null
created_at: '2023-04-06T03:56:31.313493+00:00'
updated_at: '2023-04-10T20:37:57.540862+00:00'
---

# Switch to NT Authority/System on srv01.domain.local

```bash
PsExec.exe \\srv01.domain.local -u DOMAIN\username -p password cmd.exe -s
```


