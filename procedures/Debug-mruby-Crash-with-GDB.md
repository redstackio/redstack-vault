---
tags:
  - debugging
  - gdb
  - crash-analysis
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 991cf090-6e71-4758-a55b-2037b5754a41
created_at: '2025-12-11T03:47:48.071Z'
updated_at: '2025-12-11T03:47:48.071Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1203]]'
---
# Debug mruby Crash with GDB

## Summary

This procedure uses GDB to attach to a running mirb process, continue execution to trigger a crash, and inspect the backtrace and registers for analysis of the mruby Decimal assertion failure.

## Description

After setting up the exploit in mirb, attach GDB to the process PID to debug the SIGABRT crash. This reveals the call stack showing the failure in Decimal.initialize and mpd_msword, aiding in vulnerability confirmation on Linux systems.

## Requirements

1. Running mirb process with PID (e.g., 10251)
2. GDB installed on Linux
3. Exploit setup in mirb ready to trigger

## Defense

Defensive measures and detection strategies:

- Restrict debugger attachments in production
- Log unauthorized GDB usage

## Objectives

1. Attach to and debug the crashing process
2. Obtain backtrace confirming assertion failure
3. Inspect registers for crash details

## Instructions

### Step 1: Attach GDB to Process

**Context**: Attach to the mirb PID to begin debugging.

**Command** ([[commands/gdb-attach]]):
```bash
gdb attach 10251
```

> Attaches GDB to the specified process and loads symbols.

### Step 2: Continue Execution

**Context**: Resume the process to hit the crash point.

**Command** ([[commands/gdb-continue]]):
```bash
c
```

> Continues execution until SIGABRT is received.

### Step 3: Inspect Backtrace

**Context**: View the call stack after crash.

**Command** ([[commands/gdb-backtrace]]):
```bash
bt
```

> Prints the backtrace showing assertion in mpd_msword.

### Step 4: View Registers

**Context**: Examine CPU registers at crash time.

**Command** ([[commands/gdb-info-registers]]):
```bash
info registers
```

> Displays register values like rax, rbx, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/gdb-attach]]
- [[commands/gdb-continue]]
- [[commands/gdb-backtrace]]
- [[commands/gdb-info-registers]]

## Tools Used

- [[tools/GDB]]

## Tags

- #debugging
- [[tools/GDB]]
- #crash-analysis
