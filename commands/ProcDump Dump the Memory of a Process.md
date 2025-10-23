---
id: a9087a04-b1d0-4765-beeb-d8ffbc3fef5e
name: ProcDump Dump the Memory of a Process
type: command
executor: command_prompt
data: procdump.exe -ma $_PID $_OUTPUT.dmp
output: 'C:\Users\Bob\Desktop>procdump.exe -ma 2416 output-2416.dmp


  ProcDump v9.0 - Sysinternals process dump utility

  Copyright (C) 2009-2017 Mark Russinovich and Andrew Richards

  Sysinternals - www.sysinternals.com


  [10:44:10] Dump 1 initiated: C:\Users\Bob\Desktop\output-2416.dmp

  [10:44:10] Dump 1 writing: Estimated dump file size is 519 MB.

  [10:44:17] Dump 1 complete: 519 MB written in 7.1 seconds

  [10:44:17] Dump count reached.'
created_at: '2020-01-02T18:45:14.101098+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ProcDump Dump the Memory of a Process

```command_prompt
procdump.exe -ma $_PID $_OUTPUT.dmp
```

## Expected Output

```
C:\Users\Bob\Desktop>procdump.exe -ma 2416 output-2416.dmp

ProcDump v9.0 - Sysinternals process dump utility
Copyright (C) 2009-2017 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

[10:44:10] Dump 1 initiated: C:\Users\Bob\Desktop\output-2416.dmp
[10:44:10] Dump 1 writing: Estimated dump file size is 519 MB.
[10:44:17] Dump 1 complete: 519 MB written in 7.1 seconds
[10:44:17] Dump count reached.
```


