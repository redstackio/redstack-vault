---
id: 40e1ee3e-6b5c-457b-8223-cb207d92b643
name: Verify JWT signature with JWKS endpoint
type: command
executor: bash
data: python3 jwt_tool.py JWT_HERE -X s -ju http://example.com/jwks.json
output: null
created_at: '2023-04-06T03:56:00.839770+00:00'
updated_at: '2023-04-10T20:22:36.345573+00:00'
---

# Verify JWT signature with JWKS endpoint

```bash
python3 jwt_tool.py JWT_HERE -X s -ju http://example.com/jwks.json
```
