---
id: proc-nextcloud-setup-e2e-001
tags:
  - nextcloud
  - account-setup
  - e2e-encryption
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:42.236Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Setup-Nextcloud-Account-and-Enable-E2E-Encryption

## Summary

This procedure creates a user account on a Nextcloud server and enables the end-to-end encryption feature, setting the stage for subsequent key management and exploitation in multi-device environments.

## Description

In the context of testing Nextcloud's E2E encryption, this involves standard account registration via the web interface and activating the E2E encryption app in server administration settings. This prepares the environment for key generation and data upload, assuming the attacker has server access for later steps. The procedure targets Nextcloud instances where E2E is available but not yet configured, leading to the generation of user-specific keypairs.

## Requirements

1. Access to Nextcloud server web interface (as admin for enabling E2E)
2. Valid email or credentials for user registration
3. Nextcloud server with E2E encryption app installed but disabled

## Defense

Defensive measures and detection strategies:

- Monitor admin logs for E2E enablement
- Require multi-factor authentication for admin access
- Regularly audit enabled apps and user registrations

## Objectives

1. Establish a legitimate user presence on the server
2. Activate E2E encryption to enable keypair generation
3. Prepare for initial device integration

## Instructions

### Step 1: Create User Account

**Context**: Register a new user account to simulate the victim.

Access the Nextcloud login page and select 'Create Account' or use admin interface to add user.

**Expected Output**: Confirmation email sent; user can log in.

### Step 2: Enable E2E Encryption

**Context**: Activate the E2E module server-wide.

As admin, navigate to Apps > Active apps, search for 'End-to-End Encryption', and enable it. Restart server if required.

**Expected Output**: E2E option appears in user settings.

**Success Indicators**:
- User settings show E2E toggle
- No errors in server logs

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[account-setup]]
- [[e2e-encryption]]
