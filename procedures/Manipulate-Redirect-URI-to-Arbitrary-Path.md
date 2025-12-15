---
id: uuid-manipulate-redirect
tags:
  - oauth
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/github-oauth-manipulate-redirect-to-arbitrary]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.853Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Redirect-URI-to-Arbitrary-Path

## Summary

This procedure exploits lax redirect_uri validation by setting it to an arbitrary path on the whitelisted domain, preventing code stripping since no comments widget is present.

## Description

The GitHub OAuth endpoint (/login/oauth/authorize) whitelists the entire edoverflow.com domain without path checks. By redirecting to a non-widget path like /1, the code remains in the URL after auth, enabling further leakage.

## Requirements

1. GitHub app client_id (e.g., 5f45cc999f7812d0b6d2)
2. URL encoding knowledge
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Validate redirect_uri paths explicitly
- Log anomalous redirects

## Objectives

1. Bypass code stripping logic
2. Retain code in URL for leakage
3. Test arbitrary path access

## Instructions

### Step 1: Craft Manipulated URL

**Context**: Encode redirect_uri to non-existent path.

**Command** ([[commands/github-oauth-manipulate-redirect-to-arbitrary]]):
```bash
# Browser or curl - Visit
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252F1%26scope%3Dpublic_repo
```

> Initiates auth; redirects to /1?code=... (code not stripped).

### Step 2: Verify Code Persistence

**Context**: Check URL post-redirect.

**Command** (Inspect URL):

Observe ?code parameter in address bar.

> Confirms manipulation success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/github-oauth-manipulate-redirect-to-arbitrary]]

## Tools Used

-

## Tags

- redirect-uri
- manipulation
