---
id: p2b3c4d5-f6e7-8901-bcde-f23456789012
tags:
  - csrf
  - intercept
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:58.364Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Extract-Static-Idnonce-with-Burp-Suite

## Summary

This procedure involves using Burp Suite to intercept and extract the static '_idnonce' CSRF token during an email change on IntenseDebate, exploiting its non-regeneration for later reuse in attacks.

## Description

The '_idnonce' is a WordPress-style nonce intended for CSRF protection but fails to regenerate after user ID changes (e.g., email updates), remaining valid for ~12 hours. By changing the account email to a victim's and capturing the token via proxy interception, the attacker can reuse it cross-session. This targets https://intensedebate.com/edit-user-account and requires an authenticated session. Expected outcome: Token extraction enabling CSRF PoC crafting.

## Requirements

1. Active Burp Suite proxy configured in browser
2. Authenticated session on IntenseDebate
3. Victim's target email known

## Defense

Defensive measures and detection strategies:

- Regenerate nonces on state-changing actions like email updates
- Implement per-session token binding
- Log and alert on repeated nonce usage across accounts

## Objectives

1. Trigger email change to observe nonce behavior
2. Capture unchanging '_idnonce' value
3. Enable CSRF exploitation

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to monitor requests to the edit endpoint.

No command; in Burp Suite, enable Intercept in Proxy tab and configure browser proxy to 127.0.0.1:8080.

> Expected: All traffic routed through Burp.

### Step 2: Perform Email Change

**Context**: Submit POST to change email, intercepting the request.

No command; navigate to https://intensedebate.com/edit-user-account, enter victim's email, and submit. Forward the intercepted POST in Burp.

> Note '_idnonce' (e.g., '45898fbb7a') from form data; attacker logged out post-change.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[intercept]]
- [[web]]
