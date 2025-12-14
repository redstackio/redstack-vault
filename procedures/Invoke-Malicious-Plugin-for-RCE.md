---
tags:
  - rce
  - command-execution
  - system-enumeration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/whoami-root-check]]'
  - '[[commands/cat-etc-passwd]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:24.849Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 43c1d1ba-47f1-4561-8718-2474d0fe58f3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Invoke-Malicious-Plugin-for-RCE

## Summary

This procedure invokes the installed malicious plugin in Atlassian Crowd to trigger remote code execution as root, executing commands like 'whoami' and 'cat /etc/passwd' to demonstrate privileges and enumerate users.

## Description

After upload, the rce.jar plugin exposes a servlet at /crowd/plugins/servlet/hackerone-cdl. Accessing this endpoint runs embedded commands on the server as root, exploiting the RCE. This targets Linux-based Crowd on Tomcat, allowing file reads, command execution, and further attacks like credential theft or pivoting. Prerequisites: Successful plugin installation from prior step.

## Requirements

1. Installed malicious plugin on target
2. Network access to https://target/crowd/plugins/servlet/hackerone-cdl
3. Browser or curl for invocation

## Defense

Defensive measures and detection strategies:

- Remove or secure custom servlets post-installation
- Monitor access to /plugins/servlet/ paths and anomalous command executions
- Use runtime application self-protection (RASP) to block unauthorized code execution

## Objectives

1. Trigger RCE via servlet access
2. Verify root privileges with whoami
3. Enumerate users via /etc/passwd read

## Instructions

### Step 1: Access Plugin Endpoint

**Context**: Invoke the servlet to activate the malicious code, which automatically runs commands to prove RCE.

No direct command; use browser to visit https://target/crowd/plugins/servlet/hackerone-cdl or curl GET request.

> This triggers the plugin. Expected output: Page displaying results of executed commands.

### Step 2: Execute Whoami Command

**Context**: The plugin runs [[commands/whoami-root-check]] to confirm root execution context.

The plugin executes:

```bash
whoami
```

> Displays the executing user. Expected output: 'root'.

### Step 3: Read /etc/passwd

**Context**: The plugin runs [[commands/cat-etc-passwd]] for system enumeration, listing users for further targeting.

The plugin executes:

```bash
cat /etc/passwd
```

> Outputs user database. Expected output: Lines like 'root:x:0:0:root:/root:/bin/bash', 'ec2-user:x:500:500:EC2 Default User:/home/ec2-user:/bin/bash'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/whoami-root-check]]
- [[commands/cat-etc-passwd]]

## Tools Used


## Tags

- rce
- command-execution
