---
id: uuid-execute-js-priv-esc
tags:
  - xss-execution
  - privilege-escalation
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-13T23:52:38.736Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-JavaScript-for-Privilege-Escalation

## Summary

This procedure triggers the stored XSS payload in Rocket.Chat to execute JavaScript in the victim's browser, manipulating the application's client-side state to escalate privileges for all affected users, such as granting admin roles.

## Description

Upon viewing the infected message, the unsanitized JavaScript runs in the context of the Rocket.Chat web app, allowing access to session storage, DOM manipulation, and API calls. Attackers can target user role endpoints or local storage to elevate privileges universally. This affects web sessions and chains into further exploits. Prerequisites: Injected payload from prior step; victim interaction. Expected outcomes: Elevated access confirmed via UI or API.

## Requirements

1. Victim views the channel with the injected message
2. Target Rocket.Chat instance vulnerable to client-side manipulation
3. Knowledge of app's internal APIs (e.g., via dev tools inspection)
4. Network access for any exfiltration

## Defense

Defensive measures and detection strategies:

- Strict CSP headers to prevent JS execution
- Server-side role validation, not client-side
- Audit logs for unexpected privilege changes
- User education on avoiding suspicious messages

## Objectives

1. Execute JS payload on message render
2. Modify user privileges via app APIs
3. Confirm escalation for multiple users

## Instructions

### Step 1: Induce Victim View

**Context**: Ensure the payload triggers by having a victim load the channel.

Direct victim to the channel or wait for natural viewing.

### Step 2: Script Execution

**Context**: The payload runs automatically; customize for escalation, e.g., POST to role update endpoint.

Injected script example:

```javascript
fetch('/api/v1/users.setRole', {method: 'POST', body: JSON.stringify({userId: 'victimId', role: 'admin', roomId: 'roomId'}), headers: {'X-Auth-Token': localStorage.getItem('authToken'), 'X-User-Id': localStorage.getItem('userId')}});
```

> This uses stored auth tokens to set admin role. Expected output: API response with success; UI reflects new privileges.

### Step 3: Validate Escalation

**Context**: Test elevated access.

Attempt admin actions like user management.

> Expected output: Successful admin operations.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[privilege-escalation]]
- [[client-side-exploitation]]
