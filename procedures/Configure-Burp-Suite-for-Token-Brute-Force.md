---
id: proc-17512-configure-burp
tags:
  - brute-force
  - configuration
  - web-proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:06.446Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Configure Burp Suite for Token Brute Force

## Summary

This procedure sets up Burp Suite to intercept and modify password reset token requests, preparing for automated brute forcing of the token parameter.

## Description

Burp Suite acts as a proxy to capture and alter HTTP requests to the token validation endpoint. In this attack, configure it to target /users/password/edit?reset_password_token=, marking the token for payload insertion. This enables efficient guessing without manual requests, exploiting response differences for validation.

## Requirements

1. Installed [[tools/Burp-Suite]]
2. Browser proxy configured to Burp (e.g., 127.0.0.1:8080)
3. Base reset URL from prior step

## Defense

Defensive measures and detection strategies:

- Implement client-side token validation
- Monitor for high request volumes to reset endpoints
- Use behavioral analysis for proxy-like traffic patterns

## Objectives

1. Intercept base request to token endpoint
2. Configure Intruder for token variations
3. Prepare payloads (e.g., character guesses)

## Instructions

### Step 1: Launch and Proxy Setup

**Context**: Start Burp and route traffic through it.

Open Burp Suite, ensure Proxy listener on 8080, set browser to use it.

> Navigate to reset URL; capture the GET request in Proxy > HTTP history.

### Step 2: Send to Intruder and Configure

**Context**: Mark token for brute forcing.

Right-click captured request > Send to Intruder. In Positions, highlight §reset_password_token=VALUE§ and set as payload position. Load payloads (e.g., alphanumeric list).

> Set attack type to Sniper; success: Intruder ready with token variations.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[configuration]]
- [[web-proxy]]
