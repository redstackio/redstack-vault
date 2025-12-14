---
id: proc-brave-host-local
name: Host-HTML-on-Local-Server
tags:
  - local-server
  - hosting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-http-server]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:39.941Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Host-HTML-on-Local-Server

## Summary

This procedure sets up a local web server to host the malicious HTML file, making it accessible via HTTP on a local IP address for loading in the target iOS Brave browser.

## Description

To simulate a remote malicious site, host the `blob.html` file using a basic HTTP server on the local network. This allows the iOS device to access it over Wi-Fi. No advanced setup is needed; Python's built-in module suffices. The server runs on the local IP (e.g., 192.168.1.111) and serves the file at /blob.html. This step is crucial for triggering the vulnerability without file:// protocol issues.

## Requirements

1. Python 3 installed on the hosting machine
2. HTML file in the server directory
3. Local network connectivity to iOS device

## Defense

Defensive measures and detection strategies:

- Block unauthorized local servers via firewall rules
- Monitor network for unexpected HTTP traffic from development tools
- Use HTTPS-only policies in browsers to prevent local hosting exploits

## Objectives

1. Start a local HTTP server serving the HTML file
2. Confirm accessibility from the network
3. Prepare URL for browser loading

## Instructions

### Step 1: Navigate to HTML Directory

**Context**: Change to the directory containing `blob.html` to serve from there.

Use terminal to cd into the path:

```bash
cd /path/to/html/directory
```

> This positions the server root correctly.

### Step 2: Launch Python HTTP Server

**Context**: Start the server using Python's http.server module to host on port 80 or 8000.

Execute [[commands/python-http-server]]:

```bash
python3 -m http.server 80
```

> The server listens on all interfaces. Access via http://<local-ip>:80/blob.html (e.g., http://192.168.1.111/blob.html). Expected: 'Serving HTTP on 0.0.0.0 port 80' message.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/python-http-server]]

## Tools Used


## Tags

- [[local-hosting]]
- [[web-server]]
