---
id: proc-access-unprotected-admin
tags:
  - auth-bypass
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.547Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Unprotected-Admin-Directory

## Summary

This procedure exploits improper authentication by directly accessing or modifying URLs to reach unprotected admin directories in a DoD web application, bypassing login requirements.

## Description

Following directory discovery, attackers modify the URL (e.g., changing '1' to '9' in ████████:1:0::::: to access ████████:9:0:::::) or use the bruteforced path to enter the admin area. This exposes user management features without any checks, allowing creation of privileged accounts. The target is a public-facing web app with misconfigured directory protections.

## Requirements

1. Discovered admin directory path from prior reconnaissance
2. Web browser for manual navigation
3. No credentials needed due to the vulnerability

## Defense

Defensive measures and detection strategies:

- Require authentication middleware on all admin paths
- Use URL rewriting to hide or protect sensitive directories
- Log and alert on direct access to admin endpoints

## Objectives

1. Gain entry to admin interface without login
2. Access user management tools
3. Prepare for account creation

## Instructions

### Step 1: Modify the Base URL

**Context**: Alter the known login URL to target the admin path.

**Command** (Manual Browser Action):
No command; in browser, change URL from https://target.com/path:1:0::::: to https://target.com/path:9:0:::::.

> Loads the unprotected admin directory if vulnerable.

### Step 2: Verify Access

**Context**: Confirm no authentication is prompted.

**Command** (Manual Check):
Navigate to additional unprotected URLs like █████::::::.

> Successful access shows admin features without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web-vuln]]
