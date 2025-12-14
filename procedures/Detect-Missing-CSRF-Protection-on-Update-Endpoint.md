---
id: proc-001
tags:
  - csrf
  - web-testing
  - vulnerability-detection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.414Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-Missing-CSRF-Protection-on-Update-Endpoint

## Summary

This procedure identifies Cross-Site Request Forgery (CSRF) vulnerabilities in web applications by testing state-changing endpoints for missing token validation, focusing on user profile updates in Ruby on Rails apps.

## Description

In a typical attack scenario, an attacker tests POST/PATCH endpoints like /users/update to see if requests can be forged without a CSRF token. This is common in frameworks like Ruby on Rails where protect_from_forgery may be misconfigured or absent. Prerequisites include access to the application as an authenticated user. Expected outcomes: Confirmation of exploitability, enabling further PoC development for impacts like unauthorized data changes or XSS injection.

## Requirements

1. Authenticated session to the target web app
2. Browser developer tools or proxy (e.g., Burp Suite) for request inspection
3. Knowledge of the endpoint (e.g., /users/update) and parameters (e.g., user[username])

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens (e.g., authenticity_token in Rails) on all state-changing forms
- Use SameSite cookies and origin/header validation
- Monitor for anomalous requests from external referers

## Objectives

1. Verify absence of CSRF protection on sensitive endpoints
2. Document request parameters for PoC crafting
3. Assess potential impact on user data integrity

## Instructions

### Step 1: Inspect Endpoint Request

**Context**: Use browser tools to capture a legitimate update request and note the absence of CSRF-related headers or tokens.

Navigate to the user profile edit page, submit a benign change, and inspect the network tab for the POST to /users/update. Look for parameters like authenticity_token; if missing or optional, proceed.

### Step 2: Test Forged Request

**Context**: Replay the request without any CSRF token to confirm vulnerability.

Use a tool like curl with the victim's session cookie to simulate a cross-origin request:

```bash
curl -X POST https://fanfootage.com/users/update \
  -H "Cookie: _session_id=victim_session" \
  -d "user[username]=test_change" \
  -d "_method=patch" \
  -d "utf8=✓"
```

> This command sends a forged update; if it succeeds (e.g., 200 OK and profile changes), CSRF is missing. Expected output: JSON or redirect indicating success without token errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[detection]]
