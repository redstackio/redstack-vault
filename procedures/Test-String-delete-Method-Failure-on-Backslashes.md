---
tags:
  - root-cause
  - string-delete
  - backslashes
type: procedure
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/string-delete-test-backslashes]]'
platforms:
  - Windows
  - Ruby
techniques:
  - '[[System Information Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e79b5470-0fd3-4bba-9d13-ffc10ad6ddf3
created_at: '2025-12-14T17:26:22.888Z'
updated_at: '2025-12-14T17:26:22.888Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Test String.delete Method Failure on Backslashes

## Summary

This procedure tests the String.delete method with UNUSABLE_CHARS on a string containing mixed separators and escaped backslashes to demonstrate the sanitization failure.

## Description

Implemented in string.c as rb_str_delete_bang, String.delete removes characters from UNUSABLE_CHARS but does not handle escaped backslashes correctly on Windows. Testing with a fuzz string like "FUZZ/../me/..\\please" shows that backslashes persist, allowing path traversal sequences to remain.

## Requirements

1. IRB on Windows Ruby
2. UNUSABLE_CHARS defined from prior step

## Defense

Defensive measures and detection strategies:

- Replace String.delete with gsub(/[\/:;]/, '') for path sanitization
- Use platform-specific escaping libraries
- Fuzz testing for path inputs in Ruby code

## Objectives

1. Prove delete method's inadequacy for backslashes
2. Show persistence of traversal payloads
3. Explain vulnerability root cause

## Instructions

### Step 1: Execute String.delete on Test Payload

**Context**: Apply delete to a string with traversal elements to observe that backslashes are not removed.

**Command** ([[commands/string-delete-test-backslashes]]):
```ruby
"FUZZ/../me/..\\please".delete(UNUSABLE_CHARS)
```

> Removes / and : but leaves \\ intact. Expected output: "FUZZ..me..\\please"

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/string-delete-test-backslashes]]

## Tools Used

- [[tools/IRB]]

## Tags

- root-cause
- string-delete
- backslashes
