---
tags:
  - cloudflare
  - zero-trust
  - policy-configuration
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
impact_level: low
detection_risk: low
sub_techniques: []
id: d5be9c7c-721d-4fe0-80bc-a8c4d62598e5
created_at: '2025-12-14T17:24:41.803Z'
updated_at: '2025-12-14T17:24:41.803Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Impair Defenses]]'
---
# Enable Lock Warp Switch in Zero Trust

## Summary

This procedure configures the Lock WARP switch in Cloudflare's Zero Trust platform to prevent users from disabling the WARP client on enrolled iOS devices, serving as a prerequisite for testing or enforcing mandatory VPN compliance.

## Description

In a Zero Trust environment, administrators use the dashboard to apply policies that lock security features like WARP, a VPN client that secures device traffic. This step sets up the policy on the server side, intending to block client-side disables. However, it relies on client enforcement, which can be vulnerable. The procedure targets enrolled iOS devices and assumes admin access to the Zero Trust console. Expected outcome is policy activation, visible in device management.

## Requirements

1. Administrative access to Cloudflare Zero Trust dashboard
2. Enrolled iOS device in the Zero Trust organization
3. WARP client installed on the target device (pre-6.14 for vulnerability context)

## Defense

Defensive measures and detection strategies:

- Regularly audit Zero Trust policy applications and device compliance logs
- Monitor for unexpected WARP disconnects via Zero Trust analytics
- Enforce server-side validation updates in client versions

## Objectives

1. Apply Lock WARP policy to enforce continuous VPN usage
2. Verify policy propagation to enrolled devices
3. Set up conditions for compliance testing or bypass evaluation

## Instructions

### Step 1: Access Zero Trust Dashboard

**Context**: Log in to configure device policies securely.

Navigate to the Cloudflare dashboard, select Zero Trust, and go to Settings > WARP Client. Ensure the organization has device enrollment enabled.

### Step 2: Enable Lock WARP Switch

**Context**: Activate the policy to lock the WARP client.

In the WARP Client settings, locate the 'Lock WARP' toggle for iOS devices or the specific device group. Enable it and save the configuration. The policy pushes to enrolled devices via MDM or direct enrollment.

> Policy enablement may take a few minutes to propagate; check device status in the dashboard.

### Step 3: Verify Policy Application

**Context**: Confirm the lock is active on the target device.

In the Zero Trust devices list, select the iOS device and review its compliance status. The Lock WARP should show as enforced.

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
- [[zero-trust]]
- [[policy-configuration]]
