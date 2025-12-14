---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - mock-server
  - x-accel-redirect
  - ssrf
type: procedure
tools:
  - '[[tools/mocky-io]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.260Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Mock-Server-with-X-Accel-Redirect-Header

## Summary

This procedure creates a mock HTTP server using mocky.io to return a response with the X-Accel-Redirect header, simulating an attacker-controlled backend that redirects NGINX to internal paths in a Shopify App Proxy setup.

## Description

In the context of testing Shopify's App Proxy, this sets up a controlled response to inject the X-Accel-Redirect header, which NGINX interprets to serve internal locations. It requires no coding and uses a web-based tool, targeting web platforms with NGINX proxies. Expected outcome is a mock URL that triggers redirection upon proxying.

## Requirements

1. Internet access to mocky.io
2. Basic understanding of HTTP headers
3. No credentials needed for basic mock creation

## Defense

Defensive measures and detection strategies:

- Configure NGINX to ignore X-Accel-Redirect from untrusted upstreams in proxy setups
- Monitor proxy logs for unexpected internal redirects
- Validate and sanitize headers from App Proxy backends

## Objectives

1. Generate a mock endpoint for testing proxy redirection
2. Inject X-Accel-Redirect to /collections/all for demonstration
3. Verify header propagation in proxy requests

## Instructions

### Step 1: Design Mock Response

**Context**: Access the mocky.io designer to build a custom HTTP response.

Navigate to https://designer.mocky.io/design and configure the response body (e.g., empty or placeholder text) and headers.

**Tool Usage** ([[tools/mocky-io]]):

Set HTTP Headers to {"X-Accel-Redirect": "/collections/all"} and optionally add Content-Type: text/plain.

> This creates a 200 OK response with the redirect header. Expected output: Preview shows the header in response.

### Step 2: Generate and Test Mock URL

**Context**: Produce a unique URL for the mock and validate it.

Click 'Generate' to get the mock URL, e.g., https://run.mocky.io/v3/d7cdfcbc-6994-4f3b-a323-fe8377535507.

Test with curl:

```bash
curl -I https://run.mocky.io/v3/d7cdfcbc-6994-4f3b-a323-fe8377535507
```

> Expected output: HTTP/1.1 200 OK with X-Accel-Redirect: /collections/all in headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/mocky-io]]

## Tags

- mock-server
- x-accel-redirect
- ssrf
