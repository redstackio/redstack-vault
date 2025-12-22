---
id: proc-uuid-2
tags:
  - gitlab
  - token
  - api
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:29.254Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-Personal-Access-Token

## Summary

This procedure creates a personal access token (PAT) for a GitLab user, which remains valid even after password expiration, enabling API and Git access in the bypass attack.

## Description

From the user's profile in GitLab, generate a PAT with scopes like 'api' and 'read_repository'. This token authenticates requests independently of password status, exploiting the vulnerability in GitLab's access control. Tested on self-hosted instances.

## Requirements

1. Logged-in user session
2. Access to https://gitlab.domain.com/-/profile/personal_access_tokens
3. Scopes: api, read_repository (minimum)

## Defense

Defensive measures and detection strategies:

- Regularly rotate and revoke tokens via admin dashboard
- Implement token expiration policies
- Audit token creation in logs

## Objectives

1. Obtain a valid PAT for the test user
2. Ensure token has sufficient scopes for project access
3. Store token securely for exploitation

## Instructions

### Step 1: Navigate to Token Creation

**Context**: Access the personal access tokens page.

Log in as 'user01' and go to https://gitlab.domain.com/-/profile/personal_access_tokens.

> Page loads with option to create new token.

### Step 2: Create Token

**Context**: Generate and copy the token.

Enter a name (e.g., 'test-token'), select scopes (api, read_repository), and create. Copy the generated token immediately as it won't be shown again.

> Token string (e.g., glpat-xxx) is displayed and copied.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- pat
- authentication
