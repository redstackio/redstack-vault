---
tags:
  - setup
  - login
  - rocket-chat
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.186Z'
sub_techniques: []
id: 13d77f48-6764-4045-acd1-40bd4bb7d5fe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Logout and Prepare Rocket.Chat Login

## Summary

This procedure clears any active session in Rocket.Chat to ensure a fresh login attempt, preparing for request modification in the subsequent bypass steps.

## Description

To accurately test the 2FA bypass, any existing authentication state must be reset. This involves logging out and refreshing the login page on the web interface. The procedure targets the Rocket.Chat login endpoint and assumes prior account creation. Expected outcome is a clean state where login requires full credentials including TOTP.

## Requirements

1. Active session in the target Rocket.Chat account.
2. Browser access to the web interface.

## Defense

Defensive measures and detection strategies:

- Implement session timeout and secure logout to invalidate tokens.
- Log logout events for anomaly detection.

## Objectives

1. Terminate current session to force re-authentication.
2. Verify clean login page presentation.
3. Set stage for network request interception.

## Instructions

### Step 1: Initiate Logout

**Context**: End the current authenticated session.

Click the user avatar or menu in the top-right, select 'Logout', and confirm if prompted.

> Expected output: Redirect to login page with session cleared.

### Step 2: Refresh and Verify

**Context**: Ensure no residual session data persists.

Refresh the browser page (Ctrl+R or F5) and confirm the login form appears without auto-fill or session restoration.

> Expected output: Blank login interface requiring username, password, and TOTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[login]]
- [[rocket-chat]]
