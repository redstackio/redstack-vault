---
id: d2ffa842-1be8-456e-a996-e6d6188c9e44
name: Web-Cache-Poisoning-via-Unkeyed-Query-String
type: procedure
verified: true
submitted: true
created_at: '2020-09-04T16:27:27.468017+00:00'
updated_at: '2023-05-26T18:17:49.324459+00:00'
platforms:
  - Web
tags:
  - web-applications
  - web-cache-poisoning
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Web-Cache-Poisoning-via-Unkeyed-Query-String

## Summary

This procedure demonstrates how to perform web cache poisoning by exploiting unkeyed query strings in a caching proxy or CDN. An attacker crafts a malicious URL with parameters that are ignored in the cache key, injects an XSS payload, and poisons the cache so that subsequent legitimate requests from victims receive the tainted response, leading to JavaScript execution on their browsers without direct interaction.

## Description

Web cache poisoning occurs when a caching system, such as a reverse proxy (e.g., Varnish, Cloudflare) or application-level cache, uses an incomplete cache key that excludes certain request parameters. This allows an attacker to manipulate the cached response by sending a request with malicious parameters that alter the output (e.g., injecting XSS via reflected parameters). Once poisoned, the cache serves the malicious content to all users requesting the same resource, amplifying the impact across the application's user base. This technique targets public-facing web applications and is particularly effective against sites with shared caching for unauthenticated pages like homepages. Prerequisites include network access to the target site and the ability to influence victim clicks on crafted URLs (e.g., via phishing). The attack assumes the cache does not key on query strings or specific headers like Origin.

## Requirements

1. Access to Burp Suite or similar proxy tool for intercepting and replaying HTTP requests.
2. Network connectivity to the target web application, typically over HTTP/HTTPS.
3. Basic knowledge of HTTP headers and query parameters; no elevated privileges needed on the target.
4. A victim or test user to induce cache hits (in testing, this can be simulated with multiple requests).

## Defense

Defensive measures and detection strategies:

- Implement strict cache keying that includes all query parameters and headers like Origin, User-Agent, and Authorization.
- Use cache-busting techniques such as unique cache keys per user session or Vary headers to prevent poisoning.
- Monitor for anomalous responses containing script tags or unexpected JavaScript in cached content.
- Deploy Web Application Firewalls (WAFs) to detect and block reflected XSS payloads in query parameters.
- Regularly purge caches and validate response content before caching.

## Objectives

1. Identify if query parameters are unkeyed in the cache mechanism.
2. Poison the cache with a malicious XSS payload to execute JavaScript on victim browsers.
3. Verify cache poisoning by observing the tainted response in subsequent clean requests.
4. Achieve broad impact by serving poisoned content to multiple users.

## Instructions

### Step 1: Set Up Proxy and Capture Baseline Request

**Context**: Configure Burp Suite to intercept traffic and capture a legitimate request to the target page (e.g., homepage) to establish the baseline cache behavior. This allows sending the request to Repeater for manipulation.

Browse the target application with Burp proxy enabled. In the Proxy > HTTP history tab, locate the GET request for the homepage (e.g., GET / HTTP/1.1) and right-click to send it to Repeater.

> This step verifies proxy interception and prepares for parameter testing. Expected: Request appears in Repeater with original headers and no cache poisoning yet.

### Step 2: Test for Unkeyed Query Parameters

**Context**: Add innocuous query parameters to the request and forward it to check if the cache key ignores them. Look for 'X-Cache: HIT' in responses, indicating parameters are not influencing the cache.

In Burp Repeater, append a test parameter to the URL, such as ?test=1, and send the request. Observe the response headers for cache indicators like X-Cache: HIT, confirming the parameter was ignored in the cache key.

> If the response shows a cache hit despite the added parameter, the cache is vulnerable to poisoning. Expected: Response body unchanged, but headers confirm hit without parameter inclusion.

### Step 3: Use Cache Buster Header to Isolate Parameters

**Context**: Introduce a cache-busting header like Origin to force a cache miss, ensuring the subsequent poisoning request generates a new cache entry influenced only by the malicious parameters.

Add an Origin header (e.g., Origin: evil.com) to the request from Step 2 and send it. Confirm a cache miss (e.g., X-Cache: MISS) in the response, then remove the header for poisoning attempts.

> The Origin header prevents interference from existing cache entries. Expected: Initial miss followed by ability to craft new entries.

### Step 4: Inject and Verify Poisoning Payload

**Context**: Modify the query parameter to include a reflected XSS payload that poisons the cache. Repeatedly send until the payload appears in the response, then test with a clean request to confirm persistence.

Using [[tools/Burp-Suite]] Repeater, update the URL to include the payload: /?evil='/><script>alert(1)</script>. Send the request multiple times until the response reflects the injected script (e.g., in HTML output). Then, remove all query parameters (?evil=...) and send a clean GET / request. Check if the poisoned payload is now in the cached response.

Reference the payload from [[codes/XSS-Cache-Poisoning-Payload]] for the exact injection string.

> Persistence indicates successful poisoning; the clean request should return the tainted page with alert(1) executable on load. Expected: Script tag visible in response body for clean requests, triggering XSS on victim browsers.
