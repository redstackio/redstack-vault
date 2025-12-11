---
data: 'sys_fsc2h_ctrl(0x10001, path)'
tags:
  - syscall
  - kernel
  - playstation
type: command
executor: syscall
platforms:
  - PlayStation
  - Kernel
id: 6f75acd1-1afb-499a-900b-d315c0698106
created_at: '2025-12-11T03:47:39.362Z'
updated_at: '2025-12-11T03:47:39.362Z'
verified: false
validated: true
submitted: true
---
# CMD_WAIT (0x10001)

## Command

```c
sys_fsc2h_ctrl(0x10001, path)
```

## Description

This command is used in the sys_fsc2h_ctrl kernel syscall to wait on a specified path. It is typically employed by threads to block until a signal is received for that path, setting up synchronization in multi-threaded exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0x10001` | Command value specifying wait operation | Yes |
| `path` | The path identifier to wait on | Yes |

## Examples

### Basic Usage

```c
sys_fsc2h_ctrl(0x10001, path1)
```

### Advanced Usage

```c
// In a threaded context
thread_wait(sys_fsc2h_ctrl(0x10001, path2))
```

## Expected Output

The thread enters a blocked wait state until woken by a complete operation on the path.

## Related

- [[commands/CMD_COMPLETE-(0x20003)]]
- [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]
