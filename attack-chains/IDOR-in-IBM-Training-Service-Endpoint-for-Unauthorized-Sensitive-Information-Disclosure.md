---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - information-disclosure
  - ibm
  - web
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2025-03-21T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-IBM-Training-Service]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:13.483Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the IBM training service endpoint to disclose sensitive
  information without proper authorization checks.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in IBM Training Service Endpoint for Unauthorized Sensitive Information Disclosure

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Discovery]
    B --> C[Objective]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[tools/Burp-Suite]]

### Target Environment

- Web platform
- IBM training service endpoint
- Network access to the public-facing web application

### Initial Access Requirements

- Valid user session or authentication to the IBM training service (low-privilege account)
- Ability to interact with the web endpoint
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Exploit IDOR for Information Disclosure
procedure: [[procedures/Exploit-IDOR-in-IBM-Training-Service]]

**Objective**: Manipulate object references in API requests to access unauthorized sensitive data from the IBM training service endpoint.

**Instructions**: Authenticate to the IBM training service and identify the endpoint handling object references (e.g., /training/{id}). Use a tool like Burp Suite to intercept requests and modify the ID parameter to reference another user's object. For example, change the user ID from your own to another valid ID.

Execute a test request using [[commands/curl-idor-test]] to verify unauthorized access:

```bash
curl -X GET "https://training.ibm.com/api/user/123" -H "Authorization: Bearer your_token" -H "Content-Type: application/json"
```

Replace '123' with a different user ID. If successful, the response will contain sensitive data not belonging to the authenticated user.

**Expected Output**: JSON response with sensitive information such as user training records or personal details.

**Success Indicators**:
- Response contains data for a different user or object
- No authorization error (e.g., 403 Forbidden)
- Disclosure of sensitive fields like names, emails, or training progress

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls via IDOR to disclose sensitive training data
2. Demonstrated unauthorized information access without privilege escalation
3. Highlighted improper authorization checks in the endpoint

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2025-03-21T00:00:00Z*
