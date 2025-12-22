---
tags:
  - python
  - mmap
  - observation
type: procedure
tools:
  - '[[tools/mmap-test-py]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Windows
  - Linux
techniques:
  - '[[Data from Local System]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 652fdae1-2b71-426f-b51d-178db6472d80
created_at: '2025-12-14T17:25:13.161Z'
updated_at: '2025-12-14T17:25:13.161Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Observe-Leaked-Memory-Data-or-Segfault

## Summary

This procedure inspects the output from the exploitative read to identify leaked data from adjacent pages or handles segfaults if the access faults, confirming the vulnerability's impact.

## Description

After boundary exploitation, if adjacent pages are readable, sensitive data (e.g., other process memory) is leaked; otherwise, a segfault occurs on invalid access. This final step validates the info disclosure on Python 2.7.12 systems like Windows 7 (direct demo) or Linux (adjusted). Outcomes demonstrate major leak potential.

## Requirements

1. Data from prior read() or readline()
2. Python 2.7.12 environment
3. System monitoring for crashes

## Defense

Defensive measures and detection strategies:

- Enable core dumps and analyze for mmap-related faults
- Use sandboxing for Python scripts
- Regularly audit memory access patterns

## Objectives

1. Extract and analyze leaked data
2. Detect and log segfaults
3. Assess impact of disclosure

## Instructions

### Step 1: Analyze Read Output

**Context**: Check for extra data or error conditions.

```python
# Post-read analysis
original_size = 500  # From resize
if len(leaked_data) > original_size:
    print("Leak detected: Extra data from adjacent memory")
    print(repr(leaked_data[original_size:]))  # Show leaked portion
else:
    print("No leak or segfault occurred")
```

> If leak, prints binary data from adjacent pages; else, notes segfault (e.g., AccessViolation on Windows).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/mmap-test-py]]

## Tags

- [[Python]]
- [[mmap]]
- [[observation]]
