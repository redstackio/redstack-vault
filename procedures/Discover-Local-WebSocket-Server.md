---
tags:
  - discovery
  - websocket
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/netstat]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/netstat-check-ports]]'
  - '[[commands/burp-proxy-setup]]'
platforms:
  - Windows
techniques:
  - '[[Network Sniffing]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 78c38b8f-71f6-4b1d-9f81-da18eb900f13
created_at: '2025-12-11T06:10:30.660Z'
updated_at: '2025-12-11T06:10:30.660Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1040]]'
---
# Discover Local WebSocket Server

## Summary

This procedure involves installing and running the PlayStation Now application to expose and identify the local WebSocket server listening on localhost:1235, using process monitoring and port checking tools.

## Description

By executing the PlayStation Now launcher, the AGL Electron app is spawned, starting a WebSocket server without Origin checks. This procedure uses tools to confirm the server's presence and port, setting the stage for further exploitation.

## Requirements
1. Windows machine with internet access for downloading the app
2. Administrative privileges to install and run the application
3. Installed tools: Process Monitor and netstat

## Defense

- Monitor for unexpected local servers using endpoint detection tools
- Disable unnecessary local services in applications

## Objectives
1. Confirm WebSocket server is running
2. Identify listening port and associated process
3. Gather details for traffic inspection

## Instructions

### Step 1: Install and Run Application

Download from https://download-psnow.playstation.com/downloads/psnow/pc/latest and execute C:\Program Files (x86)\PlayStationNow\psnowlauncher.exe.

> This spawns AGL and starts the server.

### Step 2: Check Listening Ports

Execute [[commands/netstat-check-ports]] to verify:

```bash
netstat -anb
```

> Look for localhost:1235 bound to psnowlauncher.exe.

### Step 3: Monitor Processes

Use [[tools/Process-Monitor]] to observe process creation and network activity related to the WebSocket server.

## MITRE ATT&CK Mapping

### Tactics
- [[Discovery]]

### Techniques
- [[Network Sniffing]]

### Sub-Techniques

## Commands Used
- [[commands/netstat-check-ports]]

## Tools Used
- [[tools/Process-Monitor]]
- [[tools/netstat]]

## Tags
- discovery
- websocket
