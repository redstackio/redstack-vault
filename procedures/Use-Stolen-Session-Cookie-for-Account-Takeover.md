---
tags:
  - account-takeover
  - impersonation
type: procedure
tools:
  - Browser
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:34.489Z'
sub_techniques: []
id: 1d159149-d387-4985-bd81-145f6920f77a
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
---
# Use-Stolen-Session-Cookie-for-Account-Takeover

## Summary

This procedure injects the stolen 'd' session cookie into requests or a browser to impersonate the victim and gain unauthorized access to their Slack account and data.

## Description

With the captured session cookie from the smuggling exploit, this enables lateral movement to the victim's Slack workspace. Targets cookie-based auth; requires the cookie value. Outcome is full control over the account, including data access.

## Requirements

1. Captured 'd' cookie value
2. Browser or HTTP client
3. Access to slack.com

## Defense

Defensive measures and detection strategies:

- Implement short-lived session tokens
- Monitor for anomalous logins from unusual IPs
- Use multi-factor authentication beyond cookies

## Objectives

1. Bypass authentication
2. Access victim data
3. Maintain persistence

## Instructions

### Step 1: Inject Cookie in Browser

**Context**: Use dev tools to set the cookie.

No command; in browser (e.g., Chrome), open DevTools > Application > Cookies > slack.com, add 'd' with stolen value.

> Refresh slack.com to authenticate as victim.

### Step 2: Verify Access

**Context**: Test for data access.

Navigate to private channels or use API calls.

> Expected: Full workspace visibility without password.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- Browser

## Tags

- ato
- slack
