---
tags:
  - proxy
  - traffic-analysis
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
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 08d1252b-f9d1-456d-b701-488c7e8bb6d4
created_at: '2025-12-11T03:47:56.481Z'
updated_at: '2025-12-11T03:47:56.481Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1040]]'
---
# Proxy Application Traffic for Inspection

## Summary

This procedure configures a system proxy and uses Burp Suite to intercept and analyze traffic between PlayStation Now components, focusing on WebSocket communications.

## Description

Setting up a proxy allows inspection of HTTP and WebSocket traffic from QAS and AGL, identified by specific User-Agent headers. This is crucial for understanding command structures. The environment requires Windows proxy settings and Burp Suite with CA installed.

## Requirements

1. Burp Suite installed and running on 127.0.0.1:8080
2. Request Highlighter extension for Burp
3. Access to Windows Internet Properties

## Defense

Defensive measures and detection strategies:

- Monitor proxy configuration changes
- Detect unusual traffic to localhost ports

## Objectives

1. Intercept application traffic
2. Highlight and analyze requests by User-Agent
3. Prepare for WebSocket testing

## Instructions

### Step 1: Configure System Proxy

**Context**: Open Internet Properties to set LAN proxy.

**Command** ([[commands/control-exe-inetcpl-cpl-4]]):
```bash
control.exe inetcpl.cpl,,4
```

> Set proxy to 127.0.0.1:8080.

### Step 2: Install Burp CA and Highlight Requests

**Context**: Add Burp CA to certificate store and configure Request Highlighter.

Highlight based on User-Agents: 'gkApollo', 'QtWebEngine/5.5.1', 'Electron/1.4.16'.

> Use Burp Suite to inspect proxied traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques



## Commands Used

- [[commands/control-exe-inetcpl-cpl-4]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Request-Highlighter]]

## Tags

- #proxy
- #traffic-analysis
