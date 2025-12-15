---
tags:
  - information-disclosure
  - php
  - pdo
  - path-disclosure
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-submit-malformed-phrasekey]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.170Z'
sub_techniques: []
id: 20641d44-5134-4e2c-ab4e-4e9a8b4fcf2e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-PDO-Quote-Error-for-Path-Disclosure

## Summary

This procedure exploits a vulnerability in PHP applications using PDO for database interactions, where array parameters are not validated before being passed to PDO::quote(). By submitting a malformed array in the phrasekey parameter during phraseChange or phrasemove actions, an exception is triggered, disclosing full server file paths in error messages and stack traces. This is useful for reconnaissance in web penetration testing.

## Description

The target application, such as a localization management system, processes user input for phrase updates without sanitizing for array types. When phrasekey is set to an array (e.g., via nested form fields like phraseChange[phraseKey][11]=test), PDO::quote() receives an array instead of a string, causing a type error warning on the relevant line in Database.php (typically line 30). This leads to a fatal PDOException on the query execution line (e.g., line 53) with a malformed SQL UPDATE statement for the 'phrases' table. The exception output includes the full server path, such as /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php, revealing the hosting environment and directory structure. This disclosure aids attackers in mapping the filesystem for subsequent exploits like LFI or privilege escalation.

## Requirements

1. HTTP access to a vulnerable PHP endpoint handling phrase management (e.g., unauthenticated if public)
2. Ability to craft POST requests with array-like parameters (e.g., using curl or browser dev tools)
3. Target running PHP with PDO and MySQL, without custom error handling that suppresses paths

## Defense

Defensive measures and detection strategies:

- Implement strict input validation to reject or flatten array parameters in web forms
- Configure PHP to suppress detailed error messages in production (e.g., display_errors=Off, log_errors=On)
- Use prepared statements correctly and wrap PDO::quote() calls with type checks
- Monitor logs for PDOException patterns or SQL syntax errors indicating malformed inputs

## Objectives

1. Trigger an unhandled exception to bypass normal error handling
2. Extract server file paths from the stack trace for reconnaissance
3. Identify potential entry points for deeper filesystem attacks

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate the phraseChange or phrasemove action in the application, typically a POST endpoint for updating translation phrases.

**Command** ([[commands/curl-submit-malformed-phrasekey]]):
```bash
curl -X POST 'http://target.com/path/to/endpoint.php' \
  -d 'action=phraseChange&phraseChange[phraseKey][11]=test' \
  --verbose
```

> This sends a POST request mimicking a form submission with an array parameter. The --verbose flag shows headers and response body. Expected output includes a 500 Internal Server Error with the warning and exception details.

### Step 2: Analyze Response for Path Disclosure

**Context**: Parse the error response to extract leaked paths and validate the vulnerability.

No specific command needed; inspect the HTTP response body for lines like "PDO::quote() expects parameter 1 to be string, array given in /full/path/to/Database.php on line 30" and the subsequent PDOException stack trace.

> Successful execution reveals paths like /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-malformed-phrasekey]]

## Tools Used

- [[tools/curl]]

## Tags

- information-disclosure
- php
- pdo
- path-disclosure
