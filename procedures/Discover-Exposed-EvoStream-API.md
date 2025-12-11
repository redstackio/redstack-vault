---
tags:
  - discovery
  - api-exposure
type: procedure
tools:
  - '[[tools/poc.py]]'
  - '[[tools/rce0923234.html]]'
  - '[[tools/unifi-video.Win7_x64.v3.10.7-beta.2_ee88ac.190725.1817.exe]]'
  - '[[tools/2019-04-21_17-47-17.mp4]]'
  - '[[tools/ubiq_rce.mp4]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/launchprocess-websocket]]'
platforms:
  - Windows
techniques:
  - '[[Network Sniffing]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9dc7ab80-7019-4c6b-b426-50231422b417
created_at: '2025-12-11T06:10:22.833Z'
updated_at: '2025-12-11T06:10:22.833Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1040]]'
---
# Discover Exposed EvoStream API

## Summary

This procedure involves identifying the exposed EvoStream API on localhost:7440 that allows unauthenticated command execution, primarily used for initial reconnaissance in privilege escalation attacks.

## Description

The EvoStream service in UniFi Video runs on Windows with SYSTEM privileges and exposes an API without access controls. This allows local users to discover and interact with commands like 'launchprocess' for arbitrary execution. The procedure targets localhost endpoints and reviews documentation for vulnerabilities.

## Requirements

1. Local access to the Windows machine running UniFi Video
2. WebSocket client or browser for testing
3. Access to EvoStream documentation

## Defense

Defensive measures and detection strategies:

- Monitor localhost traffic for unusual WebSocket connections
- Restrict service bindings to localhost and add authentication

## Objectives

1. Confirm API exposure and command support
2. Document available endpoints for further exploitation
3. Identify lack of authentication

## Instructions

### Step 1: Probe Localhost Endpoint

**Context**: Test connectivity to the EvoStream API on port 7440.

Use a WebSocket client to connect to ws://localhost:7440 and send test messages.

> Expect a response confirming the connection.

### Step 2: Review Documentation

**Context**: Analyze EvoStream docs for supported commands like 'launchprocess'.

Access official documentation to identify unauthenticated features.

> Note commands that allow binary execution with arguments.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- discovery
- api-exposure
