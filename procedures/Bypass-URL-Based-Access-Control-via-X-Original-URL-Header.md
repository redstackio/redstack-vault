---
type: procedure
description: >-
  Bypass URL-based access controls in web applications by manipulating the
  X-Original-URL header to access restricted administrative functions.
verified: true
submitted: true
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - access control
  - web applications
  - header manipulation
  - authorization bypass
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-URL-Based-Access-Control-via-X-Original-URL-Header

## Summary

This procedure exploits weak URL-based access controls in web applications by manipulating the X-Original-URL header, often used by reverse proxies or load balancers to route requests. By intercepting and modifying requests with a tool like Burp Suite, an attacker with a valid low-privilege session can bypass restrictions to perform unauthorized actions, such as deleting user accounts via admin endpoints.

## Description

Many web applications enforce access controls solely at the URL level, checking the requested path against user roles without validating manipulated inputs like custom headers. The X-Original-URL header is commonly set by proxies to preserve the original request path after internal rewrites. If the application trusts this header without re-validating permissions, an attacker can alter it to redirect the request to restricted resources (e.g., /admin/delete) while keeping the outer request appearing benign. This technique requires a valid session but no elevated privileges initially. It targets applications behind proxies like NGINX or Apache with mod_proxy, and success depends on the server parsing the header for routing. Expected outcomes include unauthorized data modification or administrative actions, highlighting broken access control vulnerabilities (OWASP Top 10 A01:2021).

## Requirements

- Valid low-privilege user session (e.g., standard user account logged in via browser)
- Burp Suite Professional or Community Edition installed and configured as a proxy
- Network access to the target web application (no firewall blocking proxy traffic)
- Browser configured to route traffic through the proxy (e.g., FoxyProxy extension)

## Defense

Defensive measures and detection strategies:

- Implement multi-layered access controls: Validate permissions at both the proxy and application layers, ignoring or sanitizing untrusted headers like X-Original-URL.
- Use strict URL rewriting rules in proxies (e.g., NGINX location blocks with deny directives) and enable logging for anomalous header values.
- Monitor for unusual request patterns, such as 404 responses on invalid paths followed by successful admin actions from low-privilege IPs.
- Employ Web Application Firewalls (WAFs) to detect header manipulation attempts and enforce role-based access control (RBAC) with least privilege.

## Objectives

1. Confirm the presence of URL-based access controls and header parsing vulnerability.
2. Bypass restrictions to access and execute administrative functions.
3. Achieve unauthorized actions like user account deletion to demonstrate impact.

## Instructions

### Step 1: Attempt Direct Access to Restricted Resource

**Context**: Verify that the target administrative resource is protected by role-based access controls, establishing a baseline for the bypass.

Using a low-privilege account, navigate to the restricted URL (e.g., https://target.com/admin) in the browser proxied through Burp Suite.

Observe the response in Burp Proxy or the browser.

### Step 2: Intercept and Route to Repeater

**Context**: Capture the failed access request to prepare for header manipulation in a controlled environment.

In Burp Suite Proxy, intercept the request to /admin. Forward it, then right-click the request in the Proxy history and select "Send to Repeater."

This isolates the request for modification without affecting the live session.

### Step 3: Test X-Original-URL Header Parsing

**Context**: Confirm the server processes the X-Original-URL header by injecting an invalid path, which should trigger a routing error if parsed.

In Burp Repeater, add a new header to the raw request: `X-Original-URL: /invalid`

Click "Send" to forward the modified request to the server.

### Step 4: Exploit Header for Unauthorized Action

**Context**: Manipulate the header to route to a sensitive administrative endpoint, bypassing the URL check on the original request path.

Edit the header in Repeater to: `X-Original-URL: /admin/delete?user_id=1` (adjust parameters based on the application's delete endpoint).

Ensure the original request path remains benign (e.g., /home). Click "Send."

Verify the action by checking the application state (e.g., user account removed).

## Expected Output

- Step 1: HTTP 403 Forbidden or similar access denied page.
- Step 2: Captured GET/POST request in Repeater with session cookies intact.
- Step 3: HTTP 404 Not Found response, confirming header influence on routing.
- Step 4: HTTP 200 OK or success response, with the unauthorized action completed (e.g., confirmation message or altered database state).
