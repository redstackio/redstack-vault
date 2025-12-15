---
tags:
  - nextcloud
  - testing
  - web-application
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-nextcloud-admin-removal-attempt]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:44.578Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bc36206d-9a1c-4dc2-b130-504e5e45964d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Test-Normal-Admin-Group-Removal-in-Nextcloud

## Summary

This procedure tests the standard group toggle functionality in Nextcloud to confirm that attempts to remove an admin from the admin group are blocked by server-side validation, setting the stage for identifying bypass opportunities.

## Description

In Nextcloud, the group management endpoint at /index.php/settings/ajax/togglegroups.php handles toggling user group memberships via POST requests with username and group parameters. Server-side logic explicitly prevents admins from removing themselves or other admins from the 'admin' group to maintain administrative integrity. This procedure demonstrates a normal request that fails due to this restriction, highlighting the intended security control. It requires authenticated admin access and is typically used in vulnerability assessment to baseline expected behavior before attempting exploits.

## Requirements

1. Authenticated session as a Nextcloud admin user
2. Valid request token from the Nextcloud session
3. Network access to the Nextcloud instance
4. Tools like curl for sending HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and trimming on all parameters in group management endpoints
- Log all group modification attempts, especially for admin users, and alert on failures
- Use role-based access controls (RBAC) that enforce checks beyond simple string equality

## Objectives

1. Verify the server-side block on admin self-removal
2. Capture the error response for analysis
3. Confirm authentication and endpoint accessibility

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain necessary session cookies and request token by logging in as an admin via the Nextcloud web interface or API.

Inspect browser developer tools or use a login request to extract the 'requesttoken' and session cookies.

### Step 2: Send Normal Removal Request

**Context**: Attempt to remove the admin user from the admin group using exact parameters to trigger the restriction.

**Command** ([[commands/curl-nextcloud-admin-removal-attempt]]):
```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: oc_session=your_session; requesttoken=your_token' \
  -d 'username=admin&group=admin'
```

> This command sends a POST request with standard parameters. The server checks for exact match on 'admin' and blocks the action, returning an error JSON response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-nextcloud-admin-removal-attempt]]

## Tools Used


## Tags

- [[nextcloud]]
- [[web-application]]
- [[testing]]
