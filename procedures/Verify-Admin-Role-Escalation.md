---
id: proc-verify-admin-role-escalation
tags:
  - verification
  - privilege-escalation
  - api
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/get-team-members]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.526Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Admin-Role-Escalation

## Summary

This procedure confirms the success of the privilege escalation by re-querying the team members API and checking for the updated admin status, then testing admin-specific actions like managing other users.

## Description

Post-exploitation verification in Fabric.io involves refreshing the API response to observe the role change from member to admin. This step validates the vulnerability's impact in the web API environment, using the same authenticated session. Expected outcomes include visible admin flag and access to restricted features, demonstrating full team control.

## Requirements

1. Successful completion of prior escalation procedure.
2. Active session post-update.
3. Access to team management UI or API for testing actions.

## Defense

Defensive measures and detection strategies:

- Implement session invalidation or role re-verification after updates.
- Monitor for rapid role changes in audit logs and alert on unauthorized escalations.
- Use client-side checks to prevent UI access without server confirmation.

## Objectives

1. Confirm the admin role has been applied.
2. Validate impact by performing admin actions.
3. Ensure persistence of the escalation.

## Instructions

### Step 1: Re-Query Team Members

**Context**: Send the GET request again to check the updated role in the response.

**Command** ([[commands/get-team-members]]):
```bash
curl -X GET "https://fabric.io/api/v2/organizations/[orgid]/apps/[appid]/team_members" \
  -H "Cookie: _fabric_session=..." \
  -H "User-Agent: Mozilla/5.0 ..."
```

> Expected output: JSON with "is_admin": true for the escalated user, e.g., {"id":"54aa4ab19ea6961359001260","is_admin":true}.

### Step 2: Test Admin Actions

**Context**: Attempt restricted operations like changing another user's role to confirm privileges.

Navigate to the team members UI and try editing/deleting a user; or craft a similar PUT for another account.

> Success: UI allows actions previously denied; API responds positively to admin-only requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/get-team-members]]

## Tools Used


## Tags

- verification
- privilege-escalation
- api
