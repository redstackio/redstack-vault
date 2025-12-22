---
id: proc-uuid-4567-8901
tags:
  - path-traversal
  - testing
  - restriction-bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:05.735Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Test-Normal-Path-Restrictions

## Summary

This procedure tests standard HTTP requests to files outside the 'public' directory, confirming the module returns 404 errors due to its error handling, before attempting bypass.

## Description

Normal clients (browsers, standard curl) normalize ../ sequences, causing the module to resolve paths within the root and trigger 404 for out-of-bounds requests. This verifies the baseline restriction before using --path-as-is to exploit.

## Requirements

1. Running vulnerable server
2. Access to localhost:80
3. Basic HTTP client

## Defense

Defensive measures and detection strategies:

- Enable detailed access logs to detect traversal attempts
- Use WAF rules to block ../ in URLs
- Regularly test for path traversal in web apps

## Objectives

1. Confirm restrictions work normally
2. Identify normalization behavior
3. Set up for exploitation step

## Instructions

### Step 1: Send Normal Traversal Request

**Context**: Attempt a request like http://127.0.0.1:80/../etc/passwd using a browser or curl without flags to observe blocking.

**Command** (Example with curl):
```bash
curl http://127.0.0.1:80/../etc/passwd
```

> Expected output: 404 Not Found, as the path is normalized and outside root.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- None (uses basic curl or browser)

## Tools Used

- [[tools/curl]]

## Tags

- path-traversal
- testing
