---
tags:
  - shopify
  - old-credentials
  - login
type: procedure
tools:
  - '[[tools/Chrome-Beta]]'
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
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:28:58.528Z'
sub_techniques: []
id: 1217057e-66f9-47e6-9c93-fc2799c8e87f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Login-to-Shopify-with-Old-Email-in-Separate-Browser

## Summary

This procedure attempts login using the old email credentials in an isolated browser, exploiting the lack of session invalidation to gain access post-email change.

## Description

Shopify sends verification codes to the old email during login attempts, allowing authentication even after the primary email update. This demonstrates the vulnerability where sessions tied to outdated credentials persist, potentially for former users or compromised old emails. A separate browser ensures isolation from the original session.

## Requirements

1. Old email address and password
2. Access to old email inbox for verification code
3. [[tools/Chrome-Beta]] for new session

## Defense

Defensive measures and detection strategies:

- Revoke all sessions on email verification code requests
- Block logins from old emails after primary change
- Implement rate limiting on verification attempts

## Objectives

1. Authenticate with old email
2. Receive and use verification code
3. Access account dashboard

## Instructions

### Step 1: Initiate Login

**Context**: Start the login process with outdated credentials.

Open [[tools/Chrome-Beta]], go to Shopify login, enter old email and password to trigger verification.

### Step 2: Complete Verification

**Context**: Use the code from the old email to finalize login.

Retrieve the code from the old inbox, input it, and observe successful dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Beta]]

## Tags

- shopify
- login
- old-email
