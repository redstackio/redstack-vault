---
id: ac-uuid-missing-issuer-totp
tags:
  - 2fa
  - totp
  - misconfiguration
  - authentication
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inspect-TOTP-URL-for-Missing-Issuer]]'
step_count: 1
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:45.516Z'
description: >-
  A misconfiguration in the 2FA setup process where the TOTP URL lacks the
  Issuer parameter, complicating user management of authentication tokens
  without direct security compromise.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Missing Issuer Parameter in TOTP 2FA QR Code Leading to Token Management Issues

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery] --> B[Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None

### Target Environment

- Web platform with TOTP-based 2FA setup
- Access to 2FA enrollment process

### Initial Access Requirements

- User account on the target platform
- Ability to initiate 2FA setup

## Detailed Attack Procedures

### Step 1: Discover Missing Issuer Parameter
procedure: [[procedures/Inspect-TOTP-URL-for-Missing-Issuer]]

**Objective**: Identify the absence of the Issuer parameter in the TOTP URL during 2FA QR code generation to assess token management complications.

**Instructions**: During the 2FA setup process on the target platform, such as Legal Robot, initiate the enrollment challenge. Observe the generated QR code and extract the underlying TOTP URL. Manually inspect the URL for the presence of the 'Issuer' parameter, which should identify the service (e.g., 'otpauth://totp/Legal%20Robot:user@example.com?secret=ABC123&issuer=Legal%20Robot'). Note the absence of '&issuer=...' in the URL structure.

**Expected Output**: A TOTP URL like 'otpauth://totp/user@example.com?secret=ABC123' without the Issuer component, confirming the misconfiguration.

**Success Indicators**:
- TOTP URL lacks Issuer parameter
- QR code scans into authenticator app without clear service labeling, leading to user confusion in managing multiple tokens

## Attack Chain Summary

### Key Achievements

1. Identified misconfiguration in 2FA setup
2. Demonstrated impact on user token management
3. Reported vulnerability without exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
