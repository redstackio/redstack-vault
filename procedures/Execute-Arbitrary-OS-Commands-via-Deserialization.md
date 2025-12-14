---
id: p4b2c3d4-e5f6-7890-abcd-ef1234567894
name: Execute-Arbitrary-OS-Commands-via-Deserialization
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.105Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - rce
  - command-execution
  - compromise
platforms:
  - Windows
tools:
  - '[[tools/ysoserial.net]]'
commands:
  - '[[commands/curl-inject-deserialization-payload]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---

# Execute-Arbitrary-OS-Commands-via-Deserialization

## Summary

This procedure leverages the deserialization RCE to run arbitrary operating system commands, enabling file operations, data exfiltration, and full system compromise on the Sitecore server.

## Description

Once the payload is deserialized, the gadget chain executes commands in the context of the web application process, typically under IIS on Windows. This allows attackers to create/read/exfiltrate files, install backdoors, or escalate privileges. The procedure builds on prior injection, iterating payloads for different commands. Target is .NET/Sitecore on Windows servers. Expected outcomes: Persistent access and data theft.

## Requirements

1. Successful initial RCE confirmation
2. ysoserial.net for payload customization
3. Secondary channel for exfiltration (e.g., HTTP response or DNS)

## Defense

Defensive measures and detection strategies:

- Run web apps under least-privilege accounts
- Enable process monitoring for unexpected command spawns
- Implement file integrity monitoring for sensitive directories

## Objectives

1. Execute commands for reconnaissance (e.g., whoami)
2. Perform file operations and exfiltration
3. Establish persistence or escalate access

## Instructions

### Step 1: Generate Command-Specific Payload

**Context**: Update the ysoserial command for desired OS actions.

Use [[tools/ysoserial.net]] to create a payload like "type C:\Windows\win.ini > exfil.txt".

### Step 2: Inject and Execute

**Context**: Re-inject the new payload to run the command.

Execute [[commands/curl-inject-deserialization-payload]] with the updated base64:

```bash
curl -H "ThumbnailsAccessToken: $(cat newpayload.b64)" https://target-sitecore.com/api/thumbnails
```

> Expected output: Command runs; for exfil, modify payload to send data back via response or beacon.

### Step 3: Verify Compromise

**Context**: Check for effects like new files or network activity.

If payload includes reverse shell, listen on attacker machine.

> Success: File created or data received.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-deserialization-payload]]

## Tools Used

- [[tools/ysoserial.net]]

## Tags

- [[rce]]
- [[command-execution]]
- [[compromise]]
