---
id: 5137b7c0-55b4-43b6-badb-3004fe95ebbe
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T09:28:04.235350+00:00'
updated_at: '2023-05-26T15:55:00.482110+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp-top-10]]'
  - '[[tags/web-applications]]'
  - '[[tags/web-cache-poisoning]]'
  - '[[tags/xss]]'
commands:
  - '[[commands/curl-normal-jsonp-request]]'
  - '[[commands/curl-poison-jsonp-with-body-callback]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Web-Cache-Poisoning-via-GET-Request

## Summary

This procedure demonstrates how to perform web cache poisoning on a JSONP endpoint using manipulated requests, leading to stored XSS execution in the victim's browser cache. By altering the callback parameter in the request body while keeping the URL parameter fixed, the cache can be poisoned if the server does not include the body in the cache key, causing subsequent legitimate requests to return and execute the attacker's payload.

## Description

Web cache poisoning exploits misconfigurations in caching mechanisms where varying request parameters (like those in the body) are not included in the cache key. In this scenario, a JSONP endpoint (e.g., geolocate.js) wraps responses in a user-supplied callback function. A normal request uses a legitimate callback in the URL query (e.g., ?callback=setCountryCookie), but by sending a POST request with a malicious callback in the body, the response uses the body value for wrapping. If the cache keys only on the URL, this poisons the cache, and future GET requests without body retrieve the poisoned response. This delivers XSS when the browser loads the script, as the malicious callback executes JavaScript like alert(1). This technique targets browser or edge caches and is common in legacy JSONP implementations without proper validation.

## Requirements

1. Network access to the target web application with a vulnerable JSONP endpoint.
2. Burp Suite Professional or Community Edition installed for request interception and manipulation.
3. Basic knowledge of HTTP requests, JSONP, and browser caching behavior.
4. A listening proxy setup (e.g., Burp at 127.0.0.1:8080) configured in the browser.

## Defense

Defensive measures and detection strategies:

- Ensure cache keys include all request parameters, headers, and body content that affect the response (e.g., use Vary: * or specific headers).
- Validate and sanitize callback parameters in JSONP endpoints; restrict to whitelisted function names and avoid direct insertion without escaping.
- Implement Content Security Policy (CSP) with 'unsafe-inline' restrictions to block inline script execution from poisoned responses.
- Monitor for anomalous requests with mismatched query/body parameters and unusual callback values; use WAF rules to block non-alphanumeric callbacks.
- Disable browser caching for sensitive scripts or use no-cache headers like Cache-Control: no-store.

## Objectives

1. Identify and intercept requests to a cacheable JSONP endpoint.
2. Poison the cache by submitting a request with a malicious callback in the body.
3. Verify cache poisoning by observing reflected malicious content in subsequent responses.
4. Achieve XSS execution by loading the poisoned script in the browser, demonstrating arbitrary JavaScript execution.

## Instructions

### Step 1: Access and Intercept the Application

**Context**: Navigate to the target application in a browser configured to proxy traffic through Burp Suite. This allows capturing the initial request to the vulnerable JSONP endpoint (e.g., geolocate.js). The goal is to understand the normal request structure, which typically includes a callback parameter in the URL query.

Configure [[tools/Burp-Suite]] as a proxy (default: 127.0.0.1:8080) and enable interception. Load the page that triggers the geolocate.js request.

**Expected Output**: Intercepted HTTP request showing GET /geolocate.js?callback=setCountryCookie (or similar legitimate callback).

### Step 2: Send Normal Request and Observe Response

**Context**: Forward the intercepted request or simulate it to retrieve the legitimate response. This establishes the baseline where the response is wrapped in the URL callback function, confirming the endpoint's behavior.

Use [[commands/curl-normal-jsonp-request]] to test outside Burp:

```bash
curl "$_TARGET_URL?callback=setCountryCookie"
```

> This command fetches the JSONP response. Replace $_TARGET_URL with the full endpoint (e.g., http://target.com/geolocate.js). The legitimate callback ensures safe wrapping.

**Expected Output**: A response like `setCountryCookie({"country":"US"});`, indicating the data is wrapped in the specified function.

### Step 3: Modify Request in Repeater for Poisoning

**Context**: In Burp Suite's HTTP History, right-click the geolocate.js request and send it to Repeater. Modify the request to include the legitimate callback in the URL query but insert a custom (non-malicious) callback like 'myfunction' in the request body as a POST. This tests if the server prioritizes the body parameter for response wrapping, potentially poisoning the cache.

Alternatively, simulate with [[commands/curl-poison-jsonp-with-body-callback]]:

```bash
curl -X POST "$_TARGET_URL?callback=setCountryCookie" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "callback=myfunction"
```

> This sends a POST request with the poison callback in the body. The server may use this for wrapping if not properly validating sources. Resend a normal GET request afterward to check for cache hit.

**Expected Output**: Response wrapped in the body callback, e.g., `myfunction({"country":"US"});`. A subsequent normal request returns the same poisoned response, confirming cache poisoning.

### Step 4: Inject XSS Payload

**Context**: Repeat the poisoning step but set the body callback to an XSS payload like 'alert(1)'. This exploits the lack of validation, causing the response to include executable JavaScript. The poisoned cache delivers this to the browser on reload.

Use [[commands/curl-poison-jsonp-with-body-callback]] with the malicious payload:

```bash
curl -X POST "$_TARGET_URL?callback=setCountryCookie" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "callback=alert(1)"
```

> Escape special characters if needed (e.g., alert%281%29 for URL encoding). Send this to poison the cache.

**Expected Output**: Response like `alert(1)({"country":"US"});`, which executes as JavaScript when loaded via <script> tag.

### Step 5: Verify XSS Execution in Browser

**Context**: Reload the target page in the proxied browser to trigger a cache hit on the poisoned response. The browser executes the malicious callback, popping an alert box if successful.

Monitor Burp's Repeater or browser console for the reflected payload. No additional command needed; observe the alert dialog.

**Expected Output**: Browser alert box displaying '1' or the payload effect, confirming XSS via cache poisoning.

**Success Indicators**:
- Poisoned response reflects the custom/myfunction callback instead of the legitimate one.
- Subsequent normal requests return the poisoned content without resending the body.
- XSS payload executes in the browser without direct injection.
