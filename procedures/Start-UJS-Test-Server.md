---
tags:
  - server
  - setup
type: procedure
tools:
  - '[[tools/rake]]'
  - '[[tools/Puma]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rake-ujs-server]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 390cf9ec-ab00-460b-b9f1-db8cc2401f6f
created_at: '2025-12-13T09:01:16.899Z'
updated_at: '2025-12-13T09:01:16.899Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start UJS Test Server

## Summary

This procedure launches the UJS test server using Rake, exposing the vulnerable /echo endpoint for exploitation.

## Description

The Rake task starts Puma on port 4567, creating a local web server that renders user input without sanitization, enabling SSTI attacks.

## Requirements

1. Dependencies installed
2. Rake and Puma available

## Defense

Defensive measures and detection strategies:

- Restrict test server exposure
- Monitor for unexpected server starts

## Objectives

1. Run the vulnerable server
2. Expose the /echo endpoint

## Instructions

### Step 1: Execute Rake Task

**Context**: Start the Puma server.

**Command** ([[commands/rake-ujs-server]]):
```bash
rake ujs:server
```

> Displays startup messages and binds to port 4567.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/rake-ujs-server]]

## Tools Used

- [[tools/rake]]
- [[tools/Puma]]

## Tags

- server
- setup
