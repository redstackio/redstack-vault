---
tags:
  - nextcloud
  - app-token
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:29:28.250Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a7fccafe-5c2a-4863-8937-c8ab8babba93
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Obtain-Nextcloud-App-Token

## Summary

This procedure generates an app token in Nextcloud with filesystem access permissions, enabling authenticated API interactions for subsequent exploitation steps.

## Description

In Nextcloud, app tokens provide a form of OAuth-like authentication for applications. This step involves creating such a token via the web interface or API, scoped to include filesystem read/write access. The token acts as initial credentials for accessing user files, setting up the scenario for testing revocation bypass. Prerequisites include a valid Nextcloud user account with token creation rights. Expected outcome: A usable token string that authenticates API calls to the filesystem.

## Requirements

1. Valid Nextcloud user login credentials
2. Network access to the Nextcloud web server (HTTPS recommended)
3. Browser or API client for token generation

## Defense

Defensive measures and detection strategies:

- Enforce short-lived tokens and automatic expiration
- Monitor token creation events in Nextcloud logs for anomalous activity
- Implement role-based access control (RBAC) to limit token scopes

## Objectives

1. Acquire authentication material for filesystem access
2. Establish baseline authenticated session
3. Prepare for permission manipulation testing

## Instructions

### Step 1: Log In to Nextcloud

**Context**: Authenticate as a user with app token privileges to access token management.

Navigate to the Nextcloud login page and sign in with valid credentials. Proceed to user settings > Security > Devices & sessions to create a new app token.

### Step 2: Generate App Token

**Context**: Create the token with explicit filesystem permissions.

Enter a name for the app (e.g., "TestApp"), select scopes including "Files" for read/write access, and generate the token. Copy the resulting token string (format: username_xxxxxxxxxxxxxxxx).

**Expected Output**: Token string displayed once, store securely for use.

### Step 3: Verify Token

**Context**: Confirm the token grants filesystem access.

Use the token in an API call to list files, e.g., via browser developer tools or a client: append the token to requests as `?token=your_token` or in headers.

**Expected Output**: Successful response with file listing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- app-token
- authentication
