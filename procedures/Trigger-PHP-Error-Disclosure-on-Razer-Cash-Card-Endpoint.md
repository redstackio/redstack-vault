---
id: proc-uuid-123
tags:
  - information-disclosure
  - php-error
  - reconnaissance
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-trigger-php-error]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T03:15:10.212Z'
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
# Trigger-PHP-Error-Disclosure-on-Razer-Cash-Card-Endpoint

## Summary

This procedure exploits a PHP application's failure to validate the presence of the 'period-hour' parameter in requests to the cash card incomplete transaction resend endpoint, resulting in an undefined index error that leaks verbose internal details such as file paths and error handling code.

## Description

In PHP-based web applications, accessing array indices without prior existence checks can trigger notices or warnings that, if not suppressed, expose sensitive implementation details. Here, the endpoint at https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend expects a 'period-hour' parameter but does not handle its absence gracefully, leading to information disclosure. This aids attackers in reconnaissance by revealing server configuration, PHP version, and potential code paths for further vulnerabilities like path traversal or additional misconfigurations. The attack requires no authentication and can be executed via standard HTTP requests.

## Requirements

1. Network access to the target web server (public internet)
2. HTTP client tool like curl or a web browser
3. No credentials or special privileges needed

## Defense

Defensive measures and detection strategies:

- Enable PHP error logging to files instead of displaying to users (set display_errors = Off in php.ini)
- Implement input validation to check for required parameters before array access (e.g., isset($_GET['period-hour']) or $_POST['period-hour'])
- Use web application firewalls (WAF) to detect and block requests with missing parameters or error-triggering patterns
- Monitor server logs for PHP notice/warning events and anomalous access to error-prone endpoints

## Objectives

1. Provoke and capture PHP error output for information gathering
2. Identify server-side details to support broader reconnaissance
3. Assess potential for chained exploits based on disclosed information

## Instructions

### Step 1: Prepare and Send Malformed Request

**Context**: Craft a request to the endpoint omitting the 'period-hour' parameter to trigger the undefined index error. This simulates an incomplete or malformed transaction resend attempt.

**Command** ([[commands/curl-trigger-php-error]]):
```bash
curl -X GET "https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend" -v
```

> This command sends a verbose GET request to the vulnerable URL. The -v flag enables detailed output, including headers and response body. Expected output includes an HTTP 200 or 500 response with PHP error text like "Notice: Undefined index: period-hour" embedded in the page, possibly under a title like "Some error has occurred! | Pay With Razer". If POST is expected, adjust to -X POST with empty body.

### Step 2: Analyze Response for Disclosed Information

**Context**: Review the response for leaked details such as PHP file paths, line numbers, or configuration snippets to inform further attacks.

**Command** (Manual inspection or pipe to grep):
```bash
curl -X GET "https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend" | grep -i "undefined index"
```

> Grep filters for error keywords. Successful execution reveals specific error messages confirming the vulnerability and any additional server info.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-php-error]]

## Tools Used


## Tags

- information-disclosure
- php-error
- reconnaissance
- web-vulnerability
