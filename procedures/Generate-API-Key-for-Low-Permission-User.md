---
id: proc-002
tags:
  - api-key
  - authentication
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:47.294Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-API-Key-for-Low-Permission-User

## Summary

This procedure generates an API token for a low-privilege HackerOne user, which will be used to test access to unauthorized resources, revealing inconsistencies in permission enforcement.

## Description

Log in as the low-permission user created in the organization, navigate to the API token settings page, and create a new token. This token inherits the user's group-based permissions but, due to the vulnerability, allows broader API access. The procedure assumes the user has been assigned to a restricted group and verifies basic token functionality.

## Requirements

1. Low-privilege user account in HackerOne
2. Access to https://hackerone.com/settings/api_token/edit
3. No prior API tokens conflicting

## Defense

Defensive measures and detection strategies:

- Align API token scopes with UI group permissions
- Log API token creations and monitor for low-priv user activity
- Implement token expiration and revocation policies

## Objectives

1. Obtain authentication credential for API testing
2. Ensure token is tied to low-perm user
3. Validate token in controlled queries

## Instructions

### Step 1: Log In as Low-Perm User

**Context**: Switch to the restricted user session.

Log in to HackerOne with the low-permission account credentials.

### Step 2: Access API Token Settings

**Context**: Navigate to token management.

Go to https://hackerone.com/settings/api_token/edit.

### Step 3: Generate Token

**Context**: Create and secure the API key.

Click to generate a new API token and copy it securely (e.g., format ██████=).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api-key
- authentication
- hackerone
