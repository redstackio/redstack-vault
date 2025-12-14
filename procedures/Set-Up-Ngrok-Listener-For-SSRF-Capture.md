---
id: proc-ngrok-ssrf-listener
tags:
  - ssrf
  - listener
  - ngrok
type: procedure
tools:
  - '[[tools/ngrok]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:01.847Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set-Up-Ngrok-Listener-For-SSRF-Capture

## Summary

This procedure sets up an ngrok tunnel to create a public endpoint for capturing SSRF requests from a target server, allowing the attacker to receive and analyze incoming data such as victim IP addresses and headers.

## Description

In an SSRF attack scenario targeting a web application like the DoD login page, ngrok exposes a local server to the internet via a temporary domain. This enables the target server to make unauthorized requests to the attacker's listener when the injected payload executes. Prerequisites include ngrok installed and run on a local machine; the procedure assumes public internet access and no firewall blocks on port 4040.

## Requirements

1. Ngrok binary installed and authenticated with an account token
2. Local machine with internet access
3. Port 4040 available for ngrok's web interface

## Defense

Defensive measures and detection strategies:

- Monitor outbound traffic for connections to dynamic DNS services like ngrok
- Implement URL whitelisting to block requests to tunneling services
- Use web application firewalls (WAF) to detect anomalous fetch requests

## Objectives

1. Establish a reliable capture point for SSRF exfiltration
2. Provide a web interface for real-time request monitoring
3. Enable analysis of captured victim metadata

## Instructions

### Step 1: Start Ngrok Tunnel

**Context**: Launch ngrok to generate a public HTTPS URL for receiving SSRF requests.

**Command** ([[commands/ngrok-http-tunnel]]):
```bash
ngrok http 80
```

> This command starts a tunnel on port 80 (default for HTTP). Ngrok outputs a forwarding URL like https://abc123.ngrok.io. Note the URL for payload crafting. Expected output includes the public URL and inspection interface details.

### Step 2: Access Ngrok Interface

**Context**: Open the local web interface to prepare for monitoring incoming requests.

**Instructions**: Navigate to http://127.0.0.1:4040 in a browser to view the dashboard.

> The interface shows real-time request logs, headers, and payloads. Successful setup is indicated by the dashboard loading without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ngrok]]

## Tags

- ssrf
- listener
- tunneling
