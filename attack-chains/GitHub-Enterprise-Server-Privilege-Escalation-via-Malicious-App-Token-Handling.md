---
tags:
  - github
  - privilege-escalation
  - access-control
  - token
  - github-apps
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Malicious-GitHub-App-for-Token-Escalation]]'
step_count: 1
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:46.963Z'
description: >-
  An attack chain exploiting improper authorization in GitHub Enterprise
  Server's GitHub Apps token handling to escalate a scoped user-to-server token
  to full organization admin/owner privileges.
skill_level: intermediate
impact_level: high
id: 0e49a26b-5e81-44b8-8726-8d908cff388a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# GitHub Enterprise Server Privilege Escalation via Malicious App Token Handling

Multi-stage attack chain demonstrating a complete attack workflow exploiting CVE-2022-23741 in GitHub Enterprise Server.

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
    A[Install Malicious App] --> B[Token Escalation]
    B --> C[Full Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on GitHub UI and API access)

### Target Environment

- GitHub Enterprise Server versions prior to 3.3.17, 3.4.12, 3.5.9, or 3.6.5
- Web platform with GitHub Apps enabled
- Organization with admin installation permissions for apps

### Initial Access Requirements

- Valid organization account with admin permissions to install GitHub Apps
- Access to create or control a GitHub App
- Network access to the GitHub Enterprise Server instance

## Detailed Attack Procedures

### Step 1: Install Malicious GitHub App and Escalate Token
procedure: [[procedures/Install-Malicious-GitHub-App-for-Token-Escalation]]

**Objective**: Leverage improper token authorization in GitHub Apps to escalate a scoped user-to-server token to full organization owner privileges.

**Instructions**: Create a malicious GitHub App configured with scoped permissions, then install it on the target organization using an admin account. During the installation process, the vulnerability in token handling allows the scoped token to be elevated beyond its intended scope, granting full admin access. Use the GitHub UI or API to register the app, request installation, and authorize with minimal scopes (e.g., read-only), but exploit the flaw to obtain elevated permissions.

**Expected Output**: Successful app installation confirmation, followed by API responses showing full organization admin capabilities, such as listing all members or modifying settings.

**Success Indicators**:
- App installation succeeds without errors
- Token validation via API calls returns elevated permissions (e.g., ability to delete repositories or manage billing)
- No authorization denials during privilege checks

## Attack Chain Summary

### Key Achievements

1. Bypassed scoped token restrictions in GitHub Apps
2. Escalated to full organization owner privileges
3. Enabled unauthorized administrative actions on the organization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2024-10-01T00:00:00Z*
