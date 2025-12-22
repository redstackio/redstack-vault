---
id: uuid-for-proc2
tags:
  - recon
  - user-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:31:43.090Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Acquire-Target-User-Email

## Summary

This procedure outlines methods to obtain a target user's email address, essential for hijacking existing accounts or registering new ones in the JWT exploitation attack against the Newspack plugin.

## Description

Email addresses can be gathered from public sources, previous interactions, or data breaches. In this attack scenario, the email populates the JWT `email` claim, allowing the attacker to impersonate the user upon successful bypass. No direct interaction with the target site is needed beyond reconnaissance.

## Requirements

1. Access to public information sources (e.g., social media, leaks)
2. Target site context for relevance
3. Basic OSINT skills

## Defense

Defensive measures and detection strategies:

- Encourage users to use unique emails
- Monitor for suspicious login attempts from known emails
- Implement email verification on registration

## Objectives

1. Identify a valid target email
2. Enable JWT payload customization
3. Facilitate account hijacking

## Instructions

### Step 1: Gather from Public Sources

**Context**: Use OSINT to find the target's email.

**Command** (No code; manual):
```bash
# Example: Search data breach databases or site footers
```

> Manually search for `test@example.org` in leaks or site contact pages. Expected: Confirmed email.

### Step 2: Validate Email Format

**Context**: Ensure the email is suitable for JWT.

**Command** (Browser Console):
```javascript
let email = 'test@example.org'; console.log(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email));
```

> Outputs `true` if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[user-discovery]]
