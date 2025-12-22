---
tags:
  - 2fa-bypass
  - response-tampering
  - business-logic
  - auth-bypass
  - account-takeover
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Tamper-with-2FA-Disable-API-Response]]'
step_count: 1
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:24:47.638Z'
description: >-
  A business logic vulnerability allowing attackers to disable two-factor
  authentication by tampering with API responses, bypassing password validation
  and enabling account takeover.
skill_level: intermediate
impact_level: high
id: 5b18194e-ef76-48a8-b2a5-a6bd8f28ec1d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# 2FA Disablement via Response Tampering in 8x8 Application

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticated Access] --> B[Response Tampering]
    B --> C[2FA Disabled]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (8x8 platform)
- Required services/ports: HTTPS (443)
- Network access requirements: Direct access to the web app as an authenticated user

### Initial Access Requirements

- Valid credentials for the target account
- Network position: Internal or direct internet access
- Prior access needed: Authenticated session to the 2FA management feature

## Detailed Attack Procedures

### Step 1: Tamper with 2FA Disable Response
procedure: [[procedures/Tamper-with-2FA-Disable-API-Response]]

**Objective**: Intercept and modify the API response during a 2FA disable attempt to bypass password validation, successfully removing 2FA protection.

**Instructions**: Authenticate to the 8x8 application and navigate to the 2FA settings. Attempt to disable 2FA using an incorrect password. Use [[tools/Burp-Suite]] to intercept the API request and response. Modify the response to indicate a successful disablement (e.g., change error status to success or alter the JSON payload to confirm removal).

**Expected Output**: The application treats the response as successful, disabling 2FA without requiring the correct password. Subsequent logins no longer prompt for 2FA.

**Success Indicators**:
- 2FA prompt disappears on next login attempt
- Account settings reflect 2FA as disabled
- No error messages post-tampering

## Attack Chain Summary

### Key Achievements

1. Bypassed password validation in 2FA removal process
2. Disabled 2FA protection via response manipulation
3. Enabled unauthorized full access to the account

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Modify Authentication Process]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
