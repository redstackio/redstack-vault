---
tags:
  - broken-access-control
  - account-deletion
  - impersonation
  - support-ticket
  - nordvpn
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-NordVPN-Login-and-Support-Form]]'
  - '[[procedures/Submit-Impersonated-Account-Deletion-Request]]'
  - '[[procedures/Monitor-Support-Processing]]'
  - '[[procedures/Verify-Account-Deletion]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:29:36.921Z'
description: >-
  Multi-stage attack exploiting broken access control in NordVPN's support
  ticket system to delete any user account by impersonating the victim via an
  unauthenticated email form.
skill_level: low
impact_level: high
id: dd029ca3-18e7-4853-bc83-95e213c9b110
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Access Removal]]'
---
# Unauthorized Account Deletion via Unauthenticated NordVPN Support Ticket

Multi-stage attack chain demonstrating exploitation of insufficient authentication in NordVPN's support ticket system, allowing any unauthorized user to delete victim accounts by submitting impersonated deletion requests through an unauthenticated web form on the login page. The attack relies on the support team's lack of verification for critical actions, leading to permanent account removal from the database.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2-4 hours |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Login Page] --> B[Submit Impersonated Request]
    B --> C[Wait for Processing]
    C --> D[Verify Deletion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual web browser actions)

### Target Environment

- Web platform
- Access to https://ucp.nordvpn.com/login/
- Victim's registered email address

### Initial Access Requirements

- Public internet access
- No authentication or credentials required
- Knowledge of victim's email (obtainable via OSINT or prior recon)

## Detailed Attack Procedures

### Step 1: Access Login and Support Form
procedure: [[procedures/Access-NordVPN-Login-and-Support-Form]]

**Objective**: Reach the unauthenticated support email form on the NordVPN user control panel login page to initiate a ticket.

**Instructions**: Open a web browser and navigate to the login interface. Locate and interact with the email support option to open the form.

**Expected Output**: Support form visible, ready for input without login.

**Success Indicators**:
- Page loads at https://ucp.nordvpn.com/login/
- Email button or link accessible and clickable

### Step 2: Submit Impersonated Account Deletion Request
procedure: [[procedures/Submit-Impersonated-Account-Deletion-Request]]

**Objective**: Impersonate the victim by using their email in an unauthenticated deletion request, creating a support ticket that bypasses ownership verification.

**Instructions**: Fill the support form with the victim's email address and a request to delete the account, specifying it as an inactive account if needed. Submit without any authentication.

**Expected Output**: Form submission success message or ticket creation confirmation.

**Success Indicators**:
- Form accepts victim email without validation
- No prompts for additional proof like PIN or payment details

### Step 3: Monitor Support Processing
procedure: [[procedures/Monitor-Support-Processing]]

**Objective**: Allow time for the support team to process the ticket and execute the deletion without further checks.

**Instructions**: Wait passively for the support team to review and action the ticket, typically a few hours.

**Expected Output**: No direct notification; proceed to verification.

**Success Indicators**:
- Elapsed time of 2-4 hours
- No rejection or follow-up from support

### Step 4: Verify Account Deletion
procedure: [[procedures/Verify-Account-Deletion]]

**Objective**: Confirm the victim's account has been removed from the database, resulting in loss of access.

**Instructions**: Attempt to access or log in with the victim's credentials or check external indicators of deletion.

**Expected Output**: Account no longer exists; login fails or database records show removal.

**Success Indicators**:
- Victim unable to log in
- Confirmation via support response or error messages indicating deletion

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to create support tickets impersonating any user
2. Triggered permanent account deletion without ownership verification
3. Demonstrated high impact on user access and data loss for inactive accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Access Removal]] Account Access Removal

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
