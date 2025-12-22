---
id: proc-uuid-test-manual-attempts
tags:
  - brute-force
  - rate-limiting
  - authentication
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
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:29:20.494Z'
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Test Manual Login Attempts for Rate Limiting

## Summary

This procedure manually tests the login form with multiple invalid credentials to detect the presence of rate limiting, account lockouts, or CAPTCHAs on the WordPress admin login.

## Description

WordPress sites without plugins like Limit Login Attempts are vulnerable to brute force if no server-side restrictions exist. By submitting 10+ failed logins, the attacker confirms the server accepts unlimited requests, paving the way for automation. This targets the /wp-login.php endpoint, observing consistent error responses without blocks.

## Requirements

1. Access to the login form from Step 1
2. List of invalid test credentials (e.g., admin:wrongpass)
3. Browser for manual input

## Defense

Defensive measures and detection strategies:

- Enable rate limiting (e.g., 5 attempts per IP)
- Integrate CAPTCHA after failures
- Log and alert on repeated 401/403 responses

## Objectives

1. Confirm no restrictions on login attempts
2. Measure response consistency
3. Identify vulnerability for escalation

## Instructions

### Step 1: Submit Invalid Logins

**Context**: Enter wrong username/password combinations repeatedly.

No command; manual browser action:

In the login form at /wp-admin/, try: username: "admin", password: "wrong1"; repeat with variations up to 20 times.

> Server returns error like "Invalid username or password" each time, without delays or blocks.

### Step 2: Monitor for Blocks

**Context**: Check for any intervention after multiple attempts.

Observe page load times and responses.

> Expected: No CAPTCHA, no IP ban, no HTTP 429; all attempts succeed in reaching the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used


## Tags

- [[brute-force]]
- [[rate-limiting]]
