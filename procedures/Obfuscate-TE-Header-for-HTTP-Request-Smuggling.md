---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - request-smuggling
  - http-smuggling
  - te-obfuscation
commands:
  - '[[commands/curl-obfuscated-te-header]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Obfuscate-TE-Header-for-HTTP-Request-Smuggling

## Summary

TE Header Obfuscation is a procedure for modifying the Transfer-Encoding header in HTTP requests to exploit differences in how front-end proxies and back-end servers parse HTTP headers. This technique is commonly used in HTTP Request Smuggling attacks to bypass web application firewalls (WAFs), load balancers, or other security controls, allowing attackers to inject and smuggle malicious requests to the backend.

## Description

HTTP Request Smuggling occurs when an attacker crafts a request that the front-end (e.g., a reverse proxy) interprets differently from the backend server, leading to desynchronization. The Transfer-Encoding (TE) header specifies chunked encoding, but obfuscating it with non-standard formatting (e.g., spaces, tabs, or invalid values like 'xchunked') can cause the front-end to ignore or misparse it while the backend processes it correctly. This procedure is applicable in scenarios targeting vulnerable web applications behind proxies, such as those using NGINX or Apache with mismatched configurations. It enables follow-on attacks like cache poisoning, session hijacking, or bypassing authentication. Prerequisites include identifying a smuggling vulnerability via probing (e.g., CL.TE or TE.CL variants) and having the ability to intercept and modify requests.

## Requirements

1. Network access to the target web application (e.g., ability to send HTTP requests).
2. A tool for crafting and sending custom HTTP requests, such as [[tools/Burp-Suite]] or curl.
3. Identification of a request smuggling vulnerability (e.g., via initial probes showing desynchronization).
4. Understanding of the target's HTTP stack (front-end vs. backend parsing behaviors).

## Defense

- Enforce consistent HTTP header parsing across all proxies and servers using the same HTTP version (e.g., HTTP/1.1 strict mode).
- Deploy a WAF configured to detect and block anomalous Transfer-Encoding headers, such as those with spaces, tabs, or invalid values.
- Monitor for signs of desynchronization, like duplicate requests or unexpected backend responses, using application logs and network traffic analysis.
- Normalize all incoming requests by rejecting ambiguous headers and enforcing Content-Length over Transfer-Encoding where possible.

## Objectives

1. Bypass front-end security controls by exploiting parsing differences.
2. Smuggle a malicious secondary request to the backend server.
3. Enable unauthorized actions, such as accessing restricted resources or poisoning caches.
4. Verify successful smuggling through backend response anomalies.

## Instructions

### Step 1: Set Up Request Interception

**Context**: Begin by intercepting or crafting an HTTP POST request to the target endpoint. This step ensures you can modify headers without automatic adjustments. Use [[tools/Burp-Suite]] for GUI-based manipulation or curl for command-line testing. The goal is to prepare a base request that triggers chunked encoding.

Navigate to the Repeater tab in Burp Suite (or prepare a curl command). Paste a sample POST request to a vulnerable endpoint, such as `/search` or a login form. Ensure the request body is formatted for chunked transfer (e.g., end with `0\r\n\r\n`).

### Step 2: Insert Obfuscated Transfer-Encoding Header

**Context**: Add an obfuscated TE header to exploit parsing discrepancies. The obfuscation tricks the front-end into ignoring the TE while the backend honors it, allowing the smuggled request to be appended after the chunked body. This step references variations to test which one bypasses the specific front-end parser.

Use the [[commands/curl-obfuscated-te-header]] command, substituting the obfuscation variant. For example, in Burp Repeater, manually insert one of the following headers just before the request body:

```http
Transfer-Encoding: xchunked
```

Or try other variations:

```http
Transfer-Encoding : chunked
```

```http
Transfer-Encoding: chunked
```

```http
Transfer-Encoding: x
```

```http
Transfer-Encoding:[tab]chunked
```

```http
[space]Transfer-Encoding: chunked
```

```http
X: X[\n]Transfer-Encoding: chunked
```

```http
Transfer-Encoding\n: chunked
```

In Burp, uncheck the "Update Content-Length" option in Repeater settings to prevent automatic header adjustments. Why this step? Standard TE headers are often normalized or blocked; obfuscation evades signature-based detection.

**Expected Output**: The request is accepted by the front-end without errors, but inspection of backend responses (via logs or additional probes) shows partial processing of the chunked body.

### Step 3: Append Smuggled Request and Trailing Sequence

**Context**: After the primary request's chunked body (ending in `0\r\n\r\n`), append the smuggled malicious request followed by another `\r\n\r\n`. This desynchronizes the streams, causing the backend to treat the appended content as a new request.

In Burp Repeater or curl, edit the body to include:

```
0\r\n\r\n
[SMUGGLED REQUEST HERE, e.g., GET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n]\r\n\r\n
```

Send the modified request. Decision point: If the front-end returns a 400 Bad Request, try a different obfuscation variant; if it passes but no smuggling occurs, confirm backend parsing with a probe request.

**Expected Output**: Front-end may respond normally to the primary request, but subsequent legitimate requests are affected (e.g., return the smuggled response), indicating success.

### Step 4: Verify Smuggling Success

**Context**: Confirm the attack by observing desynchronization effects, such as the backend processing the smuggled request or poisoning a shared cache.

Send a follow-up legitimate request and check if it returns the smuggled payload's response. In Burp, use the Inspector or logs to validate.

**Expected Output**: Anomalous responses, like accessing restricted pages or error messages revealing backend internals.

**Success Indicators**:
- Legitimate requests return smuggled content.
- No front-end blocking (e.g., 403 or 400 on TE header).
- Backend logs (if accessible) show extra requests.
