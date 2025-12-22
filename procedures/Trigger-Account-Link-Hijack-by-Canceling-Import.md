---
tags:
  - account-hijack
  - csrf-exploit
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:11.981Z'
sub_techniques:
  - '[[Additional Cloud Credentials]]'
id: fa6d0e56-5b1d-4ebb-a4cd-bc11b0cc6b74
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Account-Link-Hijack-by-Canceling-Import

## Summary

By clicking 'Cancel' on the photo import dialog in the victim's session, this procedure exploits the missing CSRF protection to unlink the victim's Facebook and link the attacker's, achieving account manipulation without further interaction.

## Description

The cancel action sends a POST request to Badoo's backend that processes the token from the URL, overriding the existing Facebook link due to absent validation of the user's session or origin. This root cause—lack of CSRF tokens and authentication checks—allows the cross-session modification, directly leading to takeover potential.

## Requirements

1. Victim session with open import dialog from malicious URL
2. No additional tools; browser interaction only
3. Target endpoint: Photo import cancel handler on m.badoo.com

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens on all mutating requests, including cancels
- Validate token against current user's Facebook ID before un/linking
- Audit logs for link changes triggered by import actions

## Objectives

1. Replace victim's Facebook link with attacker's
2. Do so stealthily via a seemingly benign cancel
3. Confirm hijack without alerting the victim

## Instructions

### Step 1: Open Import Dialog in Victim Session

**Context**: Ensure the prompt is visible.

From the previous step, confirm the Facebook photo import dialog is displayed.

### Step 2: Execute Cancel Action

**Context**: Trigger the vulnerable request.

Click the 'Cancel' or 'X' button on the dialog. This submits the form with the attacker's token.

### Step 3: Verify Link Change

**Context**: Check the override.

Navigate to victim's account settings > Linked accounts. The Facebook profile should now show the attacker's details.

### Step 4: Test Unlink of Original

**Context**: Ensure irreversibility without auth.

Attempt to log in with victim's original Facebook; it should fail or redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[Additional Cloud Credentials]] User Account Manipulation

## Commands Used


## Tools Used


## Tags

- [[account-hijack]]
- [[csrf-exploit]]
