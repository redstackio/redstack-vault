---
id: 8aed1e11-39cf-4843-a85a-d8d380b7b46f
name: Parameter-Cloaking-for-Web-Cache-Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T19:29:20.393805+00:00'
updated_at: '2023-05-26T18:26:37.062338+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - web-cache-poisoning
  - parameter-cloaking
  - xss
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-get-page-with-utm-content]]'
  - '[[commands/curl-get-page-cloaked-utm]]'
  - '[[commands/curl-get-geolocate-original]]'
  - '[[commands/curl-get-geolocate-cloaked]]'
  - '[[commands/curl-get-geolocate-xss]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Parameter-Cloaking-for-Web-Cache-Poisoning

## Summary

Parameter cloaking exploits differences in how web caches and backend applications parse query parameters, allowing attackers to inject hidden parameters that are treated as part of a legitimate parameter by the cache but parsed separately by the application. This technique can poison the cache to deliver malicious payloads, such as reflected XSS via a controllable callback parameter in a JSONP endpoint, leading to arbitrary JavaScript execution when victims load the poisoned resource.

## Description

In vulnerable web applications, caches (e.g., Varnish, CDN caches) may concatenate or misparse query parameters separated by semicolons (;), treating them as a single value for cache keying, while the application parses the full query string and processes the last occurrence of a parameter. By appending a cloaked parameter like ;callback=malicious to an ignored parameter (e.g., utm_content), the cache stores the response under the original key, but the application executes the malicious parameter. This is demonstrated on endpoints like /js/geolocate.js, where the callback parameter controls the JSONP wrapper, enabling XSS. The attack requires replaying requests to maintain cache poisoning and relies on the victim accessing the poisoned URL, such as a JavaScript resource loaded by the site.

## Requirements

1. Intercepting proxy tool like [[tools/Burp-Suite]] to capture and replay HTTP requests.
2. Network access to the target web application, including the ability to send arbitrary GET requests.
3. Identification of cacheable endpoints with controllable parameters (e.g., utm_content for tracking, callback for JSONP).
4. A listening setup to observe cache behavior, such as multiple requests from different IPs to verify poisoning.

## Defense

Defensive measures and detection strategies:

- Implement strict parameter validation and sanitization, rejecting unexpected parameters or semicolons in values.
- Configure caches to include all query parameters in the cache key (e.g., using VCL in Varnish to normalize queries).
- Use Content-Security-Policy (CSP) headers to block inline JavaScript execution from untrusted sources.
- Monitor for anomalous query strings in access logs, especially semicolons or duplicate parameters, and rate-limit repeater-like requests.
- Deploy Web Application Firewalls (WAFs) to detect and block parameter manipulation patterns.

## Objectives

1. Demonstrate parsing discrepancies between cache and application to identify cloaking opportunities.
2. Inject a cloaked malicious parameter to poison the cache with a harmful payload.
3. Achieve arbitrary code execution (e.g., XSS) when a victim loads the poisoned resource.
4. Maintain cache poisoning through repeated requests for persistence.

## Instructions

### Step 1: Identify and Test Original Request with UTM Parameter

**Context**: Locate a cacheable request containing trackable parameters like utm_content, which are often ignored by the application but included in cache keys. Use [[tools/Burp-Suite]] to intercept traffic and send the request to Repeater for modification. This step verifies normal behavior before cloaking.

**Command** ([[commands/curl-get-page-with-utm-content]]):
```bash
curl -v "http://target.example.com/page?utm_content=original_value"
```

> This sends the original request and observes the response and headers (e.g., Cache-Control). In Burp Repeater, confirm the response is cached by replaying from a different session.

### Step 2: Append Cloaked Parameter to UTM Content

**Context**: Modify the utm_content parameter by appending a semicolon and a test parameter (e.g., ;test=1234). The cache should treat this as a single utm_content value, but the application parses it as separate parameters, revealing the cloaking vulnerability.

**Command** ([[commands/curl-get-page-cloaked-utm]]):
```bash
curl -v "http://target.example.com/page?utm_content=original_value;test=1234"
```

> Replay multiple times in Burp Repeater to poison the cache. Compare responses: the cache serves the original content, but logs or backend may show the test parameter processed separately.

### Step 3: Locate and Test JSONP Endpoint

**Context**: From HTTP history in [[tools/Burp-Suite]], identify a JSONP endpoint like /js/geolocate.js with a controllable callback parameter. Send it to Repeater and verify the callback value is reflected in the response as a function wrapper.

**Command** ([[commands/curl-get-geolocate-original]]):
```bash
curl -v "http://target.example.com/js/geolocate.js?callback=setCountryCookie"
```

> Expected response is JavaScript like "setCountryCookie({data});". Confirm reflection by changing callback to a test function and observing it in the output.

### Step 4: Inject Cloaked Callback Parameter

**Context**: Append a cloaked second callback to utm_content (or similar ignored param) to override the legitimate one. The application uses the last callback (malicious), while the cache keys on the original.

**Command** ([[commands/curl-get-geolocate-cloaked]]):
```bash
curl -v "http://target.example.com/js/geolocate.js?callback=setCountryCookie&utm_content=1234;callback=myFunction"
```

> Replay in Burp Repeater. The response should reflect "myFunction({data});" despite the cache potentially serving based on the first callback.

### Step 5: Deploy XSS Payload via Cloaked Callback

**Context**: Replace the test callback with an XSS payload like alert(1). Replay the request multiple times to ensure the cache is poisoned. When a victim loads /js/geolocate.js, the browser executes the malicious JavaScript.

**Command** ([[commands/curl-get-geolocate-xss]]):
```bash
curl -v "http://target.example.com/js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=alert(1)"
```

> Replay 5-10 times to maintain poisoning. Verify by accessing the URL in a browser from a different IP/session; it should trigger alert(1) upon loading the JS.
