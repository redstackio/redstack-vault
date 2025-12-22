---
id: 4b847668-2e8b-4fd8-8c8c-ba744d4b64c7
name: Authentication-Bypass-via-Information-Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T15:03:06.981760+00:00'
updated_at: '2023-05-26T15:56:58.782392+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Gather Victim Host Information]]'
sub_techniques:
  - '[[Domain Accounts]]'
tags:
  - '[[tags/authentication]]'
  - '[[tags/broken authentication]]'
  - '[[tags/information disclosure]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-login-normal-user]]'
  - '[[commands/curl-get-admin-endpoint]]'
  - '[[commands/curl-trace-admin-endpoint]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Authentication-Bypass-via-Information-Disclosure

## Summary

This procedure exploits an information disclosure vulnerability in a web application's TRACE method to reveal a custom authorization header (X-Custom-IP-Authorization) containing the user's IP address. By intercepting and modifying requests using Burp Suite, an attacker can spoof this header to 127.0.0.1, bypassing authentication checks and gaining unauthorized access to the admin panel as if accessing from localhost.

## Description

The target web application uses a custom HTTP header, X-Custom-IP-Authorization, to enforce IP-based access controls for administrative functions, restricting access to localhost (127.0.0.1). However, the TRACE method exposes this header in its response, disclosing the mechanism. Starting with normal user credentials, the attacker logs in, intercepts subsequent requests, and uses Burp Suite's Match and Replace feature to automatically inject the spoofed header into all outgoing requests. This allows navigation to protected endpoints like /admin without triggering authentication failures. The technique relies on the application's failure to properly validate or protect the TRACE method and header disclosure, common in misconfigured web apps. It targets OWASP Broken Authentication and Information Disclosure risks, enabling privilege escalation in web environments.

## Requirements

1. Valid normal user credentials for the target web application.
2. Network access to the web application (e.g., via browser or proxy).
3. Burp Suite Professional or Community Edition installed and configured as a proxy.
4. Basic knowledge of HTTP methods (GET, TRACE) and header manipulation.

## Defense

Defensive measures and detection strategies:

- Disable or restrict the TRACE HTTP method at the web server level (e.g., via Apache mod_rewrite or Nginx configuration) to prevent header disclosure.
- Implement proper input validation and sanitization for custom headers, avoiding reliance on client-supplied IP data; use server-side proxies or trusted IP sources instead.
- Monitor web server logs for unusual HTTP methods like TRACE or anomalous header values (e.g., repeated 127.0.0.1 in X-Custom-IP-Authorization from non-local IPs).
- Use Web Application Firewalls (WAFs) to detect and block header spoofing attempts or TRACE requests.
- Enforce session-based authentication with role-based access control (RBAC) rather than IP headers, and enable logging for all admin endpoint accesses.

## Objectives

1. Gain unauthorized access to the admin panel by spoofing the IP authorization header.
2. Demonstrate information disclosure via TRACE method to understand the auth mechanism.
3. Escalate privileges from normal user to admin without valid admin credentials.
4. Expected outcome: Full access to administrative functions, potentially allowing data modification or further exploitation.

## Instructions

### Step 1: Login as Normal User

**Context**: Establish a valid session as a regular user to bypass initial login barriers and set up for request interception. This provides the necessary cookies and session tokens for subsequent requests.

**Command** ([[commands/curl-login-normal-user]]):
```bash
curl -X POST http://target.com/login -d "username=normaluser&password=normalpass" -c cookies.txt
```

> This command sends a POST request to the login endpoint with normal user credentials, storing session cookies in cookies.txt for reuse. Expected output includes a 200 OK response with a redirect or success message indicating login. Verify by checking for session cookies in the response headers.

Configure your browser to proxy through Burp Suite (typically at 127.0.0.1:8080) and navigate to the application to perform the login interactively if curl is not suitable.

### Step 2: Intercept and Send Request to Repeater

**Context**: Capture a legitimate request after login to analyze and modify it in Burp Suite's Repeater tool, allowing safe testing of endpoint access without affecting the live session.

Use Burp Suite Proxy to intercept the request when refreshing the page post-login. Right-click the intercepted request in the Proxy history and select "Send to Repeater."

No specific command here; this is a GUI action in [[tools/Burp-Suite]]. Expected output: The request appears in the Repeater tab, ready for modification, with full headers and body visible.

### Step 3: Test Admin Endpoint Access with GET

**Context**: Attempt to access the protected /admin endpoint using the standard GET method to confirm access restrictions and observe error messages revealing localhost-only access.

**Command** ([[commands/curl-get-admin-endpoint]]):
```bash
curl -X GET http://target.com/admin -b cookies.txt -x 127.0.0.1:8080
```

> In Burp Repeater, modify the method to GET and target /admin, then send. Or use curl with proxy (-x) to route through Burp. Expected output: A 403 Forbidden or similar response stating the portal can only be accessed from localhost, confirming the IP-based restriction.

### Step 4: Use TRACE Method to Disclose Authorization Header

**Context**: Switch to the TRACE HTTP method to echo request headers in the response, disclosing the X-Custom-IP-Authorization header and revealing the IP validation mechanism.

**Command** ([[commands/curl-trace-admin-endpoint]]):
```bash
curl -X TRACE http://target.com/admin -b cookies.txt -x 127.0.0.1:8080
```

> In Burp Repeater, change the method to TRACE and send to /admin. Expected output: Response includes the X-Custom-IP-Authorization header with the attacker's actual IP (e.g., X-Custom-IP-Authorization: 192.168.1.100), confirming the disclosure.

### Step 5: Configure Match and Replace for Header Spoofing

**Context**: Set up Burp Suite to automatically inject the spoofed header into all proxied requests, simulating localhost access without manual modification each time.

In Burp Suite, navigate to Proxy > Options > Match and Replace > Add. Set Type: Request header, Match: X-Custom-IP-Authorization, Replace: X-Custom-IP-Authorization: 127.0.0.1. Enable the rule.

No command; GUI configuration in [[tools/Burp-Suite]]. Expected output: Rule added successfully; test by sending a request through Proxy to see the header appended.

### Step 6: Verify Automatic Header Injection

**Context**: Confirm the Match and Replace rule works by accessing the site again and observing the header addition in intercepted requests.

Browse to the application or refresh a page with Burp Proxy active. Intercept and inspect the request.

Expected output: Requests now include X-Custom-IP-Authorization: 127.0.0.1 automatically.

### Step 7: Access Admin Panel

**Context**: With the spoofed header in place, navigate to the admin functionality to achieve the bypass.

Click on the Admin Panel link or directly access /admin via browser. Expected output: Successful access to the admin interface without authentication errors, displaying admin-specific options and data.
