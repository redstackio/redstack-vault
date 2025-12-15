---
tags:
  - information-disclosure
  - csrf-bypass
  - path-disclosure
  - php
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-without-csrf]]'
platforms:
  - Web
  - PHP
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 855cb5dd-6d6a-457c-ad43-eb8e21a735aa
created_at: '2025-12-14T17:27:03.606Z'
updated_at: '2025-12-14T17:27:03.606Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Disclosure-by-Omitting-CSRF-Token

## Summary

This procedure exploits a vulnerability in the CSPR.NG PHP web application by removing the _CSRF_TOKEN parameter from POST requests to endpoints like login, triggering an unhandled exception in debug mode that discloses the full server file path (/var/www/csprng/src/public/index.php). The disclosure occurs due to an undefined variable 'ex' on line 160, but the impact is low as the path is predictable and requires debug mode.

## Description

In the CSPR.NG application, POST requests for actions like login include a mandatory _CSRF_TOKEN to prevent cross-site request forgery. Omitting this token in debug mode causes the application to throw an exception without proper error handling, leading to a stack trace that reveals sensitive server information, specifically the absolute path to the index.php file. This technique is useful for reconnaissance in web penetration testing to gather host details, though it offers limited exploitation potential beyond confirming the server's file structure. The target environment must have debug mode enabled, which is uncommon in production but possible in development or misconfigured setups.

## Requirements

1. Network access to the CSPR.NG web application (e.g., via HTTP/HTTPS)
2. Debug mode enabled on the PHP server (check for verbose error reporting)
3. Ability to intercept and modify HTTP POST requests (e.g., using browser dev tools or curl)

## Defense

Defensive measures and detection strategies:

- Disable debug mode in production environments (set display_errors = Off in php.ini)
- Implement proper CSRF validation with fallback error handling that does not expose stack traces
- Use web application firewalls (WAF) to detect anomalous POST requests missing tokens
- Monitor server logs for exceptions related to undefined variables in authentication endpoints

## Objectives

1. Bypass CSRF protection to trigger an application exception
2. Extract server file path from the error response for reconnaissance
3. Assess the application's error handling maturity

## Instructions

### Step 1: Identify the Target Endpoint

**Context**: Locate a POST endpoint that requires a CSRF token, such as the login form. Inspect the form using browser developer tools to note the _CSRF_TOKEN field.

No command required for this step; use manual inspection.

### Step 2: Craft and Send Tampered POST Request

**Context**: Modify the POST request body to exclude the _CSRF_TOKEN parameter, simulating invalid input to force the exception.

**Command** ([[commands/curl-post-without-csrf]]):
```bash
curl -X POST 'https://target.com/login' \
  -d 'username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -v
```

> This command sends a POST request to the login endpoint without the CSRF token (e.g., omitting _CSRF_TOKEN=WqXB7vmysdM06gBarWZiNfnZ%3AOMznb0rVagzWr41P_h_N2Qj50LwPV2HZxKyJxR17lB6b). The -v flag enables verbose output to capture the full response. Expected output includes an HTTP 500 error with a PHP stack trace mentioning the undefined variable 'ex' on line 160 and the path /var/www/csprng/src/public/index.php.

### Step 3: Analyze Response for Disclosure

**Context**: Review the error response for path information and confirm no further data leakage.

No command required; parse the response manually for paths like /var/www/csprng/src/public/index.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-without-csrf]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[csrf-bypass]]
- [[path-disclosure]]
- [[php]]
- [[web-vulnerability]]
