---
tags:
  - inspection
  - dev-tools
  - rocket-chat
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.183Z'
sub_techniques: []
id: a7e5937e-4e55-4260-9f37-8dabada74973
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect Rocket.Chat Login Requests with Web Inspector

## Summary

This procedure uses browser developer tools to monitor the structure of login requests in Rocket.Chat, enabling modification for the 2FA bypass exploit.

## Description

The Web Inspector (Developer Tools) allows real-time inspection of HTTP requests to the /api/v1/login endpoint. In the attack scenario, this reveals the JSON payload format (username, password, code). Prerequisites include a modern browser like Chrome or Firefox. Successful inspection confirms the request details for script-based exploitation.

## Requirements

1. Browser with Developer Tools (e.g., Chrome DevTools).
2. Access to the Rocket.Chat login page.

## Defense

Defensive measures and detection strategies:

- Enable HTTPS and HSTS to prevent request tampering.
- Server-side logging of malformed requests.

## Objectives

1. Capture and analyze the normal login request payload.
2. Identify fields for modification (e.g., adding 'cas').
3. Prepare console for script execution.

## Instructions

### Step 1: Open Developer Tools

**Context**: Launch the inspection interface.

Press F12 or right-click on the page and select 'Inspect Element'. Navigate to the 'Network' tab.

> Expected output: Empty or ongoing network log.

### Step 2: Simulate Normal Login

**Context**: Trigger a request to observe its structure.

Enter credentials (including valid TOTP) and submit the login form. Filter the Network tab for 'login'.

> Expected output: POST request details showing JSON body with user, password, code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Inspector]]

## Tags

- [[inspection]]
- [[dev-tools]]
- [[rocket-chat]]
