---
id: 3c6af9af-d475-47e4-9494-7a028a3b0a77
name: Create Large Object with OID
type: command
executor: bash
data: SELECT lo_from_bytea(oid, 'your file data goes in here');
output: null
created_at: '2023-04-06T03:56:35.993442+00:00'
updated_at: '2023-04-10T20:23:17.646217+00:00'
---

# Create Large Object with OID

```bash
SELECT lo_from_bytea(oid, 'your file data goes in here');
```
