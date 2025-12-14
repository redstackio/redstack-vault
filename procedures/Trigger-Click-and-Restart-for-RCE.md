---
id: proc-trigger-click-rce
tags:
  - rce
  - jvm
  - file-write
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:28:12.937Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[PowerShell]]'
---
# Trigger-Click-and-Restart-for-RCE

## Summary

This procedure captures a user click via clickjacking to trigger XSS payload, downloading a malicious user.vmoptions file, and restarts Burp Suite to execute arbitrary OS commands via JVM OOM handler.

## Description

The click on the overlaid button sends a compromised request via the WebSocket, exploiting XSS to download and write user.vmoptions to Burp's app directory. The file sets -Xmx5m (low heap) and -XX:OnOutOfMemoryError='open -a Calculator' (macOS command to launch Calculator). Restarting Burp causes immediate OOM, triggering the command with user privileges. This achieves RCE without direct code injection.

## Requirements

1. Clickjacking payload rendered
2. Burp Suite installed at /Applications/Burp Suite Professional.app/
3. User permissions to write to app contents and restart Burp

## Defense

Defensive measures and detection strategies:

- Validate and sandbox file writes to application directories
- Disable or validate JVM flags like OnOutOfMemoryError
- Monitor for unexpected file modifications in Burp dir (e.g., integrity checks)

## Objectives

1. Write malicious JVM options via exploited websocket
2. Induce OOM on restart for command execution
3. Demonstrate RCE with user-level privileges

## Instructions

### Step 1: Perform Click and Download Payload

**Context**: Click the button to trigger the XSS-mediated file download.

**Command** (JS-triggered; no CLI):
Click 'CLICK ME!!!'; JS executes fetch/write via debugging API.

> Expected output: user.vmoptions created with malicious flags. Verify: ls /Applications/Burp\ Suite\ Professional.app/Contents/user.vmoptions

### Step 2: Restart Burp Suite

**Context**: Quit and relaunch Burp to trigger OOM and command.

**Command** (Manual):
Quit Burp via UI or kill process; relaunch from Applications.

> Expected output: Burp starts, hits OOM, launches Calculator. Success if app opens without full Burp load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[PowerShell]] PowerShell (adapted for macOS shell command)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- rce
- jvm
- file-write
