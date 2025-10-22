---
id: 0169d4ee-ca2f-4cd9-b452-adb708f9e2f6
name: Encode JWT with custom key ID header
type: command
executor: bash
data: 'jwt.encode({"some": "payload"}, "secret", algorithm="HS256", headers={"kid":
  "http://evil.example.com/custom.key"})'
output: null
created_at: '2023-04-06T03:56:00.787091+00:00'
updated_at: '2023-04-10T20:22:34.479056+00:00'
---

# Encode JWT with custom key ID header

```bash
jwt.encode({"some": "payload"}, "secret", algorithm="HS256", headers={"kid": "http://evil.example.com/custom.key"})
```
