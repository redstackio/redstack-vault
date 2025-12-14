---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567896
tags:
  - rce-trigger
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:32.337Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Trigger-RCE-by-Saving-Configuration

## Summary

This procedure saves the misconfigured AV path, invoking the plugin's scanning mechanism to execute the chained PHP shell command, achieving remote code execution on the server.

## Description

Upon saving in Protection settings, the files_antivirus plugin validates the AV path by attempting shell execution, running the PHP interpreter on the uploaded file. This leads to RCE, allowing arbitrary commands, data exfiltration, or lateral movement. Errors in scanning are ignored, but execution succeeds in ownCloud 10.4.1.3.

## Requirements

1. Malicious AV path configured
2. Uploaded PHP payload in place
3. Admin session active

## Defense

Defensive measures and detection strategies:

- Implement safe configuration saving with path execution sandboxing
- Monitor shell executions from web processes via auditd or SELinux
- Alert on AV scan failures or unusual command invocations

## Objectives

1. Invoke shell execution via plugin mechanism
2. Run arbitrary PHP code on server
3. Confirm RCE with payload output

## Instructions

### Step 1: Save Configuration

**Context**: Commit the AV path changes to trigger validation.

Click the Save button in Protection settings.

> The plugin executes the path immediately. Expected output: Possible scan error message, but PHP code runs in background.

### Step 2: Verify Execution

**Context**: Interact with the PHP shell to confirm RCE.

If the payload is a web shell, access it via URL with ?cmd=whoami or similar; check server logs for execution evidence.

> Output like user id or system info indicates success. For non-web shells, monitor server for effects.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce-trigger
- execution
