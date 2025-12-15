---
tags:
  - information-disclosure
  - path-disclosure
  - php
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-trigger-passwordlock-error]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.569Z'
sub_techniques: []
id: a0cdde25-af7f-480a-80d4-e7eca68b8173
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Disclosure-in-PasswordLock

## Summary

This procedure exploits a lack of input validation in the PasswordLock library by supplying a non-string value to the password parameter, triggering a PHP hash() function warning that discloses the full server path in the error message. It is primarily used in web application security testing to identify information disclosure vulnerabilities during code reviews or penetration tests.

## Description

The PasswordLock library, used for password-based locking and unlocking in PHP applications, fails to validate that the password input is a string before passing it to PHP's hash() function in methods like hashAndEncrypt() and decryptAndVerify(). When a non-string (e.g., integer or array) is provided, PHP issues a warning: "hash() expects parameter 2 to be string, given [type]", and if error reporting is enabled (e.g., display_errors=On), the full file path to the library is included in the output. This can reveal sensitive server details like the document root or application directory, aiding further attacks such as path traversal. The vulnerability was reported via HackerOne and led to the library's deprecation. Prerequisites include access to a web endpoint using this library and the ability to craft HTTP requests with invalid input types.

## Requirements

1. Network access to the target web application endpoint (e.g., HTTP/HTTPS)
2. Knowledge of the password input field name (e.g., via form inspection or source code)
3. PHP environment with error display enabled (common in development or misconfigured production)
4. HTTP client like curl for sending requests

## Defense

Defensive measures and detection strategies:

- Implement strict input validation to ensure password is a string (e.g., using is_string() check before hashing)
- Disable PHP error display in production (set display_errors=Off and log_errors=On)
- Use error logging to files instead of outputting to responses
- Monitor application logs for hash() warnings and unusual input patterns
- Deprecate or replace vulnerable libraries like PasswordLock with secure alternatives (e.g., Sodium for encryption)

## Objectives

1. Trigger the PHP warning to disclose the full server path
2. Collect path information for potential follow-on reconnaissance
3. Validate the vulnerability presence without causing denial of service

## Instructions

### Step 1: Identify the Target Endpoint

**Context**: Locate the web form or API endpoint that uses the PasswordLock library for password handling, such as a login or unlock feature. Inspect the HTML source or use developer tools to confirm the password field name (typically 'password').

No command required for this step; perform manual inspection.

> Expected: Confirmation of endpoint URL (e.g., http://target.com/login) and input field.

### Step 2: Send Invalid Input to Trigger Error

**Context**: Craft an HTTP request with a non-string value (e.g., integer 123) in the password field to bypass validation and invoke hash() with invalid type, generating the disclosure warning.

**Command** ([[commands/curl-trigger-passwordlock-error]]):
```bash
curl -X POST 'http://target.com/login' -d 'username=test' -d 'password=123' -v
```

> This sends a POST request with 'password=123' (integer-like string, but PHP may interpret based on context; for array, use tools like Burp to send JSON/array payloads). The -v flag enables verbose output to capture full response including headers and body. Expected output includes the PHP warning with path, e.g., "Warning: hash() expects parameter 2 to be string, integer given in /var/www/html/lib/PasswordLock.php on line 45".

### Step 3: Analyze Response for Disclosure

**Context**: Review the response body for the error message and extract the path information.

No specific command; parse the output manually or with grep:

```bash
grep -i "hash\(\)" response.txt
```

> Expected: Isolation of the full path from the warning message for documentation or further use.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-passwordlock-error]]

## Tools Used


## Tags

- information-disclosure
- path-disclosure
- php
- web
