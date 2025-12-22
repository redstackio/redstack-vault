---
data: 'call rax ; Call WinExec(\"calc.exe\", SW_SHOWNORMAL)'
tags:
  - rop
  - rce
type: command
output: Calculator application launches.
executor: asm
platforms:
  - Windows
id: c594ffd6-cd1a-441c-a636-8b9b9b4b75c8
created_at: '2025-12-13T23:55:06.742Z'
updated_at: '2025-12-13T23:55:06.742Z'
verified: false
validated: true
submitted: true
---
# rop-stage4-call-winexec

## Command

```asm
call rax ; Call WinExec("calc.exe", SW_SHOWNORMAL)
```

## Description

Final ROP call to WinExec for RCE demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rax | Address of WinExec | Yes |

## Examples

### Basic Usage

End of ROP chain.

## Expected Output

calc.exe process starts.

## Related

- [[commands/rop-stage3-prepare-params]]
