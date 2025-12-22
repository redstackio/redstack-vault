---
id: ac-github-race-admin-001
tags:
  - race-condition
  - github
  - privilege-escalation
  - auth-bypass
  - persistence
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
verified: false
platforms:
  - GitHub Enterprise Server
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-GitHub-User-to-Org-Race-Condition]]'
step_count: 1
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:17.997Z'
description: >-
  Exploits a race condition in GitHub Enterprise Server's user-to-organization
  conversion process to gain persistent administrative access to all
  organization repositories.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# Persistent Unauthorized Admin Access via Race Condition in GitHub User-to-Organization Conversion

Multi-stage attack chain demonstrating exploitation of a race condition in GitHub Enterprise Server to achieve persistent admin access over organization repositories.

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
    A[Initiate User-to-Org Conversion] --> B[Exploit Race Condition]
    B --> C[Gain Persistent Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or scripting tool for API requests (e.g., curl for racing requests)

### Target Environment

- GitHub Enterprise Server versions 3.7 to 3.11.0 (prior to patches: 3.7.19, 3.8.12, 3.9.7, 3.10.4, 3.11.1)
- Access to a user account with conversion privileges
- Network access to the GitHub Enterprise instance

### Initial Access Requirements

- Valid user account on the target GitHub Enterprise Server
- Ability to initiate organization creation/conversion
- No prior admin access required, but timing precision for race

## Detailed Attack Procedures

### Step 1: Exploit Race Condition in Conversion
procedure: [[procedures/Exploit-GitHub-User-to-Org-Race-Condition]]

**Objective**: Bypass authentication controls during user-to-organization conversion to retain or gain unauthorized admin privileges over all repositories.

**Instructions**: Initiate the conversion process while simultaneously sending racing requests to manipulate the authentication state, exploiting the unsynchronized logic to persist admin access.

Use scripting to send parallel API requests to the conversion endpoint. For example, start the conversion via the GitHub API and immediately follow with admin action requests before validation completes.

```bash
# Example: Initiate conversion (adapt to actual API endpoints)
curl -X POST https://github.enterprise/api/user/convert-to-org -H "Authorization: token USER_TOKEN" -d '{"org_name": "target_org"}'

# Simultaneously, race with admin privilege assertion (in parallel script or tool)
curl -X POST https://github.enterprise/api/orgs/target_org/admin/actions -H "Authorization: token USER_TOKEN" -d '{"action": "grant_admin"}'
```

**Expected Output**: Successful conversion with retained admin privileges, allowing access to organization settings and repositories without re-authentication.

**Success Indicators**:
- Conversion completes but admin access persists across sessions
- Ability to modify/delete repositories in the organization
- API responses confirm admin role without expected auth prompts

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication during account conversion
2. Achieved persistent admin control over all organization repositories
3. Enabled potential data exfiltration, modification, or deletion

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
