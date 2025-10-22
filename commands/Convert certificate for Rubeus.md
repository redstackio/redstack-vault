---
id: 3176843c-b3b9-4468-b0e0-90fd5608c427
name: Convert certificate for Rubeus
type: command
executor: bash
data: openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider
  v1.0" -export -out cert.pfx
output: null
created_at: '2023-04-06T03:56:28.361239+00:00'
updated_at: '2023-04-10T20:37:28.980808+00:00'
---

# Convert certificate for Rubeus

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```
