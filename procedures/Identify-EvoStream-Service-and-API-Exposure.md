---
id: proc-evostream-identify
tags:
  - recon
  - service-discovery
  - evostream
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/netstat-listen]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:30:58.569Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Identify-EvoStream-Service-and-API-Exposure

## Summary

This procedure identifies the EvoStream service in Ubiquiti UniFi Video, which runs as SYSTEM and exposes an unauthenticated API on localhost:7440, setting the stage for command injection exploitation.

## Description

The EvoStream service (evostream.exe) is part of UniFi Video and binds to localhost:7440 without authentication. Analyzing this local service reveals the launchprocess endpoint, allowing arbitrary command execution. This is a reconnaissance step for local privilege escalation or remote exploitation via SSRF.

## Requirements

1. Local access to the target Windows system with user privileges
2. Basic networking tools like netstat available
3. UniFi Video installed and running

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized local service queries on port 7440
- Restrict UniFi Video to non-SYSTEM execution if possible
- Use endpoint detection to alert on evostream.exe process inspection

## Objectives

1. Confirm EvoStream service presence and privileges
2. Verify API exposure on localhost:7440
3. Identify potential for unauthenticated access

## Instructions

### Step 1: Check Listening Ports

**Context**: Use netstat to identify services bound to localhost:7440.

**Command** ([[commands/netstat-listen]]):
```bash
netstat -ano | findstr :7440
```

> This command lists processes listening on port 7440. Expected output includes evostream.exe PID. Cross-reference PID with Task Manager to confirm SYSTEM privileges.

### Step 2: Verify API Endpoint

**Context**: Test the API without authentication by referencing documentation or sending a basic request.

**Command** ([[commands/curl-api-test]]):
```bash
curl -X POST http://localhost:7440/jsonrpc -d '{"jsonrpc": "2.0", "method": "launchprocess", "params": {"appName":"test"}, "id": 1}'
```

> Sends a test JSON-RPC request to the launchprocess method. Successful response indicates unauthenticated access; error or no auth prompt confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/netstat-listen]]
- [[commands/curl-api-test]]

## Tools Used


## Tags

- recon
- service-discovery
