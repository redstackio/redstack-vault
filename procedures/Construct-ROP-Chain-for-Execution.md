---
tags:
  - rop
  - bypass-nx
type: procedure
tools:
  - '[[tools/Python3]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 861beae0-c217-427c-98e0-82c34db18bf8
created_at: '2025-12-14T17:28:28.360Z'
updated_at: '2025-12-14T17:28:28.360Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Construct-ROP-Chain-for-Execution

## Summary

This procedure constructs a ROP chain in the overflow payload to bypass NX, using gadgets to build strings, load modules, prepare execve args, and execute xcalc via int 0x80 syscall.

## Description

Exploiting the overflow, the payload at offset 0xac overwrites the return address with ROP gadgets from hw.so and hl.exe. It calls strncpy to assemble '/usr/bin/xcalc' and 'DISPLAY=:0' in .bss, loads hw.so for base resolution, sets execve pointers, and invokes syscall. Fixed addresses ensure portability on Linux GoldSrc clients.

## Requirements

1. Knowledge of gadget addresses in hw.so and hl (e.g., via objdump)
2. Python3 for payload encoding (avoid nulls)
3. Overflow triggered from prior steps

## Defense

Defensive measures and detection strategies:

- Enable DEP/NX and ASLR to randomize gadget locations
- Use RELRO and stack canaries
- Scan for ROP patterns in memory dumps or via anti-cheat tools

## Objectives

1. Bypass NX with ROP for code execution
2. Execute xcalc as proof-of-concept RCE
3. Demonstrate full client compromise

## Instructions

### Step 1: Build Payload with Gadgets

**Context**: Chain strncpy calls for string construction in .bss.

**Command** (Python scripting):
```python
rop = flat([
    strncpy_addr, 0, bss_str1, len('/usr/bin/xcalc'),
    # Repeat for DISPLAY=:0
    sys_loadmodule_addr, hw_so_ptr,
    execve_prep_gadgets,
    int80_gadget
])
payload = b'A' * offset + rop  # Pad to 0xac
```

> Encodes ROP; expected output is binary payload ready for packet insertion.

### Step 2: Inject and Execute

**Context**: Overflow delivers payload, triggering ROP on return.

**Command** (Integrated in delta packet):
```python
# Insert payload into string field at 0xac in delta_data
socket.sendto(delta_packet_with_rop, client_addr)
```

> Execution flows to ROP; success if xcalc launches.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python3]]

## Tags

- rop
- bypass-nx
