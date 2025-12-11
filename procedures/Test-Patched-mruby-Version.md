---
tags:
  - testing
  - mitigation
type: procedure
tools:
  - '[[tools/ASAN]]'
tactics: []
commands: []
platforms:
  - macOS
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 126cf0f6-e4fb-469f-a9b7-1edff757946e
created_at: '2025-12-11T03:47:48.025Z'
updated_at: '2025-12-11T03:47:48.025Z'
verified: false
validated: true
submitted: true
---
# Test Patched mruby Version

## Summary

This procedure tests the patched mruby version to ensure it handles invalid Time values without crashing.

## Description

Running the crash script on the patched binary should raise an ArgumentError instead of causing a segmentation fault, confirming the fix.

## Requirements

1. Patched mruby binary
2. Crash script 'crash.rb'

## Defense

Defensive measures and detection strategies:

- Validate all time inputs in code
- Log and alert on ArgumentErrors

## Objectives

1. Confirm no crash occurs
2. Verify error handling
3. Ensure vulnerability is mitigated

## Instructions

### Step 1: Execute on Patched Binary

**Context**: Run the script to test the fix.

**Command** ([[commands/mruby-patched-execute]]):
```bash
./mruby/bin/mruby crash.rb
```

> Expect ArgumentError: out of Time range.

## MITRE ATT&CK Mapping

### Tactics



### Techniques



### Sub-Techniques



## Commands Used

- [[commands/mruby-patched-execute]]

## Tools Used

- #mruby

## Tags

- #testing
- #mitigation
