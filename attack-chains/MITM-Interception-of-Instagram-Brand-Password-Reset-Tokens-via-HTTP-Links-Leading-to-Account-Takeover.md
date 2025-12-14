---
id: ac-001
tags:
  - mitm
  - http-downgrade
  - token-interception
  - account-takeover
  - broken-auth
type: attack_chain
tools:
  - '[[tools/Wireshark]]'
  - '[[tools/Local-Proxy-Tool]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-and-Inspect-Password-Reset-Link]]'
  - '[[procedures/Intercept-Token-via-Network-Traffic-Capture]]'
  - '[[procedures/Exploit-Intercepted-Token-for-Account-Takeover]]'
step_count: 3
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.453Z'
description: >-
  Multi-stage attack exploiting HTTP-based password reset links in Instagram
  Brand emails to intercept security tokens via man-in-the-middle simulation,
  enabling unauthorized account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Valid Accounts]]'
---
# MITM Interception of Instagram Brand Password Reset Tokens via HTTP Links Leading to Account Takeover

The vulnerability stems from Instagram Brand's password reset process, where emails contain links using the HTTP scheme instead of HTTPS. This exposes sensitive security tokens to interception during transmission, particularly in unencrypted network segments. An attacker can simulate a man-in-the-middle (MITM) attack to capture the token, then use it to reset the victim's password before they do, resulting in full account takeover. The attack was demonstrated by requesting a reset, inspecting the link, capturing traffic with Wireshark and a local proxy, and exploiting the token. This could lead to widespread compromises if scaled.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Password Reset] --> B[Intercept Token via MITM]
    B --> C[Exploit Token for Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Wireshark]]
- [[tools/Local-Proxy-Tool]]

### Target Environment

- Web platform (Instagram Brand at https://en.instagram-brand.com)
- Email access for the target account
- Network tools for traffic interception

### Initial Access Requirements

- Valid email address associated with an Instagram Brand account
- Ability to receive emails
- Local network control for proxy setup (no prior target access needed beyond email)

## Detailed Attack Procedures

### Step 1: Initiate and Inspect Password Reset Link
procedure: [[procedures/Initiate-and-Inspect-Password-Reset-Link]]

**Objective**: Trigger the password reset process and examine the email link to confirm the HTTP scheme usage, identifying the vulnerable token transmission.

**Instructions**: Navigate to the Instagram Brand sign-in page and request a password reset for the target email. Check the inbox, copy the link from the email, and inspect it in a text editor to reveal the HTTP scheme and token.

**Expected Output**: Email link in format `http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<security token>`.

**Success Indicators**:
- Password reset email received
- Link inspection shows HTTP scheme and visible token parameter

### Step 2: Intercept Token via Network Traffic Capture
procedure: [[procedures/Intercept-Token-via-Network-Traffic-Capture]]

**Objective**: Simulate MITM by capturing unencrypted traffic during link access to extract the security token before it upgrades to HTTPS.

**Instructions**: Set up Wireshark to monitor traffic and attach a local proxy to the browser. Access the copied HTTP link, capture the GET request to mandrillapp.com, and follow the redirects to observe the token in clear text.

**Expected Output**: Captured request showing `http://instagram-brand.com/register/reset/<token>?email=<email>`, with token exposed.

**Success Indicators**:
- Traffic capture reveals HTTP request with token
- Redirect chain confirms exposure before HTTPS

### Step 3: Exploit Intercepted Token for Account Takeover
procedure: [[procedures/Exploit-Intercepted-Token-for-Account-Takeover]]

**Objective**: Use the captured token to automate a password reset request, completing the account takeover before the victim acts.

**Instructions**: With the token in hand, send a request to the reset endpoint using the intercepted value to change the password. Automate if needed to beat the victim's timing.

**Expected Output**: Successful password change confirmation, granting attacker access to the account.

**Success Indicators**:
- Password reset completes with new credentials
- Account login succeeds with new password

## Attack Chain Summary

### Key Achievements

1. Confirmed HTTP vulnerability in password reset emails
2. Demonstrated token interception via simulated MITM
3. Achieved account takeover through token exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Defense Evasion]]

---
*Last updated: 2024-10-01T00:00:00Z*
