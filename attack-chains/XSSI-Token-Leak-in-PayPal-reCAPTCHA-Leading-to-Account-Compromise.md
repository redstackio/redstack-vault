---
tags:
  - xssi
  - token-leak
  - recaptcha
  - paypal
  - account-compromise
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Set-Up-Malicious-Site-for-XSSI-Token-Leak]]'
  - '[[procedures/Trigger-Token-Leak-on-Victim-Visit]]'
  - '[[procedures/Induce-Victim-Login-and-Security-Challenge]]'
  - '[[procedures/Complete-Challenge-with-Leaked-Token-to-Expose-Credentials]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Man in the Browser]]'
description: >-
  Multi-stage attack exploiting XSSI in PayPal's reCAPTCHA to leak tokens and
  compromise user accounts
skill_level: intermediate
impact_level: high
id: f4844216-f903-4c38-a358-624d36e0ee8f
created_at: '2025-12-11T06:10:40.538Z'
updated_at: '2025-12-11T06:10:40.538Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1185]]'
---
# XSSI Token Leak in PayPal reCAPTCHA Leading to Account Compromise

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in PayPal's security challenge flow via XSSI to leak sensitive tokens, complete CAPTCHA challenges, and expose victim credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Malicious Site] --> B[Victim Visits Site]
    B --> C[Victim Logs In]
    C --> D[Attacker Completes Challenge]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specific, basic web development tools

### Target Environment

- Web platform with JavaScript
- Services: reCAPTCHA
- Tech stack: JavaScript

### Initial Access Requirements

- Ability to host a malicious website
- Victim must visit the site and interact with PayPal login

## Detailed Attack Procedures

### Step 1: Set Up Malicious Site - [[procedures/Set-Up-Malicious-Site-for-XSSI-Token-Leak]]

**Procedure**: [[procedures/Set-Up-Malicious-Site-for-XSSI-Token-Leak]]

**Objective**: Create a site that includes the vulnerable PayPal JS file to exploit XSSI and leak tokens.

**Expected Output**: A functional malicious webpage that can capture leaked tokens.

**Success Indicators**:
- The script inclusion loads the PayPal JS file.
- Tokens are exposed and capturable via JavaScript.

### Step 2: Trigger Token Leak - [[procedures/Trigger-Token-Leak-on-Victim-Visit]]

**Procedure**: [[procedures/Trigger-Token-Leak-on-Victim-Visit]]

**Objective**: Leak the security challenge token when the victim visits the malicious site.

**Expected Output**: Attacker receives the leaked token.

**Success Indicators**:
- Token is sent to attacker's server or logged.
- No errors in script execution.

### Step 3: Induce Victim Login - [[procedures/Induce-Victim-Login-and-Security-Challenge]]

**Procedure**: [[procedures/Induce-Victim-Login-and-Security-Challenge]]

**Objective**: Have the victim follow a login link and enter credentials, triggering the challenge.

**Expected Output**: Victim's authentication request is queued.

**Success Indicators**:
- Victim completes login form.
- Security challenge (CAPTCHA) is presented.

### Step 4: Complete Challenge - [[procedures/Complete-Challenge-with-Leaked-Token-to-Expose-Credentials]]

**Procedure**: [[procedures/Complete-Challenge-with-Leaked-Token-to-Expose-Credentials]]

**Objective**: Use the leaked token to solve the CAPTCHA and replay authentication to expose credentials.

**Expected Output**: Victim's email and plaintext password are retrieved.

**Success Indicators**:
- CAPTCHA solved successfully.
- Authentication replay exposes credentials.

## Attack Chain Summary

### Key Achievements

1. Successful token leak via XSSI.
2. Induction of victim interaction with PayPal login.
3. Credential exposure through challenge completion.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Man in the Browser]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Credential Access]]

*Last updated: 2023-10-01*
