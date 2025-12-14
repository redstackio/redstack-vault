---
tags:
  - token-generation
  - csrf-prep
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:11.987Z'
sub_techniques: []
id: 4f432f3c-0740-48d8-8fc3-3daf5d725f14
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Facebook-Photo-Import-URL-with-Token

## Summary

This procedure involves logging into the attacker's Badoo account and initiating the Facebook photo import to capture a URL containing a session token, which lacks CSRF protection and can be used to manipulate account links cross-session.

## Description

Targeting the photo import feature on m.badoo.com, the attacker accesses the import option, which generates a unique token in the URL query parameters. This token is intended for photo syncing but, due to missing safeguards, allows unauthorized linking changes when processed in another user's session. The procedure assumes the attacker account is already linked to Facebook and focuses on extracting the exploitable URL for delivery to the victim.

## Requirements

1. Active attacker Badoo session with Facebook linked
2. Browser developer tools (optional, for URL inspection)
3. Target: m.badoo.com photo upload section

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all state-changing endpoints, including cancel actions
- Validate token ownership against the current user's session before processing
- Rate-limit import initiations and log token generations for anomalies

## Objectives

1. Produce a valid, token-embedded URL for the attack
2. Ensure the token enables link override without authentication
3. Minimize exposure by copying the URL immediately

## Instructions

### Step 1: Log In as Attacker

**Context**: Establish the session for token generation.

Open m.badoo.com in a browser, log in with attacker credentials, and navigate to profile photos.

### Step 2: Initiate Photo Import

**Context**: Trigger the feature to generate the vulnerable URL.

Click 'Import photos via Facebook'. The page will redirect to a URL like `https://m.badoo.com/photo/import_fb?token=xyz456&other_params`.

### Step 3: Capture the URL

**Context**: Extract the full link for victim delivery.

Copy the entire address bar content, ensuring the token parameter is included. Do not proceed to import; the URL alone is sufficient.

### Step 4: Verify Token Validity

**Context**: Test the URL in a sandbox if needed.

Paste the URL into a new tab (logged out) to confirm it loads without errors, indicating the token is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-generation]]
- [[csrf-prep]]
