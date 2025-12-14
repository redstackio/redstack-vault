---
id: proc-uuid-1
name: Set Up Ngrok Listener for Request Capture
tags:
  - ssrf
  - tunnel
  - capture
type: procedure
tools:
  - '[[tools/ngrok]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ngrok-start-tunnel]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.282Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set Up Ngrok Listener for Request Capture

## Summary

This procedure sets up a ngrok tunnel to create a public endpoint for capturing HTTP requests triggered by the SSRF exploit, allowing the attacker to receive and inspect server-side fetches from the vulnerable DoD login page.

## Description

In the context of SSRF exploitation, ngrok provides a secure tunnel from a local server to the internet, generating a temporary public URL. This is used to receive cross-domain requests initiated by the injected fetch API script on the target server. The procedure assumes local installation of ngrok and focuses on starting the tunnel and monitoring for incoming traffic. Expected outcomes include a stable public URL for payload integration and real-time visibility into exfiltrated data.

## Requirements

1. Ngrok installed on the attacker's machine (download from ngrok.com)
2. Internet connectivity for tunnel creation
3. Local port 4040 available for monitoring dashboard

## Defense

Defensive measures and detection strategies:

- Monitor outbound network traffic for connections to dynamic DNS services like ngrok
- Implement URL allowlisting on server-side request handlers to block external domains
- Use web application firewalls (WAF) to detect anomalous fetch requests in JavaScript payloads

## Objectives

1. Establish a reliable public endpoint for SSRF-induced requests
2. Enable real-time monitoring of captured headers and payloads
3. Prepare for data analysis in subsequent steps

## Instructions

### Step 1: Start Ngrok Tunnel

**Context**: Initiate the ngrok service to expose a local HTTP server publicly, generating a domain for the payload.

**Command** ([[commands/ngrok-start-tunnel]]):
```bash
ngrok http 80
```

> This command starts a tunnel on port 80, outputting a public URL like https://abc123.ngrok.io. Copy this URL for use in the SSRF payload. The tunnel forwards requests to your local machine.

### Step 2: Access Monitoring Dashboard

**Context**: Open the ngrok web interface to inspect incoming requests in real-time.

**Command** (Browser Access):
```bash
# No CLI command; open in browser
open http://127.0.0.1:4040
```

> The dashboard displays request details including headers, body, and response times. Verify the tunnel is active before proceeding.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/ngrok-start-tunnel]]

## Tools Used

- [[tools/ngrok]]

## Tags

- ssrf
- tunnel
- capture
