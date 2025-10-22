---
id: f33b5dea-2d7d-47b3-a674-b8c90bf7bf4f
name: SMBMap with domain credentials
type: command
executor: bash
data: smbmap -H 10.10.10.10 -d "DOMAIN.LOCAL" -u "USERNAME" -p "Password123*"
output: null
created_at: '2023-04-06T03:56:03.238094+00:00'
updated_at: '2023-04-10T20:26:35.786286+00:00'
---

# SMBMap with domain credentials

```bash
smbmap -H 10.10.10.10 -d "DOMAIN.LOCAL" -u "USERNAME" -p "Password123*"
```
