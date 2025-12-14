---
tags:
  - information-disclosure
  - path-disclosure
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Path-Disclosure-in-PasswordLock]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.575Z'
description: >-
  An information disclosure attack exploiting lack of input validation in the
  PasswordLock library, triggering a PHP warning that reveals the full server
  path.
id: fa867c68-cc6a-4fb4-a3d8-000aa0c52d89
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Full Path Disclosure via PHP hash() Warning in PasswordLock Library

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger Vulnerability] --> B[Extract Path Information]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specific (uses standard HTTP client like curl)

### Target Environment

- Web application using PHP
- PasswordLock library integrated for password handling
- Exposed endpoint accepting password input (e.g., login or unlock form)

### Initial Access Requirements

- Network access to the web application
- No credentials required for unauthenticated endpoints
- Ability to send crafted HTTP requests

## Detailed Attack Procedures

### Step 1: Trigger Vulnerability and Capture Error
procedure: [[procedures/Trigger-Path-Disclosure-in-PasswordLock]]

**Objective**: Send invalid (non-string) input to the password field to trigger a PHP hash() warning, disclosing the server path in the error message.

**Instructions**: Identify the endpoint using the PasswordLock library (e.g., a login form). Use [[commands/curl-trigger-passwordlock-error]] to send a non-string value like an integer or array in the password parameter:

```bash
curl -X POST 'http://target.com/login' -d 'password=123' -d 'username=test' --verbose
```

Monitor the response for the PHP warning: "Warning: hash() expects parameter 2 to be string, integer given in /full/server/path/to/PasswordLock.php on line X".

**Expected Output**: HTTP response containing the error message with the full server path (e.g., "/var/www/html/...").

**Success Indicators**:
- PHP warning appears in response
- Full server path is visible in the error output

## Attack Chain Summary

### Key Achievements

1. Successful triggering of input validation flaw
2. Extraction of sensitive server path information
3. Potential for further reconnaissance based on disclosed paths

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
