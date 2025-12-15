---
tags:
  - code-review
  - php
  - impresscms
type: procedure
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:10.881Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1245dcf8-9a6b-4d4f-ab3b-4c5ba7d0ff5b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-ImpressCMS-Autologin-Code-for-Type-Juggling

## Summary

This procedure involves reviewing the ImpressCMS autologin.php source code to identify a type juggling vulnerability in the password hash comparison, enabling potential authentication bypass.

## Description

In ImpressCMS 1.4.2, the autologin feature in /plugins/preloads/autologin.php fetches users via cookies 'autologin_uname' and 'autologin_pass'. The verification on lines 62-63 uses a loose '!=' comparison on an MD5 hash of (user_pass . ICMS_DB_PASS . ICMS_DB_PREFIX . timestamp), which can be bypassed if the hash starts with '0e' (interpreted as scientific notation zero in PHP). This procedure details static code analysis to spot this flaw, a prerequisite for exploitation. Expected outcome: Confirmation of vulnerability for further crafting of exploits.

## Requirements

1. Access to ImpressCMS source code (download from official repo or target server)
2. Text editor or IDE for PHP code review
3. Basic knowledge of PHP type juggling and MD5 weaknesses

## Defense

Defensive measures and detection strategies:

- Use strict '===' comparisons in authentication logic
- Disable or remove autologin features in production
- Monitor for anomalous login attempts via cookie manipulation

## Objectives

1. Identify unsafe comparison operators in auth scripts
2. Understand exploitation vector via '0e' MD5 collisions
3. Document vulnerable code lines for reporting

## Instructions

### Step 1: Download and Locate Script

**Context**: Obtain the target file for analysis.

Download ImpressCMS source and navigate to /plugins/preloads/autologin.php.

### Step 2: Review Cookie Handling

**Context**: Examine user fetching logic.

Inspect lines 51-54: Look for icms::$user->getFromCookie('autologin_uname', 'autologin_pass') usage.

### Step 3: Identify Hash Comparison

**Context**: Pinpoint the vulnerable comparison.

Check lines 62-63 for MD5 computation and '!=' operator: if (md5(...) != $autologin_pass) – note loose equality allows type juggling.

**Expected Output**: Documentation of vulnerability, e.g., "Vulnerable: loose != on MD5 hash enables 0e collision bypass."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- vulnerability-analysis
