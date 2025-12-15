---
tags:
  - auth-bypass
  - oauth-flow
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
id: 56ae1795-2083-41a3-b202-f85e431c0950
created_at: '2025-12-14T17:24:48.027Z'
updated_at: '2025-12-14T17:24:48.027Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Sign-in-with-Apple-Flow

## Summary

This procedure uses the newly created Apple ID to start the 'Sign in with Apple' authentication on Cloudflare's login page, linking it to the existing account via email match without verification.

## Description

Cloudflare integrates Apple's authentication as an OAuth-like flow on their login page, but fails to check for existing account linkages or require additional email proof. By initiating this flow with the rogue Apple ID, the attacker tricks the system into associating the authentication with the victim's account. This step assumes the Apple ID from the prior procedure is ready and targets users without their own linked Apple ID.

## Requirements

1. Functional Apple ID created with victim's email
2. Access to Cloudflare's login page (dash.cloudflare.com/login)
3. Web browser supporting OAuth redirects

## Defense

Defensive measures and detection strategies:

- Add linkage confirmation prompts during Apple sign-in
- Log and alert on new provider authentications for existing emails
- Enforce 2FA re-verification on alternative login methods

## Objectives

1. Trigger Apple's authentication flow within Cloudflare
2. Link the rogue Apple ID to the victim's account
3. Proceed to session establishment

## Instructions

### Step 1: Access Cloudflare Login

**Context**: Navigate to the target login interface.

Open a web browser and go to the Cloudflare dashboard login page at https://dash.cloudflare.com/login.

### Step 2: Select Sign in with Apple

**Context**: Choose the Apple authentication option to begin the flow.

On the login page, locate and click the 'Sign in with Apple' button, which initiates the redirect to Apple's authorization endpoint.

### Step 3: Authenticate with Rogue Apple ID

**Context**: Complete the authentication using controlled credentials.

Enter the credentials of the newly created Apple ID on Apple's prompt. Authorize the connection to Cloudflare, allowing the email to be shared.

**Expected Output**: Redirect back to Cloudflare with an authenticated session token.

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
- [[oauth-flow]]
