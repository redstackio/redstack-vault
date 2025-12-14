---
tags:
  - backdoor-test
  - account-takeover
  - access-verification
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.994Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d6f7c34c-87a9-47d0-8d5e-d5d945f218c4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-and-Test-Backdoor-Access

## Summary

This procedure tests the backdoor by attempting login via the linked external provider from a fresh session, confirming unauthorized access to the victim's Shopify resources.

## Description

With the external login linked, the backdoor persists even if the victim later verifies the email or resets the password. Testing involves simulating victim login at partners.shopify.com/organizations, where the 'Log in with Google' option appears, granting access to organizations and shops. This web-based procedure highlights the takeover potential.

## Requirements

1. Linked external login from prior steps
2. New browser session or incognito mode
3. Victim's email for login prompt

## Defense

Defensive measures and detection strategies:

- Revoke external logins for unverified accounts periodically
- Detect multiple login attempts from external providers on new accounts
- Alert on access to organizations via recently linked externals

## Objectives

1. Confirm external login enables access without verification
2. Access victim's organizations and shops
3. Demonstrate persistent backdoor functionality

## Instructions

### Step 1: Initiate Login in New Session

**Context**: Start a fresh login flow to test the backdoor.

No command; go to https://partners.shopify.com/organizations and enter the victim's email.

> Expected: Prompt for login methods, including 'Log in with Google'.

### Step 2: Use External Login

**Context**: Authenticate via the linked Google account.

Click 'Log in with Google' and sign in with the linked account.

> Expected: Successful login to the account.

### Step 3: Verify Access

**Context**: Check for unauthorized resource access.

Navigate to profile, organizations, or shops.

> Expected: Full access without password or verification; potential info disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[backdoor-test]]
- [[account-takeover]]
- [[access-verification]]
