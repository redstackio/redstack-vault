---
id: b23a592d-7aff-4dae-af4a-a8294ba281c8
name: Export Data from Large Object
type: command
executor: bash
data: SELECT lo_export(oid, '/tmp/testexport');
output: null
created_at: '2023-04-06T03:56:35.993589+00:00'
updated_at: '2023-04-10T20:23:17.646217+00:00'
---

# Export Data from Large Object

```bash
SELECT lo_export(oid, '/tmp/testexport');
```
