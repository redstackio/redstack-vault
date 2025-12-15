---
tags:
  - idor
  - access-control
  - data-exposure
  - veris
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-idor-exploit]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-IDOR-to-Access-Organizational-Rules]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
description: >-
  A critical Insecure Direct Object Reference vulnerability in the Veris
  platform allowing unauthorized remote access to sensitive rules of any
  organization by manipulating identifiers.
skill_level: intermediate
impact_level: high
id: a6c0fb61-a385-4e9b-abb0-fdf00ecf2c9f
created_at: '2025-12-14T17:25:23.271Z'
updated_at: '2025-12-14T17:25:23.271Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Veris Platform to Access Any Organization's Rules Remotely

Multi-stage attack chain demonstrating a complete attack workflow exploiting an Insecure Direct Object Reference (IDOR) in the Veris platform. An attacker with basic access can manipulate object identifiers in API requests to retrieve sensitive rules belonging to other organizations, leading to unauthorized data exposure and potential further compromise.

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
    A[Identify Vulnerable Endpoint] --> B[Manipulate Identifier for Unauthorized Access]
    B --> C[Retrieve Sensitive Rules]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Target OS/Platform: Web application (Veris platform)
- Required services/ports: HTTPS on standard web ports (443)
- Network access requirements: Internet access to the Veris platform endpoint

### Initial Access Requirements

- Credential requirements: Valid user account in the Veris platform (authenticated session)
- Network position: External remote access
- Prior access needed: Basic authentication to the platform

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint

procedure: [[procedures/Exploit-IDOR-to-Access-Organizational-Rules]]

**Objective**: Locate the API endpoint that uses direct object references for organizational rules without proper access controls.

**Instructions**: Use a proxy tool like [[tools/Burp-Suite]] to intercept and analyze legitimate requests to the Veris platform. Identify endpoints handling rules retrieval, such as those using organization IDs in URLs or parameters (e.g., /api/rules/{org_id}).

**Expected Output**: Captured request showing identifier usage, e.g., GET /api/rules/12345 where 12345 is the user's own org ID.

**Success Indicators**:
- Endpoint identified with manipulable identifier
- Request format confirmed

### Step 2: Manipulate Identifier for Unauthorized Access

procedure: [[procedures/Exploit-IDOR-to-Access-Organizational-Rules]]

**Objective**: Alter the object identifier in the request to access rules from a target organization, bypassing access controls.

**Instructions**: Modify the intercepted request by changing the organization ID to a target org's ID (e.g., enumerate or guess IDs like 12346). Replay the request using [[commands/curl-idor-exploit]]:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" "https://veris.example.com/api/rules/12346" -X GET
```

**Expected Output**: JSON response containing the target organization's rules data.

**Success Indicators**:
- Unauthorized rules retrieved without errors
- Sensitive data exposed in response

## Attack Chain Summary

### Key Achievements

1. Identified IDOR in rules retrieval endpoint
2. Manipulated identifiers to access arbitrary organizations' data
3. Achieved remote unauthorized data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
