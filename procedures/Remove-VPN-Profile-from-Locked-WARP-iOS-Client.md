---
tags:
  - defense-evasion
  - vpn-bypass
  - ios
  - client-side
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:42.737Z'
sub_techniques: []
id: 9a861074-d81e-4151-b9ba-7f0f45d7b3ae
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Remove VPN Profile from Locked WARP iOS Client

## Summary

This procedure exploits a client-side enforcement flaw in the WARP iOS client (CVE-2022-3337) to remove the VPN profile despite the 'Lock WARP switch' being enabled, allowing evasion of Cloudflare Zero Trust policies on enrolled devices.

## Description

In Cloudflare Zero Trust environments, the Lock WARP switch policy is designed to prevent users from disabling or removing the WARP VPN profile on managed iOS devices. However, prior to version 6.15, the iOS client fails to adequately validate and enforce this server-side policy, permitting direct profile deletion through iOS settings. This bypass enables users to disconnect from enforced security controls, potentially accessing restricted resources or compromising device compliance. The procedure requires an enrolled iOS device with the vulnerable WARP client and tests the removal process.

## Requirements

1. Enrolled iOS device with WARP client (version < 6.15)
2. Lock WARP switch enabled via Zero Trust dashboard
3. Physical access to the iOS device

## Defense

Defensive measures and detection strategies:

- Update WARP iOS client to version 6.15 or later to enforce profile locking
- Implement device management tools (e.g., MDM) to monitor and restrict iOS settings changes
- Log and alert on VPN profile removal events in Zero Trust analytics

## Objectives

1. Bypass server-side Lock WARP policy through client-side deletion
2. Evade Zero Trust enforcement and restrictions
3. Compromise security controls for the enrolled device

## Instructions

### Step 1: Verify Locked State

**Context**: Confirm the policy is active before attempting bypass.

Open the WARP app on the iOS device and check that the WARP switch cannot be toggled off. Sync the device with Zero Trust if needed.

> Expected output: WARP switch appears locked in the app interface.

### Step 2: Access iOS VPN Settings

**Context**: Navigate to the system-level VPN management to exploit the enforcement gap.

Go to iOS Settings > General > VPN & Device Management (or Profiles & Device Management on older iOS versions). Locate the Cloudflare WARP VPN profile in the list.

> Expected output: WARP profile visible despite lock policy.

### Step 3: Delete the Profile

**Context**: Perform the unauthorized removal, which succeeds due to inadequate client validation.

Tap the WARP profile, select 'Remove Profile' or 'Delete VPN', and confirm the action. No additional authentication is required.

> Expected output: Profile removed successfully; WARP app shows disconnected state, and device is no longer enforced by Zero Trust.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[defense-evasion]]
- [[vpn-bypass]]
- [[ios]]
