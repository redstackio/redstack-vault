---
id: proc-netcat-listener
tags:
  - ssrf
  - listener
  - verification
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/netcat-listen-on-port]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T05:32:10.505Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Set-Up-Netcat-Listener-for-SSRF

## Summary

This procedure sets up a simple TCP listener using netcat to capture incoming HTTP requests from a vulnerable server like Shopify during SSRF testing, confirming that the target fetches the referenced URL.

## Description

Netcat acts as a server to log requests triggered by SVG uploads. In the Shopify SSRF scenario, it verifies private server access by capturing GET requests to a controlled endpoint. Requires a machine with netcat installed and an open port; outcomes include logged evidence of SSRF exploitation.

## Requirements

1. Netcat installed on a test machine
2. Firewall allowing inbound on port 3001
3. Public IP or accessible endpoint for the listener

## Defense

Defensive measures and detection strategies:

- Block unexpected inbound connections on non-standard ports
- Use IDS to alert on netcat-like traffic patterns
- Restrict server outbound requests to trusted domains

## Objectives

1. Establish a listener for SSRF verification
2. Capture and log incoming requests
3. Confirm exploitation success

## Instructions

### Step 1: Initiate Listener

**Context**: Start netcat in listen mode on the desired port.

**Command** ([[commands/netcat-listen-on-port]]):
```bash
netcat -l -p 3001 -v
```

> Explanation: -l enables listen mode, -p specifies port 3001, -v provides verbose output. Expected output: "Listening on [0.0.0.0] (family 0, port 3001)".

### Step 2: Monitor for Connections

**Context**: Keep the terminal open to watch for incoming SSRF-triggered requests.

No additional command; observe logs.

> Expected: Upon trigger, logs show "Connection from [Shopify IP] port 3001" followed by HTTP GET details.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/netcat-listen-on-port]]

## Tools Used

- [[tools/netcat]]

## Tags

- ssrf
- netcat
