---
id: c99e1236-70d9-4bd0-803a-263229892a14
name: Web-Cache-Poisoning-via-Unkeyed-Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T16:31:54.694782+00:00'
updated_at: '2023-05-26T01:06:31.261570+00:00'
platforms:
  - Web
tags:
  - web-cache-poisoning
  - xss
  - web-applications
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
commands:
  - '[[commands/curl-get-homepage-observe-cookie]]'
  - '[[commands/curl-replay-request-to-achieve-cache-hit]]'
  - '[[commands/curl-send-poisoned-cookie-request]]'
  - '[[commands/curl-verify-cache-poisoning]]'
tools:
  - '[[tools/cURL]]'
validated: true
---

# Web-Cache-Poisoning-via-Unkeyed-Cookie

## Summary

This procedure exploits an unkeyed cookie parameter (such as 'fehost') in a web application's caching mechanism to perform cache poisoning. By injecting an XSS payload into the cookie value, the attacker poisons the cached response, causing subsequent visitors to execute arbitrary JavaScript, such as alert(1), without direct interaction.

## Description

Web cache poisoning occurs when a caching proxy or CDN stores a malicious response based on manipulated request parameters that are not properly keyed or validated. In this case, the 'fehost' cookie selects the cache backend (e.g., prod-cache-01) but is unkeyed, meaning variations in its value can poison different cache entries. The attacker first observes the normal cookie, replays requests to populate the cache, then modifies the cookie to inject an XSS payload like 'hellohacker"-alert(1)-"hellohacker' to break out of a quoted context in the response. Once the poisoned response is cached (indicated by 'x-cache: hit'), any victim accessing the page retrieves and executes the injected JavaScript. This targets public-facing web applications with reverse proxies like Varnish or CloudFront that mishandle cookies.

## Requirements

1. Network access to the target web application (no authentication required for public pages).
2. Knowledge of the unkeyed cookie parameter (e.g., 'fehost') from initial reconnaissance.
3. Installed curl tool for HTTP manipulation.
4. Optional: A cache-busting parameter in the URL (e.g., ?cb=123) to control caching behavior.

## Defense

- Key all cache-varying headers and cookies explicitly in the caching layer (e.g., VCL in Varnish).
- Validate and sanitize cookie values server-side before rendering in HTML.
- Implement Content Security Policy (CSP) to block inline JavaScript execution.
- Monitor for anomalous cache hits with injected payloads via WAF logs.

## Objectives

1. Identify and capture the unkeyed cookie used for cache selection.
2. Poison the cache by injecting an XSS payload via cookie manipulation.
3. Verify the poisoning by retrieving the malicious cached response.
4. Simulate victim access to confirm JavaScript execution potential.

## Instructions

### Step 1: Observe Initial Cookie on Homepage

**Context**: Send a request to the target homepage to capture the initial 'fehost' cookie value in the response headers. This establishes the baseline cache selector (e.g., prod-cache-01).

**Command** ([[commands/curl-get-homepage-observe-cookie]]):
```bash
curl -v -c cookies.txt $_TARGET_URL
```

> The verbose (-v) output will display response headers. Look for the 'Set-Cookie' header containing 'fehost=prod-cache-01' or similar. The cookie is saved to cookies.txt for reuse. This step confirms the cookie's presence and value without triggering caching issues.

### Step 2: Replay Request to Populate and Confirm Cache

**Context**: Replay the request using the captured cookie multiple times to populate the cache. Monitor for 'x-cache: hit' in the response to ensure the content is cached.

**Command** ([[commands/curl-replay-request-to-achieve-cache-hit]]):
```bash
curl -v -b cookies.txt $_TARGET_URL
```

> Repeat this command several times (e.g., 5-10 iterations) until the verbose output shows 'x-cache: hit' in the response headers, indicating the response is now served from cache. If a cache-buster query parameter exists (e.g., ?cb=$(date +%s)), omit it to allow caching.

### Step 3: Inject XSS Payload into Cookie to Poison Cache

**Context**: Override the 'fehost' cookie with a modified value containing an XSS payload to poison the cache. The payload 'hellohacker"-alert(1)-"hellohacker' is designed to break out of a quoted string context in the cached HTML, injecting <script>alert(1)</script> effectively.

**Command** ([[commands/curl-send-poisoned-cookie-request]]):
```bash
curl -v -H "Cookie: fehost=hellohacker\"-alert(1)-\"hellohacker" $_TARGET_URL
```

> Send this request multiple times until 'x-cache: hit' appears in the headers and the response body reflects the injected payload (e.g., the alert(1) executes if viewed in a browser). The escaping (\") handles the quotes in the shell. This poisons the cache entry for the default 'fehost' selector.

### Step 4: Verify Poisoning by Retrieving Cached Response

**Context**: Request the page without the modified cookie to simulate a victim access. The cache should serve the poisoned response, confirming successful poisoning.

**Command** ([[commands/curl-verify-cache-poisoning]]):
```bash
curl -v $_TARGET_URL
```

> The verbose output should show 'x-cache: hit' and the response body should contain the injected payload (e.g., search for 'alert(1)'). To fully verify, paste the response into an HTML viewer or browser console; the XSS should trigger. If a cache-buster was present, ensure the clean URL is used.
