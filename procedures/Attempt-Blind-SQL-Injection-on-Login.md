---
id: proc-002
tags:
  - sqli
  - blind-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.979Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Blind-SQL-Injection-on-Login

## Summary

This procedure tests a web login form for blind SQL injection vulnerabilities by injecting payloads into credential fields, aiming to bypass authentication or infer database structure through response timing or errors, though exploitation may fail on hardened targets.

## Description

Blind SQL injection exploits unsanitized inputs in login forms where direct error-based output is suppressed, relying on boolean conditions or time delays. In this DoD report scenario, attempts on the admin panel login failed to extract data but confirmed potential issues. Prerequisites include access to the form; outcomes involve vulnerability validation for reporting or further chaining.

## Requirements

1. Accessible login form on web app
2. Proxy tool (e.g., Burp Suite) for request manipulation
3. Basic SQL payload knowledge

## Defense

Defensive measures and detection strategies:

- Use prepared statements and input parameterization in code
- Deploy intrusion detection systems (IDS) to flag anomalous queries
- Rate-limit login attempts to prevent timing attacks

## Objectives

1. Confirm SQLi vulnerability in login handling
2. Attempt authentication bypass
3. Gather evidence for escalation

## Instructions

### Step 1: Inject Basic Payload

**Context**: Test username field with tautology to bypass password check.

Intercept login POST request and modify username to ' OR 1=1 --.

> Submit form; check for successful login or generic errors indicating injection processing.

### Step 2: Time-Based Blind Test

**Context**: Use sleep functions to detect true/false conditions via delays.

Inject payload like admin' AND IF(1=1, SLEEP(5), 0) -- into password.

> Expected: 5-second delay on true condition, confirming blind SQLi; no delay or error otherwise.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sqli]]
- [[injection]]
