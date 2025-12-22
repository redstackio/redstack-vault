---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - referrer-leak
  - info-disclosure
  - account-takeover
  - http-header
type: attack_chain
tools:
  - '[[tools/Local-Proxy-for-Traffic-Monitoring]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Password-Reset-Link]]'
  - '[[procedures/Monitor-Referer-Header-Leakage]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.020Z'
description: >-
  Multi-stage attack exploiting referrer header leakage on a password reset page
  to disclose sensitive tokens to third-party domains, enabling account
  takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Account Takeover via Referer Header Leakage of Password Reset Tokens

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of proper Referrer-Policy on instagram-brand.com's password reset page, leading to leakage of sensitive reset tokens and email addresses via HTTP Referer headers to third-party analytics services.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger Reset Link] --> B[Monitor Leakage]
    B --> C[Capture and Exploit Token]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Local-Proxy-for-Traffic-Monitoring]]

### Target Environment

- Web platform
- Access to password reset functionality on target site (e.g., instagram-brand.com)
- Third-party services like Google Analytics and WordPress Pixel

### Initial Access Requirements

- Valid user email on the target platform
- Ability to request password reset
- Network access to intercept browser traffic

## Detailed Attack Procedures

### Step 1: Trigger Password Reset
procedure: [[procedures/Trigger-Password-Reset-Link]]

**Objective**: Initiate the password reset process to generate a sensitive reset link containing the security token and email address.

**Instructions**: Request a password reset via the target's forgot password feature, providing the target user's email. Receive the email and click the reset link, which navigates to https://instagram-brand.com/register/reset/<security_token>?email=<email_address>. This step sets up the conditions for leakage without further interaction.

**Expected Output**: Browser loads the password reset page, and the full URL is now in the browser's address bar.

**Success Indicators**:
- Password reset email received
- Reset page loaded successfully

### Step 2: Monitor and Capture Leakage
procedure: [[procedures/Monitor-Referer-Header-Leakage]]

**Objective**: Intercept HTTP requests to observe the Referer header sending the sensitive reset URL to third-party domains.

**Instructions**: With a local proxy configured, load the password reset page and monitor outgoing requests. Observe GET requests to domains like www.google-analytics.com and pixel.wp.com, where the Referer header includes the full reset URL with token and email.

**Expected Output**: Proxy logs showing Referer headers with sensitive data leaked to external sites.

**Success Indicators**:
- Referer headers captured containing token and email
- Confirmation of leakage to third-party endpoints

## Attack Chain Summary

### Key Achievements

1. Successful generation of a sensitive password reset link
2. Detection and capture of leaked reset tokens via Referer headers
3. Potential for account takeover by exploiting the captured link on third-party controlled domains

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
