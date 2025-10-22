---
id: b834da02-9204-4c23-ab3e-3413f403bfbc
name: Check if PrintSpooler service is running on DC
type: command
executor: bash
data: rpcdump.py 10.10.10.10 | grep -A 6 "spoolsv"
output: null
created_at: '2023-04-06T03:56:02.745283+00:00'
updated_at: '2023-04-10T20:36:02.527266+00:00'
---

# Check if PrintSpooler service is running on DC

```bash
rpcdump.py 10.10.10.10 | grep -A 6 "spoolsv"
```
