---
tags:
  - token-theft
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:12.479Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f07de7e0-afbb-4fc8-a3fb-6a078adc2f1f
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-Password-Reset-Token

## Summary

This procedure sets up the attacker-controlled domain to intercept and log the password reset token exposed via the open redirect.

## Description

Upon redirect, the Mars site appends the token to the attacker's URL. The server must capture this from query parameters. Simple HTTP logging or a capture script suffices. Outcome is the raw token for immediate use in reset.

## Requirements

1. Attacker-controlled web server (e.g., simple HTTP endpoint)
2. Logging capability (access logs or custom script)
3. HTTPS to avoid browser warnings (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Strip sensitive params (like tokens) before redirects
- Use HTTP-only cookies for tokens instead of URL params
- Monitor external redirects for token leaks

## Objectives

1. Receive and parse the redirect request
2. Extract the token from URL parameters
3. Store securely for next steps

## Instructions

### Step 1: Configure Server Endpoint

**Context**: Set up a page to handle the redirect and log params.

Host a simple HTML page at `/capture` on attacker.com that logs GET params, e.g., using server-side script to write to file: token = request.query['token'].

> Ensure the endpoint echoes or forwards to mimic legitimacy if needed.

### Step 2: Log Incoming Request

**Context**: Capture the token when victim clicks.

Review server logs after redirect: look for `?token=abc123` in access logs or custom output.

> Token is valid for a short window (e.g., 15-60 min), so act quickly.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[credential-access]]
