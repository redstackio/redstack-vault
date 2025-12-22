---
id: proc-login-guest-rocket-chat
tags:
  - initial-access
  - guest-login
  - rocket-chat
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.015Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login-as-Guest-in-Rocket.Chat

## Summary

This procedure establishes initial access to a Rocket.Chat instance as a guest user, requiring no credentials if guest mode is enabled, setting the stage for privilege escalation attacks.

## Description

In vulnerable Rocket.Chat deployments, guest access allows unauthenticated entry into the chat application. This procedure authenticates via the web interface, enabling subsequent interactions over DDP WebSocket for method calls. It targets environments where guest permissions are not tightly controlled, leading to potential escalation chains. Expected outcome: Active guest session with limited 'user' role.

## Requirements

1. Network access to Rocket.Chat web interface (e.g., https://target.com)
2. Modern web browser with JavaScript enabled
3. Guest access enabled on the target instance

## Defense

Defensive measures and detection strategies:

- Disable guest access in Rocket.Chat settings to prevent unauthenticated entry
- Monitor login events for guest sessions and enforce CAPTCHA or rate limiting on auth endpoints
- Log all DDP method calls and alert on unusual user role queries

## Objectives

1. Gain foothold as guest user for further exploitation
2. Establish WebSocket connection for API interactions
3. Validate target vulnerability to guest-based attacks

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Rocket.Chat instance to initiate guest authentication.

No command required; use browser to visit the login URL (e.g., https://target.com/login).

> Select 'Login as guest' option. Expected output: Redirect to chat dashboard with guest indicator.

### Step 2: Verify Guest Session

**Context**: Confirm successful login and session establishment.

Inspect browser console or network tab for user object in API responses.

> Look for 'roles': ['user'] in session data. Expected output: Active session without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- guest-login
