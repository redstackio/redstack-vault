---
data: 'sys_fsc2h_ctrl(0x20003, path, data)'
tags:
  - syscall
  - kernel
  - playstation
type: command
executor: syscall
platforms:
  - PlayStation
  - Kernel
id: 448657cb-e2d3-4bd5-89aa-b5c1346dbb4b
created_at: '2025-12-11T03:47:39.359Z'
updated_at: '2025-12-11T03:47:39.359Z'
verified: false
validated: true
submitted: true
---
# CMD_COMPLETE (0x20003)

## Command

```c
sys_fsc2h_ctrl(0x20003, path, data)
```

## Description

This command writes data into the buffer pointed by the specified path and wakes up the associated thread in the sys_fsc2h_ctrl syscall. It is crucial for signaling in race condition exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0x20003` | Command value specifying complete operation | Yes |
| `path` | The path to complete | Yes |
| `data` | Data to write to the buffer | Yes |

## Examples

### Basic Usage

```c
sys_fsc2h_ctrl(0x20003, path2, data)
```

### Advanced Usage

```c
// In exploit context
sys_fsc2h_ctrl(0x20003, path, exploit_data);
```

## Expected Output

Data is written to the buffer, and the waiting thread is woken.

## Related

- [[commands/CMD_WAIT-(0x10001)]]
- [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]
