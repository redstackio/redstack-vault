---
id: 40da1d03-afee-4c9a-835f-3009c6a4cbc6
name: Append Data to Large Object
type: command
executor: bash
data: SELECT lo_put(oid, offset, 'some other data');
output: null
created_at: '2023-04-06T03:56:35.993522+00:00'
updated_at: '2023-04-10T20:23:17.646217+00:00'
---

# Append Data to Large Object

```bash
SELECT lo_put(oid, offset, 'some other data');
```


