---
id: 072de30a-f370-4578-86cb-739471e2c50b
name: Extract Public Key from SSL Certificate
type: command
executor: bash
data: openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout
output: null
created_at: '2023-04-06T03:56:00.633501+00:00'
updated_at: '2023-04-10T20:22:33.490177+00:00'
---

# Extract Public Key from SSL Certificate

```bash
openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout
```
