---
id: proc-uuid-4
tags:
  - csrf
  - poc-generation
  - burp-suite
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.617Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Generate-Login-CSRF-Proof-of-Concept

## Summary

This procedure intercepts a login request and uses Burp Suite to create a CSRF PoC HTML file that can force authentication as the attacker.

## Description

The login form lacks CSRF protection, allowing forged POST requests. By intercepting a legitimate login with Burp and generating a PoC, an HTML file is created that submits attacker credentials automatically when loaded.

## Requirements

1. Burp Suite proxy configured in browser
2. Attacker credentials
3. Target login endpoint accessible

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all state-changing forms, including login
- Validate referer headers and origins
- Monitor for cross-site requests

## Objectives

1. Intercept and analyze login request
2. Generate exploitable CSRF HTML
3. Enable forced authentication

## Instructions

### Step 1: Configure Proxy and Attempt Login

**Context**: Set up interception.

Configure browser to proxy through Burp Suite, then attempt to log in with credentials.

> Expected: Request intercepted in Burp Proxy tab.

### Step 2: Generate CSRF PoC

**Context**: Use Burp tools to create HTML.

In the intercepted request, right-click and select 'Engagement tools' > 'Generate CSRF PoC', copy the resulting HTML.

> Expected: HTML form with hidden fields for credentials and auto-submit script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]
