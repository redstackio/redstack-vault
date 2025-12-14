---
data: (gdb) i r
tags:
  - debugging
  - gdb
type: command
output: null
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.359Z'
id: 5a623841-4b59-4c58-972d-375fe475900a
verified: false
validated: true
submitted: true
---
# gdb-info-registers

## Command

```bash
(gdb) i r
```

## Description

This GDB command displays the values of all CPU registers at the point of crash, helping identify invalid pointers (e.g., in rdi) passed to free functions during the double-free in pngcrush.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
(gdb) i r
```

(Execute immediately after segfault is caught.)

### Advanced Usage

```bash
(gdb) info registers rdi rip
```

(Focus on specific registers like rdi (pointer arg) and rip (instruction pointer).)

## Expected Output

'rax            0x0\nrbx            0x7864d0\n...\nrdi            0x5555555555555555\nrip            0x7ffff784a939 <free+9>', showing invalid rdi value causing the free failure.

## Related

- [[procedures/Debug-Segfault-with-GDB]]
- [[commands/gdb-backtrace]]
