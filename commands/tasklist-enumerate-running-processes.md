---
id: a73cdd95-4848-40ec-97d1-4ec5e3ea5292
name: tasklist-enumerate-running-processes
type: command
executor: command_prompt
data: tasklist
output: |-
  Image Name                     PID Session Name        Session#    Mem Usage
  ========================= ======== ================ =========== ============
created_at: '2020-03-04T20:00:45.593036+00:00'
updated_at: '2023-05-30T19:55:11.440197+00:00'
platforms:
  - Windows
tags:
  - process-discovery
  - enumeration
  - living-off-land
verified: true
validated: true
---

# tasklist-enumerate-running-processes

## Command

```command_prompt
tasklist
```

## Description

This command enumerates all currently running processes on a Windows system, displaying key details such as image name, PID, session, and memory usage. It is a basic invocation useful for initial process discovery in red team engagements or troubleshooting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| No user-specified parameters | Basic execution lists all processes in table format | No |
| `/v` | (Optional flag) Verbose output with additional details | No |
| `/fo table` | (Built-in default) Output format as table | Built-in |

## Examples

### Basic Usage

Enumerates all processes without filters.

```command_prompt
tasklist
```

### Advanced Usage

Enumerates processes verbosely.

```command_prompt
tasklist /v
```

## Expected Output

A table listing running processes, for example:

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0         8 K
System                           4 Services                   0     1,252 K
Registry                        92 Services                   0     4,392 K
...

Success is indicated by the table appearing without errors. The file tasklist.exe is located in System32.

## Related

- [[tools/tasklist]]
- [[procedures/Process-Discovery-via-Tasklist]]
