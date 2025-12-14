---
id: proc-analyze-error-001
tags:
  - information-disclosure
  - error-analysis
  - path-recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/grep-php-warning]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:26:12.019Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Analyze-PHP-Error-for-Server-Path-Disclosure

## Summary

This procedure parses the PHP error response from the malformed request to extract and interpret the disclosed server file path for reconnaissance.

## Description

Upon triggering the error, the response contains a warning like 'Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 192', revealing the internal structure.

## Requirements

1. Captured response from previous POST request
2. Text processing tools like grep
3. Knowledge of PHP error formats

## Defense

Defensive measures and detection strategies:

- Disable error reporting in production (display_errors=Off)
- Log errors without exposing paths to users
- Monitor for trim() warnings in application logs

## Objectives

1. Identify disclosed path components
2. Infer server hosting environment
3. Support further targeted exploits

## Instructions

### Step 1: Capture and Search Response

**Context**: Extract the warning from the HTTP response.

**Command** ([[commands/grep-php-warning]]):
```bash
curl -s ... > response.txt
grep -i "warning" response.txt
```

> Output: Warning message with path like /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 192.

### Step 2: Parse Path Information

**Context**: Analyze the path for directory structure.

**Command** ([[commands/grep-php-warning]]):
```bash
echo "Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 192" | sed -n 's/.*in \(.*\) on line \([0-9]*\)/Path: \1, Line: \2/p'
```

> Expected: Path: /srv/data/web/vhosts/www.localize.im/htdocs/index.php, Line: 192.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/grep-php-warning]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[error-analysis]]
