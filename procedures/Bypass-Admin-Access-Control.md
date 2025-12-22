---
id: proc-uuid-admin-bypass
tags:
  - access-bypass
  - client-side
  - admin
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - JavaScript
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:08:48.156Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Admin-Access-Control

## Summary

This procedure bypasses client-side JavaScript checks to access the admin interface, potentially allowing unauthorized entry with default credentials.

## Description

Many applications use client-side pathname checks to restrict admin access, which can be easily bypassed. In this Moodle instance, `/admin/user.php` relies on `window.location.pathname` validation in JavaScript, making it vulnerable to tampering. Combined with SSRF-disclosed configs, default creds like `admin/admin` may grant full control.

## Requirements

1. Access to the target domain
2. Browser with developer tools
3. Optional: Leaked config from SSRF

## Defense

Defensive measures and detection strategies:

- Enforce server-side access controls only
- Remove or secure client-side restrictions
- Log and alert on direct admin URL access
- Change default credentials and enable MFA

## Objectives

1. Gain unauthorized admin panel access
2. Exploit weak authentication for escalation
3. Access sensitive admin functions

## Instructions

### Step 1: Direct Navigation

**Context**: Attempt access without authentication.

Navigate to `/admin/user.php` in the browser.

**Expected Output**: JavaScript alert or block due to pathname check.

### Step 2: Disable Client-Side Check

**Context**: Bypass the restriction.

Open browser dev tools (F12), go to Console, and execute: `window.location.pathname = '/admin/user.php';` or disable JS entirely via browser settings.

**Expected Output**: Page loads without block.

### Step 3: Attempt Default Login

**Context**: Use exposed credentials.

If login form appears, enter `admin/admin` or creds from SSRF-leaked config.

**Expected Output**: Successful admin dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Client Software

## Commands Used


## Tools Used


## Tags

- [[access-bypass]]
- [[client-side]]
- [[admin]]
