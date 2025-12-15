---
tags:
  - information-disclosure
  - csrf-bypass
  - path-disclosure
  - php
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-without-csrf]]'
platforms:
  - Web
  - PHP
complexity: low
procedures:
  - '[[procedures/Trigger-Path-Disclosure-by-Omitting-CSRF-Token]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
description: >-
  A single-step attack exploiting a CSRF token omission in POST requests to
  trigger an exception in debug mode, disclosing the server file path in the
  CSPR.NG web application.
skill_level: beginner
impact_level: low
id: b9aad9ad-80f5-495d-b02e-651c95a2a9c8
created_at: '2025-12-14T17:27:03.609Z'
updated_at: '2025-12-14T17:27:03.609Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Full Path Disclosure via CSRF Token Removal in CSPR.NG

## Overview

This attack chain demonstrates a vulnerability in the CSPR.NG application where removing the CSRF token from user-generated POST requests, such as login or user data changes, triggers an exception in debug mode. The exception reveals the full server file path (/var/www/csprng/src/public/index.php) due to an undefined variable on line 160 of index.php. While the path is predictable and only exploitable in debug mode, it represents an information disclosure risk. The attack requires direct interaction with the web application and is limited in impact, as no further exploitation is possible beyond path confirmation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Modify POST Request] --> B[Trigger Exception and Disclose Path]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform running PHP-based CSPR.NG application
- Debug mode enabled on the server
- Access to POST endpoints (e.g., login)

### Initial Access Requirements

- Network access to the web application
- No credentials required for initial request modification, but valid session may be needed for some endpoints

## Detailed Attack Procedures

### Step 1: Trigger Path Disclosure
procedure: [[procedures/Trigger-Path-Disclosure-by-Omitting-CSRF-Token]]

**Objective**: Modify a POST request to the login endpoint by removing the CSRF token, causing an exception that discloses the server file path.

**Instructions**: Use [[commands/curl-post-without-csrf]] to send a tampered POST request to the login endpoint without the _CSRF_TOKEN parameter:

```bash
curl -X POST 'https://target.com/login' \
  -d 'username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=' \
  -H 'Content-Type: application/x-www-form-urlencoded'
```

This omits the CSRF token, triggering an error on line 160 of index.php due to an undefined variable 'ex'.

**Expected Output**: An error response including a stack trace with the full server path, such as "/var/www/csprng/src/public/index.php on line 160".

**Success Indicators**:
- HTTP response contains exception details with file path
- Path like "/var/www/csprng/src/public/index.php" is visible in the error message

## Attack Chain Summary

### Key Achievements

1. Successful omission of CSRF token to bypass validation
2. Triggered debug-mode exception revealing server path
3. Confirmed information disclosure without further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
