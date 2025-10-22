---
id: 4571dc44-e39d-48c5-95a9-193ac695ffcf
name: Run mitm6
type: command
executor: bash
data: sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay
  CA.domain.local -v
output: null
created_at: '2023-04-06T03:56:05.989470+00:00'
updated_at: '2023-04-10T20:26:16.822815+00:00'
---

# Run mitm6

```bash
sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay CA.domain.local -v
```
