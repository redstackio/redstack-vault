---
id: 2e89ae3d-d1bb-4ad3-8f89-e4af3b72b723
name: Cache-Key-Injection
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T18:59:33.447621+00:00'
updated_at: '2023-05-26T01:16:29.698815+00:00'
platforms:
  - Web
tags:
  - '[[tags/Web-Applications]]'
  - '[[tags/Web-Cache-Poisoning]]'
  - xss
  - parameter-pollution
  - header-injection
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
commands:
  - '[[commands/curl-poison-js-localize]]'
  - '[[commands/curl-poison-login]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Cache-Key-Injection

## Summary

This procedure exploits cache key injection vulnerabilities in web applications by crafting requests that share the same cache key but deliver malicious payloads. It combines client-side parameter pollution in the 'lang' parameter with response header injection to poison the cache, leading to the execution of arbitrary JavaScript (e.g., XSS via alert(1)) on subsequent legitimate requests to the poisoned endpoint.

## Description

Web applications often generate cache keys based on URL parameters or components like the 'lang' query parameter. If these keys are not properly isolated or encoded, attackers can manipulate requests to poison the cache with malicious content. In this scenario, the application redirects after login and imports a JavaScript file (/js/localize.js) that is vulnerable to parameter pollution because the 'lang' value is not URL-encoded. By injecting CRLF characters into the Origin header and polluting parameters, the attacker forces the inclusion of malicious JavaScript. The first request poisons the cache for /js/localize.js, and the second poisons /login, causing the cache to serve the tainted JS file, which executes the payload on the login page. This technique requires a proxy like Burp Suite to intercept and modify requests, and it targets applications using caching mechanisms like Varnish or application-level caches.

## Requirements

1. Access to a proxy tool like [[tools/Burp-Suite]] for intercepting and modifying HTTP requests.
2. Knowledge of the target's login flow and cache key generation (e.g., based on 'lang=en').
3. Network access to the target web application.
4. Basic understanding of HTTP headers, URL encoding, and CRLF injection.

## Defense

Defensive measures and detection strategies:

- Implement strict cache key isolation by including unique identifiers (e.g., session tokens) in cache keys to prevent shared poisoning.
- URL-encode all query parameters before using them in cache keys or script imports.
- Validate and sanitize HTTP headers, especially Origin, to block CRLF injections.
- Monitor for anomalous requests with repeated parameters or unusual header values; use WAF rules to detect parameter pollution patterns.
- Enable cache-busting with non-cacheable headers (e.g., Cache-Control: no-cache) on sensitive endpoints like login.

## Objectives

1. Poison the cache with a malicious JavaScript file via parameter pollution and header injection.
2. Trigger execution of the payload on a subsequent request to a shared cache key endpoint.
3. Demonstrate XSS execution (e.g., alert(1)) to confirm cache poisoning success.

## Instructions

### Step 1: Intercept and Analyze Login Request

**Context**: Begin by capturing the normal login request to understand the flow, including any redirects and parameter usage in cache keys. This step identifies the vulnerability in the 'lang' parameter and the imported /js/localize.js file.

Use [[tools/Burp-Suite]] Proxy to intercept traffic. Navigate to the login page and submit a login attempt.

**Command** (N/A - GUI step in Burp):

Observe the request in Burp's HTTP history: Look for the 'lang' parameter in the redirect URL and confirm that /js/localize.js is imported without URL encoding on 'lang'.

> This step verifies the application's behavior: The redirect appends arbitrary content to 'lang', and the JS import is susceptible to pollution.

### Step 2: Poison the JavaScript File Cache

**Context**: Craft a request to /js/localize.js that pollutes the 'lang' parameter and injects a malicious payload via the Origin header using CRLF to simulate a response body with JavaScript.

Execute [[commands/curl-poison-js-localize]] to send the poisoning request:

```bash
curl -X GET "http://target.com/js/localize.js?lang=en?utm_content=z&cors=1&x=1" \
  -H "Origin: x%0d%0aContent-Length:%208%0d%0a%0d%0aalert(1)$$$$" \
  -H "Host: target.com"
```

> Expected: The server caches the response with the injected alert(1) script due to the shared cache key from 'lang=en'. No immediate output, but verify in Burp Repeater by resending a clean request to /js/localize.js?lang=en and checking for the injected content in the response.

### Step 3: Poison the Login Endpoint Cache

**Context**: Send a similar poisoning request to the /login endpoint, ensuring it shares the same cache key ('lang=en') to deliver the tainted JS file on redirect.

Execute [[commands/curl-poison-login]] to send the poisoning request:

```bash
curl -X GET "http://target.com/login?lang=en?utm_content=x%26cors=1%26x=1$$Origin=x%250d%250aContent-Length:%208%250d%250a%250d%250aalert(1)$$%23" \
  -H "Host: target.com"
```

> Expected: The /login response is cached with the poisoned redirect to the malicious JS. Resend a clean GET /login?lang=en in Burp Repeater; the response should include the injected script, triggering alert(1) when loaded in a browser.

### Step 4: Verify Poisoning Success

**Context**: Test the poisoned cache by accessing the login page normally to confirm payload execution.

In Burp Repeater or a browser (with proxy enabled), send GET /login?lang=en.

**Expected Output**: The page loads with an alert(1) popup due to the cached malicious JS from /js/localize.js.

> Success confirms the cache key collision and injection. Clear the cache or wait for expiration to reset.
