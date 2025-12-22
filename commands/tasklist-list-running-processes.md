---
id: a73cdd95-4848-40ec-97d1-4ec5e3ea5292
name: tasklist-list-running-processes
type: command
executor: command_prompt
data: tasklist.exe
output: |-
  Image Name                     PID Session Name        Session#    Mem Usage
  ========================= ======== ================ =========== ============ 
  System Idle Process              0 Services                   0          8 K
  System                           4 Services                   0        140 K
  Registry                        88 Services                   0     70,192 K
  ...
created_at: '2020-01-02T18:45:14.100849+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - discovery
  - processes
verified: true
validated: true
---

# tasklist-list-running-processes

## Command

```command_prompt
tasklist.exe
```

## Description

Lists all currently running processes on a Windows system, including PID, session, and memory usage, to identify targets for further actions like memory dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Default lists all processes | N/A |

## Examples

### Basic Usage

```command_prompt
tasklist.exe
```

### Advanced Usage

```command_prompt
tasklist.exe /fi "imagename eq lsass.exe"
```

## Expected Output

A table format showing Image Name, PID, Session Name, Session#, and Mem Usage for all processes.

## Related

- [[procedures/Dump-Process-Memory-Using-Procdump]]
