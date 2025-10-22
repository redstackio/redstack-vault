---
id: 449843b1-795e-41b4-b1b0-2811db8ee708
name: RPCDump with egrep filter on MS-RPRN and MS-PAR
type: command
executor: bash
data: python3 ./rpcdump.py @10.0.2.10 | egrep 'MS-RPRN|MS-PAR'
output: null
created_at: '2023-04-06T03:56:02.824819+00:00'
updated_at: '2023-04-10T20:25:51.539032+00:00'
---

# RPCDump with egrep filter on MS-RPRN and MS-PAR

```bash
python3 ./rpcdump.py @10.0.2.10 | egrep 'MS-RPRN|MS-PAR'
```
