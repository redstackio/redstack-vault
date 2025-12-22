---
tags:
  - rce
  - trigger
  - windows
  - openssl
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/trigger-openssl-tls]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:26:17.495Z'
sub_techniques: []
id: de896801-037b-425f-a90e-a59e38f7f2da
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Hijack Execution Flow]]'
---
# Trigger OpenSSL Usage to Execute Malicious Code

## Summary

This procedure forces an application using vulnerable OpenSSL to load the tampered configuration, resulting in the execution of the malicious engine DLL for arbitrary code execution.

## Description

When OpenSSL initializes (e.g., during TLS operations), it reads openssl.cnf from OPENSSLDIR and loads specified engines. With the injected config, this triggers DLL execution in the process context, enabling RCE and potential escalation to SYSTEM in services like Apache or VPNs.

## Requirements

1. Vulnerable application/service running with OpenSSL
2. Malicious config and DLL in place
3. Ability to interact with or restart the application

## Defense

Defensive measures and detection strategies:

- Run services under least privilege; isolate OpenSSL configs
- Log OpenSSL engine loads and monitor for anomalous DLLs (e.g., via ETW)
- Use sandboxing or containerization for OpenSSL-dependent apps

## Objectives

1. Invoke OpenSSL to read malicious config
2. Execute payload for RCE
3. Escalate privileges if in service context

## Instructions

### Step 1: Trigger TLS Operation

**Context**: Initiate an OpenSSL call, such as a TLS connection, to load the config.

**Command** ([[commands/trigger-openssl-tls]]):
```cmd
openssl s_client -connect localhost:443
```

> For testing; in real scenarios, connect to the service (e.g., browser to HTTPS site) or restart service with net start. Payload executes on load.

### Step 2: Monitor Execution

**Context**: Verify RCE by checking for payload effects (e.g., spawned process).

**Command** (built-in tasklist):
```cmd
tasklist /fi "imagename eq cmd.exe"
```

> If payload spawns cmd.exe, success; indicates code execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell
- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used

- [[commands/trigger-openssl-tls]]

## Tools Used


## Tags

- [[rce]]
- [[trigger]]
- [[openssl]]
