---
tags:
  - account-takeover
  - session-hijacking
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-with-session-cookie]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 517e1770-5589-4a88-a94c-2a395ac04104
created_at: '2025-12-11T06:10:40.569Z'
updated_at: '2025-12-11T06:10:40.569Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Impersonate User with Stolen Session Cookie

## Summary

This procedure uses a stolen session cookie to impersonate a user on a web platform, bypassing authentication and gaining access to protected resources.

## Description

By injecting the leaked cookie into HTTP requests or browser sessions, attackers can authenticate as the victim without IP or device restrictions. This targets platforms like HackerOne where sessions are not bound, allowing full access to user permissions.

## Requirements

1. Leaked session cookie value
2. Access to the target web platform
3. Tools for HTTP request manipulation

## Defense

Defensive measures and detection strategies:

- Bind sessions to IP addresses or devices
- Monitor for session reuse from different locations

## Objectives

1. Achieve authenticated access as the victim
2. Bypass login mechanisms
3. Enable further exploration

## Instructions

### Step 1: Prepare Cookie Injection

**Context**: Set up the request with the stolen cookie.

**Command** ([[commands/curl-with-session-cookie]]):
```bash
curl -H 'Cookie: session=leaked_cookie_value' https://hackerone.com/dashboard
```

> This sends an authenticated request to the dashboard.

### Step 2: Verify Access

**Context**: Confirm impersonation by accessing user-specific pages.

Navigate or request protected endpoints to ensure no authentication challenges.

> Look for successful responses indicating account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/curl-with-session-cookie]]

## Tools Used

- [[tools/cURL]]

## Tags

- [[account-takeover]]
- [[session-hijacking]]
