---
tags:
  - xss
  - token-theft
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/open-xss-token-theft-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: f90064d1-9c3e-45b5-b061-80fe77a63e1b
created_at: '2025-12-13T23:56:20.467Z'
updated_at: '2025-12-13T23:56:20.467Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Token Theft

## Summary

This procedure exploits XSS to access and exfiltrate authentication tokens from localStorage in an authenticated session.

## Description

After user authentication, the injected JS can read localStorage values like authToken and alert or send them to an attacker-controlled server.

## Requirements

1. Authenticated session in the target application
2. Vulnerable endpoint
3. Browser with stored tokens

## Defense

Defensive measures and detection strategies:

- Avoid storing sensitive data in localStorage
- Use HttpOnly cookies for auth tokens

## Objectives

1. Steal auth tokens
2. Enable account takeover
3. Demonstrate full impact

## Instructions

### Step 1: Authenticate and Open URL

**Context**: Log in, then inject the payload.

Execute [[commands/open-xss-token-theft-url]] to open:

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-token-theft-payload'
```

> Payload: <script>alert(localStorage.getItem('authToken'))</script>

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/open-xss-token-theft-url]]

## Tools Used

- [[Browser]]

## Tags

- [[xss]]
- [[token-theft]]
