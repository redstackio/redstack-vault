---
id: proc-637840-003
tags:
  - path-traversal
  - mariadb
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-dlopen-sh]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:26:06.596Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
---
# Trigger-dlopen-via-Malicious-Server-Connection

## Summary

This procedure connects the MariaDB client to a malicious server that specifies a traversed plugin path, triggering dlopen of an arbitrary file and executing init/fini code if present.

## Description

During the connection handshake, the server sends the crafted path, causing the client to invoke dlopen without validation. If the traversed file exists, it's loaded as a library, running init/fini functions for code execution. This exploits the client's trust in server-provided paths. Side effect includes potential dialog plugin abuse for password prompts.

## Requirements

1. Malicious MariaDB server configured to send custom plugin paths
2. MariaDB client on victim machine
3. Controlled file at traversed location

## Defense

Defensive measures and detection strategies:

- Disable dynamic plugin loading or whitelist paths
- Use client-side firewalls to restrict connections
- Monitor process memory for unexpected library loads

## Objectives

1. Initiate connection to malicious server
2. Trigger dlopen with malicious path
3. Achieve code execution via loaded library

## Instructions

### Step 1: Configure Malicious Server

**Context**: Set server to respond with malicious plugin path during handshake.

No specific command; modify server config or use custom handler:

> Server specifies path like the crafted one from previous procedure.

### Step 2: Connect Client and Trigger

**Context**: Run client connection to invoke dlopen.

Execute [[commands/execute-dlopen-sh]] to simulate:

```bash
./dlopen.sh
```

> Upon connection, dlopen attempts the traversed path; success loads file and prints init/fini if executed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

### Sub-Techniques


## Commands Used

- [[commands/execute-dlopen-sh]]

## Tools Used


## Tags

- path-traversal
- mariadb
- dlopen-trigger
