---
tags:
  - unauthorized-access
  - source-code-exposure
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: c5569901-866f-4ace-b453-600a11eb7efa
created_at: '2025-12-13T09:01:26.715Z'
updated_at: '2025-12-13T09:01:26.715Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Linked PullRequest Service

## Summary

This procedure uses the compromised HackerOne account to access the linked PullRequest service and view sensitive source code.

## Description

With valid login, the attacker authenticates to PullRequest via HackerOne SSO, gaining access to pull requests containing infrastructure source code and potentially unrevoked API keys.

## Requirements

1. Valid login to the compromised HackerOne account
2. Internet access to app.pullrequest.com
3. Web browser

## Defense

Defensive measures and detection strategies:

- Regularly audit and revoke access to linked services
- Monitor login activity from unusual IPs

## Objectives

1. Authenticate to linked service
2. Expose source code
3. Identify persistent access vectors

## Instructions

### Step 1: Navigate to PullRequest Login

**Context**: Initiate SSO login.

Go to https://app.pullrequest.com/login and select 'Sign in with HackerOne'.

> Redirects to authenticated session.

### Step 2: Access Pull Requests

**Context**: View sensitive content.

Navigate to the pull requests section to access HackerOne's codebase.

> Displays source code and related data.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- unauthorized-access
- source-code-exposure
