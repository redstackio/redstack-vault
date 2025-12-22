---
tags:
  - cookie-stuffing
  - csrf
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/set-secure-admin-session-id-cookie]]'
  - '[[commands/set-master-udr-cookie]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0ffb5f20-4177-4816-82f2-5f5af7f91b85
created_at: '2025-12-13T23:56:03.996Z'
updated_at: '2025-12-13T23:56:03.996Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Perform Cookie Stuffing for Login CSRF

## Summary

This procedure performs cookie stuffing to enable Login CSRF by setting path-specific cookies to override legitimate ones during OAuth authorization.

## Description

Cookie stuffing exploits RFC 6265 path precedence to inject evil cookies like _secure_admin_session_id and _master_udr on /admin/oauth path. This forces the victim to log in under the attacker's session. Used in web-based CSRF attacks on OAuth flows. Requires JavaScript execution on a malicious page.

## Requirements

1. JavaScript access on victim browser
2. Knowledge of target cookie names and paths
3. Malicious page to execute document.cookie

## Defense

Defensive measures and detection strategies:

- Use CSRF tokens in OAuth flows
- Set cookies with strict paths and HttpOnly flags

## Objectives

1. Stuff evil session cookies
2. Override legitimate cookies
3. Enable forced login

## Instructions

### Step 1: Set Session ID Cookie

**Context**: Use document.cookie to set _secure_admin_session_id with specific path.

**Command** ([[commands/set-secure-admin-session-id-cookie]]):
```javascript
document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
```

> This overrides broader path cookies.

### Step 2: Set UDR Cookie

**Context**: Set _master_udr cookie similarly.

**Command** ([[commands/set-master-udr-cookie]]):
```javascript
document.cookie = '_master_udr=EVIL;path=/admin/oauth';
```

> Completes the stuffing for CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/set-secure-admin-session-id-cookie]]
- [[commands/set-master-udr-cookie]]

## Tools Used



## Tags

- cookie-stuffing
- csrf
