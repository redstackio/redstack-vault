---
id: 586606f2-1300-4ef0-be96-5a071fa8946a
name: Export Certificate to PFX format
type: command
executor: bash
data: openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider
  v1.0" -export -out cert.pfx
output: null
created_at: '2023-04-06T03:56:05.732356+00:00'
updated_at: '2023-04-10T20:25:45.495574+00:00'
---

# Export Certificate to PFX format

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```
