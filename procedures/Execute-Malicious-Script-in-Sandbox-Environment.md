---
id: 44b5803f-e84d-4b98-8150-b531cffc3609
name: Execute Malicious Script in Sandbox Environment
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:48.214Z'
updated_at: '2025-12-11T03:47:48.214Z'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - sandbox
  - mruby
  - crash
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

# Execute Malicious Script in Sandbox Environment

## Summary

This procedure runs the malicious Ruby script in a sandboxed environment to produce a detailed crash report, confirming the denial of service impact.

## Description

The sandbox execution generates a backtrace showing the segmentation fault in mrb_ary_concat, useful for validating the exploit in isolated settings.

## Requirements

1. Sandbox binary at ./bin/sandbox
2. crash.rb file available
3. Sandbox environment configured

## Defense

Defensive measures and detection strategies:

- Restrict sandbox executions in production
- Monitor for crash reports indicating null pointer issues

## Objectives

1. Execute script in sandbox
2. Obtain detailed crash report
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Run in Sandbox

**Context**: Execute the script to generate crash report.

**Command** ([[commands/./bin/sandbox-crash.rb]]):
```bash
./bin/sandbox crash.rb
```

> Produces detailed crash report with backtrace, register context, and loaded features.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Impact]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/./bin/sandbox-crash.rb]]

## Tools Used

- #sandbox

## Tags

- #sandbox
- [[commands/./bin/sandbox-crash.rb]]
