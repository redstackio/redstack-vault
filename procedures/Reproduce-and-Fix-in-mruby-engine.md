---
tags:
  - buffer-overflow
  - mruby-engine
type: procedure
tools:
  - '[[tools/ASAN]]'
tactics:
  - '[[Execution]]'
  - '[[Reconnaissance]]'
commands: []
platforms:
  - macOS
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 56911ed7-d7dc-465f-bcd8-c032377edbb0
created_at: '2025-12-11T03:47:48.022Z'
updated_at: '2025-12-11T03:47:48.022Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1499]]'
---
# Reproduce and Fix in mruby-engine

## Summary

This procedure reproduces the buffer overflow in mruby-engine sandbox and applies a similar patch to fix it.

## Description

The vulnerability affects mruby-engine similarly, causing crashes in the sandbox. The patch adds range checks, raising errors instead.

## Requirements

1. mruby-engine installed
2. Crash script 'crash.rb'
3. diff tool

## Defense

Defensive measures and detection strategies:

- Patch mruby-engine source
- Sandbox untrusted scripts

## Objectives

1. Reproduce crash in engine
2. Apply and verify fix
3. Prevent DoS in engine

## Instructions

### Step 1: Execute in Sandbox

**Context**: Run script in mruby-engine to crash.

**Command** ([[commands/sandbox-execute-crash]]):
```bash
./bin/sandbox crash.rb
```

> Leads to segmentation fault or error.

### Step 2: Apply Patch

**Context**: Generate diff for fix.

**Command** ([[commands/diff-mruby-engine-patch]]):
```bash
diff --git a/ext/mruby_engine/mruby-time/src/time.c b/ext/mruby_engine/mruby-time/src/time.c
```

> Applies analogous range checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Reconnaissance]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/sandbox-execute-crash]]
- [[commands/diff-mruby-engine-patch]]

## Tools Used

- #mruby-engine
- #diff

## Tags

- #buffer-overflow
- #mruby-engine
