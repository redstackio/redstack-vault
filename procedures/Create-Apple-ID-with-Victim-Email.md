---
tags:
  - auth-bypass
  - apple-id
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2dbfe0d9-cb80-439f-b395-df37ad8a44f4
created_at: '2025-12-14T17:24:48.032Z'
updated_at: '2025-12-14T17:24:48.032Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Apple-ID-with-Victim-Email

## Summary

This procedure involves registering a new Apple ID using the email address of an existing Cloudflare account, exploiting the absence of prior linkage to enable later authentication bypass.

## Description

In the context of Cloudflare's authentication system, this step sets up the foundation for account takeover by creating an Apple ID that matches the victim's email. Apple's system allows new registrations without immediate verification if the email isn't already claimed, allowing an attacker to control the authentication flow. This is particularly effective against users without an existing Apple ID linked to their email. Prerequisites include knowing the victim's email and access to a web browser.

## Requirements

1. Knowledge of the target's Cloudflare-associated email address
2. Access to Apple's account creation webpage (appleid.apple.com)
3. No existing Apple ID linked to the email

## Defense

Defensive measures and detection strategies:

- Implement email verification during Apple ID linkage on login flows
- Monitor for multiple authentication attempts from new Apple IDs
- Educate users to link their own Apple IDs proactively

## Objectives

1. Gain control of an Apple ID tied to the victim's email
2. Prepare for unauthorized authentication to Cloudflare
3. Enable 2FA circumvention

## Instructions

### Step 1: Navigate to Apple ID Creation

**Context**: Access Apple's registration page to begin creating the account.

Visit https://appleid.apple.com/account in a web browser and select the option to create a new Apple ID.

### Step 2: Enter Victim's Email and Complete Registration

**Context**: Input the target's email and provide necessary details to finalize creation.

Fill in the email field with the victim's Cloudflare email address. Provide a password, name, and other required information. Skip any optional verifications if possible, and confirm the account creation.

**Expected Output**: Receipt of a confirmation email (if sent) or direct access to the new Apple ID dashboard.

### Step 3: Verify Apple ID Access

**Context**: Ensure the new ID is functional for subsequent use.

Log in to the new Apple ID using the provided credentials to confirm control.

**Expected Output**: Successful login without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[apple-id]]
