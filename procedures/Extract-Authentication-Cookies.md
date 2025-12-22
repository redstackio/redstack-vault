---
tags:
  - saml
  - persistence
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.126Z'
sub_techniques: []
id: 73a94bae-7dfb-4a4e-a83b-b251a2d315f8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Extract-Authentication-Cookies

## Summary

This procedure captures Set-Cookie headers from the SAML response and uses them to maintain an authenticated session as the impersonated admin user.

## Description

After the POST triggers login, the 302 response includes cookies (wordpress_logged_in, wordpress_sec, saml_login) that authenticate the session. Attackers extract these for browser import or further requests, enabling dashboard access and site control. Applies to WordPress; prerequisites: successful POST; outcomes: persistent admin access.

## Requirements

1. Successful 302 response from ACS
2. Ability to parse HTTP headers
3. Browser or tool for cookie import

## Defense

Defensive measures and detection strategies:

- Secure cookie flags (HttpOnly, Secure, SameSite)
- Monitor for anomalous login patterns from SAML
- Rotate session tokens on suspicious activity

## Objectives

1. Identify and copy authentication cookies
2. Apply to client for session reuse
3. Verify admin dashboard access

## Instructions

### Step 1: Parse Response Headers

**Context**: From curl -v output, locate Set-Cookie lines.

Look for:

```http
Set-Cookie: wordpress_logged_in_[hash]=...; path=/
Set-Cookie: wordpress_sec_[hash]=...; path=/
Set-Cookie: saml_login=1; path=/
```

> Copy all relevant cookies. Expected output: List of cookie name=value pairs.

### Step 2: Import Cookies

**Context**: Use in browser dev tools or subsequent curl.

For browser: Edit application cookies for the domain. For curl:

```bash
curl -b "wordpress_logged_in_[hash]=...; wordpress_sec_[hash]=..." https://target.com/wp-admin/
```

> Expected output: Access to /wp-admin without re-auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[saml]]
- [[Persistence]]
