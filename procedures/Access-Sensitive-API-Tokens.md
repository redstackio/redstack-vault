---
tags:
  - discovery
  - api-token
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Jenkins
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cecfa3af-9349-4d34-953b-7206178e2b14
created_at: '2025-12-11T03:47:56.626Z'
updated_at: '2025-12-11T03:47:56.626Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Access Sensitive API Tokens

## Summary

This procedure involves navigating authenticated Jenkins interfaces to retrieve exposed API tokens.

## Description

Once logged in, users can access their profile or manage users section to view API tokens, which may grant further access to APIs or integrations. This exploits poor access controls in misconfigured instances.

## Requirements

1. Authenticated Jenkins session
2. Permissions to view user configurations
3. Web browser access

## Defense

Defensive measures and detection strategies:

- Disable or restrict API token visibility
- Implement role-based access control (RBAC)

## Objectives

1. Retrieve API tokens
2. Use tokens for automated access
3. Escalate privileges if possible

## Instructions

### Step 1: Navigate to User Profile

**Context**: Access the user configuration page.

Go to https://jenkins.target.com/user/yourusername/configure.

### Step 2: View API Tokens

**Context**: Locate and copy exposed tokens.

In the configuration page, find the 'API Token' section and note the tokens.

> Tokens can be tested via API calls like curl with Authorization header.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser]]

## Tags

- [[Discovery]]
- #api-token
