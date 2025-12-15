---
tags:
  - traffic-capture
  - netcat
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:09.536Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6e8bc5b5-6f56-4a98-844c-33694636a9bf
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Capture-Redirect-Traffic

## Summary

This procedure sets up a listener on the redirect target port to capture incoming requests and verify that sensitive headers are forwarded from the undici client.

## Description

Using a tool like netcat, listen on port 2333 for the redirected request from a.com. This captures the full HTTP request, including headers, to confirm the leakage of Proxy-Authorization and x-auth-token, which should be cleared per RFC 9110 but are not in undici.

## Requirements

1. Port 2333 free on localhost
2. netcat (nc) installed
3. Previous steps completed (redirect and request executed)

## Defense

Defensive measures and detection strategies:

- Implement header inspection in servers to log unexpected auth headers
- Use IDS to detect anomalous header patterns in traffic
- Enforce strict origin checks in client redirect handlers

## Objectives

1. Intercept and log the redirected request
2. Validate presence of leaked sensitive headers
3. Document evidence of vulnerability for reporting

## Instructions

### Step 1: Start Listener

**Context**: Launch netcat to listen for incoming connections on port 2333.

**Command** (netcat listen):
```bash
nc -l 2333
```

> Binds to port 2333. Expected output: Waiting for connection; upon request, displays raw HTTP request with headers.

### Step 2: Trigger and Observe

**Context**: After starting listener, execute the undici request from previous procedure to send traffic.

**Command** (no new command; observe output):

> In netcat terminal, expect: GET / HTTP/1.1 ... Proxy-Authorization: secret Proxy-Authorization ... x-auth-token: secret x-auth-token. This confirms leakage.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- traffic-capture
- netcat
