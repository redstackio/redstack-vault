---
tags:
  - ssrf
  - deployment
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/install-uppy-companion-globally]]'
  - '[[commands/start-uppy-companion-server]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T04:08:55.571Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 918fc5d2-605d-440d-85ea-32d327ce7418
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Deploy-Uppy-Companion-Server

## Summary

This procedure installs and starts the Uppy Companion server, a Node.js proxy that handles URL-based file uploads, setting up the environment for SSRF exploitation by enabling arbitrary URL fetching without validation.

## Description

The Uppy Companion server, part of the Uppy file uploader ecosystem, exposes a /get endpoint in url.js that directly fetches URLs from req.body.url via the downloadURL function. This procedure deploys it locally, configuring it to listen on localhost:3020 with debug mode enabled, allowing exploitation of internal resources like metadata services or local files. Prerequisites include Node.js and npm; the server runs as a background process vulnerable to SSRF when integrated with the Uppy client.

## Requirements

1. Node.js (v12+) and npm installed on a Linux or macOS system
2. Administrative privileges (sudo) for global installation
3. A configuration file (conf.json) specifying server host, port, and debug: true
4. Open port 3020 for local access

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URLs/protocols in the Companion server code (e.g., restrict to external HTTP/HTTPS)
- Run the server behind a firewall blocking internal outbound requests
- Monitor server logs for suspicious /get endpoint calls to internal IPs (e.g., 169.254.169.254, 127.0.0.1)
- Use network segmentation to isolate the server from internal services like metadata endpoints

## Objectives

1. Establish a running Companion server instance vulnerable to SSRF
2. Enable integration with Uppy client for URL submission
3. Prepare for exfiltration of internal data via fetched responses

## Instructions

### Step 1: Install Companion Globally

**Context**: Globally install the @uppy/companion package using npm to make the companion binary available system-wide.

**Command** ([[commands/install-uppy-companion-globally]]):
```bash
sudo npm install -g @uppy/companion
```

> This command installs the package with elevated privileges, outputting installation progress and success messages. Expected output includes "added X packages" and no errors.

### Step 2: Configure and Start Server

**Context**: Create a JSON config file and launch the server to bind to the specified port, enabling the vulnerable endpoint.

**Command** ([[commands/start-uppy-companion-server]]):
```bash
companion --config conf.json
```

> The config file should include {"debug": true, "server": {"host": "localhost", "port": 3020}}. Expected output: Server startup logs like "Companion running on http://localhost:3020".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/install-uppy-companion-globally]]
- [[commands/start-uppy-companion-server]]

## Tools Used

- [[tools/npm]]

## Tags

- ssrf
- deployment
- node.js
