---
id: 1abf33ab-e658-4148-a552-f6a34a3582d3
name: mona Search for a JMP to ESP Instruction
type: command
executor: bash
data: '!mona jmp -r esp'
output: "[+] Command used:\n!mona jmp -r esp\n\n---------- Mona command started on\
  \ 2020-04-03 12:27:59 (v2.0, rev 583) ----------\n...\n[+] Results :\n  0x625011af\
  \ : jmp esp |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH:\
  \ False, OS: False, v-1.0- (C:\\Users\\Victim\\Desktop\\vulnserver-master\\essfunc.dll)\n\
  ..."
created_at: '2019-09-21T00:36:54.550104+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mona Search for a JMP to ESP Instruction

```bash
!mona jmp -r esp
```

## Expected Output

```
[+] Command used:
!mona jmp -r esp

---------- Mona command started on 2020-04-03 12:27:59 (v2.0, rev 583) ----------
...
[+] Results :
  0x625011af : jmp esp |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\Victim\Desktop\vulnserver-master\essfunc.dll)
...
```
