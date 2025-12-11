---
tags:
  - rce
  - websocket
  - electron
  - local-exploit
type: attack_chain
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/netstat]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
  - '[[Execution]]'
commands:
  - '[[commands/netstat-check-ports]]'
  - '[[commands/burp-proxy-setup]]'
platforms:
  - Windows
complexity: medium
procedures:
  - '[[procedures/Discover-Local-WebSocket-Server]]'
  - '[[procedures/Inspect-and-Proxy-WebSocket-Traffic]]'
  - '[[procedures/Exploit-RCE-via-Malicious-URL-Loading]]'
step_count: 3
techniques:
  - '[[Network Sniffing]]'
  - '[[Exploitation for Client Execution]]'
description: >-
  Chained vulnerabilities in PlayStation Now allowing remote code execution
  through local WebSocket exploitation and Electron nodeIntegration
skill_level: intermediate
impact_level: high
id: e4f30da4-07ae-4fc6-a8b5-e4b33247c3eb
created_at: '2025-12-11T06:10:30.674Z'
updated_at: '2025-12-11T06:10:30.674Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1040]]'
  - '[[T1203]]'
---
# Remote Code Execution via PlayStation Now WebSocket and Electron Vulnerabilities

## Overview

This attack chain exploits vulnerabilities in PlayStation Now version 11.0.2, chaining a local WebSocket server lacking Origin header checks, the ability to command an Electron-based AGL app to load arbitrary URLs, and enabled nodeIntegration allowing JavaScript to access Node.js APIs. The result is remote code execution on the victim's machine, such as launching applications like calc.exe, initiated from a malicious website on the same machine.

## Attack Flow

```mermaid
graph LR
    A[Discover Local Server] --> B[Inspect Traffic] --> C[Exploit RCE]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools
- [[tools/Process-Monitor]]
- [[tools/netstat]]
- [[tools/Burp-Suite]]

### Target Environment
- Windows OS with PlayStation Now version 11.0.2 installed
- Local WebSocket server running on localhost:1235
- Network access to localhost

### Initial Access Requirements
- Ability to run the PlayStation Now application on the target machine
- Access to execute tools for discovery and proxying

## Step 1: Server Discovery - [[procedures/Discover-Local-WebSocket-Server]]

### Objective

Install and run the PlayStation Now application to expose the vulnerable local WebSocket server and identify listening ports.

### Instructions

Download and install PlayStation Now from https://download-psnow.playstation.com/downloads/psnow/pc/latest. Execute the launcher using the path C:\Program Files (x86)\PlayStationNow\psnowlauncher.exe, which spawns the AGL Electron app and starts the WebSocket server on localhost:1235.

Use [[commands/netstat-check-ports]] to verify the listening port:

```bash
netstat -anb
```

Monitor processes with [[tools/Process-Monitor]] to confirm the WebSocket server is active.

### Validation

Confirm the WebSocket server is listening on localhost:1235 and associated with psnowlauncher.exe.

## Step 2: Traffic Inspection - [[procedures/Inspect-and-Proxy-WebSocket-Traffic]]

### Objective

Proxy and analyze WebSocket communications to understand commands for loading URLs in the AGL app.

### Instructions

Set up [[tools/Burp-Suite]] to proxy local traffic. Configure it to intercept WebSocket connections to localhost:1235.

Use [[commands/burp-proxy-setup]] to start proxying:

```bash
# Configure Burp Suite to listen on localhost and proxy WebSocket traffic
```

Interact with the PlayStation Now app to generate traffic, then inspect WebSocket messages in Burp Suite to identify commands for loading arbitrary URLs.

### Validation

Observe WebSocket messages without Origin checks, confirming the ability to send commands from unauthorized sources.

## Step 3: RCE Exploitation - [[procedures/Exploit-RCE-via-Malicious-URL-Loading]]

### Objective

Connect to the WebSocket server from a malicious local website and command the AGL app to load a URL with malicious JavaScript, leveraging nodeIntegration for code execution.

### Instructions

Host a malicious website locally that connects to ws://localhost:1235. Send a WebSocket message commanding the AGL app to load a URL containing JavaScript that accesses Node.js APIs (e.g., child_process.spawn) to execute commands like launching calc.exe.

Example malicious JavaScript payload:

```javascript
require('child_process').spawn('calc.exe');
```

Validate execution by observing the spawned process.

### Validation

Confirm arbitrary code execution, such as calc.exe launching on the target machine.

## Attack Chain Summary

### Key Achievements
1. Identified vulnerable local WebSocket server
2. Analyzed traffic to discover URL loading commands
3. Achieved RCE through chained exploitation
