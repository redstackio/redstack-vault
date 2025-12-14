---
id: proc-lichess-auth-001
tags:
  - authentication
  - session-cookie
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:13.595Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Lichess-and-Obtain-Session-Cookie

## Summary

This procedure authenticates a user to the Lichess platform to obtain a valid session cookie, enabling authenticated requests to protected endpoints like image uploads.

## Description

Lichess uses session-based authentication via a cookie named 'lila2'. This step involves logging in through the web interface or API to capture the cookie, which is required for subsequent authenticated actions such as file uploads. The target environment is the public Lichess.org web application, and success results in a cookie that can be used in tools like curl for API interactions. Prerequisites include a valid Lichess account.

## Requirements

1. Valid Lichess username and password
2. Web browser or API client for login
3. Network access to https://lichess.org

## Defense

Defensive measures and detection strategies:

- Monitor for unusual login patterns from new IPs
- Enforce multi-factor authentication (MFA) if available
- Log session cookie issuances and validate against expected user agents

## Objectives

1. Establish authenticated session
2. Extract session cookie for API use
3. Enable access to protected upload endpoints

## Instructions

### Step 1: Log In to Lichess

**Context**: Access the login page and authenticate to generate the session cookie.

No specific command; use a web browser to navigate to https://lichess.org/login, enter credentials, and inspect the response headers or browser dev tools (Network tab) to copy the 'lila2' cookie value.

> Upon successful login, the cookie will appear in the Set-Cookie header or application storage. Replace 'YOUR_SESSION_COOKIE' in subsequent commands with the actual value.

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
- session-management
