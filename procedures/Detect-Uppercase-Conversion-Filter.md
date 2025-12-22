---
id: proc-uuid-003
tags:
  - xss
  - filter-detection
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.617Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-Uppercase-Conversion-Filter

## Summary

This procedure identifies an uppercase conversion filter applied to the reflected serial input, which sanitizes lowercase letters and breaks standard JavaScript function names like alert().

## Description

Testing with lowercase inputs reveals that the application converts the serial parameter to uppercase before reflection, rendering JavaScript keywords like "alert" as "ALERT", which browsers do not execute. This filter is a partial defense but can be bypassed. Build on prior reflection confirmation.

## Requirements

1. Web browser for testing and inspection
2. Completion of input reflection observation
3. Understanding of JavaScript case sensitivity

## Defense

Defensive measures and detection strategies:

- Combine uppercase filtering with proper encoding
- Test for bypasses like encoding in security audits
- Implement content security policy (CSP) to block inline scripts

## Objectives

1. Confirm application of uppercase filter
2. Demonstrate failure of standard XSS payloads
3. Identify need for filter bypass techniques

## Instructions

### Step 1: Test with Lowercase Script

**Context**: Submit a basic XSS payload to observe conversion.

Use [[tools/Browser]] to load:

```url
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=<script>alert('xss')</script>
```

> Inspect source; expect "<SCRIPT>ALERT('XSS')</SCRIPT>", which does not execute due to case.

### Step 2: Verify Non-Execution

**Context**: Confirm the filter prevents JS run.

Attempt to trigger; no alert should appear.

> This indicates the uppercase transformation as the blocking mechanism.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[xss]]
- [[filter-detection]]
