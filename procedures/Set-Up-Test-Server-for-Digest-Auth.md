---
tags:
  - setup
  - test-server
  - digest-auth
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/python3-http-server-digest]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-12-14T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:31:30.977Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: eb7f7bd1-246f-4dc5-9806-e201e0a657af
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Set-Up-Test-Server-for-Digest-Auth

## Summary

This procedure sets up a local Python HTTP server with Digest Authentication enabled to simulate a target for testing curl's timing vulnerability in Digest Authentication processing.

## Description

In the context of exploiting the timing attack in curl's lib/vauth/digest.c (line 360), a test server is required to announce Digest challenges with various algorithms (e.g., MD5, SHA-1). The server runs on localhost:8080 and protects a resource at /protected, allowing curl clients to authenticate while the attack measures response times. This setup is essential for reproducing the non-constant-time strcmp() behavior without affecting production systems. Expected outcomes include a running server that responds to authentication attempts with measurable latencies.

## Requirements

1. Python 3 installed on a Linux system
2. Local network access (localhost)
3. Port 8080 available

## Defense

Defensive measures and detection strategies:

- Use constant-time comparisons in client libraries like curl (e.g., upgrade to curl 8.5.0+ using Curl_timestrcmp())
- Monitor for unusual authentication timing patterns or repeated failed logins from the same IP
- Disable legacy algorithms like MD5 in server configurations to reduce fingerprinting value

## Objectives

1. Create a controlled environment for timing attack reproduction
2. Enable Digest Authentication challenges for algorithm testing
3. Verify server readiness for PoC execution

## Instructions

### Step 1: Start the HTTP Server with Digest Auth

**Context**: Launch a simple Python server that supports Digest Authentication to host a protected endpoint.

**Command** ([[commands/python3-http-server-digest]]):
```bash
python3 -m http.server 8080 --digest
```

> This command starts the server on port 8080 with a custom --digest flag (assuming a modified http.server module or wrapper for Digest support). Expected output includes 'Server running on http://localhost:8080' and logs for incoming requests. The server will challenge clients with Digest nonces and algorithm options.

### Step 2: Verify Server Accessibility

**Context**: Confirm the server is protecting resources and responding to unauthenticated requests with 401 challenges.

**Command** (use curl for basic test):
```bash
curl -v http://localhost:8080/protected
```

> This manual verification shows a 401 Unauthorized response with WWW-Authenticate: Digest header, confirming setup success. No timing measurement here; proceed to PoC.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/python3-http-server-digest]]

## Tools Used

- [[tools/Python]]

## Tags

- setup
- test-server
- digest-auth
