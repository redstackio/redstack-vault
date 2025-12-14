---
tags:
  - token-theft
  - session-hijacking
type: procedure
tools:
  - '[[tools/Python-HTTP-Server]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:46:32.152Z'
sub_techniques: []
id: bd7a7f37-8d95-4ba9-b2ec-0095671438e9
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Retrieve-and-Apply-Stolen-Session-Token

## Summary

This procedure captures the exfiltrated Meteor.loginToken from the attacker's server logs and injects it into a new browser session to hijack the victim's Rocket.Chat account.

## Description

After payload execution, the JavaScript sends the token to the attacker's HTTP server. The attacker monitors logs for the request, extracts the token, opens the Rocket.Chat site in a clean browser, and sets it in localStorage using dev tools. Meteor.js detects the token and logs in the attacker as the victim, enabling seamless session takeover without passwords.

## Requirements

1. Running HTTP server from payload hosting
2. Access to server logs for token extraction
3. Browser dev tools access on attacker's machine

## Defense

Defensive measures and detection strategies:

- Rotate session tokens frequently and use HttpOnly/Secure cookies
- Implement token binding to user agents or IPs
- Detect anomalous logins from new locations/devices

## Objectives

1. Securely retrieve the stolen token
2. Authenticate attacker as victim
3. Validate hijacked access

## Instructions

### Step 1: Monitor Server Logs

**Context**: Watch for the incoming token exfiltration request.

No command; tail the Python server output or access logs for a GET/POST to /steal with token parameter.

> Expected: Log entry like "GET /steal?token=abc123 HTTP/1.1" from victim's IP.

### Step 2: Inject Token into Browser

**Context**: Apply the token to hijack the session.

Open Rocket.Chat URL, open console, and run:

```javascript
localStorage.setItem('Meteor.loginToken', 'extracted-token-value');
```

> Browser reloads and redirects to dashboard as victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python-HTTP-Server]]

## Tags

- credential-access
- localstorage
