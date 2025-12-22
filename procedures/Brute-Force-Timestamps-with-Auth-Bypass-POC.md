---
tags:
  - brute-force
  - poc-script
  - auth-bypass
type: procedure
tools:
  - '[[tools/impresscms-auth-bypass-poc]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/run-impresscms-auth-bypass-poc]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:10.875Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Password Guessing]]'
id: c8f338b1-e0c5-412a-a73b-dfd39ad911cf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Brute-Force-Timestamps-with-Auth-Bypass-POC

## Summary

This procedure automates the brute-forcing of timestamps in autologin_pass cookies using a custom PHP PoC script to find an MD5 collision exploiting type juggling, enabling authentication bypass in ImpressCMS.

## Description

The PoC script (auth-bypass.php) sends HTTP requests to the target ImpressCMS site, incrementing timestamps in the cookie until the computed MD5 hash starts with '0e', tricking the loose '!=' comparison into allowing autologin. Requires PHP and curl extension. Due to the rarity of collisions, it may take significant time (impractical in some cases), but succeeds in lab environments. Outcome: Successful unauthorized login as the target user.

## Requirements

1. PHP 7+ with curl extension
2. Target ImpressCMS URL and username
3. Local or remote access to run the script
4. Patience for potential long runtime

## Defense

Defensive measures and detection strategies:

- Patch to use strict comparisons or disable autologin
- Implement CAPTCHA or rate-limiting on login endpoints
- Monitor server logs for high-volume requests from single IP

## Objectives

1. Automate collision discovery via timestamp brute-force
2. Obtain valid cookies for persistent access
3. Gain shell or dashboard access as the user

## Instructions

### Step 1: Prepare PoC Script

**Context**: Ensure the auth-bypass.php is available and configured.

Download or write the script to handle URL and username args, compute MD5, and send requests.

### Step 2: Execute Brute-Force

**Context**: Run the script to iterate timestamps.

Execute [[commands/run-impresscms-auth-bypass-poc]]:

```bash
php auth-bypass.php http://localhost/impresscms/ admin
```

The script outputs progress like "[-] 2021-01-20 022141" until success.

### Step 3: Use Output Cookies

**Context**: Apply successful cookies for access.

Set cookies in browser or subsequent requests: autologin_uname=admin; autologin_pass=2021-01-20 022141:0.

**Expected Output**: "[-] Starting authentication bypass attack... [-] You can autologin with the following cookies: [-] Cookie: autologin_uname=admin; autologin_pass=2021-01-20 022141:0"

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]
- [[Valid Accounts]]

### Sub-Techniques

- [[Password Guessing]]

## Commands Used

- [[commands/run-impresscms-auth-bypass-poc]]

## Tools Used

- [[tools/impresscms-auth-bypass-poc]]

## Tags

- brute-force
- md5-exploit
