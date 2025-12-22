---
data: 'sys_fsc2h_ctrl(0x20005, path, buffer)'
tags:
  - syscall
  - kernel
  - playstation
type: command
executor: syscall
platforms:
  - PlayStation
  - Kernel
id: 1553c4eb-d13b-425b-9928-94d666c33888
created_at: '2025-12-11T03:47:39.361Z'
updated_at: '2025-12-11T03:47:39.361Z'
verified: false
validated: true
submitted: true
---
# CMD_RESOLVE (0x20005)

## Command

```c
sys_fsc2h_ctrl(0x20005, path, buffer)
```

## Description

This command sets the pointer of a specified path to a local stack buffer in the sys_fsc2h_ctrl syscall and enters a sleep state. It is used to manipulate pointers in exploit scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0x20005` | Command value specifying resolve operation | Yes |
| `path` | The path to resolve | Yes |
| `buffer` | Pointer to local stack buffer | Yes |

## Examples

### Basic Usage

```c
sys_fsc2h_ctrl(0x20005, path2, stack_buffer)
```

### Advanced Usage

```c
// With sleep
sys_fsc2h_ctrl(0x20005, path, buffer);
sleep();
```

## Expected Output

Path pointer is updated to the buffer, and the thread sleeps.

## Related

- [[commands/CMD_WAIT-(0x10001)]]
- [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]
