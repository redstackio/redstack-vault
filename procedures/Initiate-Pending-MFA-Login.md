---
tags:
  - mfa
  - login
  - session
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.650Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4fda91b2-bdf1-41b3-a210-1eba62fab581
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Pending-MFA-Login

## Summary

This procedure starts the Moneybird login process with MFA enabled, creating a pending authentication session that remains vulnerable to persistence exploits.

## Description

In the context of exploiting session management flaws, this step involves beginning the two-step verification flow without completing it. This generates a temporary session token that, due to the vulnerability, is not invalidated by subsequent account changes. The target environment is the Moneybird web application, where users authenticate via email/password followed by MFA. Prerequisites include valid credentials and browser access. Expected outcome is a suspended login state ready for later exploitation.

## Requirements

1. Valid Moneybird account credentials (email and password)
2. Web browser with developer tools enabled
3. Direct network access to Moneybird's login endpoint

## Defense

Defensive measures and detection strategies:

- Implement immediate session invalidation on password or MFA changes
- Monitor for multiple concurrent login attempts from the same account
- Use short-lived session tokens for MFA pendings

## Objectives

1. Establish a pending MFA session for persistence testing
2. Capture session identifiers for verification
3. Set up conditions for bypassing security updates

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication entry point to begin the process.

Navigate to https://my.moneybird.com/login in your web browser.

> This loads the login form. Expected output: Login interface with email and password fields.

### Step 2: Submit Credentials

**Context**: Trigger the MFA flow by providing initial authentication details.

Enter the target account's email and password, then submit the form.

> This initiates the MFA challenge. Do not proceed to verify the MFA code. Expected output: Redirect to MFA prompt (e.g., SMS or app code entry).

### Step 3: Inspect Session

**Context**: Document the pending session for later use.

Open browser developer tools (F12), go to the Network tab, and note any session cookies or auth tokens from the login request.

> Expected output: Visible session ID or token in request headers or cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mfa]]
- [[login]]
- [[session]]
