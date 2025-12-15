---
tags:
  - session-management
  - cookie-persistence
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.439Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6888cd4d-6632-4076-b8df-105f03ab8988
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Second Account in Same Session

## Summary

This procedure creates a second GitLab account in the same browser session without clearing cookies, allowing the old session cookie to persist alongside the new one for later exploitation.

## Description

GitLab does not properly invalidate old session IDs when creating new accounts in the same browser, enabling session cookie mixing. This step simulates the victim's login by registering another account, capturing the new `_gitlab_session` cookie while keeping the first one's token valid.

## Requirements

1. Existing browser session from first account
2. Temporary email for second account
3. Access to browser dev tools or Burp for cookie inspection

## Defense

Defensive measures and detection strategies:

- Invalidate all prior sessions on new account creation
- Enforce cookie clearing or new session issuance post-registration
- Log multi-account creations from same IP/session

## Objectives

1. Register second account without session reset
2. Extract new session cookie
3. Maintain old session context for token reuse

## Instructions

### Step 1: Register New Account

**Context**: Use the same browser tab/session to avoid cookie clearance.

Navigate to GitLab registration page, enter new details with temporary email, and complete signup/login via email confirmation. Do not log out.

### Step 2: Extract New Cookie

**Context**: Inspect the new session cookie for use in request modification.

Open browser dev tools (Network tab) or Burp Suite history to copy the `_gitlab_session` value for the second account.

No command; manual inspection. Expected output: New cookie value like `b9dbae76ceaed44954d57d0d505eca00`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-hijacking
- multi-account
