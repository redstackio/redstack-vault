---
id: 332af589-5e5f-411c-997e-4243c0483f89
name: Export unprotected PFX certificate using Certipy
type: command
executor: bash
data: certipy cert -export -pfx "PATH_TO_PFX_CERT" -password "CERT_PASSWORD" -out
  "unprotected.pfx"
output: null
created_at: '2023-04-06T03:56:06.176894+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# Export unprotected PFX certificate using Certipy

```bash
certipy cert -export -pfx "PATH_TO_PFX_CERT" -password "CERT_PASSWORD" -out "unprotected.pfx"
```
