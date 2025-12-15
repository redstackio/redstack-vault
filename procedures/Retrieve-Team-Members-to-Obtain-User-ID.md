---
id: proc-retrieve-team-members-user-id
tags:
  - reconnaissance
  - api
  - user-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-team-members]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:51.538Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve-Team-Members-to-Obtain-User-ID

## Summary

This procedure involves authenticating as an app member and querying the team members API to extract the attacker's user ID, which is necessary for targeting the privilege escalation update. It leverages the exposed API response to gather internal identifiers without additional permissions.

## Description

In the Fabric.io application, the team members endpoint returns detailed user information, including IDs, for any authenticated member. This step is part of a privilege escalation attack where the ID is used to craft a malicious update request. The target environment is the web-based SaaS platform, requiring an active session. Expected outcomes include obtaining the exact user ID (e.g., a MongoDB ObjectID like 54aa4ab19ea6961359001260) while confirming the current non-admin role.

## Requirements

1. Valid login credentials for a non-admin app member account.
2. Access to browser developer tools or a tool like curl/Burp Suite for API requests.
3. Knowledge of the organization ID (orgid) and app ID (appid) from the app settings page.
4. Active HTTPS session to fabric.io.

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict team members API to admins only.
- Log and monitor API calls to /team_members for unusual access patterns from non-admin users.
- Use rate limiting on user enumeration endpoints to prevent reconnaissance.

## Objectives

1. Gather the attacker's user ID for targeted updates.
2. Confirm current permissions to ensure escalation potential.
3. Identify other team members for potential follow-on attacks.

## Instructions

### Step 1: Authenticate and Navigate to Team Members

**Context**: Log in to establish a session and reach the team members view, which triggers the API call.

**Command** ([[commands/get-team-members]]):
```bash
curl -X GET "https://fabric.io/api/v2/organizations/[orgid]/apps/[appid]/team_members" \
  -H "Cookie: _fabric_session=..." \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0"
```

> This command sends a GET request to fetch the team list. Replace [orgid] and [appid] with actual values from the URL. Expected output is a JSON array of users, e.g., {"name":"alice","email":"alice@mailinator.com","id":"54aa4ab19ea6961359001260","is_activated":true,"is_admin":false}.

### Step 2: Extract User ID

**Context**: Parse the response to isolate the ID of the target user (attacker's own account).

No specific command; manually inspect the JSON response or use jq for parsing if automated:

```bash
curl ... | jq '.[] | select(.name == "alice") | .id'
```

> Outputs the user ID string for use in the next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/get-team-members]]

## Tools Used


## Tags

- reconnaissance
- api
- user-discovery
