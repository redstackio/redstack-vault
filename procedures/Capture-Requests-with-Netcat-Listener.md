---
tags:
  - netcat
  - listener
  - capture
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/nc-listen-port]]'
verified: false
platforms:
  - macOS
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:28:36.557Z'
sub_techniques: []
id: 06af9706-bd42-4dde-98ea-650d2e6c272e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Capture-Requests-with-Netcat-Listener

## Summary

This procedure deploys a netcat listener on Server2 to capture incoming HTTP requests, specifically to log headers like Proxy-Authorization that may be leaked during a redirect from curl.

## Description

Netcat acts as a basic TCP server listening on port 8081, dumping all received data to stdout for inspection. In this attack scenario, it intercepts the redirected request from curl, revealing if sensitive headers are forwarded. This is useful for verifying client-side vulnerabilities in tools like curl. Requires netcat installed and port 8081 free on Server2.

## Requirements

1. Netcat (nc) utility installed (standard on most Unix-like systems)
2. Port 8081 available on Server2
3. Terminal access to Server2 for monitoring output
4. No firewall blocking inbound TCP on 8081

## Defense

Defensive measures and detection strategies:

- Block unauthorized listeners on internal ports via host firewalls
- Monitor for netcat processes (e.g., via ps aux | grep nc)
- Use network segmentation to prevent cross-host redirects to untrusted endpoints

## Objectives

1. Intercept redirected HTTP requests for header analysis
2. Capture evidence of Proxy-Authorization leakage
3. Validate the redirect chain's impact on credential security

## Instructions

### Step 1: Start Netcat Listener

**Context**: Bind to port 8081 and prepare to receive TCP connections.

**Command** ([[commands/nc-listen-port]]):
```bash
nc -l 8081
```

> This enters listen mode; upon connection, it displays raw HTTP request data including headers. Keep the terminal open to observe incoming traffic.

### Step 2: Verify Listener

**Context**: Test the listener with a manual connection before the main attack.

**Command** ([[commands/nc-listen-port]]):
```bash
# From another terminal: echo "GET / HTTP/1.1\r\nHost: server2\r\n\r\n" | nc server2 8081
```

> Expected output in listener terminal: Displays the test GET request, confirming capture functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-port]]

## Tools Used

- [[tools/netcat]]

## Tags

- netcat
- tcp-listener
- packet-capture
