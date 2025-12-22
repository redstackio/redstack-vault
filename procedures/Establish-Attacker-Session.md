---
id: proc-snapchat-session-001
name: Establish-Attacker-Session
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.362Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - session-establishment
  - authentication
platforms:
  - Web
  - Mobile (Android)
commands: []
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Establish-Attacker-Session

## Summary

This procedure logs the attacker into their own Snapchat account to establish a valid session, capturing necessary authentication headers for subsequent API requests in the account takeover chain.

## Description

In the Snapchat API, normal login establishes a session with headers like X-Snapchat-Client-Auth, which are required for authenticated requests. This step uses Burp Suite to perform and intercept the login, ensuring the session is active. It targets the mobile Android flow but works similarly on web. Prerequisites include the attacker's Snapchat credentials (username/password). Expected outcome: Active session tokens without alerting defenses.

## Requirements

1. Attacker's valid Snapchat username and password
2. Burp Suite configured as a proxy for the Snapchat app or API client
3. Network access to gcp.api.snapchat.com
4. Snapchat app version around 10.78 or compatible for header matching

## Defense

Defensive measures and detection strategies:

- Monitor for unusual login patterns from known devices
- Rate-limit API login attempts
- Implement device fingerprinting to detect proxy usage like Burp

## Objectives

1. Obtain valid session headers (e.g., X-Snapchat-Client-Auth)
2. Verify session usability for API calls
3. Prepare for escalation without invalidating the session

## Instructions

### Step 1: Configure Proxy and Login

**Context**: Set up Burp Suite to intercept traffic from the Snapchat Android app, then perform a standard login to capture session details.

**Command** (Manual via App, Intercepted in Burp):
No direct command; use Snapchat app login while proxied.

> Perform username/password login in the app. Burp will capture the POST to /login or equivalent, responding with 200 OK and headers like X-Snapchat-Client-Auth: [token]. Copy these for reuse.

### Step 2: Verify Session

**Context**: Send a simple authenticated request to confirm the session is active.

**Command** ([[curl-session-verify]]):
```bash
curl -X GET 'https://gcp.api.snapchat.com/user/me' -H 'X-Snapchat-Client-Auth: [token]'
```

> Expected output: JSON with attacker's user details. Success if no 401 Unauthorized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-establishment
- authentication
