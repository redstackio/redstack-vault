---
id: proc-concrete-dir-predict-001
tags:
  - directory-prediction
  - ccm-token
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/php-time]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:24.090Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Predict-Update-Directory-Using-CCM-Token

## Summary

This procedure exploits the predictability of the updates directory name in Concrete CMS, generated via PHP time(), by correlating it with the time-based ccm_token obtainable from unauthenticated requests, allowing quick location of the payload with minimal brute-force.

## Description

The updates subdirectory is named with the Unix timestamp from time() at unzip time. The ccm_token, visible in unauthenticated pages (e.g., via /ccm_token in source), is also time-derived, providing an approximate timestamp. Attackers try 2-3 nearby values (e.g., 1600080000, 1600080001) via directory enumeration. This facilitates payload access post-unzip. Prerequisites: unzip done, web access; expected outcome: exact directory found.

## Requirements

1. Unauthenticated access to retrieve ccm_token
2. List of nearby timestamps
3. Tool for directory brute-force (e.g., browser or curl)

## Defense

Defensive measures and detection strategies:

- Use random or UUID-based directory names instead of time()
- Hide or obfuscate ccm_token generation
- Rate-limit directory access attempts

## Objectives

1. Approximate timestamp from ccm_token
2. Locate exact updates directory
3. Enable payload access with low guesswork

## Instructions

### Step 1: Retrieve CCM Token

**Context**: Get time-based token for timestamp approximation.

Make unauthenticated GET to http://target/ and inspect HTML source for ccm_token value.

> Expected output: Token like a time-derived string; extract approximate Unix time (e.g., via decoding if needed).

### Step 2: Brute-Force Directories

**Context**: Test nearby timestamps for the directory.

Try URLs: http://target/updates/1600080000/, http://target/updates/1600080001/, etc. Use [[commands/php-time]] locally to generate candidates: echo time();

```php
<?php echo time(); ?>
```

> Run in PHP CLI for current time approximation. Expected output: 200 OK for correct directory, 404 for others; locate poc.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/php-time]]

## Tools Used


## Tags

- directory-prediction
- ccm-token
- concrete-cms
