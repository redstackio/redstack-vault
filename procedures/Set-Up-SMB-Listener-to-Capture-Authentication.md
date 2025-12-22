---
id: proc-uuid-2
name: Set-Up-SMB-Listener-to-Capture-Authentication
tags:
  - smb
  - listener
  - capture
type: procedure
tools:
  - '[[tools/Impacket]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/impacket-smbserver-listen]]'
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T03:46:09.064Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Set-Up-SMB-Listener-to-Capture-Authentication

## Summary

This procedure sets up an SMB server to listen for incoming connections from the target server during SSRF exploitation, capturing NTLMv2 authentication attempts including domain credentials and hashes.

## Description

Once the SSRF is triggered, the target server attempts to access the UNC path over SMB, sending its credentials in NTLMv2 format. Using a tool like Impacket's smbserver, the attacker can log these auth attempts, enabling hash capture for cracking or relay.

## Requirements

1. Attacker machine with public IP or reachable by target
2. Impacket toolkit installed
3. Port 445 open on attacker firewall

## Defense

Defensive measures and detection strategies:

- Firewall rules to block outbound SMB from web/app servers
- Enable SMB signing and restrict NTLM usage
- Log and alert on anomalous SMB traffic from internal servers

## Objectives

1. Intercept server authentication during SSRF
2. Capture NTLMv2 hashes
3. Prepare for offline cracking or relay

## Instructions

### Step 1: Start SMB Server Listener

**Context**: Launch a fake SMB share to receive connections and log auth data.

**Command** ([[commands/impacket-smbserver-listen]]):

```bash
impacket-smbserver share . -smb2support -debug
```

> This creates a share named 'share' in the current directory, supports SMB2, and enables debug logging to capture incoming auth.

### Step 2: Monitor for Connections

**Context**: Watch logs for target server's connection and auth attempt post-SVG upload.

No command; tail the output or logs:

```bash
tail -f smbserver.log
```

> Look for lines showing NTLMv2 challenge-response from the target's domain (e.g., TAKETWO).

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and SMB Relay (adapted for capture)

## Commands Used

- [[commands/impacket-smbserver-listen]]

## Tools Used

- [[tools/Impacket]]

## Tags

- smb
- listener
- ntlmv2
