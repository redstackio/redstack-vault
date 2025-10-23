---
id: a9b32d73-00eb-4e09-bbe0-39534b8057cc
name: Get TGT using PEM certificate and private key
type: command
executor: bash
data: gettgtpkinit.py -cert-pem "PATH_TO_PEM_CERT" -key-pem "PATH_TO_PEM_KEY" "FQDN_DOMAIN/TARGET_SAMNAME"
  "TGT_CCACHE_FILE"
output: null
created_at: '2023-04-06T03:56:06.176766+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# Get TGT using PEM certificate and private key

```bash
gettgtpkinit.py -cert-pem "PATH_TO_PEM_CERT" -key-pem "PATH_TO_PEM_KEY" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
```


