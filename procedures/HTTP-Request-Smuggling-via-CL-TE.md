---
type: procedure
description: >-
  Exploit Content-Length/Transfer-Encoding (CL.TE) inconsistencies in HTTP
  parsing to smuggle malicious requests past front-end proxies and web
  application firewalls.
verified: true
submitted: false
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - cl-te
  - web-vulnerability
  - request-smuggling
commands:
  - '[[commands/curl-send-clte-smuggling]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# HTTP-Request-Smuggling-via-CL-TE

## Summary

HTTP Request Smuggling via CL.TE vulnerabilities exploits discrepancies in how front-end servers and back-end applications parse HTTP requests, particularly mismatches between Content-Length and Transfer-Encoding headers. This allows attackers to inject malicious requests that bypass security controls, enabling attacks like cache poisoning, session hijacking, or unauthorized access to admin functions.

## Description

HTTP Request Smuggling leverages inconsistencies in HTTP header interpretation between proxies (e.g., load balancers) and backend servers. In a CL.TE scenario, the attacker sets both Content-Length and Transfer-Encoding: chunked headers, causing the front-end to read based on Content-Length (treating the rest as the next request), while the backend processes it as chunked, leading to desynchronization. This can result in smuggled requests being processed unexpectedly, bypassing WAFs, poisoning caches with malicious content, or hijacking user sessions. The technique is effective against misconfigured HTTP/1.1 servers and is commonly used in web penetration testing to demonstrate request manipulation flaws. Prerequisites include identifying vulnerable endpoints through probing and access to a proxy tool for request crafting.

## Requirements

1. Access to a vulnerable web application or proxy chain (e.g., via browser or direct network access).
2. Knowledge of the target's HTTP parsing behavior (test with tools like [[tools/Burp-Suite]]).
3. Tools for manipulating and sending raw HTTP requests, such as Burp Suite or curl.

## Defense

Defensive measures and detection strategies:

- Deploy a WAF configured to normalize HTTP requests and reject ambiguous headers (e.g., both Content-Length and Transfer-Encoding present).
- Ensure consistent HTTP parsing across all proxies and backends by disabling ambiguous header support or enforcing HTTP/2 where possible.
- Monitor for anomalous request patterns, such as duplicate headers or unexpected chunked encodings in logs.
- Regularly patch web servers (e.g., Apache, Nginx) and test configurations with tools like HTTP Request Smuggling detectors.

## Objectives

1. Bypass security measures like WAFs and proxies to inject malicious requests.
2. Exploit CL.TE vulnerabilities to desynchronize request parsing and smuggle payloads.
3. Achieve outcomes like cache poisoning, session fixation, or cross-site scripting by smuggling additional requests.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Probe the target to confirm CL.TE vulnerability by sending test requests and observing if the backend misinterprets the body as a new request. Use a proxy like [[tools/Burp-Suite]] to intercept and modify traffic.

**Command** ([[commands/curl-send-clte-smuggling]]):
```bash
curl -X POST -H "Host: $_TARGET_HOST" -H "Content-Length: $_CL_VALUE" -H "Transfer-Encoding: chunked" --data-binary $'0\r\n\r\n$_SMUGGLED_PAYLOAD\r\n' http://$_TARGET_URL/
```

> This step sends a probe request to test desynchronization. Replace placeholders with target details. If successful, the smuggled payload (e.g., a second GET request) will be processed separately by the backend.

### Step 2: Craft and Send Smuggling Payload

**Context**: Use a pre-built smuggling payload to inject malicious content. Embed the smuggled request after the chunked body to trick the parser. Reference example payloads for structure.

**Code** ([[codes/CL-TE-Smuggling-Payload-with-SMUGGLED]]):

The raw HTTP payload is used here to illustrate the structure. Send it via the command in Step 1, substituting the $_SMUGGLED_PAYLOAD variable with content from this code.

> Expected: The front-end consumes the Content-Length body, forwarding the remaining "SMUGGLED" as a new request to the backend, confirming the vulnerability.

### Step 3: Verify and Exploit

**Context**: Analyze responses for signs of smuggling success, such as unexpected backend processing or cache entries. If successful, chain with further exploits like injecting admin requests.

> Check server logs or responses for the smuggled payload execution. If the backend echoes or acts on the smuggled part (e.g., "SMUGGLED" appears in output), the attack succeeded. Proceed to deliver payloads like XSS or session cookies.
