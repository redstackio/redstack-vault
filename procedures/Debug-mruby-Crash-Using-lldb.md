---
id: 7aa35b7b-82ea-4b10-9bbd-ced1406d1d4b
name: Debug mruby Crash Using lldb
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:48.227Z'
updated_at: '2025-12-11T03:47:48.227Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - debugging
  - mruby
  - lldb
commands:
  - '[[commands/./dev/bin/mruby-crash.rb]]'
  - '[[commands/lldb-./dev/bin/mruby-crash.rb]]'
  - '[[commands/target-create-"./dev/bin/mruby"]]'
  - '[[commands/settings-set----target.run-args-"crash.rb"]]'
  - '[[commands/register-read]]'
  - '[[commands/./bin/sandbox-crash.rb]]'
  - >-
    [[commands/diff---git-a/mrbgems/mruby-compiler/core/codegen.c-b/mrbgems/mruby-compiler/core/codegen.c]]
platforms:
  - macOS
tools: []
skill_level: advanced
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---

# Debug mruby Crash Using lldb

## Summary

This procedure uses lldb to debug and analyze the segmentation fault caused by the null pointer dereference in mruby, inspecting backtrace and registers to confirm the vulnerability.

## Description

Debugging reveals the crash location in ary_concat and improper stack management. This is useful for vulnerability verification and understanding the root cause in codegen.c.

## Requirements

1. lldb installed on macOS
2. mruby binary and crash.rb available
3. Debugging privileges

## Defense

Defensive measures and detection strategies:

- Use hardened debugging environments
- Log and alert on debugger attachments to production processes

## Objectives

1. Set up debugging session
2. Run and capture crash
3. Analyze backtrace and registers

## Instructions

### Step 1: Start lldb Session

**Context**: Initiate the debugger with mruby and the script.

**Command** ([[commands/./dev/bin/mruby-crash.rb]]):
```bash
lldb ./dev/bin/mruby crash.rb
```

> Sets up the debugging session.

### Step 2: Create Target

**Context**: Specify the executable target.

**Command** ([[commands/target-create-"./dev/bin/mruby"]]):
```bash
target create "./dev/bin/mruby"
```

> Current executable set to './dev/bin/mruby' (x86_64).

### Step 3: Set Run Arguments

**Context**: Configure arguments for the run.

**Command** ([[commands/settings-set----target.run-args-"crash.rb"]]):
```bash
settings set -- target.run-args "crash.rb"
```

> Sets the configuration.

### Step 4: Run the Program

**Context**: Execute under debugger.

**Command** ([[commands/r]]):
```bash
r
```

> Process launched, stops at crash with EXC_BAD_ACCESS.

### Step 5: Get Backtrace

**Context**: Inspect call stack.

**Command** ([[commands/bt]]):
```bash
bt
```

> Backtrace showing crash in ary_concat.

### Step 6: Read Registers

**Context**: Analyze register state.

**Command** ([[commands/register-read]]):
```bash
register read
```

> Values of registers like rax, rbx, etc.

### Step 7: Quit lldb

**Context**: Exit the session.

**Command** ([[commands/q]]):
```bash
q
```

> Quits lldb.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/./dev/bin/mruby-crash.rb]]
- [[commands/target-create-"./dev/bin/mruby"]]
- [[commands/settings-set----target.run-args-"crash.rb"]]
- [[commands/r]]
- [[commands/bt]]
- [[commands/register-read]]
- [[commands/q]]

## Tools Used

- #lldb

## Tags

- #debugging
- #lldb
