---
tags:
  - privilege-escalation
  - api-bypass
  - authorization-bypass
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Bypass-UI-Restrictions-and-Escalate-Privileges-via-Inflection-API]]
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.598Z'
description: >-
  A multi-stage attack exploiting insufficient backend authorization in the
  Inflection application's users API, allowing read-only users to escalate
  privileges to admin level by bypassing UI restrictions.
skill_level: intermediate
impact_level: high
id: cc157834-c3e6-4506-9a6b-ef568a88fb19
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Privilege Escalation in Inflection: Read-Only to Admin via API Authorization Bypass

Multi-stage attack chain demonstrating a complete privilege escalation workflow in the Inflection application by exploiting missing API authorization checks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Observe UI Restrictions] --> B[Exploit API Endpoint]
    B --> C[Privilege Escalation Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web application (Inflection platform)
- Access to the application as a read-only user
- Network access to the API endpoints

### Initial Access Requirements

- Valid read-only user credentials
- Browser or API client for testing
- No prior admin access needed

## Detailed Attack Procedures

### Step 1: Identify UI Restrictions on Users Page
procedure: [[procedures/Bypass-UI-Restrictions-and-Escalate-Privileges-via-Inflection-API]]

**Objective**: Confirm that the UI prevents read-only users from accessing the users management page, highlighting the frontend restriction.

**Instructions**: Log in to the Inflection application as a read-only user and navigate to the users section. Observe that the page is hidden or access is denied due to permission checks in the UI.

**Expected Output**: UI displays an error or hides the users page, indicating read-only restrictions.

**Success Indicators**:
- Users page is inaccessible via the interface
- No admin features visible to read-only user

### Step 2: Test and Exploit API Endpoint for Privilege Modification
procedure: [[procedures/Bypass-UI-Restrictions-and-Escalate-Privileges-via-Inflection-API]]

**Objective**: Bypass UI restrictions by directly calling the users API endpoint with a PUT request to modify user privileges, exploiting the lack of backend authorization.

**Instructions**: Use [[commands/curl-put-privilege-escalation]] to send a PUT request to the users API endpoint, targeting your own user account to elevate privileges to admin. Replace placeholders with actual values like the target user ID and API base URL.

```bash
curl -X PUT -H "Authorization: Bearer YOUR_READ_ONLY_TOKEN" -H "Content-Type: application/json" -d '{"role": "admin"}' https://inflection.example.com/api/users/YOUR_USER_ID
```

Verify the change by checking your account permissions or attempting admin actions.

**Expected Output**: HTTP 200 response confirming the privilege update, with the user's role changed to admin.

**Success Indicators**:
- API request succeeds without authorization error
- User privileges elevated to admin level
- Access to previously restricted features granted

## Attack Chain Summary

### Key Achievements

1. Bypassed UI-enforced restrictions on read-only users
2. Exploited missing API authorization to perform unauthorized privilege changes
3. Achieved full administrative access, compromising system control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
