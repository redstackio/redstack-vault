---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - broken-auth
  - session-replay
  - wordpress
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.170Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Capture-and-Replay-WordPress-Session-After-Logout

## Summary

This procedure demonstrates the exploitation of broken session management in WordPress.com by capturing an authenticated AJAX request for account settings, logging out, and replaying the request to access sensitive information, highlighting OWASP A2: Broken Authentication and Session Management.

## Description

In this attack scenario, an attacker with temporary access to a user's session (e.g., via cookie theft) can maintain access even after the user logs out. The target is WordPress.com's AJAX endpoint for loading account templates. The procedure involves proxying traffic with Burp Suite to capture and replay requests. Expected outcome: Server-side session validation fails, allowing post-logout access to account settings, including password change forms. Prerequisites include valid credentials and Burp Suite configured as a proxy.

## Requirements

1. Valid WordPress.com login credentials.
2. Burp Suite installed and running with browser proxy configured (e.g., 127.0.0.1:8080).
3. Network access to WordPress.com (no firewall blocks on HTTP/HTTPS).

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout by destroying server-side session state and cookies.
- Use short-lived session tokens with automatic expiration and monitor for anomalous replayed requests via WAF rules.
- Enable HTTP-only and secure flags on session cookies to prevent client-side access.

## Objectives

1. Capture an authenticated request to demonstrate session details.
2. Replay the request after logout to bypass authentication.
3. Access sensitive account data unauthorized.

## Instructions

### Step 1: Login and Navigate to Account Settings

**Context**: Authenticate and trigger the target AJAX request.

No specific command; use browser to log in at wordpress.com and go to account settings, proxying through Burp.

> Browser navigation establishes session; observe AJAX GET to `/wp-admin/admin-ajax.php` in Burp Proxy.

### Step 2: Capture and Forward to Repeater

**Context**: Intercept the request for replay preparation.

In Burp Proxy, intercept the request and send to Repeater.

> Captured request includes session cookies like `wordpress_logged_in_*`; preserve all headers.

### Step 3: Logout and Replay

**Context**: Test session invalidation by replaying post-logout.

Perform logout in browser, then in Burp Repeater, click Go to send the original request.

> Server responds with 200 OK and settings HTML if vulnerable; confirms persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[broken-auth]]
- [[session-replay]]
