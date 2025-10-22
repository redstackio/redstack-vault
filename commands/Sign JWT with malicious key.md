---
id: dbdd5b83-5d97-406d-86e5-5ef1c4825cac
name: Sign JWT with malicious key
type: command
executor: bash
data: "jwt.sign({\n  data: 'test'\n}, maliciousKey, { algorithm: 'HS256', header:\
  \ { kid: 'malicious.key' } })\n"
output: null
created_at: '2023-04-06T03:56:00.761287+00:00'
updated_at: '2023-04-10T20:22:38.428459+00:00'
---

# Sign JWT with malicious key

```bash
jwt.sign({
  data: 'test'
}, maliciousKey, { algorithm: 'HS256', header: { kid: 'malicious.key' } })

```
