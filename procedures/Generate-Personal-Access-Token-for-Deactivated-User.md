---
tags:
  - gitlab
  - token-generation
  - impersonation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:59.528Z'
sub_techniques: []
id: 6936ebdc-46c2-4ef6-932b-96aa5554c6ca
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-Personal-Access-Token-for-Deactivated-User

## Summary

This procedure generates a personal access token for a deactivated GitLab user using admin impersonation, enabling API access despite restrictions.

## Description

GitLab allows admins to create tokens for other users via impersonation. For deactivated users, this token retains validity for GraphQL API calls, bypassing the :access_api restriction enforced only in REST. Prerequisites include admin access and the user being deactivated.

## Requirements

1. Admin privileges
2. Deactivated user exists
3. Access to Admin Area > Users > Impersonation Tokens

## Defense

Defensive measures and detection strategies:

- Disable impersonation tokens for admins
- Log all token creations and monitor for deactivated users
- Rotate tokens regularly

## Objectives

1. Create API-scoped token for deactivated user
2. Verify token usability in GraphQL
3. Highlight policy enforcement gap

## Instructions

### Step 1: Access Impersonation Tokens

**Context**: Navigate to the deactivated user's profile in admin panel.

Go to Admin Area > Users, select the deactivated user, and click 'Impersonation Tokens' tab.

### Step 2: Create Token

**Context**: Generate token with necessary scopes.

Enter a name, select 'api' scope, set expiration if needed, and create. Copy the generated token.

> Token is valid for GraphQL despite user status.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- token
- api-scope
- bypass
