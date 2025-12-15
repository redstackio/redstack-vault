---
tags:
  - cloudflare
  - warp
  - ios
  - bypass
  - client-side
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - iOS
  - Mobile
techniques:
  - '[[Impair Defenses]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4a453e2c-6274-4b27-a03d-a136b0e04ea8
created_at: '2025-12-14T17:24:41.798Z'
updated_at: '2025-12-14T17:24:41.798Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Impair Defenses]]'
---
# Bypass Lock Using Disable WARP Quick Action

## Summary

This procedure exploits insufficient policy verification in the Cloudflare WARP iOS client to bypass the Lock WARP switch enabled via Zero Trust, allowing unauthorized disabling of the VPN client and evasion of security policies.

## Description

The Lock WARP feature in Zero Trust aims to prevent users from turning off WARP on managed devices, but the iOS client performs inadequate checks against server policies, relying on local enforcement. By accessing the 'Disable WARP' quick action in iOS Control Center or app shortcuts, a user can disconnect WARP despite the lock. This affects enrolled devices running WARP versions before 6.14, leading to exposure of traffic to unsecured networks. Prerequisites include an enrolled device with the policy active.

## Requirements

1. Enrolled iOS device with WARP client (pre-6.14)
2. Active Lock WARP policy from Zero Trust
3. Physical access to the device

## Defense

Defensive measures and detection strategies:

- Upgrade WARP client to version 6.14 or later for fixed policy enforcement
- Monitor Zero Trust logs for unauthorized disconnect events
- Implement additional MDM restrictions on quick actions and app behaviors

## Objectives

1. Disable WARP client despite Lock policy
2. Evade Zero Trust compliance enforcement
3. Expose device to unsecured traffic for potential further compromise

## Instructions

### Step 1: Open WARP App on iOS Device

**Context**: Prepare the device interface for quick action access.

Launch the Cloudflare WARP app from the home screen. Ensure the device is connected via WARP (status shows active).

### Step 2: Access Disable WARP Quick Action

**Context**: Exploit the quick action to trigger disable without policy check.

Swipe down to open Control Center or use the app's shortcut menu. Locate and tap the 'Disable WARP' quick action tile. The client bypasses server verification due to the flaw, processing the request locally.

> The action succeeds silently if the vulnerability is present, changing WARP status to off.

### Step 3: Verify Bypass Success

**Context**: Confirm the policy evasion and WARP disablement.

Check the WARP app status or network settings; WARP should be disconnected. Test by accessing a site that requires WARP (e.g., internal resource) – it should fail or route unsecured.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Impair Defenses]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cloudflare]]
- [[warp]]
- [[ios]]
- [[bypass]]
- [[client-side]]
