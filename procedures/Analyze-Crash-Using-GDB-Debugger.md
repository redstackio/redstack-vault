---
id: proc-mruby-gdb-analyze
tags:
  - debug
  - gdb
  - crash-analysis
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/gdb-backtrace]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.742Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Analyze-Crash-Using-GDB-Debugger

## Summary

This procedure uses GDB to debug and analyze the segmentation fault from the MRuby crash, generating a backtrace to confirm the null pointer dereference location in mrb_vm_exec at vm.c:1592.

## Description

After executing the PoC, the interpreter segfaults due to a null pointer in VM execution. GDB attachment allows inspection of the stack, revealing the call chain from main through sandbox_eval, method missing handling, and range object access. This confirms the root cause: mishandled 'break' in NoMethodError contexts. Applicable to Linux environments with the built MRuby.

## Requirements

1. GDB installed on Linux x64
2. Core dump or running process from the crashed sandbox execution
3. MRuby source code for symbol resolution

## Defense

Defensive measures and detection strategies:

- Integrate core dump analysis in CI/CD pipelines for crash reproduction
- Use tools like Dr. Memory or Valgrind alongside GDB for comprehensive memory debugging
- Patch VM code to add null checks before dereferencing method or range objects

## Objectives

1. Locate the exact crash site in the MRuby codebase
2. Trace the execution path leading to the null pointer
3. Document the vulnerability for reporting and fixing

## Instructions

### Step 1: Attach GDB to Crash

**Context**: Start GDB on the sandbox binary and load the core dump or re-run under debugger to catch the segfault.

Launch GDB:

```bash
gdb ./sandbox
```

Then run the PoC inside GDB:

```bash
run vm_exec.rb
```

> Expected: GDB halts at segmentation fault.

### Step 2: Generate Backtrace

**Context**: Use the backtrace command to inspect the stack frames and identify the null pointer access.

Execute [[commands/gdb-backtrace]]:

```bash
bt
```

> This displays frames from mrb_vm_exec (vm.c:1592) to main, highlighting null access in break handling. Expected output: Detailed stack trace confirming vulnerability in method missing and range creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/gdb-backtrace]]

## Tools Used

- [[tools/GDB]]

## Tags

- debug
- gdb
- crash-analysis
