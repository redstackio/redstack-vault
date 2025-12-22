---
tags:
  - wordpress
  - ajax
  - md5
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/compute-md5-hash]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:17.948Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 064f24df-6aa4-4775-86b9-5a67d5ca91f8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Predictable AJAX Endpoints in Redux Framework

## Summary

This procedure identifies the predictable AJAX endpoints in the Gutenberg Template Library & Redux Framework WordPress plugin by computing MD5 hashes of the site URL concatenated with known salts ('-redux' and '-support'), enabling subsequent unauthenticated access.

## Description

The Redux Framework plugin generates AJAX action endpoints using MD5 hashes of the site's home URL plus fixed salts, making them guessable without authentication. This procedure computes these hashes, which are used in actions like 'redux_support' to access sensitive data. It targets WordPress sites running vulnerable plugin versions (4.2.11 and below) and requires only the public site URL. Expected outcome: Obtain hash values for endpoint construction, facilitating information disclosure.

## Requirements

1. Target WordPress site URL (e.g., https://example.com)
2. Access to a system with md5sum or equivalent (Linux/macOS/Bash)
3. Knowledge of plugin salts ('-redux', '-support')

## Defense

Defensive measures and detection strategies:

- Update to Redux Framework version 4.2.12 or higher
- Implement authentication checks on all AJAX actions
- Monitor for unusual MD5 hash patterns in logs or anomalous requests to admin-ajax.php

## Objectives

1. Compute predictable endpoint hashes for AJAX actions
2. Prepare for unauthenticated requests to sensitive endpoints
3. Gather initial reconnaissance on target system

## Instructions

### Step 1: Obtain Site URL

**Context**: Retrieve the full home URL of the target WordPress site, as used by the plugin for hashing.

No command required; note the URL (e.g., https://example.com).

### Step 2: Compute MD5 Hash for Endpoints

**Context**: Generate the hashes by concatenating the site URL with each salt and computing MD5. This reveals the predictable endpoints.

**Command** ([[commands/compute-md5-hash]]):
```bash
echo -n "https://example.com-redux" | md5sum
```

> This command outputs the MD5 hash (e.g., 'a1b2c3d4e5f67890123456789012345') without newline artifacts. Repeat for '-support' salt: echo -n "https://example.com-support" | md5sum. Use these hashes in subsequent AJAX action parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/compute-md5-hash]]

## Tools Used

- None

## Tags

- [[wordpress]]
- [[ajax]]
- [[md5]]
