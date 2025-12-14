---
tags:
  - idor
  - account-manipulation
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-to-Disable-Owner-Account]]'
step_count: 1
techniques:
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:30:18.271Z'
description: >-
  An Insecure Direct Object Reference (IDOR) vulnerability in the Multiple Admin
  feature allows a malicious admin to disable the owner's account, locking them
  out indefinitely.
skill_level: intermediate
impact_level: high
id: f627c34c-7a73-45bd-a387-056e2f10eb85
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# IDOR in Linktree Multiple Admin Feature to Permanently Disable Owner Account

Multi-stage attack chain demonstrating a complete attack workflow targeting the Linktree application's Multiple Admin feature via an IDOR vulnerability.

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
    A[Initial Access as Malicious Admin] --> B[Exploit IDOR to Disable Owner]
    B --> C[Account Lockout Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual exploitation via web interface or browser tools)

### Target Environment

- Web application (Linktree platform)
- Required services/ports: HTTPS (443)
- Network access requirements: Valid admin credentials for the target account

### Initial Access Requirements

- Credential requirements: Malicious admin account with access to the Multiple Admin feature
- Network position: Direct access to the Linktree web application
- Prior access needed: Owner must have granted admin access to the attacker

## Detailed Attack Procedures

### Step 1: Exploit IDOR in Multiple Admin Feature
procedure: [[procedures/Exploit-IDOR-to-Disable-Owner-Account]]

**Objective**: Use insecure direct object reference to access and disable the owner's admin account, resulting in permanent lockout.

**Instructions**: Log in as a malicious admin and navigate to the Multiple Admin management interface. Identify the owner's account ID through enumeration or direct reference in the UI. Modify the request to target the owner's user ID directly, bypassing authorization checks to trigger the disable action.

**Expected Output**: Confirmation that the owner's account has been disabled, with the owner unable to log in or access their Linktree account.

**Success Indicators**:
- Owner account status changes to disabled in the admin panel
- Attempted login by owner fails with access denied error

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access owner account controls
2. Permanently disabled the owner's admin access
3. Achieved indefinite lockout without recovery options

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Access Removal]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
