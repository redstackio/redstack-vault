---
id: proc-fpd-php-trim-001
name: Trigger PHP Trim Error for Full Path Disclosure
tags:
  - fpd
  - information-disclosure
  - php
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-malformed-array]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.181Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger PHP Trim Error for Full Path Disclosure

## Summary

This procedure exploits a Full Path Disclosure (FPD) vulnerability in PHP-based web applications like Localize.im by sending a crafted POST request with malformed array parameters. The attack tricks the trim() function into receiving an array instead of a string, triggering a PHP warning that reveals the server's internal file path, such as /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 191. This can aid in reconnaissance for further attacks by exposing the directory structure.

## Description

The vulnerability occurs in the project languages update endpoint due to improper validation of POST parameters. By appending '[]' to array notations (e.g., updatePhrases[previous][ID][0][]), the request passes an array to the trim() function, which expects a string. This causes a type error and a warning message that includes the full path to the PHP file where the error occurred. The target environment is a web application on PHP, accessible via HTTPS. Prerequisites include obtaining a valid CSRF token through normal application interaction and knowing the project and language IDs. Expected outcomes include the disclosure of sensitive path information without requiring elevated privileges.

## Requirements

1. Network access to the target web application (e.g., https://www.localize.im)
2. Valid CSRF token obtained from an authenticated session
3. Knowledge of specific project ID and language ID from the application
4. curl or similar tool for sending HTTP POST requests
5. Basic understanding of PHP error handling and HTTP requests

## Defense

Defensive measures and detection strategies:

- Input validation: Ensure all parameters passed to trim() or similar functions are strings by using type checks (e.g., is_string()) before processing
- Error handling: Suppress or log PHP warnings without exposing paths in production (use error_reporting(0) or custom error handlers)
- Web Application Firewall (WAF): Configure rules to detect and block requests with unusual array notations like extra '[]' in POST data
- Monitoring: Log and alert on PHP warnings or errors in application logs, scanning for path disclosures

## Objectives

1. Trigger a PHP type error to disclose the internal server file path
2. Gather reconnaissance information on the server's directory structure
3. Identify potential paths for further exploitation, such as local file inclusion

## Instructions

### Step 1: Obtain CSRF Token and Identifiers

**Context**: Interact with the Localize.im application to get necessary session data, including the CSRF token, project ID, and language ID. This is typically done by logging in and navigating to the project languages page.

**Command** (No specific command; use browser or [[commands/curl-post-malformed-array]] for session setup if needed):

Inspect the page source or network tab in browser dev tools to extract CSRFToken, project ID (e.g., from URL /projects/123), and language ID (e.g., /languages/456).

> Expected output: Values like CSRFToken=abc123, PROJECT_ID=123, LANGUAGE_ID=456.

### Step 2: Craft and Send Malformed POST Request

**Context**: Use the extracted values to build a POST request to the update endpoint, modifying array parameters by appending '[]' to force an array input to trim(), triggering the error.

**Command** ([[commands/curl-post-malformed-array]]):
```bash
curl -X POST 'https://www.localize.im/projects/[PROJECT_ID]/languages/[LANGUAGE_ID]' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'CSRFToken=[YOUR_CSRF_TOKEN]&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SECRET_CODES]&updatePhrases[translatorID]=[YOUR_ID]&updatePhrases[previous][testID][0][]='
```

> Replace placeholders with actual values. This sends data that mimics a legitimate update but includes the malformed updatePhrases[previous][testID][0][] parameter. Expected output: HTTP response containing a PHP warning with the full path, e.g., "Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 191".

### Step 3: Analyze Response for Disclosure

**Context**: Review the response body for the error message and extract the disclosed path.

No command needed; parse the output manually or with grep:

```bash
grep -i "warning.*trim" response.txt
```

> Expected output: The line with the full path. Success if path is visible; failure if no warning appears (e.g., due to invalid token).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-malformed-array]]

## Tools Used


## Tags

- fpd
- information-disclosure
- php
- web-vuln
