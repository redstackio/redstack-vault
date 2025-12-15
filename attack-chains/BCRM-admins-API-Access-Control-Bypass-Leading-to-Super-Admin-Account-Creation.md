---
tags:
  - access-control
  - api-bypass
  - admin-creation
  - bcrm
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-BCRM-Admins-API-Endpoint]]'
  - '[[procedures/Create-Unauthorized-Super-Admin-via-Admins-API]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.288Z'
description: >-
  An attack chain exploiting insufficient access controls on the BCRM service's
  /admins API endpoint to create unauthorized super-admin accounts, granting
  elevated privileges.
skill_level: intermediate
impact_level: high
id: 825eabdd-7224-4cd1-8d9e-262074241a92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# BCRM /admins API Access Control Bypass Leading to Super-Admin Account Creation

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access controls in the BCRM service to create super-admin accounts.

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
    A[Discovery of Public API Endpoint] --> B[Exploitation for Account Creation]
    B --> C[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web platform
- BCRM service instances
- Publicly accessible /admins API endpoint
- Network access to the API (no authentication required for invitation endpoint)

### Initial Access Requirements

- Internet access to the target BCRM instance
- No prior credentials needed due to public accessibility
- Knowledge of LINE Official Account integration (optional for context)

## Detailed Attack Procedures

### Step 1: Discover Publicly Accessible /admins API Endpoint
procedure: [[procedures/Discover-BCRM-Admins-API-Endpoint]]

**Objective**: Identify the /admins API endpoint designed for inviting regular admins, which lacks restrictions on super-admin creation.

**Instructions**: Review BCRM documentation or test common API paths to locate the /admins endpoint. Use a tool like curl to probe the endpoint and confirm its public accessibility:

```bash
curl -X GET https://target-bcrm-instance.com/admins
```

This request should return information about the endpoint's purpose without requiring authentication, indicating insufficient access controls.

**Expected Output**: Response detailing admin invitation functionality or a list of existing admins, confirming public access.

**Success Indicators**:
- Endpoint responds without authentication
- Documentation or response hints at admin creation capabilities

### Step 2: Exploit /admins API to Create Super-Admin Account
procedure: [[procedures/Create-Unauthorized-Super-Admin-via-Admins-API]]

**Objective**: Bypass access controls by sending a crafted request to create an internal super-admin account, achieving privilege escalation.

**Instructions**: Craft a POST request to the /admins endpoint with payload specifying super-admin privileges. Use curl to send the request:

```bash
curl -X POST https://target-bcrm-instance.com/admins \
  -H "Content-Type: application/json" \
  -d '{"email": "attacker@example.com", "role": "super-admin", "invite": true}'
```

Adjust the payload based on observed API schema; the lack of validation allows super-admin role assignment.

**Expected Output**: Confirmation of account creation, such as a success message or new admin in the system.

**Success Indicators**:
- Account created with super-admin privileges
- Ability to log in with elevated access

## Attack Chain Summary

### Key Achievements

1. Discovery of vulnerable public API endpoint
2. Successful creation of unauthorized super-admin account
3. Potential for full system compromise via elevated privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
