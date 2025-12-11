---
id: d1065fb1-951e-4ceb-83f7-e6e56eb5c7e6
name: Execute Malicious Script with mruby Interpreter
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:48.230Z'
updated_at: '2025-12-11T03:47:48.230Z'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - denial-of-service
  - mruby
  - execution
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
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1499]]'
---

# Execute Malicious Script with mruby Interpreter

## Summary

This procedure executes a malicious Ruby script using the mruby interpreter to trigger a segmentation fault due to null pointer dereference, resulting in a crash and potential denial of service.

## Description

By running the crafted script, the vulnerability in code generation is exploited, causing improper stack handling and a crash in ary_concat. This is particularly impactful in production environments using mruby, such as e-commerce scripting engines.

## Requirements

1. mruby binary installed at ./dev/bin/mruby
2. Crafted crash.rb file available
3. Execution privileges on the target system

## Defense

Defensive measures and detection strategies:

- Sanitize and validate input scripts before execution
- Implement crash monitoring and rate limiting on mruby-based services

## Objectives

1. Trigger the vulnerability through script execution
2. Cause interpreter crash
3. Demonstrate denial of service potential

## Instructions

### Step 1: Run the Script

**Context**: Execute the crash.rb script to induce the segmentation fault.

**Command** ([[commands/./dev/bin/mruby-crash.rb]]):
```bash
./dev/bin/mruby crash.rb
```

> This command runs the script, resulting in 'crash.rb:1:3: '*' interpreted as argument prefix' followed by Segmentation fault: 11.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Impact]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/./dev/bin/mruby-crash.rb]]

## Tools Used

- #mruby

## Tags

- [[Endpoint Denial of Service]]
- #mruby
