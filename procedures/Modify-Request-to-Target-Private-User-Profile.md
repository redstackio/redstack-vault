---
tags:
  - information-disclosure
  - api
  - request-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-query-private-profile]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:02.055Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a7805335-36bc-4970-8c65-acf4a68a414d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Modify-Request-to-Target-Private-User-Profile

## Summary

This procedure modifies a captured legitimate API request to target a private user's profile endpoint, exploiting the lack of privacy enforcement in the backend API to retrieve unauthorized data.

## Description

Using artifacts from a profile update request, change the HTTP method to GET and the path to /api/users/<private_username>. Retain CSRF and session headers to maintain authentication. This reveals data hidden by front-end privacy settings. Applicable to web APIs with inconsistent access controls. Outcomes include access to private user details without following the account.

## Requirements

1. Captured request from previous procedure (CSRF token, cookies)
2. Known private username (e.g., from public search)
3. Proxy tool or curl with auth headers

## Defense

Defensive measures and detection strategies:

- Enforce profile visibility checks in all API responses
- Log and alert on cross-user API queries
- Use role-based access control for user data endpoints

## Objectives

1. Successfully query private profile API
2. Bypass front-end privacy restrictions
3. Obtain response with hidden fields

## Instructions

### Step 1: Edit Request in Proxy Tool

**Context**: Transform the PATCH /api/me request into a GET for a private user.

**Command** ([[commands/curl-query-private-profile]]):
```bash
curl -X GET https://www.every.org/api/users/bug.hunter3 \
  -H "X-CSRF-Token: <captured_token>" \
  -H "Cookie: session=<session_cookie>" \
  -H "User-Agent: Mozilla/5.0..."
```

> Remove JSON body, update path to target private username (e.g., bug.hunter3). Forward via Burp Repeater. Expected output: 200 OK JSON response with user data.

### Step 2: Verify Response Accessibility

**Context**: Confirm the endpoint returns data for private profiles.

Check for presence of 'data.user' object without errors.

**Expected Output**: Full user profile JSON, including unauthorized fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-query-private-profile]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- information-disclosure
- api-modification
