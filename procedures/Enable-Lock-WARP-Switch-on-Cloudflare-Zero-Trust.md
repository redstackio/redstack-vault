---
tags:
  - configuration
  - zero-trust
  - setup
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
  - Cloudflare
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:42.740Z'
sub_techniques: []
id: bc71f150-09c8-450b-be81-b76f146c455e
validated: true
---
# Enable Lock WARP Switch on Cloudflare Zero Trust

## Summary

This procedure configures the 'Lock WARP switch' feature in the Cloudflare Zero Trust platform to enforce VPN profile retention on enrolled iOS devices, serving as a prerequisite for testing client-side bypass vulnerabilities.

## Description

The Lock WARP switch is a server-side policy in Cloudflare Zero Trust that aims to prevent users from disabling or removing the WARP VPN client on managed devices. By enabling this feature via the dashboard, administrators intend to maintain continuous enforcement of security policies. However, as discovered in CVE-2022-3337, this setup reveals inadequate client-side validation in the WARP iOS app (versions before 6.15), allowing unauthorized profile removal. This procedure assumes administrative access and targets enrolled iOS devices in a Zero Trust environment.

## Requirements

1. Administrative credentials for the Cloudflare Zero Trust organization
2. Access to the Cloudflare dashboard over HTTPS
3. Enrolled iOS device with WARP client installed

## Defense

Defensive measures and detection strategies:

- Regularly audit Zero Trust dashboard configurations for enabled policies
- Monitor device enrollment logs for unexpected profile changes
- Enforce client updates to WARP version 6.15 or later to patch the vulnerability

## Objectives

1. Activate server-side enforcement to lock the WARP VPN profile
2. Prepare the environment for vulnerability testing
3. Ensure policy application to target devices

## Instructions

### Step 1: Access Zero Trust Dashboard

**Context**: Log in to initiate configuration changes.

Navigate to the Cloudflare Zero Trust dashboard at https://dash.teams.cloudflare.com and sign in with admin credentials.

> Expected output: Successful login to the dashboard interface.

### Step 2: Configure Device Settings

**Context**: Enable the lock feature for enrolled devices.

Go to Settings > WARP Client, select the target team or device policy, and toggle on the 'Lock WARP switch' option. Save the changes to apply the policy.

> Expected output: Confirmation message indicating the policy is active; enrolled devices should reflect the locked state upon sync.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[configuration]]
- [[zero-trust]]
