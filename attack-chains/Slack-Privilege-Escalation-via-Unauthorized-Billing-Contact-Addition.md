---
id: ac-slack-billing-escalation-001
tags:
  - privilege-escalation
  - slack
  - api
  - billing
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
  - '[[procedures/Slack-API-Billing-Contact-Escalation]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:36.727Z'
description: >-
  Demonstrates privilege escalation in Slack where a team admin can add
  unauthorized emails to billing contacts, bypassing owner-only restrictions via
  API misuse.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Slack Privilege Escalation via Unauthorized Billing Contact Addition

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient authorization in Slack's API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticate as Team Admin] --> B[Send Unauthorized API Request]
    B --> C[Verify Escalation as Owner]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Slack workspace with team admin access
- Access to Slack API endpoints
- No specific ports; web-based API over HTTPS

### Initial Access Requirements

- Valid team admin credentials for authentication
- Network access to the Slack workspace domain (e.g., workspace.slack.com)
- No prior owner access needed, but verification requires it

## Detailed Attack Procedures

### Step 1: Authenticate as Team Admin
procedure: [[procedures/Slack-API-Billing-Contact-Escalation]]

**Objective**: Obtain a valid authentication token as a team admin to enable API requests.

**Instructions**: Log in to the Slack workspace using team admin credentials via the web interface or API to retrieve the session token (starts with 'xoxs-').

**Expected Output**: Authentication token for subsequent API calls.

**Success Indicators**:
- Token obtained and valid for admin-level requests
- No authentication errors

### Step 2: Send Unauthorized API Request to Add Billing Contact
procedure: [[procedures/Slack-API-Billing-Contact-Escalation]]

**Objective**: Exploit the API endpoint to add an unauthorized email to the billing contacts list, escalating privileges.

**Instructions**: Use an HTTP client to send a POST request to the /api/team.billing.addContact endpoint with the admin token and target email. Execute [[commands/slack-add-billing-contact]]:

```bash
curl -X POST 'https://workspace.slack.com/api/team.billing.addContact' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -d 'email=hacker@hacker.com&token=xoxs-3206092076-3204538285-3743137121-836b042620&set_active=true&_attempts=1'
```

**Expected Output**: API response indicating successful addition (e.g., {"ok":true}).

**Success Indicators**:
- No authorization error; request succeeds
- Email added without owner privileges

### Step 3: Verify Escalation by Checking Billing Contacts
procedure: [[procedures/Slack-API-Billing-Contact-Escalation]]

**Objective**: Confirm the privilege escalation by viewing the updated billing contacts as the team owner.

**Instructions**: Log in as the team owner and navigate to the billing settings in the Slack admin dashboard to inspect the contacts list.

**Expected Output**: The unauthorized email (e.g., hacker@hacker.com) appears in the billing contacts.

**Success Indicators**:
- Added email visible in owner view
- Potential for further unauthorized billing modifications

## Attack Chain Summary

### Key Achievements

1. Bypassed owner-only restrictions using admin token
2. Added arbitrary email to sensitive billing contacts
3. Demonstrated risk to financial and billing data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
