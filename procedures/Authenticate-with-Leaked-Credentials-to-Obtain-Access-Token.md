---
id: proc-authenticate-leaked-credentials
tags:
  - authentication
  - valid-accounts
  - api
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
updated_at: '2025-12-14T17:28:51.717Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate with Leaked Credentials to Obtain Access Token

## Summary

This procedure uses discovered leaked credentials to authenticate against a target's API, obtaining a valid access token for further unauthorized actions, as seen in the Starbucks credential leak allowing API access.

## Description

With credentials extracted from a public source, submit an authentication request to the target's login endpoint. For Starbucks' China operations, this involves POSTing to an API auth service. Prerequisites: Valid credentials and API endpoint knowledge (often inferred from docs or leaks). Outcomes: Token for API calls, enabling limited functionality like coupon generation.

## Requirements

1. Leaked credentials (username/password or key)
2. Known authentication endpoint URL
3. HTTP client for requests (e.g., curl, browser dev tools)

## Defense

Defensive measures and detection strategies:

- Rotate credentials immediately upon leak detection
- Implement rate limiting and anomaly detection on auth endpoints
- Use multi-factor authentication (MFA) to mitigate credential reuse

## Objectives

1. Gain authenticated session via leaked creds
2. Obtain bearer token for API access
3. Validate token scope for exploitation

## Instructions

### Step 1: Prepare Authentication Request

**Context**: Format the request with leaked credentials.

Construct a POST request to the auth endpoint, e.g., https://api.starbucks.cn/auth, with JSON body {"username": "leaked_user", "password": "leaked_pass"}.

> Use tools like curl: curl -X POST -H "Content-Type: application/json" -d '{"username":"user","password":"pass"}' https://api.example.com/auth

### Step 2: Submit and Capture Token

**Context**: Execute the request and parse the response for the token.

Send the request and extract the access_token from the JSON response.

> Store the token securely for next steps; test by making a simple API call with Authorization: Bearer <token>.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[valid-accounts]]
- [[api]]
