---
tags:
  - cloudflare
  - warp
  - ios
  - bypass
  - zero-trust
  - defense-evasion
type: attack_chain
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - iOS
  - Mobile
complexity: low
procedures:
  - '[[procedures/Enable-Lock-Warp-Switch-in-Zero-Trust]]'
  - '[[procedures/Bypass-Lock-Using-Disable-WARP-Quick-Action]]'
step_count: 2
techniques:
  - '[[Impair Defenses]]'
description: >-
  Attack chain demonstrating the bypass of the Lock Warp switch in Cloudflare
  Zero Trust using the Disable WARP quick action on iOS devices, due to
  insufficient client-side policy verification.
skill_level: intermediate
impact_level: high
id: a144381e-299d-4af5-88e7-1be4185446fb
created_at: '2025-12-14T17:24:41.819Z'
updated_at: '2025-12-14T17:24:41.819Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Impair Defenses]]'
---
# Bypass Cloudflare WARP Lock on iOS via Disable Quick Action

## Overview

This attack chain exploits a vulnerability in the Cloudflare WARP client on iOS, where the Lock Warp switch in the Zero Trust platform fails to prevent disabling the client due to inadequate client-side enforcement. An administrator enables the lock policy, but an enrolled user can bypass it using the 'Disable WARP' quick action, allowing unauthorized disconnection from the secure VPN tunnel and exposure to unsecured network traffic. This undermines device compliance and security policies, fixed in WARP client version 6.14.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable Lock Policy] --> B[Bypass via Quick Action]
    B --> C[Unauthorized WARP Disable]

    style A fill:#3498db
    style B fill:#e74c3c
    style C fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Cloudflare Zero Trust dashboard access (admin)
- Enrolled iOS device with WARP client installed

### Target Environment

- iOS platform
- Cloudflare Zero Trust service
- WARP client app (versions prior to 6.14)

### Initial Access Requirements

- Administrative access to Zero Trust for policy configuration
- Physical or enrolled access to the target iOS device
- No special network position required beyond device enrollment

## Detailed Attack Procedures

### Step 1: Enable Lock Warp Switch
procedure: [[procedures/Enable-Lock-Warp-Switch-in-Zero-Trust]]

**Objective**: Configure the Zero Trust policy to lock the WARP client on the enrolled iOS device, attempting to enforce mandatory VPN usage.

**Instructions**: Log in to the Cloudflare Zero Trust dashboard as an administrator. Navigate to the device settings or policies section, and enable the 'Lock WARP' switch for the target enrolled device or group. This policy is intended to prevent users from disabling WARP, enforcing compliance through server-side configuration.

**Expected Output**: Policy applied successfully, with the Lock WARP switch activated in the dashboard for the device.

**Success Indicators**:
- Lock WARP policy shows as enabled in Zero Trust dashboard
- Device enrollment confirms policy application

### Step 2: Bypass Lock Using Disable Quick Action
procedure: [[procedures/Bypass-Lock-Using-Disable-WARP-Quick-Action]]

**Objective**: Circumvent the Lock WARP policy by exploiting client-side enforcement weaknesses to disable the WARP client via the quick action.

**Instructions**: On the enrolled iOS device, open the Cloudflare WARP app. Despite the Lock WARP policy being enabled, access the Control Center or home screen quick actions. Tap the 'Disable WARP' quick action tile. The client fails to verify the server-enforced policy adequately, allowing the disable to proceed without authentication or block.

**Expected Output**: WARP client disconnects successfully, showing a confirmation or status change to disabled in the app.

**Success Indicators**:
- WARP status changes to disconnected/off
- Device can access unsecured network traffic without WARP enforcement

## Attack Chain Summary

### Key Achievements

1. Successfully enabled Lock WARP policy in Zero Trust to enforce device security.
2. Bypassed the policy using the Disable WARP quick action due to client-side verification flaws.
3. Achieved unauthorized disable of WARP, exposing the device to potential risks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Impair Defenses]]

### MITRE ATT&CK Tactics

- [[Defense Evasion]]

---
*Last updated: 2023-10-01*
