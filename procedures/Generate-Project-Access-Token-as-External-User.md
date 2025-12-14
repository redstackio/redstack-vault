---
id: uuid-3
tags:
  - gitlab
  - project-token
  - generation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:30:27.325Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Generate-Project-Access-Token-as-External-User

## Summary

Creates a project access token in GitLab as an external maintainer, which unexpectedly grants internal privileges due to bot user association.

## Description

The token is generated via UI or API with scopes like api and read_repository. The root cause is the token linking to an internal bot user, not inheriting external status. This enables API access beyond project scope. Expected outcomes: Token usable for internal resource access.

## Requirements

1. Maintainer access to a project as external user
2. Web browser or API client
3. GitLab instance with token feature enabled

## Defense

Defensive measures and detection strategies:

- Validate token creator status and restrict bot user privileges
- Monitor token creation events for external users
- Limit token scopes for external roles

## Objectives

1. Obtain a functional project token
2. Set scopes for broad access
3. Prepare for API exploitation

## Instructions

### Step 1: Access Token Settings

**Context**: Log in as external user and go to project settings.

Navigate to `/<namespace>/<project>/-/settings/access_tokens`.

> Token creation form loads.

### Step 2: Create Token

**Context**: Generate token with required scopes.

Enter name, select scopes (api, read_repository), set expiration if needed, and create.

> Token displayed once; copy it securely.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- access-token
- bot-user
