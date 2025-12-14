---
id: proc-setup-http-listener-001
name: Setup-HTTP-Listener-for-SSRF-POC
tags:
  - ssrf
  - listener
  - poc
type: procedure
tools:
  - '[[tools/Python-HTTP-Server]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/start-python-http-server]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.117Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Setup-HTTP-Listener-for-SSRF-POC

## Summary

This procedure sets up a simple HTTP listener server to capture incoming requests from a vulnerable application like GitLab during an SSRF exploitation POC, allowing verification of server-side fetches to arbitrary URLs.

## Description

In SSRF attacks, the attacker needs a controllable endpoint to receive and log requests made by the target server. This procedure uses Python's built-in HTTP server to listen on a specified port (e.g., 4444), which must be publicly accessible via port forwarding. Once running, any request from the target (e.g., GitLab fetching a repository URL) will be logged, confirming the SSRF. Prerequisites include Python 3 installed and network access to expose the port.

## Requirements

1. Python 3.x installed on the attacker's machine
2. Port 4444 available and forwarded on the router for public access
3. Firewall rules allowing inbound traffic on port 4444

## Defense

Defensive measures and detection strategies:

- Monitor outbound network connections from application servers for unexpected destinations
- Implement URL whitelisting in import features to restrict to trusted domains like GitHub
- Use web application firewalls (WAF) to detect anomalous request patterns

## Objectives

1. Establish a reliable listener to capture SSRF-triggered requests
2. Log request details including IP, path, and headers for analysis
3. Validate the vulnerability without disrupting the target

## Instructions

### Step 1: Start the HTTP Server

**Context**: Launch the listener to begin capturing potential SSRF requests on the designated port.

**Command** ([[commands/start-python-http-server]]):
```bash
python3 -m http.server 4444
```

> This command starts a basic HTTP server serving files from the current directory on port 4444. In the POC, no files are needed; the server will log all incoming GET requests to stdout, showing the remote IP and requested path. Expected output includes startup message and request logs upon hits.

### Step 2: Configure Port Forwarding

**Context**: Ensure the listener is reachable from the internet if the target is external.

**Command**: No bash command; configure router UI to forward external port 4444 to local port 4444.

> Access router admin panel (e.g., 192.168.1.1), add port forward rule for TCP 4444. Test accessibility using an external tool like curl from another machine.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/start-python-http-server]]

## Tools Used

- [[tools/Python-HTTP-Server]]

## Tags

- ssrf
- listener
- http-server
