---
id: 853f447f-7994-4b83-852b-b3c261803ef2
name: HTTP-Request-Smuggling-CL-TE-Differential-Response
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:18:39.664961+00:00'
updated_at: '2023-05-26T18:38:51.939221+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# HTTP-Request-Smuggling-CL-TE-Differential-Response

## Summary

This procedure demonstrates how to perform an HTTP Request Smuggling attack using a combination of Content-Length (CL) and Transfer-Encoding (TE) headers to inject a malicious request. By crafting a smuggled request and observing differential responses from the server, attackers can confirm the vulnerability, potentially leading to request desynchronization, cache poisoning, or bypassing security controls in web applications.

## Description

HTTP Request Smuggling exploits inconsistencies in how front-end and back-end servers parse HTTP requests, particularly when both CL and TE headers are present. In a CL.TE variant, the attacker sends a request with a short CL followed by a chunked TE body that includes a second, smuggled request (e.g., to a 404 endpoint). If the front-end processes the TE but the back-end uses CL, the smuggled request may be interpreted separately, resulting in a differential response. This technique is useful in scenarios where the application is behind a proxy or load balancer, allowing attackers to test for parsing discrepancies without needing authenticated access. The procedure assumes use of a proxy tool like Burp Suite to intercept and modify requests.

## Requirements

1. Access to a vulnerable web application endpoint (e.g., a login or search form) that accepts POST requests.
2. Burp Suite or similar proxy tool installed and configured to intercept traffic.
3. Network access to the target server, typically over HTTP/1.1.
4. Basic understanding of HTTP headers and request smuggling concepts.

## Defense

Defensive measures and detection strategies:

- Normalize HTTP requests by removing or rejecting ambiguous headers like dual CL and TE.
- Use strict HTTP/1.1 parsing on all proxies and back-ends (e.g., enforce one parsing method).
- Implement request logging and anomaly detection for mismatched header lengths or chunked bodies.
- Deploy Web Application Firewalls (WAFs) with rules for smuggling patterns.

## Objectives

1. Craft and send a smuggled HTTP request to test for CL.TE vulnerability.
2. Observe differential responses to confirm server parsing inconsistencies.
3. Validate the potential for further exploitation like bypassing authentication.

## Instructions

### Step 1: Intercept the Base Request

**Context**: Begin by capturing a legitimate POST request to the target endpoint using a proxy tool. This establishes the baseline for modification and ensures you can observe how the server handles normal traffic.

Use [[tools/Burp-Suite]] to intercept the request and forward it to the Repeater tab for manipulation.

> In Burp Suite, configure your browser proxy to 127.0.0.1:8080, navigate to the target site, and intercept a POST request (e.g., to /search or /login).

### Step 2: Modify the Request for Smuggling

**Context**: Alter the intercepted request to include both Content-Length and Transfer-Encoding headers, smuggling a secondary request in the chunked body. This step aims to desynchronize the front-end and back-end parsers.

Use the smuggled payload from [[codes/HTTP-Request-Smuggling-CL-TE-Payload]] in Burp Repeater:

```http
POST / HTTP/1.1
Host: your-lab-id.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked
5e

POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1 
0
```

> Replace 'your-lab-id.web-security-academy.net' with the actual target host. Send the modified request and note if the response indicates a 404 for the smuggled path, confirming differential processing.

### Step 3: Analyze the Response

**Context**: Send the modified request and compare the response to a baseline legitimate request. A differential response (e.g., 404 instead of 200) indicates successful smuggling.

In Burp Repeater, send the request multiple times and inspect the HTTP response code and body.

> Expected signs of success include the server responding as if the smuggled POST /404 was processed separately, often showing a 404 Not Found page or error.

## Expected Output

Upon successful execution, the server response will show a differential behavior, such as a 404 status for the smuggled request embedded in what appears to be a single request. Sample response:

```
HTTP/1.1 404 Not Found
Content-Type: text/html

<html><body>404 - Page Not Found</body></html>
```

This confirms the vulnerability, as the front-end and back-end have parsed the request differently.
