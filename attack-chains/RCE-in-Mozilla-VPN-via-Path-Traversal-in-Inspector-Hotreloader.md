---
tags:
  - path-traversal
  - rce
  - mozilla-vpn
  - websocket
  - qt
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/send-websocket-live-reload]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-Developer-Mode-in-Mozilla-VPN]]'
  - '[[procedures/Create-Malicious-HTML-for-WebSocket-Exploitation]]'
  - '[[procedures/Exploit-Path-Traversal-for-Arbitrary-File-Write]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:29.922Z'
description: >-
  Multi-stage attack exploiting path traversal in Mozilla VPN client's inspector
  feature to achieve arbitrary file writes and remote code execution on Windows
  via a malicious webpage.
skill_level: intermediate
impact_level: high
id: 2b569237-50eb-4901-93b9-68ff01ada54e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# RCE in Mozilla VPN via Path Traversal in Inspector Hotreloader

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the Mozilla VPN client's inspector feature, allowing arbitrary file writes and remote code execution on Windows systems with developer mode enabled.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install and Setup VPN Client] --> B[Enable Developer Mode]
    B --> C[Deploy Malicious Webpage]
    C --> D[Trigger Exploitation via WebSocket]
    D --> E[Arbitrary File Write and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- HTTP server for hosting malicious HTML and payload file (e.g., Python's http.server)

### Target Environment

- Windows OS
- Mozilla VPN client installed
- Port 8765 open locally for WebSocket (inspector server)
- Staging servers enabled in developer mode

### Initial Access Requirements

- User must install and run Mozilla VPN client
- Victim must open attacker-controlled webpage
- No prior credentials or network access needed beyond local execution

## Detailed Attack Procedures

### Step 1: Install Mozilla VPN Client
procedure: [[procedures/Enable-Developer-Mode-in-Mozilla-VPN]]

**Objective**: Obtain and prepare the target application for exploitation by installing the Mozilla VPN client on a Windows machine.

**Instructions**: Download the Mozilla VPN client from the official website and install it. Launch the client to ensure it runs properly. This step sets up the environment where the inspector feature is available.

**Expected Output**: Mozilla VPN client installed and running on the system.

**Success Indicators**:
- Client executable present in installation directory (e.g., C:\Users\user\AppData\Local\Mozilla\Mozilla VPN)
- Application launches without errors

### Step 2: Enable Developer Mode and Staging Servers
procedure: [[procedures/Enable-Developer-Mode-in-Mozilla-VPN]]

**Objective**: Activate developer options to enable the inspector WebSocket server and staging mode, which exposes the vulnerable hotreloader functionality.

**Instructions**: With the client open, access the help menu and click the 'Help' title 6 times rapidly to unlock developer options. Check the 'Use Staging Servers' box, then fully close and reopen the client to apply changes.

**Expected Output**: Developer mode activated; inspector server listening on ws://localhost:8765/.

**Success Indicators**:
- Developer menu visible in settings
- Staging servers option enabled
- WebSocket connection testable via browser dev tools

### Step 3: Create and Trigger Malicious HTML for Exploitation
procedure: [[procedures/Create-Malicious-HTML-for-WebSocket-Exploitation]] and [[procedures/Exploit-Path-Traversal-for-Arbitrary-File-Write]]

**Objective**: Deliver the exploit payload via a malicious webpage that connects to the local inspector and sends a path traversal command to write an arbitrary file, leading to RCE.

**Instructions**: Host a malicious HTML file on an attacker-controlled server (e.g., http://attacker.com/malicious.html) containing JavaScript to establish a WebSocket to ws://localhost:8765/ and send the live_reload command with traversal payload. Also host the payload file (e.g., traversal_poc.dll) on the same server. Trick the user into opening the HTML page while the VPN client is running in dev mode. The script will execute [[commands/send-websocket-live-reload]] to download and write the file to an arbitrary location like C:\Users\user\AppData\Local\Mozilla\traversal_poc.dll.

**Expected Output**: Arbitrary file written to target location; potential DLL loaded for RCE if placed in executable path.

**Success Indicators**:
- WebSocket connection established and command sent
- File appears in target directory (e.g., via file explorer)
- Logs in VPN client or network traffic show download from attacker server

## Attack Chain Summary

### Key Achievements

1. Enabled vulnerable inspector feature in Mozilla VPN client
2. Delivered exploit via user-interaction with malicious webpage
3. Achieved arbitrary file write bypassing temp folder restrictions, enabling RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
