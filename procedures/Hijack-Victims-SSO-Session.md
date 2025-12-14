---
id: proc-hijack-sso-session
tags:
  - session-hijacking
  - impersonation
type: procedure
tools: []
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
updated_at: '2025-12-14T04:38:39.636Z'
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Hijack Victim's SSO Session

## Summary

This procedure injects the stolen session cookie into the attacker's browser to impersonate the victim across all services using the shared SSO domain.

## Description

With the UBIC_AUTH cookie, the attacker accessed account.ubnt.com, store.ubnt.com, and more, even after victim logout, due to the cookie's domain-wide scope and lack of HttpOnly enforcement in some contexts.

## Requirements

1. Stolen valid session cookie
2. Browser with cookie import capability (e.g., extension)
3. Target services under the same domain

## Defense

Defensive measures and detection strategies:

- Enforce HttpOnly on session cookies to prevent client-side access
- Implement session binding to IP/User-Agent and logout propagation across services

## Objectives

1. Set the cookie in attacker's session
2. Gain unauthorized access to victim accounts
3. Demonstrate persistence post-victim actions

## Instructions

### Step 1: Import Cookie

**Context**: Load the cookie into the browser for reuse.

**Instructions**: Use a cookie editor extension (e.g., EditThisCookie) to add UBIC_AUTH=leaked_value for .ubnt.com domain.

### Step 2: Trigger Set-Cookie

**Context**: Use an API call to solidify the session.

**Instructions**: Visit https://sso.ubnt.com/api/sso/v1/user/self; the response's Set-Cookie header binds the session.

### Step 3: Access Services

**Context**: Impersonate across ecosystem.

**Instructions**: Navigate to account.ubnt.com (manage profile), community.ubnt.com (post as victim), store.ubnt.com (view orders). Test persistence by logging out from another session.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[impersonation]]
