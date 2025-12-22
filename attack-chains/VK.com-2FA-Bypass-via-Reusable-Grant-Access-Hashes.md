---
id: ac-vk-2fa-bypass-316078
tags:
  - 2fa-bypass
  - auth-bypass
  - account-takeover
  - improper-authentication
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-Reusable-Grant-Access-Hash]]'
  - '[[procedures/Bypass-2FA-with-Reusable-Hash]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[Domain Controller Authentication]]'
updated_at: '2025-12-14T17:24:47.578Z'
description: >-
  Multi-stage attack exploiting improper authentication in VK.com's grant_access
  endpoint to bypass 2FA using unexpired, unbound hashes after initial account
  access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Domain Controller Authentication]]'
---
# VK.com 2FA Bypass via Reusable Grant Access Hashes

Multi-stage attack chain demonstrating a complete attack workflow exploiting VK.com's login system to bypass two-factor authentication (2FA) using persistent hashes generated on the grant_access endpoint.

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
    A[Prerequisite: Prior Account Access] --> B[Generate Reusable Hash]
    B --> C[Bypass 2FA and Access Account]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or proxy tool like Burp Suite for inspecting requests

### Target Environment

- Target Platform: Web (VK.com login system)
- Required Services/Ports: HTTPS (443)
- Network Access Requirements: Internet access to VK.com

### Initial Access Requirements

- Credential Requirements: Attacker must have previously accessed the victim's VK.com account at least once (e.g., via phishing or shared session)
- Network Position: External attacker with HTTP access
- Prior Access Needed: Yes, initial login or session to victim's account

## Detailed Attack Procedures

### Step 1: Generate Reusable Hash
procedure: [[procedures/Generate-Reusable-Grant-Access-Hash]]

**Objective**: Interact with the grant_access endpoint to generate a hash that lacks expiration and binding to 2FA status or session resets.

**Instructions**: Assuming prior access, navigate to the login flow and trigger the grant_access endpoint. Use a tool like curl to simulate the request if needed, capturing the generated hash from the response.

**Expected Output**: A hash value in the response that can be extracted for reuse.

**Success Indicators**:
- Hash generated without errors
- No expiration timestamp in hash metadata

### Step 2: Bypass 2FA with Reusable Hash
procedure: [[procedures/Bypass-2FA-with-Reusable-Hash]]

**Objective**: Reuse the unbound hash to authenticate without providing a 2FA code, enabling login or access token retrieval.

**Instructions**: Submit the captured hash to subsequent login requests on VK.com, bypassing the 2FA prompt. Monitor for successful session establishment.

**Expected Output**: Successful login or access token without 2FA verification.

**Success Indicators**:
- Account access granted without 2FA code
- Session cookies or tokens obtained

## Attack Chain Summary

### Key Achievements

1. Exploitation of unexpired hashes for persistent access
2. Bypassing 2FA protection leading to potential account takeover
3. Retrieval of access tokens without additional authentication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Domain Controller Authentication]] Domain Policy Modification: Group Policy Modification (adapted for web auth bypass)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
