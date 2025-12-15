---
id: ac-vk-2fa-bypass-001
tags:
  - 2fa-bypass
  - auth-bypass
  - account-takeover
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-VK-User-Reset-Hash]]'
  - '[[procedures/Access-VK-Login-Endpoint-with-Reset-Hash]]'
  - '[[procedures/Bypass-VK-2FA-and-Gain-Account-Access]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.862Z'
description: >-
  A multi-step attack exploiting insufficient verification in VK.com's session
  reset functionality to bypass 2FA and achieve full account takeover.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# VK.com Account Takeover via 2FA Bypass Using Session Reset Hash

Multi-stage attack chain demonstrating a complete attack workflow exploiting VK.com's session reset to bypass 2FA and take over user accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Obtain Reset Hash] --> B[Access Login Endpoint]
    B --> C[Bypass 2FA and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- VK.com web platform
- Access to a user's reset hash (via email, social engineering, or prior compromise)
- No special ports or services required beyond standard HTTPS (443)

### Initial Access Requirements

- Knowledge of a target user's reset hash
- Internet access to VK.com
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Obtain Reset Hash
procedure: [[procedures/Obtain-VK-User-Reset-Hash]]

**Objective**: Acquire the session reset hash for the target user to initiate the bypass.

**Instructions**: Trigger the session reset functionality for the target user, typically via email or account recovery options. The reset_hash is generated and can be intercepted or obtained through various means such as phishing or accessing recovery emails.

**Expected Output**: A valid reset_hash string associated with the victim's account.

**Success Indicators**:
- Reset hash received or extracted
- Hash is unique and tied to the target user

### Step 2: Access Login Endpoint with Reset Hash
procedure: [[procedures/Access-VK-Login-Endpoint-with-Reset-Hash]]

**Objective**: Use the reset_hash to access the login endpoint without identity verification.

**Instructions**: Open a web browser and navigate to `https://login.vk.com` appending the reset_hash as a parameter, e.g., `https://login.vk.com?reset_hash=example_hash`. The system processes this without checking requester identity.

**Expected Output**: Session reset initiated, leading to a login prompt that skips standard verification.

**Success Indicators**:
- Page loads with session reset context
- No additional identity prompts appear

### Step 3: Bypass 2FA and Gain Account Access
procedure: [[procedures/Bypass-VK-2FA-and-Gain-Account-Access]]

**Objective**: Complete the login process to gain full unauthorized access to the account.

**Instructions**: Upon processing the reset_hash, the endpoint logs in the associated user automatically, bypassing 2FA checks. Interact with the resulting session to access account features, messages, and settings.

**Expected Output**: Full session access to the victim's VK.com account dashboard.

**Success Indicators**:
- Logged in as the target user without 2FA
- Ability to view private data and perform actions

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA using unverified reset_hash
2. Achieved full account takeover without credentials
3. Enabled unauthorized access to sensitive user data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
