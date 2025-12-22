---
id: proc-2
tags:
  - csgo
  - info-leak
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/connect-to-csgo-server]]'
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:54.652Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Client-Download-and-Info-Leak-via-Curl

## Summary

This procedure induces the CS:GO client to connect to the malicious server and download files, exploiting curl's case-sensitive header parsing to leak uninitialized heap memory into downloaded files.

## Description

Upon connection, the client parses the server's .res file and uses curl to fetch listed resources. The exploit crafts responses where the first 'Content-Length' allocates a buffer, but a lowercase 'content-length: 0' causes curl to write nothing, leaving the buffer with heap garbage which is blindly written to disk.

## Requirements

1. Running malicious server from prior procedure
2. Victim CS:GO client with console enabled
3. Network connectivity to attacker IP

## Defense

- Validate HTTP response consistency in client downloads
- Sanitize or reject responses with duplicate headers
- Log and alert on zero-byte downloads

## Objectives

1. Force client to perform vulnerable downloads
2. Generate files containing leaked memory
3. Maintain stable connection for further steps

## Instructions

### Step 1: Connect Client to Server

**Context**: Victim uses in-game console to join the malicious server, triggering automatic downloads.

**Command** ([[commands/connect-to-csgo-server]]):
```bash
connect YOUR_IP:1337
```
(Entered in CS:GO developer console)

> Connects the client to the server at specified IP and port. Expected output: Client loads map, downloads files, and joins without errors; leaked files appear in client directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- [[commands/connect-to-csgo-server]]

## Tools Used

- [[tools/curl]]

## Tags

- csgo
- info-leak
- curl
