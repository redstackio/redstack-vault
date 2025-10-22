---
id: 2c1f19c9-9183-4bd2-86b4-e5b0063b5fec
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:28.398254+00:00'
updated_at: '2023-04-10T20:37:30.878948+00:00'
---

# Code Snippet 2c1f19c9

**Language**: ps1

```ps1
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword Password123
```
