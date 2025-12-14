---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - rce
  - script-injection
  - persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Network Device
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:31:19.072Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Achieve-RCE-via-Startup-Scripts

## Summary

This procedure uses administrative access on the Cisco TelePresence SX80 to inject custom startup scripts via the web interface, enabling remote code execution for persistence, data interception, or backdoor establishment in video conference sessions.

## Description

With admin privileges, the SX80's script management allows adding executable code that runs on device startup or during operations. This can include commands for logging keystrokes, intercepting SIP/UDP traffic, or executing shell-like instructions. In DoD contexts, this compromises sensitive communications. The vulnerability stems from lack of input sanitization in the script endpoint.

## Requirements

1. Valid admin session from prior authentication
2. Access to https://███████/web/scripts endpoint
3. Knowledge of SX80 scripting syntax for code injection

## Defense

Defensive measures and detection strategies:

- Disable or restrict script addition in device config
- Audit script logs and changes via centralized monitoring
- Use endpoint detection to flag unauthorized code execution on network devices

## Objectives

1. Inject persistent scripts for RCE
2. Intercept conference data
3. Establish backdoor for ongoing access

## Instructions

### Step 1: Access Script Management

**Context**: Navigate to the admin section for script control.

From the dashboard, go to configuration > scripts or directly to https://███████/web/scripts.

> The interface should allow uploading or editing startup scripts.

### Step 2: Inject Custom Script

**Context**: Add arbitrary code to execute on startup.

Enter script content (e.g., commands to run a reverse shell or log traffic) and save.

> Scripts execute automatically; test by rebooting the device to confirm RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- script-injection
- persistence
