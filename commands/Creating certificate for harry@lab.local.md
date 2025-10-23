---
id: 180e7a07-ccd3-465b-ae66-8dac6b3e6f63
name: Creating certificate for harry@lab.local
type: command
executor: bash
data: ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User
  --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123
output: null
created_at: '2023-04-06T03:56:28.398318+00:00'
updated_at: '2023-04-10T20:37:30.878980+00:00'
---

# Creating certificate for harry@lab.local

```bash
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123
```


