---
tags:
  - information-disclosure
  - api
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-capture-profile-patch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:02.056Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f0f1fdb5-ea2e-4322-936a-31661887ecc9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Capture-Legitimate-Profile-Update-Request

## Summary

This procedure involves triggering and intercepting a legitimate profile update request on a web application to capture authentication artifacts like CSRF tokens and session cookies, which are then reused for unauthorized API queries.

## Description

In the context of the every.org platform, users update profiles via a PATCH request to /api/me. By navigating to the settings page and submitting an update, an attacker can proxy this request to obtain headers and tokens. This sets the stage for modifying the request to target other users' private data. The target environment is a web-based API with session-based authentication. Expected outcomes include a complete HTTP request replica for further manipulation.

## Requirements

1. Authenticated session to the target web application (e.g., every.org)
2. Proxy tool like Burp Suite configured to intercept traffic
3. Access to profile settings page

## Defense

Defensive measures and detection strategies:

- Implement request signing or additional auth checks beyond CSRF
- Monitor for unusual request patterns from authenticated sessions
- Rate-limit API calls to profile endpoints

## Objectives

1. Obtain valid CSRF token and session cookies
2. Capture full request structure for replication
3. Ensure no disruption to normal user workflow

## Instructions

### Step 1: Configure Proxy and Navigate to Settings

**Context**: Set up interception and access the profile update interface to trigger the request.

**Command** ([[commands/curl-capture-profile-patch]]):
```bash
# Note: This is a manual trigger; use browser with proxy. Equivalent curl for testing (requires prior auth):
curl -X PATCH https://www.every.org/api/me \
  -H "X-CSRF-Token: <captured_token>" \
  -H "Cookie: session=<session_cookie>" \
  -H "Content-Type: application/json" \
  -d '{"some_field": "updated_value"}'
```

> This command simulates the PATCH request. In practice, use Burp Suite to intercept the browser-submitted request. Expected output: 200 OK with updated profile confirmation.

### Step 2: Intercept and Save Request Details

**Context**: Capture all headers, method, and body from the proxied request.

Export the intercepted request from Burp Suite for modification in the next procedure.

**Expected Output**: Saved request file with full HTTP details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-capture-profile-patch]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- information-disclosure
- request-interception
