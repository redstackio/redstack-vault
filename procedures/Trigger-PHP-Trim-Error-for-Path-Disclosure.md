---
id: proc-php-trim-path-disclosure
tags:
  - information-disclosure
  - php
  - path-disclosure
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/get-localize-homepage]]'
  - '[[commands/post-malformed-signin-localize]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.958Z'
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
# Trigger-PHP-Trim-Error-for-Path-Disclosure

## Summary

This procedure exploits a PHP type error in the sign-in functionality of localize.io by submitting POST parameters formatted as arrays, causing the trim() function to receive an array instead of a string and output a warning that discloses the internal server file path.

## Description

The vulnerability occurs in the sign-in endpoint where user input for username and password is processed using PHP's trim() function without proper validation for array inputs. By using array notation (e.g., sign_in[username][]) in POST data, the application triggers a PHP warning: "trim() expects parameter 1 to be string, array given". This warning includes the full path to the script file, such as /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 732. The disclosed path reveals hosting provider details (Host Europe dedicated server), which can assist in reconnaissance for further attacks like targeted phishing or infrastructure mapping. The target environment is a PHP-based web application accessible via HTTP.

## Requirements

1. Network access to http://www.localize.io/
2. Ability to send custom HTTP GET and POST requests (e.g., via curl, browser dev tools, or Burp Suite)
3. No authentication or special privileges required

## Defense

Defensive measures and detection strategies:

- Input validation: Ensure POST parameters are treated as strings and reject array notation.
- Error handling: Suppress or log PHP warnings without displaying them to users (use error_reporting(0) or custom error handlers).
- Web Application Firewall (WAF): Block requests with unusual parameter formats like [].
- Monitoring: Log all sign-in attempts and alert on error messages containing file paths.

## Objectives

1. Disclose internal server file paths to reveal hosting environment.
2. Gather reconnaissance data for potential follow-on attacks.
3. Demonstrate the impact of unhandled PHP type errors in web applications.

## Instructions

### Step 1: Access the Homepage

**Context**: Load the target site to confirm accessibility and view the sign-in form structure.

**Command** ([[commands/get-localize-homepage]]):
```bash
curl -X GET http://www.localize.io/
```

> This command sends a GET request to the homepage. Expected output is the HTML response (HTTP 200) containing the sign-in form, verifying the endpoint is live.

### Step 2: Submit Malformed Sign-In Request

**Context**: Send a POST request to the sign-in handler with array-formatted parameters to trigger the trim() error.

**Command** ([[commands/post-malformed-signin-localize]]):
```bash
curl -X POST http://www.localize.io/ -d "sign_in[username][]=test&sign_in[password][]=test"
```

> This command submits dummy credentials as arrays, causing the PHP error. Expected output includes the warning message with the full server path, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/get-localize-homepage]]
- [[commands/post-malformed-signin-localize]]

## Tools Used

- None

## Tags

- information-disclosure
- php
- path-disclosure
- web-vulnerability
