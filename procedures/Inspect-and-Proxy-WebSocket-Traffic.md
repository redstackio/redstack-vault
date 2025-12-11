---
tags:
  - proxy
  - inspection
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
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 23ac8f07-6cf9-44c3-a837-5476417d9b8a
created_at: '2025-12-11T06:10:30.657Z'
updated_at: '2025-12-11T06:10:30.657Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1040]]'
---
# Inspect and Proxy WebSocket Traffic

## Summary

This procedure sets up proxying for WebSocket traffic to analyze communications in the PlayStation Now app, identifying vulnerabilities like missing Origin checks.

## Description

Using Burp Suite, intercept and inspect WebSocket messages to and from localhost:1235, revealing commands that can load arbitrary URLs in the AGL app.

## Requirements
1. Burp Suite installed and configured
2. Running PlayStation Now application
3. Local access to configure proxy

## Defense

- Implement strict Origin checks on WebSocket servers
- Use network monitoring for anomalous local traffic

## Objectives
1. Capture WebSocket messages
2. Identify URL loading commands
3. Confirm lack of Origin validation

## Instructions

### Step 1: Configure Proxy

Set up Burp Suite to proxy local WebSocket traffic on localhost:1235 using [[commands/burp-proxy-setup]]:

```bash
# Launch Burp Suite and configure proxy listener for localhost
```

### Step 2: Generate and Inspect Traffic

Interact with the app to generate WebSocket communications, then review messages in Burp Suite's WebSocket history.

> Look for commands that instruct AGL to load URLs.

## MITRE ATT&CK Mapping

### Tactics
- [[Discovery]]

### Techniques
- [[Network Sniffing]]

### Sub-Techniques

## Commands Used
- [[commands/burp-proxy-setup]]

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- proxy
- inspection
