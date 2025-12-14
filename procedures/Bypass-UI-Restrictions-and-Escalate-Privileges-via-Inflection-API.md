---
id: proc-uuid-123
tags:
  - privilege-escalation
  - api-bypass
  - authorization-bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-put-privilege-escalation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.593Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-UI-Restrictions-and-Escalate-Privileges-via-Inflection-API

## Summary

This procedure exploits a privilege escalation vulnerability in the Inflection application by bypassing UI restrictions on the users page through direct API calls, allowing a read-only user to modify their privileges to admin level due to insufficient backend authorization checks.

## Description

In the Inflection web application, read-only users are prevented from accessing the users management page via the UI, but the underlying API endpoint for user modifications (PUT /api/users/{id}) lacks proper authorization validation. An attacker with read-only access can send unauthorized PUT requests to elevate their own or other users' privileges, leading to full administrative control. This was discovered by testing API endpoints independently of UI constraints, revealing the disconnect between frontend and backend security. The attack requires only valid read-only credentials and network access to the API, with potential for system-wide compromise including data access and configuration changes.

## Requirements

1. Valid read-only user account and authentication token for the Inflection application
2. Network access to the web application's API endpoints (typically over HTTPS)
3. API client tool like curl for sending HTTP requests
4. Knowledge of the target user ID (often obtainable from other API calls or user profile)

## Defense

Defensive measures and detection strategies:

- Implement consistent authorization checks on all API endpoints, verifying user roles server-side regardless of UI restrictions
- Use role-based access control (RBAC) with granular permissions and audit logs for privilege changes
- Monitor API logs for anomalous PUT requests from low-privilege accounts and enable rate limiting on sensitive endpoints
- Conduct regular API security testing, including authorization bypass scenarios, and apply web application firewalls (WAF) to block unauthorized modifications

## Objectives

1. Bypass frontend UI restrictions to access hidden administrative functions
2. Escalate user privileges from read-only to admin via API manipulation
3. Gain full system access for potential data exfiltration or further exploitation

## Instructions

### Step 1: Verify UI Restrictions

**Context**: Confirm the read-only limitations in the user interface to establish the baseline restriction before attempting API bypass.

Log in as a read-only user and attempt to navigate to the users management page.

**Expected Output**: Access denied or page hidden, confirming UI enforcement.

### Step 2: Identify API Endpoint

**Context**: Determine the users API endpoint structure, typically /api/users/{id}, by inspecting network traffic or documentation.

Use browser developer tools or a proxy like Burp Suite to capture requests during normal usage and infer the endpoint.

**Expected Output**: Confirmation of the PUT method for user updates.

### Step 3: Execute Privilege Escalation Request

**Context**: Send a PUT request to modify the user's role, exploiting the missing authorization check.

**Command** ([[commands/curl-put-privilege-escalation]]):
```bash
curl -X PUT -H "Authorization: Bearer YOUR_READ_ONLY_TOKEN" -H "Content-Type: application/json" -d '{"role": "admin"}' https://inflection.example.com/api/users/YOUR_USER_ID
```

> This command sends a JSON payload updating the role to 'admin'. Replace YOUR_READ_ONLY_TOKEN with your auth token (e.g., from login response) and YOUR_USER_ID with the target ID. Expected output is a 200 OK response with updated user details; errors indicate failed escalation.

### Step 4: Validate Escalation

**Context**: Test the new privileges by accessing admin-only features.

Attempt to view or modify the users page via UI or API.

**Expected Output**: Successful access to admin functions.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-put-privilege-escalation]]

## Tools Used

- [[tools/curl]]

## Tags

- [[privilege-escalation]]
- [[api-bypass]]
- [[authorization-bypass]]
