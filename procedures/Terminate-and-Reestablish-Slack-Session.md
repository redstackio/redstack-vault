---
id: proc-uuid-2
tags:
  - csrf
  - web
  - session-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.695Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Terminate and Reestablish Slack Session

## Summary

This procedure logs out of the current Slack session to invalidate it temporarily, then logs back in to create a new session, demonstrating that the old CSRF token remains valid.

## Description

As part of the CSRF bypass attack, logging out should normally invalidate tokens, but in this vulnerability, the crumb token persists. This step tests token non-expiration by re-authenticating and accessing the settings page again, where a new token is generated but can be overridden. Performed via standard browser UI on web platform.

## Requirements

1. Active Slack session from prior login
2. Valid credentials
3. Browser access

## Defense

Defensive measures and detection strategies:

- Enforce token regeneration and invalidation on logout
- Log session terminations and monitor re-authentications
- Rate-limit login attempts

## Objectives

1. End current session
2. Create new session with fresh token
3. Confirm old token usability

## Instructions

### Step 1: Initiate Logout

**Context**: Terminate the session.

Click user avatar > Sign out or use settings logout option.

> Redirects to login page, session cookies cleared.

### Step 2: Re-authenticate

**Context**: Establish new session.

Enter credentials at https://app.slack.com and login.

> Dashboard access granted.

### Step 3: Return to Settings

**Context**: Load page to generate new token.

Navigate to https://sehacure.slack.com/account/settings.

> New crumb token in form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[session-management]]
