---
id: proc-extract-owncloud-cookies
tags:
  - cookie-extraction
  - session-hijacking
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
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:57.725Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Extract ownCloud Session Cookies

## Summary

This procedure captures session cookies from an authenticated ownCloud session in the browser, enabling their use in forged CSRF requests to impersonate the victim.

## Description

After admin login, use browser developer tools to inspect and copy the oc_sessionPassphrase and oclt1tejv3yd cookies. These are required for the curl-based exploitation, as the CSRF bypass relies on valid session authentication without token validation.

## Requirements

1. Authenticated session in browser
2. Developer tools enabled (F12 in most browsers)
3. Target cookies: oc_sessionPassphrase and oclt1tejv3yd

## Defense

Defensive measures and detection strategies:

- Set HttpOnly and Secure flags on session cookies
- Monitor for unusual cookie access patterns
- Use token-based auth alongside cookies

## Objectives

1. Obtain valid session cookies
2. Prepare for request forgery
3. Ensure cookies are current

## Instructions

### Step 1: Open Developer Tools

**Context**: Inspect the active session.

**Command** (browser action):
```bash
# Press F12, go to Application/Storage > Cookies > http://localhost:8080
```

> Locate and copy oc_sessionPassphrase and oclt1tejv3yd values. Expected output: Cookie strings extracted.

### Step 2: Validate Cookies

**Context**: Test if cookies enable access.

**Command** (manual test):
```bash
# Paste into a simple curl GET request to /index.php/apps/files
```

> Expected output: Successful response without login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cookies
- session
