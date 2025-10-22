---
id: dd35a8e4-b5ee-4808-863d-087eff1cfdb5
name: find "jmp esp" with mona.py
type: command
executor: bash
data: '!mona find -type instr -s "jmp esp" -m <DLL>

  '
output: null
created_at: '2020-07-14T18:15:02.616750+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# find "jmp esp" with mona.py

```bash
!mona find -type instr -s "jmp esp" -m <DLL>

```
