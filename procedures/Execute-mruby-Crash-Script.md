---
tags:
  - denial-of-service
  - mruby
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
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: c3e250a9-f93f-4bbf-95c5-4ac65b3533ae
created_at: '2025-12-11T03:47:48.031Z'
updated_at: '2025-12-11T03:47:48.031Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1499]]'
---
# Execute mruby Crash Script

## Summary

This procedure executes a crafted Ruby script in mruby to trigger a buffer overflow, resulting in process crashes and denial of service.

## Description

Running the script with mruby binary causes the mrb_time_asctime function to overflow due to unchecked snprintf on invalid tm fields, leading to segmentation faults or buffer overreads. This can be used to disrupt mruby-based services like shopify-scripts.

## Requirements

1. Compiled mruby binary
2. Crash script file 'crash.rb'
3. macOS environment

## Defense

Defensive measures and detection strategies:

- Use patched mruby versions with range checks
- Monitor process crashes and anomalous memory access

## Objectives

1. Achieve denial of service through crash
2. Observe varying crash behaviors
3. Prepare for debugging

## Instructions

### Step 1: Run the Script

**Context**: Execute the script to trigger the vulnerability.

**Command** ([[commands/mruby-execute-crash]]):
```bash
./dev/bin/mruby crash.rb
```

> This runs the script, leading to a segmentation fault in some executions due to buffer overflow.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Reconnaissance]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/mruby-execute-crash]]

## Tools Used

- #mruby

## Tags

- [[Endpoint Denial of Service]]
- #mruby
