---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - authentication
  - session-extraction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:22.355Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-FetLife-Authentication

## Summary

This preparatory procedure extracts authentication artifacts needed for exploiting FetLife's invitation endpoint, including session cookies and CSRF tokens.

## Description

Authentication is required for the POST /users/invitation endpoint. This involves logging into FetLife and inspecting network requests or page source to obtain the _fl_sessionid cookie and authenticity_token, which prevent unauthorized or forged requests. This step ensures subsequent exploits use valid credentials without triggering auth errors.

## Requirements

1. Web browser with dev tools (e.g., Chrome Inspector)
2. Valid FetLife login credentials
3. Access to https://fetlife.com

## Defense

Defensive measures and detection strategies:

- Enforce short session timeouts and token rotation
- Monitor for unusual token extraction patterns in logs
- Use HTTPS-only and HSTS to prevent MITM

## Objectives

1. Obtain valid session cookie for request authentication
2. Extract CSRF token to bypass protection
3. Prepare for authenticated exploitation

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate and reach the invitation page.

Open browser, log in to FetLife, and navigate to https://fetlife.com/users/invitation.

### Step 2: Extract Session ID

**Context**: Capture the session cookie.

In dev tools > Application > Cookies, copy the value of _fl_sessionid.

### Step 3: Extract Authenticity Token

**Context**: Get the CSRF token from the form.

In dev tools > Elements, search for <input name="authenticity_token"> and copy its value.

> Expected: Token string like "abc123def456...".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- session-extraction
