---
id: 4185b621-4941-430d-9264-e588a187f979
type: procedure
name: Enumerate-Web-Server-Version-via-Error-Messages
verified: true
submitted: true
created_at: '2020-07-24T15:31:13.065644+00:00'
updated_at: '2023-05-26T18:08:17.897224+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - web-applications
  - reconnaissance
commands:
  - '[[commands/curl-trigger-web-error]]'
platforms:
  - Web
tools: []
validated: true
---

# Enumerate-Web-Server-Version-via-Error-Messages

## Summary

This procedure demonstrates how to fingerprint a web server's version and other sensitive details by intentionally triggering error messages through malformed URL requests. By appending special characters or accessing non-existent resources, attackers can elicit responses that leak server software, version numbers, and configuration details, aiding in further reconnaissance or targeted exploitation.

## Description

Web applications often expose server information in error pages generated when handling invalid requests, such as appending special characters (e.g., a tilde ~ or null byte %00) to a URL or navigating to a non-existent path. This technique is a form of passive reconnaissance that exploits poor error handling to gather host information without active scanning. It is particularly effective against misconfigured servers running Apache, IIS, or Nginx, where default error pages include headers like Server: Apache/2.4.41. The procedure assumes HTTP access to the target and focuses on HTTP responses rather than HTTPS (though adaptable). Success reveals details mappable to known vulnerabilities for subsequent attacks.

## Requirements

1. Network access to the target web application (HTTP/HTTPS port 80/443 open).
2. Command-line tool like curl installed on the attacker's machine.
3. Basic knowledge of HTTP requests and URL encoding.
4. Optional: Proxy tool like Burp Suite for intercepting and modifying requests in a browser context.

## Defense

Defensive measures and detection strategies:

- Customize error pages to remove sensitive information (e.g., server version) using server configurations like Apache's ErrorDocument directive.
- Implement web application firewalls (WAFs) to detect and block anomalous requests, such as those with special characters or invalid paths.
- Enable logging of all HTTP errors (e.g., via access logs) and monitor for patterns of probing requests from unknown IPs.
- Use security headers like ServerTokens Prod in Apache to minimize exposed information.

## Objectives

1. Trigger an error response from the web server to expose version and configuration details.
2. Analyze the error message for fingerprinting the server software and potential vulnerabilities.
3. Verify the technique without causing denial-of-service or alerting the target.

## Instructions

### Step 1: Verify Normal Access to the Target URL

**Context**: First, confirm the target web application is accessible and responds normally. This establishes a baseline and ensures the server is reachable before attempting error induction. Use a simple HEAD request to minimize data transfer while checking for initial server headers.

**Command** ([[commands/curl-trigger-web-error]]):

```bash
curl -I http://$_TARGET_URL
```

> This command sends a HEAD request to the target URL, displaying HTTP headers including any initial Server response. If the site loads normally, you should see a 200 OK status. Look for partial server info in headers; if none, proceed to error triggering. Replace $_TARGET_URL with the actual site, e.g., http://example.com.

### Step 2: Trigger Error Message by Appending Special Character

**Context**: Modify the URL by appending a special character (e.g., ~ or %00) or accessing a non-existent resource to force the server to generate an error page. This step exploits default error handling to leak detailed server information in the response body or headers. Analyze the output for strings like "Apache/2.4" or database errors that reveal versions.

**Command** ([[commands/curl-trigger-web-error]]):

```bash
curl http://$_TARGET_URL/nonexistent~ || curl "http://$_TARGET_URL/%00"
```

> Execute the command to request a non-existent path or inject a special character. The server will return a 404 or 500 error with an HTML body containing sensitive details. Expected output includes error pages with server software/version (e.g., "Server: nginx/1.18.0"). If using %00, it may trigger parsing errors revealing backend configs. Pipe output to grep for keywords like "Server:" or "version" to extract info quickly.
