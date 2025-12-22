---
id: proc-002
tags:
  - error-trigger
  - network-interrupt
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:24:56.717Z'
skill_level: beginner
impact_level: informational
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Trigger-Error-via-Connection-Drop

## Summary

This procedure describes interrupting a network connection during interaction with a web lab to trigger an error message that discloses internal Node.js application code.

## Description

Error handling in web applications, particularly those built with Node.js, can inadvertently expose sensitive information if not properly sanitized. In this scenario, a connection drop during an active session causes the server to return a detailed error stack trace, revealing source code snippets, file paths, and application logic. This is common in development or lab environments lacking production-level error obfuscation. The technique relies on transient network failures to bypass normal response paths.

## Requirements

1. Active lab session from prior access
2. Ability to interrupt network (e.g., Wi-Fi toggle or cable unplug)
3. Browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize error messages to remove code traces
- Use custom error pages in production
- Log connection drops for anomaly detection

## Objectives

1. Provoke an unhandled error condition
2. Expose internal application details
3. Collect evidence of disclosure

## Instructions

### Step 1: Initiate Interaction

**Context**: Perform an action in the lab to establish an ongoing request.

Submit a form, load a resource, or navigate within the lab to create an active connection.

> Expected output: Request sent, awaiting response.

### Step 2: Interrupt Connection

**Context**: Drop the network to force an error on the server side.

Enable airplane mode, disconnect Wi-Fi, or use network throttling tools to simulate a drop. Wait 5-10 seconds before restoring.

> Expected output: Browser displays a server error page with Node.js stack trace, including code lines.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- error-trigger
- network-interrupt
