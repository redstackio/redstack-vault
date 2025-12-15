---
tags:
  - idor
  - privilege-escalation
  - web
  - api
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
  - '[[procedures/Exploit-IDOR-in-Veris-Rule-Creation-Endpoint]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.385Z'
description: >-
  An authenticated user exploits an Insecure Direct Object Reference (IDOR)
  vulnerability in the Veris application's rule creation API to create rules for
  unauthorized groups and venues, achieving privilege escalation.
skill_level: intermediate
impact_level: high
id: d91f9fef-ab72-4468-b3a1-b61069685b5d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR Privilege Escalation in Veris for Unauthorized Rule Creation in Arbitrary Groups and Venues

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in the Veris application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Capture Original Request] --> B[Modify Parameters]
    B --> C[Send Tampered Request]
    C --> D[Confirm Rule Creation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or a proxy like Burp Suite for request interception

### Target Environment

- Veris web application
- Authenticated user session
- Access to group_id and venue_id of target unauthorized resources (e.g., via enumeration or known values)

### Initial Access Requirements

- Valid authenticated session in Veris
- Network access to the Veris API endpoints
- No prior elevated privileges needed

## Detailed Attack Procedures

### Step 1: Capture the Original Request
procedure: [[procedures/Exploit-IDOR-in-Veris-Rule-Creation-Endpoint]]

**Objective**: Intercept the legitimate HTTP request for creating a rule in the user's own group and venue to understand the request structure.

**Instructions**: Use browser developer tools or a proxy to monitor network traffic while creating a test rule in your authorized group and venue. Identify the POST request to the rule creation endpoint, noting the group_id and venue_id parameters.

**Expected Output**: Captured HTTP request with JSON payload including group_id and venue_id specific to your resources.

**Success Indicators**:
- Request intercepted successfully
- Parameters like group_id and venue_id visible in the request body or query

### Step 2: Modify the Parameters
procedure: [[procedures/Exploit-IDOR-in-Veris-Rule-Creation-Endpoint]]

**Objective**: Tamper with the group_id and venue_id to target unauthorized groups and venues.

**Instructions**: Edit the captured request by replacing the values of group_id and venue_id with those of the target unauthorized resources. For example, if using curl, construct the modified request as follows (replace placeholders with actual values):

```bash
curl -X POST 'https://veris.example.com/api/rules' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"group_id": "TARGET_GROUP_ID", "venue_id": "TARGET_VENUE_ID", "rule_data": "your_rule_payload"}'
```

**Expected Output**: Modified request ready for replay, with altered IDs.

**Success Indicators**:
- Parameters successfully changed to unauthorized values
- Request structure remains valid

### Step 3: Send the Modified Request
procedure: [[procedures/Exploit-IDOR-in-Veris-Rule-Creation-Endpoint]]

**Objective**: Replay the tampered request to the server to attempt unauthorized rule creation.

**Instructions**: Submit the modified HTTP request to the rule creation endpoint using the same authentication token.

**Expected Output**: Server processes the request without additional validation.

**Success Indicators**:
- Request sent without errors
- No immediate authorization denial

### Step 4: Confirm Rule Creation
procedure: [[procedures/Exploit-IDOR-in-Veris-Rule-Creation-Endpoint]]

**Objective**: Verify that the rule was created for the targeted unauthorized group and venue.

**Instructions**: Check the server's response and, if possible, log in as an admin or query the API to confirm the new rule exists in the targeted resources.

**Expected Output**: Success response (e.g., 200 OK with rule ID) confirming creation.

**Success Indicators**:
- Rule appears in the unauthorized group/venue
- No access denied errors

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization checks via IDOR
2. Achieved privilege escalation by creating rules in arbitrary groups and venues
3. Demonstrated potential for unauthorized control over other users' resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
