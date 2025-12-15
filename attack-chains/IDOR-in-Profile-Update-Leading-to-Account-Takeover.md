---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - account-takeover
  - web-vulnerability
  - dod
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Register-Account-on-Target-Web-Application]]'
  - '[[procedures/Login-and-Navigate-to-Account-Page]]'
  - '[[procedures/Intercept-Profile-Update-Request-Using-Burp-Suite]]'
  - '[[procedures/Exploit-IDOR-by-Modifying-ID-Parameter]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.277Z'
description: >-
  Exploits an Insecure Direct Object Reference (IDOR) vulnerability in a U.S.
  Department of Defense web application's profile update feature to takeover
  another user's account by changing their email address.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# IDOR in Profile Update Leading to Account Takeover

Multi-stage attack chain demonstrating a complete workflow to exploit an IDOR vulnerability in a DoD web application for unauthorized account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Account] --> B[Login and Access Profile]
    B --> C[Intercept Update Request]
    C --> D[Modify ID for IDOR Exploit]
    D --> E[Account Takeover via Email Change]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (DoD platform)
- Required services/ports: HTTPS (443)
- Network access requirements: Direct internet access to the target URL

### Initial Access Requirements

- No prior credentials needed for registration
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Register Account
procedure: [[procedures/Register-Account-on-Target-Web-Application]]

**Objective**: Create an authenticated attacker account to gain initial access to the application.

**Instructions**: Navigate to the registration page and complete the account creation process.

**Expected Output**: Successful account registration with login credentials.

**Success Indicators**:
- Confirmation email or success message
- Ability to login with new credentials

### Step 2: Login and Navigate to Account Page
procedure: [[procedures/Login-and-Navigate-to-Account-Page]]

**Objective**: Authenticate as the attacker and access the profile management section.

**Instructions**: Use the login endpoint to authenticate and then proceed to the account page.

**Expected Output**: Access to the account dashboard with update options.

**Success Indicators**:
- Profile page loads with personal details
- Update button visible

### Step 3: Intercept Profile Update Request Using Burp Suite
procedure: [[procedures/Intercept-Profile-Update-Request-Using-Burp-Suite]]

**Objective**: Capture the legitimate profile update request to analyze its structure.

**Instructions**: Configure Burp Suite proxy and trigger the update action to intercept the POST request.

**Expected Output**: Captured HTTP POST request showing parameters like ID and email.

**Success Indicators**:
- Request intercepted in Burp Repeater
- Original ID matches attacker's account

### Step 4: Exploit IDOR by Modifying ID Parameter
procedure: [[procedures/Exploit-IDOR-by-Modifying-ID-Parameter]]

**Objective**: Alter the request to target a victim's account and change their email for takeover.

**Instructions**: Modify the ID parameter in the intercepted request to the victim's ID, update the email, and forward the request.

**Expected Output**: Victim's email successfully updated to attacker's email.

**Success Indicators**:
- Server response indicates success (e.g., 200 OK)
- Subsequent forgot password on new email grants access

## Attack Chain Summary

### Key Achievements

1. Unauthorized email modification via IDOR
2. Full account takeover using password reset
3. No password verification required for changes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T12:00:00Z*
