---
tags:
  - cookie-manipulation
  - md5-collision
  - php
type: procedure
tools:
  - '[[tools/impresscms-auth-bypass-poc]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:10.878Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 91cf7d38-3284-40bf-aa14-f3b7885670e2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Craft-Malicious-Autologin-Cookies-for-MD5-Collision

## Summary

This procedure crafts HTTP cookies for ImpressCMS autologin exploitation, targeting the type juggling vulnerability by formatting the autologin_pass cookie with timestamps to force MD5 hashes into '0e' scientific notation.

## Description

Exploitation requires setting 'autologin_uname' to a target username like 'admin' and 'autologin_pass' to a string like 'YYYY-MM-DD HHMMSS:0'. The MD5 of (stored_password . db_pass . db_prefix . timestamp) must start with '0e' followed by digits to equal '0' in loose comparison. This step prepares these values manually or via script, assuming knowledge of DB credentials (inferred from code) or brute-forcing timestamps. Outcome: Ready-to-use cookies for testing bypass.

## Requirements

1. Target username (e.g., 'admin')
2. Knowledge of DB prefix and pass (from config.php or code review)
3. PHP environment to test MD5 computations locally
4. HTTP client like curl for manual request testing

## Defense

Defensive measures and detection strategies:

- Implement strict type comparisons (===) in auth code
- Rate-limit cookie-based logins
- Log and alert on repeated autologin attempts with unusual timestamps

## Objectives

1. Format cookies to exploit loose MD5 equality
2. Verify potential collision via local MD5 testing
3. Prepare for automated brute-forcing

## Instructions

### Step 1: Set Username Cookie

**Context**: Specify the target account.

Define autologin_uname=admin.

### Step 2: Format Timestamp Cookie

**Context**: Create incremental timestamp strings.

Generate autologin_pass as '2021-01-20 022141:0', incrementing the timestamp (e.g., via loop in PHP) until MD5(user_pass . ICMS_DB_PASS . ICMS_DB_PREFIX . timestamp) starts with '0e'.

### Step 3: Test Cookie Manually

**Context**: Send a single request to validate format.

Use curl to send cookies to the target login endpoint:

```bash
curl -b "autologin_uname=admin; autologin_pass=2021-01-20 022141:0" http://target/impresscms/
```

**Expected Output**: If collision hits, response shows logged-in state (e.g., user dashboard).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/impresscms-auth-bypass-poc]]

## Tags

- cookie-exploitation
- auth-bypass
