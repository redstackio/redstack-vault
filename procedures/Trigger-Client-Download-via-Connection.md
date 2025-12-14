---
tags:
  - client-trigger
  - rce-execution
type: procedure
tools: []
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
updated_at: '2025-12-14T05:32:10.354Z'
sub_techniques: []
id: b431a074-a1a3-4f82-aad9-abca8053000a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Client-Download-via-Connection

## Summary

This procedure involves a client connecting to the exploited server, triggering the download and eventual loading of the malicious DLL for remote code execution.

## Description

Upon connection, CL_BatchResourceRequest processes the queued eventscript, downloading via HTTP (bypassing CL_CheckFile's weak checks). The DLL lands in the mod folder and loads on restart via client.dll's Initialize. Prerequisites: Server configured and queued, victim client. Outcome: RCE on client, potential malware spread.

## Requirements

1. Vulnerable GoldSource client (build 7960)
2. Network connectivity to server
3. Malicious DLL hosted

## Defense

Defensive measures and detection strategies:

- Avoid connecting to untrusted game servers
- Monitor client downloads for unexpected files
- Implement full IsSafeFileToDownload in CL_CheckFile for all types

## Objectives

1. Initiate resource batch request on connect
2. Download and place DLL in mod folder
3. Achieve execution on game restart

## Instructions

### Step 1: Client Connects to Server

**Context**: Victim launches game and joins the server, starting the download process.

**Command**:
No command; game client action.

> In-game: Connect via console `connect server_ip:port`. Expected output: Connection successful, resource requests sent.

### Step 2: Verify Download and Load

**Context**: Post-connection, check for DLL placement and restart to trigger load.

**Command**:
No command; observe filesystem.

> DLL appears in mod/bin/. Restart game: Payload executes via client.dll. Success: RCE indicators like process injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- client-trigger
- rce-execution
