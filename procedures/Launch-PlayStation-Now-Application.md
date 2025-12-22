---
tags:
  - discovery
  - websocket
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Request-Highlighter]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/websocket-seturldefaultbrowser-calc]]'
  - '[[commands/require-child-process-exec-calc]]'
platforms:
  - Windows
techniques:
  - '[[Network Sniffing]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ece7d882-e168-44a2-abef-bf54ded71878
created_at: '2025-12-11T03:47:56.484Z'
updated_at: '2025-12-11T03:47:56.484Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1040]]'
---
# Launch PlayStation Now Application

## Summary

This procedure launches the PlayStation Now application to start its internal components, including the local WebSocket server and AGL Electron app, enabling discovery of network listeners and processes.

## Description

By running psnowlauncher.exe, the application spawns AGL.exe and binds a WebSocket server to localhost:1235. This is the initial step for analyzing and exploiting the application's vulnerabilities. The target environment is Windows with the application installed. Expected outcomes include identifying the server's port and associated processes.

## Requirements

1. Windows machine with PlayStation Now version 11.0.2 installed
2. Administrative access to run monitoring tools
3. Network monitoring tools like Process Monitor and netstat

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected process spawns from psnowlauncher.exe
- Use application whitelisting to restrict Electron-based apps

## Objectives

1. Initialize the vulnerable WebSocket server
2. Identify listening ports and processes
3. Prepare for traffic inspection and exploitation

## Instructions

### Step 1: Run the Application

**Context**: Launch the main executable to start all components.

Launch psnowlauncher.exe from its installation directory.

> This spawns AGL.exe and starts the WebSocket server at localhost:1235.

### Step 2: Verify Network Listeners

**Context**: Use [[commands/netstat-anb]] to confirm the WebSocket server is running.

**Command** ([[commands/netstat-anb]]):
```bash
netstat -anb
```

> Look for psnowlauncher.exe bound to port 1235 in the output.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques



## Commands Used

- [[commands/netstat-anb]]

## Tools Used

- [[tools/Process-Monitor]]
- #netstat

## Tags

- [[Discovery]]
- [[commands/websocket-seturl-example]]
