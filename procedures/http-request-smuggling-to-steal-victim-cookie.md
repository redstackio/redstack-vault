---
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
  - session-hijacking
commands:
  - '[[commands/curl-send-smuggled-post-request]]'
  - '[[commands/curl-retrieve-smuggled-response]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
verified: true
validated: true
---

# HTTP Request Smuggling to Steal Victim Cookie

## Summary

This procedure exploits HTTP Request Smuggling vulnerabilities, specifically Content-Length (CL) discrepancies between front-end and back-end servers, to hijack the request queue. By sending a smuggled POST request with an inflated Content-Length, the attacker causes the next legitimate user's request (e.g., a comment submission) to be stored and interpretable as the smuggled payload's body. The attacker then retrieves this stored request to extract the victim's session cookie, enabling account takeover.

## Description

HTTP Request Smuggling (HRS) abuses inconsistencies in how proxies or load balancers parse HTTP headers like Content-Length and Transfer-Encoding. In a CL-based attack, the front-end uses the declared Content-Length, but the back-end may ignore extra data or interpret subsequent requests as part of the body. This procedure targets POST endpoints (e.g., user comments) in web applications behind misconfigured proxies. The attack requires no authentication for public endpoints but assumes the attacker can observe or trigger user traffic timing. Success leads to session hijacking without direct credential theft. Map to MITRE: Exploitation via public-facing app and collection of authentication material.

## Requirements

1. Network access to the target web application (public-facing endpoint like /comment).
2. Knowledge of the POST request structure (e.g., form fields for comments).
3. Tools: Burp Suite for interception and Repeater (GUI-based) or curl for scripted testing.
4. Ability to time requests to coincide with victim activity (or simulate in lab).

## Defense

Defensive measures and detection strategies:

- Enforce strict HTTP/1.1 parsing at all proxies/load balancers (e.g., reject dual CL/TE headers).
- Use request normalization tools like ModSecurity to validate and sanitize headers.
- Implement per-request timeouts and queue flushing to prevent smuggling persistence.
- Monitor logs for mismatched Content-Length values or anomalous request chaining (e.g., via WAF rules).
- Enable HSTS and secure cookies to limit session reuse impact.

## Objectives

1. Smuggle a malformed POST request to disrupt the request queue and store the subsequent victim request.
2. Retrieve the stored victim request containing sensitive headers like Cookie.
3. Extract and validate the stolen cookie for session hijacking.

## Instructions

### Step 1: Intercept and Craft the Smuggled POST Request

**Context**: Begin by capturing a normal POST request to a user-action endpoint (e.g., submitting a comment). Modify it to include an inflated Content-Length header, making the body appear incomplete to the back-end. This causes the back-end to treat the next incoming request's headers (including the victim's Cookie) as continuation of the body. Use Burp Suite's Proxy to intercept or Repeater to test; alternatively, use curl for direct sending. The goal is to queue the smuggling without immediate detection.

**Command** ([[commands/curl-send-smuggled-post-request]]):
```bash
curl -X POST $_TARGET_URL \
  -H "Content-Length: $_CONTENT_LENGTH" \
  -H "Content-Type: $_CONTENT_TYPE" \
  -d "$_POST_DATA"
```

> This command sends the smuggled request. Start with Content-Length around 400 (adjust based on typical request size). The POST data should be partial (e.g., a short comment) to leave room for the victim's request. Why: The discrepancy forces the back-end to buffer and misinterpret the queue. Expected: HTTP 200/400 response from front-end, but back-end queues it. Verify by checking application logs or response delays.

### Step 2: Trigger and Retrieve the Stored Victim Request

**Context**: Immediately after sending the smuggled request, a victim user submits their request (e.g., posts a comment), which gets prepended to your smuggling payload in the back-end queue. Send a retrieval request (often a simple POST with zero-length body) to the same endpoint to fetch the stored data. This exposes the victim's full request, including headers like Cookie. If the initial retrieval is incomplete (e.g., partial Cookie), incrementally increase the original Content-Length (e.g., from 400 to 500) and repeat until the full Cookie is captured.

**Command** ([[commands/curl-retrieve-smuggled-response]]):
```bash
curl -X POST $_TARGET_URL \
  -H "Content-Length: 0" \
  -d ""
```

> This pulls the queued victim request. Why: The zero-length body acts as a desynchronization trigger, dumping the stored payload. Expected: Response body containing the victim's request text, including lines like "Cookie: session=abc123...". If incomplete, decision point: If Cookie is truncated, resend smuggled request with higher Content-Length and retry retrieval.

### Step 3: Extract Cookie and Validate Hijack

**Context**: Parse the retrieved response for the Cookie header. Manually copy the session token (e.g., from "Cookie: JSESSIONID=xyz; auth=token"). Test by injecting it into your browser or a new curl request to a protected endpoint. Why: Confirms the smuggling success and enables impersonation. No automated command needed; use grep on response if scripted: `echo "$RESPONSE" | grep -i cookie`.

> Expected: Successful access to victim's account features (e.g., view private data). If fails, check for CSRF tokens or IP binding.
