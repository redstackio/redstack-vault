---
id: p4d5e6f7-g8h9-0123-defg-456789012345
tags:
  - authentication
  - jwt
  - guest-access
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:28.848Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Guest-to-Obtain-JWT-Token

## Summary

This procedure authenticates as a guest user in the TalentMAP API to retrieve a JWT token, which is then used for subsequent unauthorized requests in the IDOR exploitation.

## Description

The API allows guest login with default credentials, returning a JWT token that authenticates requests but fails to enforce object-level permissions. This low-privilege access serves as the entry point for IDOR attacks, highlighting broken access controls.

## Requirements

1. API running at http://localhost:8000
2. Web browser for login interaction
3. Guest credentials: username 'guest', password 'guestpassword'

## Defense

Defensive measures and detection strategies:

- Disable or monitor guest accounts
- Implement token scoping to limit endpoint access
- Log all authentication events

## Objectives

1. Gain authenticated session as guest
2. Extract JWT from response
3. Enable API requests without full privileges

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the API's login interface.

Browse to http://localhost:8000 in a web browser.

> Loads the login form. Expected output: Login page displayed.

### Step 2: Submit Guest Credentials

**Context**: Enter and submit the guest login details.

Enter username: guest, password: guestpassword, and submit.

> Authenticates and returns JWT in response (e.g., JSON with token field). Expected output: Successful login with token.

### Step 3: Copy JWT Token

**Context**: Extract the token for header use.

Copy the token value from the browser's developer tools or response body.

> Prepares token for Authorization: Bearer {token}. Expected output: Valid JWT string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- authentication
- jwt
- guest-access
