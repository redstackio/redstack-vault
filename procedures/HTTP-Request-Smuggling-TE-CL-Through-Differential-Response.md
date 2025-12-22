---
type: procedure
description: >-
  Craft and send a TE.CL HTTP request smuggling payload to exploit parsing
  differences between front-end and back-end servers, observing a differential
  response.
verified: true
submitted: true
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
commands:
  - '[[commands/curl-http-smuggling-te-cl]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# HTTP-Request-Smuggling-TE-CL-Through-Differential-Response

## Summary

This procedure demonstrates how to perform an HTTP Request Smuggling attack using the TE.CL variant, where both Transfer-Encoding: chunked and Content-Length headers are included in the request. By exploiting inconsistencies in how the front-end proxy and back-end server parse the request, an attacker can smuggle an additional malicious request into the body. Success is confirmed by observing a differential response, such as the back-end processing a smuggled POST to a non-existent endpoint like /404 while the front-end interprets it differently.

## Description

HTTP Request Smuggling occurs when there is ambiguity in HTTP request parsing due to conflicting headers like Transfer-Encoding (TE) and Content-Length (CL). In the TE.CL variant, the front-end may use the CL header (e.g., Content-Length: 4) to determine the body length, while the back-end honors the TE: chunked, treating the remaining data as a new request. This allows smuggling a second request, such as a POST to /404, which can poison caches, bypass authentication, or access admin functions. This procedure focuses on detection via differential responses in a lab environment like Web Security Academy, using tools like Burp Suite for interception and modification. It requires a vulnerable application with a misconfigured proxy chain and maps to MITRE ATT&CK technique T1190 for exploiting public-facing applications.

## Requirements

1. Network access to a vulnerable web application with a front-end proxy (e.g., load balancer) and back-end server.
2. Burp Suite Professional or Community Edition installed and configured as a proxy.
3. Basic knowledge of HTTP protocol and request structure.
4. A legitimate POST endpoint on the target (e.g., search or login form) to base the smuggling on.

## Defense

Defensive measures and detection strategies:

- Configure front-end proxies to reject requests with both TE and CL headers (e.g., using NGINX or Apache strict parsing).
- Implement request normalization to remove or prioritize one header consistently across the stack.
- Monitor access logs for anomalous requests with chunked encoding followed by unexpected HTTP methods or paths.
- Use Web Application Firewalls (WAFs) like ModSecurity with rules to detect smuggling patterns (e.g., multiple HTTP/1.1 in body).

## Objectives

1. Intercept and modify a legitimate request to include conflicting TE and CL headers.
2. Smuggle a secondary POST request to a non-existent endpoint (/404) within the chunked body.
3. Observe a differential response confirming the back-end processed the smuggled request differently from the front-end.
4. Verify vulnerability for further exploitation like cache poisoning or session hijacking.

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Begin by capturing a normal POST request to establish a baseline and prepare for modification. This step ensures you can observe normal behavior before introducing the smuggling payload.

**Instructions**: Configure your browser to use Burp Suite as a proxy (default: 127.0.0.1:8080). Navigate to a POST endpoint on the target application (e.g., a search form). Submit the request to trigger interception. In Burp Proxy, forward the request and send it to the Repeater tab for modification.

**Expected Output**: A standard HTTP response (e.g., 200 OK with search results). No errors or unusual behavior.

### Step 2: Craft Smuggling Payload

**Context**: Modify the intercepted request to include both Content-Length: 4 and Transfer-Encoding: chunked, appending a smuggled POST /404 request in the chunked body. The small CL value causes the front-end to see only the chunk size prefix, while the back-end interprets the rest as a new request.

**Command** ([[commands/curl-http-smuggling-te-cl]]):

Use the following curl command to send the payload directly, or paste the raw request into Burp Repeater using [[tools/Burp-Suite]] for easier inspection.

```bash
curl -i -X POST http://$_TARGET_HOST/ \
  -H "Host: $_TARGET_HOST" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Content-Length: 4" \
  -H "Transfer-Encoding: chunked" \
  --data-raw $'5e\r\nPOST /404 HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 15\r\n\r\nx=1 \r\n0\r\n\r\n'
```

**Code** ([[codes/HTTP-Smuggling-TE-CL-Request]]):

For precise control, use the raw HTTP code snippet in Burp Repeater:

```
POST / HTTP/1.1
Host: $_TARGET_HOST
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
5e
POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1 
0
```

> The '5e' is the hex chunk size (94 bytes for the smuggled request). Replace $_TARGET_HOST with the actual domain (e.g., your-lab-id.web-security-academy.net). Send the request and compare to a normal POST.

**Expected Output**: The front-end may return a 400 Bad Request or partial response based on CL:4, but the back-end processes the smuggled POST, potentially returning a 404 Not Found embedded or as a differential element.

### Step 3: Analyze Differential Response

**Context**: Send the modified request and verify the smuggling by checking for inconsistencies in the response, such as elements from the /404 page appearing unexpectedly or log evidence of the second request.

**Instructions**: In Burp Repeater, click 'Send' on the modified request. Inspect the response headers and body for signs of the smuggled request (e.g., 404 status or error message for /404). Repeat with a normal request for comparison. If using curl, pipe output to a file for analysis: curl ... > response.txt.

**Expected Output**: Differential response, e.g., front-end sees invalid request (400), but response body includes /404 content or server logs show two requests. Success if the smuggled POST is executed by the back-end.

**Success Indicators**:
- Response contains 404 elements not present in normal requests.
- No full rejection of the request despite conflicting headers.
- Repeatable behavior confirming parsing inconsistency.
