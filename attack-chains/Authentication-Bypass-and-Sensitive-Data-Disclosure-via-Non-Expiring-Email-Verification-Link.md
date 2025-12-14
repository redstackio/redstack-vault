---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - auth-bypass
  - sensitive-disclosure
  - web-vuln
  - email-verification
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Register-User-Account-to-Trigger-Verification-Email]]'
  - '[[procedures/Access-Email-Verification-Link]]'
  - '[[procedures/Bypass-Authentication-Using-Non-Expiring-Verification-Link]]'
  - '[[procedures/Decode-Base64-Parameter-to-Disclose-Sensitive-User-Data]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:11.090Z'
description: >-
  Multi-stage attack exploiting non-expiring email verification links in
  Zomato's registration flow to bypass authentication and disclose sensitive
  user data via Base64-encoded URL parameters.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Authentication Bypass and Sensitive Data Disclosure via Non-Expiring Email Verification Link

Multi-stage attack chain demonstrating a complete attack workflow exploiting Zomato's registration process.

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
    A[Register User] --> B[Access Verification Link]
    B --> C[Exploit Non-Expiring Link for Auth Bypass]
    C --> D[Decode and Disclose Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual web interaction and Base64 decoding)

### Target Environment

- Web application (e.g., zomato.com registration flow)
- Email service for receiving verification emails
- No specific ports or services beyond standard HTTPS (port 443)

### Initial Access Requirements

- Access to a victim's email address or ability to register with a controlled email
- No prior credentials needed
- Network access to the target web app and email provider

## Detailed Attack Procedures

### Step 1: Register User Account
procedure: [[procedures/Register-User-Account-to-Trigger-Verification-Email]]

**Objective**: Initiate the registration process to generate and receive the verification email containing the exploitable link.

**Instructions**: Navigate to the target web application's registration page (e.g., zomato.com/register). Enter a full name, email address (controlled or victim's), and password. Submit the form to trigger the email sending process.

**Expected Output**: Registration confirmation message and an email delivered to the provided address with a 'Verify Email Address' link in the body.

**Success Indicators**:
- Email received with verification link
- Link URL contains 'fbcid' parameter

### Step 2: Access Email Verification Link
procedure: [[procedures/Access-Email-Verification-Link]]

**Objective**: Use the verification link to initially activate the account and observe the authentication mechanism.

**Instructions**: Open the received email and click the 'Verify Email Address' link. This performs a GET request to the endpoint with the 'fbcid' parameter, authenticating the user without a password.

**Expected Output**: Successful account activation and redirection to the logged-in dashboard or profile page.

**Success Indicators**:
- User session established
- Account marked as verified

### Step 3: Bypass Authentication Using Non-Expiring Verification Link
procedure: [[procedures/Bypass-Authentication-Using-Non-Expiring-Verification-Link]]

**Objective**: Reuse the same link after activation to gain unauthorized access to the victim's account without entering credentials.

**Instructions**: After initial activation, log out if necessary. Copy the verification link URL from the email or browser history. Paste it into a new browser tab or incognito window and access it again. The link remains valid, directly authenticating via the URL parameters.

**Expected Output**: Direct login to the victim's account/session without password prompt.

**Success Indicators**:
- Access to account dashboard
- Session cookies set for the victim

### Step 4: Decode Base64 Parameter to Disclose Sensitive User Data
procedure: [[procedures/Decode-Base64-Parameter-to-Disclose-Sensitive-User-Data]]

**Objective**: Extract and decode the 'fbcid' parameter to reveal embedded sensitive information for further exploitation.

**Instructions**: Copy the 'fbcid' value from the verification URL. Use a Base64 decoder (e.g., online tool or command-line) to decode it. The decoded string exposes the unique user ID, 4-digit verification code, and email address.

**Expected Output**: Plaintext sensitive data: user ID, code, and email.

**Success Indicators**:
- Decoded data matches victim details
- Potential for phishing or session hijacking

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to takeover victim account
2. Disclosed sensitive user data via URL parameter
3. Demonstrated risks on shared devices due to URL logging
4. Highlighted lack of link expiration and encoding security

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T12:00:00Z*
