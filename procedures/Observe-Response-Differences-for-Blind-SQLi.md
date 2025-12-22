---
tags:
  - blind-sqli
  - response-analysis
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.347Z'
sub_techniques: []
id: f85b7196-6f50-44ff-857e-be463fd9bfff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Response Differences for Blind SQLi

## Summary

This procedure observes server response behaviors to distinguish between successful and failed SQL conditions in a blind SQL injection scenario, enabling boolean-based exploitation.

## Description

For the www.ibm.com vulnerability, successful SQL queries (no syntax error) result in an endless redirect loop, while failed queries (syntax error) return a 500 status code. This difference allows inference of boolean conditions without direct data output, crucial for blind exfiltration.

## Requirements

1. Tool for sending and timing HTTP requests (e.g., curl)
2. Ability to detect redirects and status codes
3. Knowledge of boolean SQL logic

## Defense

Defensive measures and detection strategies:

- Normalize response behaviors to avoid information leakage
- Implement rate limiting on suspicious paths
- Log and alert on repeated 500 errors or redirect loops

## Objectives

1. Identify response patterns for true/false conditions
2. Confirm endless redirect for success and 500 for failure
3. Set up for conditional payload testing

## Instructions

### Step 1: Test True Condition Payload

**Context**: Inject a always-true condition to observe success response.

**Command** ([[commands/curl-send-request]]):
```bash
curl -i -L --max-redirs 1 "https://www.ibm.com/'AND1=1--"
```

> Limits redirects to detect loop; expect redirect behavior indicating success.

### Step 2: Test False Condition Payload

**Context**: Inject a always-false condition to observe failure response.

**Command** ([[commands/curl-send-request]]):
```bash
curl -i "https://www.ibm.com/'AND1=2--"
```

> Expect 500 error confirming failure distinction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-request]]

## Tools Used


## Tags

- [[blind-sqli]]
- [[web]]
