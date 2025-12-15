---
id: proc-uuid-4
tags:
  - header-capture
  - netcat
  - leak-verification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:30:26.614Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture-Leaked-Headers-on-Target-Port

## Summary

This procedure sets up a listener on a specified port (e.g., 2333) to intercept and log incoming HTTP requests after a redirect, verifying the presence of leaked Proxy-Authorization headers in the undici vulnerability PoC.

## Description

Using tools like netcat, this listens for TCP connections on port 2333, capturing the full request including headers. In the attack scenario, after the undici request triggers the redirect, the leaked header appears in the captured data, confirming information disclosure. Requires the port to be free and no firewall blocks.

## Requirements

1. Netcat (nc) installed
2. Port 2333 available and not in use
3. Prior steps completed (redirect and request sent)

## Defense

Defensive measures and detection strategies:

- Block unsolicited inbound connections on non-standard ports
- Use IDS to detect anomalous HTTP requests with proxy headers
- Implement header validation in receiving servers

## Objectives

1. Intercept the post-redirect request
2. Extract and verify sensitive header leakage
3. Document the proof-of-concept evidence

## Instructions

### Step 1: Start Listener

**Context**: Launch netcat to listen on the target port for incoming connections.

**Command** (nc listen):
```bash
nc -l 2333
```

> Binds to port 2333. Expected output: Waiting for connection; no output until request arrives.

### Step 2: Trigger Request and Observe

**Context**: From another terminal, run the undici request; observe the capture here.

**Contextual Action**: Ensure the exploit.js from prior procedure is executed.

> Incoming data shows: GET / HTTP/1.1 ... Proxy-Authorization: secret Proxy-Authorization.

### Step 3: Analyze Capture

**Context**: Review the logged request for the leaked header.

**Command** (if logging to file):
```bash
nc -l 2333 > capture.txt
```

> Saves output to file. Expected output: File contains full request with headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- header-capture
- netcat
- leak-verification
