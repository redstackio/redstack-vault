---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - gitlab
  - merge-request
  - access-token
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.678Z'
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
# Prepare-Merge-Request-and-Access-Token-in-GitLab

## Summary

This procedure prepares the attacker's resources in GitLab by creating a branch, merge request, and personal access token to facilitate API calls for the IDOR exploitation.

## Description

Within the attacker's private project, create a new branch to trigger a merge request (IID 1). Generate a personal access token with API scopes to authenticate subsequent requests. This enables interaction with the status check responses endpoint without UI restrictions.

## Requirements

1. Access to attacker_project in GitLab
2. Permissions to create branches and merge requests
3. Ability to generate personal access tokens

## Defense

Defensive measures and detection strategies:

- Monitor token creation and usage in audit logs
- Limit token scopes to minimum required
- Rotate tokens regularly and revoke unused ones

## Objectives

1. Create a merge request for API targeting
2. Obtain a valid access token for authenticated API calls
3. Ensure the setup allows SHA retrieval via error responses

## Instructions

### Step 1: Create Branch and Merge Request

**Context**: In attacker_project, initiate a merge request to get an IID for API use.

**Instructions**: Navigate to https://gitlab.domain.com/attacker01/attacker_project/-/branches/new, create a branch (e.g., 'test-branch'). On branch creation, click 'Create new merge request', name it arbitrarily, and create (IID 1).

### Step 2: Generate Access Token

**Context**: Create a token for API authentication.

**Instructions**: Go to https://gitlab.domain.com/-/profile/personal_access_tokens, create a new token named 'TOKEN' with scopes 'api' and 'read_api'. Copy the token value securely.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- merge-request
- access-token
