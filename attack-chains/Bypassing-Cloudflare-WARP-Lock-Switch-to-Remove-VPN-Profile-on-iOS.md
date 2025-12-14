---
tags:
  - defense-evasion
  - vpn-bypass
  - cloudflare-zero-trust
  - ios
  - warp-client
type: attack_chain
tools: []
tactics:
  - '[[Defense Evasion]]'
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-Lock-WARP-Switch-on-Cloudflare-Zero-Trust]]'
  - '[[procedures/Remove-VPN-Profile-from-Locked-WARP-iOS-Client]]'
step_count: 2
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:42.742Z'
description: >-
  Demonstrates a vulnerability allowing unauthorized removal of the VPN profile
  from a locked WARP iOS client, evading Zero Trust enforcement policies.
skill_level: intermediate
impact_level: high
id: 592561cc-851c-4ca3-beaf-fdf88163390c
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Bypassing Cloudflare WARP Lock Switch to Remove VPN Profile on iOS

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable Lock WARP Switch] --> B[Remove VPN Profile]
    B --> C[Bypass Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses Cloudflare dashboard and iOS device interface)

### Target Environment

- iOS device enrolled in Cloudflare Zero Trust
- WARP iOS client installed (version prior to 6.15)
- Required services: VPN, Zero Trust Platform
- Network access: Admin access to Cloudflare Zero Trust dashboard

### Initial Access Requirements

- Administrative credentials for Cloudflare Zero Trust platform
- Physical access to enrolled iOS device
- No prior compromise needed; assumes legitimate user or admin role

## Detailed Attack Procedures

### Step 1: Enable Lock WARP Switch
procedure: [[procedures/Enable-Lock-WARP-Switch-on-Cloudflare-Zero-Trust]]

**Objective**: Configure the server-side policy to lock the WARP VPN profile on enrolled iOS devices, setting up the enforcement that will be bypassed.

**Instructions**: Log in to the Cloudflare Zero Trust dashboard as an administrator. Navigate to the device settings for the enrolled iOS device, and enable the 'Lock WARP switch' feature to prevent profile removal.

**Expected Output**: Confirmation in the dashboard that the Lock WARP switch is active for the target device.

**Success Indicators**:
- Dashboard shows Lock WARP switch enabled
- iOS client reflects locked state (switch cannot be toggled off normally)

### Step 2: Remove VPN Profile from Locked Client
procedure: [[procedures/Remove-VPN-Profile-from-Locked-WARP-iOS-Client]]

**Objective**: Exploit inadequate client-side enforcement to delete the VPN profile, bypassing Zero Trust policies and evading security restrictions.

**Instructions**: On the enrolled iOS device with WARP client version prior to 6.15, navigate to iOS Settings > General > VPN & Device Management. Locate the WARP VPN profile and attempt to delete it directly. Despite the lock, the client permits removal due to missing validation.

**Expected Output**: VPN profile successfully removed from the device, disconnecting from Zero Trust enforcement.

**Success Indicators**:
- VPN profile no longer listed in iOS settings
- Device evades enforced policies (e.g., can access restricted resources without VPN)

## Attack Chain Summary

### Key Achievements

1. Enabled server-side lock policy via Zero Trust dashboard
2. Bypassed client-side enforcement to remove locked VPN profile
3. Evaded Zero Trust security controls, enabling policy circumvention on enrolled devices

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Disable or Modify Tools]]

### MITRE ATT&CK Tactics

- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
