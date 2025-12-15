---
id: proc-uuid-2
tags:
  - nextcloud
  - user-enumeration
  - admin-creation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-ocs-users-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:43.058Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Unauthorized-User-Creation-on-Nextcloud-Server

## Summary

This procedure verifies successful exploitation by querying the Nextcloud server for the newly created user and checking group membership, confirming unauthorized admin access.

## Description

After the malicious deeplink triggers a POST to `/ocs/v1.php/cloud/users`, use the OCS API to list users and groups. If the victim lacks admin access, target other controllers. Assumes attacker has alternative server access (e.g., existing creds) or uses the new user for login. Expected outcome: Confirmation of 'hacker' user in admin group, enabling further persistence.

## Requirements

1. Access to Nextcloud server (admin creds or new user details)
2. Network connectivity to OCS API endpoint
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Enable API rate limiting and audit logs for user creation events
- Require MFA for admin actions
- Review desktop client logs for anomalous deeplink handling
- Use WAF to block suspicious POST patterns

## Objectives

1. Confirm new user existence and group assignment
2. Validate exploit success via login test
3. Identify escalation potential

## Instructions

### Step 1: Query Users via OCS API

**Context**: Retrieve the user list to check for the injected user.

**Command** ([[commands/curl-ocs-users-query]]):
```bash
curl -X GET "https://{instance}/ocs/v2.php/cloud/users" -u "admin:{admin-pass}" -H "OCS-APIRequest: true"
```

> Parses XML/JSON for 'hacker' user. Expected: Response includes `<users><element>hacker</element></users>`.

### Step 2: Check Group Membership and Test Login

**Context**: Verify admin group and authenticate with new creds.

Query groups:
```bash
curl -X GET "https://{instance}/ocs/v2.php/cloud/groups" -u "hacker:{new-pass}" -H "OCS-APIRequest: true"
```

Then test login via web interface or API.

> Expected: 'admin' in groups list; successful auth confirms access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

-

## Commands Used

- [[commands/curl-ocs-users-query]]

## Tools Used

-

## Tags

- nextcloud
- api-query
- verification
