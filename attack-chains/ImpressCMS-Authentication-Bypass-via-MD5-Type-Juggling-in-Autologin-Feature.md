---
tags:
  - auth-bypass
  - php
  - md5
  - type-juggling
  - impresscms
type: attack_chain
tools:
  - '[[tools/impresscms-auth-bypass-poc]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-ImpressCMS-Autologin-Code-for-Type-Juggling]]'
  - '[[procedures/Craft-Malicious-Autologin-Cookies-for-MD5-Collision]]'
  - '[[procedures/Brute-Force-Timestamps-with-Auth-Bypass-POC]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:10.883Z'
description: >-
  Multi-stage attack exploiting type juggling in ImpressCMS autologin to bypass
  authentication using crafted cookies and MD5 hash collisions.
skill_level: intermediate
impact_level: high
id: 80ca4a47-33c4-4d1d-9468-321c18cf53b4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
---
# ImpressCMS Authentication Bypass via MD5 Type Juggling in Autologin Feature

Multi-stage attack chain demonstrating exploitation of a type juggling vulnerability in ImpressCMS's autologin feature, allowing unauthorized access to user accounts via crafted cookies that exploit loose MD5 hash comparisons.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30-60 minutes (depending on collision luck) |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Analysis] --> B[Cookie Crafting]
    B --> C[Brute Force Exploitation]
    C --> D[Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/impresscms-auth-bypass-poc]]

### Target Environment

- ImpressCMS 1.4.2 or vulnerable versions
- PHP environment with MySQL backend
- Web server exposing the ImpressCMS installation
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Direct access to the target web application

### Initial Access Requirements

- No prior credentials needed
- Ability to send HTTP requests to the target
- Knowledge of a target username (e.g., 'admin')

## Detailed Attack Procedures

### Step 1: Code Analysis
procedure: [[procedures/Analyze-ImpressCMS-Autologin-Code-for-Type-Juggling]]

**Objective**: Identify the type juggling vulnerability in the autologin script by reviewing the source code.

**Instructions**: Download and inspect the ImpressCMS source code, focusing on /plugins/preloads/autologin.php. Look for cookie-based user fetching and MD5 hash comparisons.

**Expected Output**: Confirmation of loose '!=' comparison on lines 62-63, vulnerable to '0e' MD5 hashes being treated as zero.

**Success Indicators**:
- Vulnerability identified in password hash verification
- Understanding of exploitation via scientific notation collisions

### Step 2: Cookie Crafting
procedure: [[procedures/Craft-Malicious-Autologin-Cookies-for-MD5-Collision]]

**Objective**: Prepare crafted cookies exploiting the type juggling by formatting autologin_pass with timestamps for MD5 collision potential.

**Instructions**: Set 'autologin_uname' to the target username (e.g., 'admin'). Format 'autologin_pass' as 'YYYY-MM-DD HHMMSS:0', where the timestamp is incremented to find an MD5 hash starting with '0e' followed by digits.

**Expected Output**: Valid cookie values ready for testing, such as autologin_pass=2021-01-20 022141:0.

**Success Indicators**:
- Cookies structured correctly for loose equality bypass
- MD5 computation verifies potential collision format

### Step 3: Brute Force Exploitation
procedure: [[procedures/Brute-Force-Timestamps-with-Auth-Bypass-POC]]

**Objective**: Automate sending requests with incremental timestamps until a colliding MD5 hash enables autologin.

**Instructions**: Use the PoC script to target the installation. Execute [[commands/run-impresscms-auth-bypass-poc]] with the target URL and username:

```bash
php auth-bypass.php http://localhost/impresscms/ admin
```

Monitor for successful collision detection.

**Expected Output**: Script output showing successful cookies, e.g., "[-] You can autologin with the following cookies: [-] Cookie: autologin_uname=admin; autologin_pass=2021-01-20 022141:0".

**Success Indicators**:
- Successful HTTP response indicating logged-in session
- Access to user dashboard without credentials

## Attack Chain Summary

### Key Achievements

1. Identified type juggling flaw in autologin.php
2. Crafted exploitable cookies using timestamp-based MD5 collisions
3. Achieved unauthorized access via brute-forced autologin

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Brute Force]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
