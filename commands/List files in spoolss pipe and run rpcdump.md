---
id: f76400a9-4dfc-4b99-971e-ef9507621210
name: List files in spoolss pipe and run rpcdump
type: command
executor: bash
data: 'ls \\dc01\pipe\spoolss

  python rpcdump.py DOMAIN/user:password@10.10.10.10'
output: null
created_at: '2023-04-06T03:56:07.489536+00:00'
updated_at: '2023-04-10T20:26:01.852654+00:00'
---

# List files in spoolss pipe and run rpcdump

```bash
ls \\dc01\pipe\spoolss
python rpcdump.py DOMAIN/user:password@10.10.10.10
```
