---
id: 17383032-0ebd-4117-acdf-9fbd8163792b
name: find "jmp esp" with gdb
type: command
executor: bash
data: 'find /b <from addr>, <to addr>, 0xff, 0xe4

  '
output: null
created_at: '2020-07-14T18:15:02.616555+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# find "jmp esp" with gdb

```bash
find /b <from addr>, <to addr>, 0xff, 0xe4

```
