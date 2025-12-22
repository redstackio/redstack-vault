---
id: ac-mfa-phone-hijack-001
tags:
  - mfa
  - authentication
  - access-control
  - persistence
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Arbitrary-MFA-Phone-Number]]'
step_count: 1
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:24:47.690Z'
description: >-
  An attack chain exploiting improper access control in the MFA phone number
  registration feature, allowing a registered user to associate an arbitrary
  phone number with their account without verifying the current MFA code,
  enabling potential account takeover or persistence.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Unverified MFA Phone Number Registration for Account Persistence

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Access] --> B[MFA Manipulation]
    B --> C[Persistence Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools or proxy like Burp Suite

### Target Environment

- Web application with MFA enabled (e.g., Superhuman/Grammarly)
- Required services/ports: HTTPS (443)
- Network access requirements: Valid session as registered user

### Initial Access Requirements

- Credential requirements: Valid username/password for target account
- Network position: Direct internet access
- Prior access needed: Logged-in session to the account

## Detailed Attack Procedures

### Step 1: MFA Phone Number Manipulation
procedure: [[procedures/Register-Arbitrary-MFA-Phone-Number]]

**Objective**: Associate an attacker-controlled phone number with the victim's MFA settings without verifying the existing MFA code, enabling future persistence or takeover.

**Instructions**: Log in to the target account using valid credentials. Navigate to the MFA settings page and attempt to add a new phone number for SMS-based 2FA. Submit the registration form with an arbitrary phone number (e.g., the attacker's number) without entering or verifying the current MFA code. This exploits the lack of authentication checks in the registration endpoint.

For testing via API (if exposed), intercept the request using a proxy and modify the phone number parameter:

```bash
curl -X POST https://api.target.com/mfa/register-phone \
  -H "Authorization: Bearer <session_token>" \
  -d "phone_number=+1234567890" \
  -d "verify_current=false"
```

**Expected Output**: Successful response indicating the phone number has been registered (e.g., JSON {"status": "success", "phone": "+1234567890"}).

**Success Indicators**:
- New phone number appears in MFA settings
- No prompt for current MFA code during registration
- Ability to receive MFA codes on the new number in subsequent logins

## Attack Chain Summary

### Key Achievements

1. Bypassed MFA verification during phone registration
2. Enabled association of unauthorized phone numbers
3. Established persistence mechanism for account access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*
