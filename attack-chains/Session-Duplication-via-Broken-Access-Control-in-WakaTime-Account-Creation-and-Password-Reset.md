---
tags:
  - broken-access-control
  - account-takeover
  - api-impersonation
  - session-duplication
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Account-with-Victims-Email]]'
  - '[[procedures/Obtain-and-Use-Attackers-API-Key]]'
  - '[[procedures/Log-Attacker-Coding-Activity]]'
  - '[[procedures/Victim-Password-Reset-and-New-API-Key]]'
  - '[[procedures/Log-Victim-Coding-Activity]]'
  - '[[procedures/Achieve-Simultaneous-Dashboard-Activity]]'
step_count: 7
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.460Z'
description: >-
  An attack chain exploiting broken access control in WakaTime's registration
  and password reset to create duplicate sessions, allowing an attacker to
  impersonate a victim and sabotage their coding activity statistics.
skill_level: intermediate
impact_level: high
id: f18783b2-ba6f-4882-b107-6fce87957654
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Session Duplication via Broken Access Control in WakaTime Account Creation and Password Reset

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in WakaTime's account management to enable duplicate API key usage and activity sabotage.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register with Victim Email] --> B[Obtain Attacker API Key]
    B --> C[Log Attacker Activity]
    C --> D[Victim Reset Password]
    D --> E[Victim Obtains New API Key]
    E --> F[Log Victim Activity]
    F --> G[Simultaneous Dashboard Sabotage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
    style G fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- Web browser for account interactions
- Coding platforms (e.g., VS Code with WakaTime extension) for API key usage

### Target Environment

- WakaTime web application
- No specific ports or services required beyond standard HTTPS access
- Internet connectivity for API submissions

### Initial Access Requirements

- Knowledge of victim's email address
- No prior credentials needed; exploits public registration endpoint
- Attacker must have access to a development environment for simulating coding activity

## Detailed Attack Procedures

### Step 1: Register Account with Victim's Email
procedure: [[procedures/Register-Account-with-Victims-Email]]

**Objective**: Create an unauthorized account using the victim's email to establish initial control.

**Instructions**: Navigate to the WakaTime registration page and submit the form using the victim's email address and arbitrary credentials. The endpoint does not validate email uniqueness or ownership at registration.

**Expected Output**: Successful account creation confirmation, allowing access to the dashboard.

**Success Indicators**:
- Account dashboard accessible with the victim's email
- No email verification prompt blocks registration

### Step 2: Obtain Attacker's API Key
procedure: [[procedures/Obtain-and-Use-Attackers-API-Key]]

**Objective**: Generate an API key tied to the hijacked account for activity submission.

**Instructions**: After logging in with the newly created account, download and install a supported coding platform (e.g., VS Code extension). The platform will prompt for API key generation, which is issued without additional identity checks.

**Expected Output**: API key displayed or copied to the clipboard, ready for integration.

**Success Indicators**:
- API key successfully generated and integrated into the coding platform
- No revocation or validation errors occur

### Step 3: Log Attacker Coding Activity
procedure: [[procedures/Log-Attacker-Coding-Activity]]

**Objective**: Submit malicious or sabotaging coding activity to the victim's account.

**Instructions**: Use the coding platform with the attacker's API key to open and edit files, simulating or performing actual coding. The WakaTime API will automatically log heartbeats and activity data to the account.

**Expected Output**: Activity events visible in the attacker's dashboard view of the account.

**Success Indicators**:
- Coding sessions logged under the victim's email
- Dashboard shows inflated or altered statistics

### Step 4: Trigger Victim Password Reset
procedure: [[procedures/Victim-Password-Reset-and-New-API-Key]]

**Objective**: Force the victim to reset the password, gaining legitimate access without alerting the attacker.

**Instructions**: The victim, unaware, attempts registration with their email and fails due to the existing account. They then use the password reset feature, which emails a reset link. Upon reset, a new password is set without invalidating the existing session or API key.

**Expected Output**: Victim receives reset email and successfully logs in with new credentials.

**Success Indicators**:
- Victim account access granted via reset
- No notification of duplicate activity or key revocation

### Step 5: Victim Obtains New API Key
procedure: [[procedures/Victim-Password-Reset-and-New-API-Key]]

**Objective**: Allow the victim to generate their own API key, enabling parallel usage.

**Instructions**: Victim installs a coding platform and requests a new API key post-login. The system issues a fresh key without revoking the attacker's existing one.

**Expected Output**: New API key issued to the victim for their platform integration.

**Success Indicators**:
- Victim's platform connects successfully with the new key
- Attacker's prior key remains functional

### Step 6: Log Victim Coding Activity
procedure: [[procedures/Log-Victim-Coding-Activity]]

**Objective**: Enable the victim to log legitimate activity, creating overlap with attacker's submissions.

**Instructions**: Victim codes normally using their platform and API key. Activity is submitted via the WakaTime API without session checks.

**Expected Output**: Victim's coding sessions appear in the dashboard alongside attacker's.

**Success Indicators**:
- Dashboard updates with victim's real activity
- No conflicts or blocks from duplicate keys

### Step 7: Achieve Simultaneous Dashboard Activity
procedure: [[procedures/Achieve-Simultaneous-Dashboard-Activity]]

**Objective**: Demonstrate sabotage through aggregated, unisolated activity on the shared dashboard.

**Instructions**: Continue parallel logging from both sides. The dashboard aggregates all API submissions, leading to mixed statistics, reputation damage, and incorrect rankings.

**Expected Output**: Unified dashboard showing combined (and potentially falsified) coding metrics.

**Success Indicators**:
- Attacker's fake activity dilutes or inflates victim's stats
- Victim notices anomalies in rankings or totals

## Attack Chain Summary

### Key Achievements

1. Unauthorized account creation with victim's email without validation
2. Generation of multiple valid API keys for the same account
3. Parallel activity logging enabling impersonation and sabotage

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

---
*Last updated: 2023-10-01T00:00:00Z*
