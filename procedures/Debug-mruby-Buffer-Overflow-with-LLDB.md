---
tags:
  - debugging
  - buffer-overflow
type: procedure
tools:
  - '[[tools/ASAN]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - macOS
techniques:
  - '[[Account Access Removal]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 76d6bd9e-403a-4d69-b7d9-d336a31177f6
created_at: '2025-12-11T03:47:48.029Z'
updated_at: '2025-12-11T03:47:48.029Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1531]]'
---
# Debug mruby Buffer Overflow with LLDB

## Summary

This procedure uses LLDB to debug and analyze the buffer overflow crash in mruby, inspecting stack traces, registers, and invalid structures.

## Description

LLDB reveals the crash in strlen called from snprintf in mrb_time_asctime, with invalid tm_mon values like 6484120 causing the overflow. This helps in understanding the root cause for exploitation or mitigation.

## Requirements

1. LLDB installed
2. mruby binary with debug symbols
3. Crash script 'crash.rb'

## Defense

Defensive measures and detection strategies:

- Compile with ASAN for memory error detection
- Use bounds checking in time functions

## Objectives

1. Identify the exact point of failure
2. Inspect invalid time structures
3. Confirm buffer overflow

## Instructions

### Step 1: Launch LLDB

**Context**: Start the debugger on mruby with the script.

**Command** ([[commands/lldb-launch-mruby]]):
```bash
lldb ./dev/bin/mruby crash.rb
```

> Launches LLDB session.

### Step 2: Set Target

**Context**: Configure the target executable.

**Command** ([[commands/lldb-target-create]]):
```bash
target create "./dev/bin/mruby"
```

> Sets the mruby binary as target.

### Step 3: Set Run Arguments

**Context**: Pass the script as argument.

**Command** ([[commands/lldb-set-run-args]]):
```bash
settings set -- target.run-args "crash.rb"
```

> Configures run arguments.

### Step 4: Run the Program

**Context**: Execute and observe crash.

**Command** ([[commands/lldb-run]]):
```bash
r
```

> Runs the process, may crash with EXC_BAD_ACCESS.

### Step 5: Inspect Backtrace

**Context**: View call stack.

**Command** ([[commands/lldb-backtrace]]):
```bash
bt
```

> Shows stack trace with crash in strlen.

### Step 6: Read Registers

**Context**: Check CPU state.

**Command** ([[commands/lldb-register-read]]):
```bash
register read
```

> Displays register values.

### Step 7: Navigate Stack

**Context**: Move to previous frame.

**Command** ([[commands/lldb-up]]):
```bash
up
```

> Navigates up the stack.

### Step 8: Print tm Struct

**Context**: Inspect time structure.

**Command** ([[commands/lldb-print-tm]]):
```bash
p *tm
```

> Shows invalid tm_mon=6484120.

### Step 9: Print d Struct

**Context**: Inspect datetime structure.

**Command** ([[commands/lldb-print-d]]):
```bash
p *d
```

> Shows invalid fields.

### Step 10: Quit LLDB

**Context**: Exit the debugger.

**Command** ([[commands/lldb-quit]]):
```bash
q
```

> Quits LLDB.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Access Removal]]

### Sub-Techniques



## Commands Used

- [[commands/lldb-launch-mruby]]
- [[commands/lldb-target-create]]
- [[commands/lldb-set-run-args]]
- [[commands/lldb-run]]
- [[commands/lldb-backtrace]]
- [[commands/lldb-register-read]]
- [[commands/lldb-up]]
- [[commands/lldb-print-tm]]
- [[commands/lldb-print-d]]
- [[commands/lldb-quit]]

## Tools Used

- #lldb

## Tags

- #debugging
- #buffer-overflow
