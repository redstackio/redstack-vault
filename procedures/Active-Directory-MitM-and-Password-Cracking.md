---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - >-
    [[techniques/Use-Alternate-Authentication-Material-Pass-the-Hash|T1550.002 -
    Use Alternate Authentication Material: Pass the Hash]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
  - ntlm-relay
  - hash-cracking
commands:
  - '[[commands/responder-capture-ntlm-hashes]]'
  - '[[commands/hashcat-crack-netntlmv2]]'
platforms:
  - Windows
tools:
  - '[[tools/Responder]]'
  - '[[tools/Hashcat]]'
verified: true
validated: true
---

# Active-Directory-MitM-and-Password-Cracking

## Summary

This procedure outlines how to conduct a Man-in-the-Middle (MitM) attack in an Active Directory environment by poisoning name resolution protocols to relay NTLM authentication and capture NetNTLMv2 hashes, followed by offline cracking of those hashes using Hashcat to recover plaintext passwords for further exploitation.

## Description

Active Directory relies on NTLM for authentication in legacy or misconfigured environments, making it vulnerable to relay attacks. An attacker positions themselves on the network to intercept authentication attempts, typically by poisoning LLMNR or NBT-NS queries when victims try to access non-existent resources like SMB shares. Tools like Responder facilitate this by responding to poisoned queries and capturing the resulting NetNTLMv2 hashes during the authentication challenge-response. Once captured, these hashes are resistant to direct replay in modern setups but can be cracked offline using high-performance tools like Hashcat with dictionary or rule-based attacks. Success depends on weak passwords and large wordlists. This technique enables credential theft for lateral movement, privilege escalation, or access to domain resources, particularly effective in Windows domains without SMB signing enforced.

## Requirements

1. Layer 2 network access to the target AD environment (same subnet as victims and domain controllers).
2. Administrative privileges on the attacker's machine for running poisoning tools.
3. Responder installed for hash capture and Hashcat for cracking.
4. A comprehensive wordlist (e.g., crackstation.txt) and optionally rules for enhanced cracking.
5. Captured hashes in a format compatible with Hashcat (e.g., from Responder logs).

## Defense

- Enforce SMB signing and disable NTLM where possible, favoring Kerberos.
- Disable LLMNR and NBT-NS via Group Policy; rely solely on DNS for name resolution.
- Implement strong password policies, account lockouts, and monitor for anomalous authentication patterns using tools like Microsoft ATA.
- Use network segmentation, EDR solutions to detect poisoning tools, and enable Protected Users group to limit hash usability.

## Objectives

1. Intercept and capture NTLM authentication hashes via relay.
2. Crack captured NetNTLMv2 hashes to obtain plaintext credentials.
3. Enable use of recovered credentials for domain compromise or escalation.

## Instructions

### Step 1: Capture NTLM Hashes via Relay

**Context**: Deploy Responder to poison LLMNR, NBT-NS, and MDNS queries on the network, tricking victims into authenticating to the attacker's machine and capturing their NetNTLMv2 hashes when they attempt resource access (e.g., typing a wrong share name in Explorer).

**Command** ([[commands/responder-capture-ntlm-hashes]]):
```bash
responder -I $_INTERFACE -w -r -d
```

> Run this on the attacker's interface connected to the target network. The -w enables WPAD poisoning, -r for NBT-NS relay, -d for MDNS. Monitor the console for poisoned requests. Hashes are saved to /usr/share/responder/logs/ as .txt files in the format username::domain:challenge:hash:...

**Expected Output**: Console logs like "[LLMNR] Poisoned answer sent to <IP> for name <query>" and captured hashes in log files, e.g., "JDOE::DOMAIN:1122334455667788:ABCDEF0123456789ABCDEF0123456789:0102030405060708:::".

### Step 2: Crack Captured NetNTLMv2 Hashes

**Context**: Load the captured hashes into Hashcat and perform a dictionary attack to brute-force potential passwords. This step assumes hashes are extracted into a single file (e.g., via Responder's output parser or manual copy).

**Command** ([[commands/hashcat-crack-netntlmv2]]):
```bash
hashcat -m 5600 -a 0 $_HASH_FILE $_WORDLIST
```

> Extract hashes from Responder logs into $_HASH_FILE (one per line). Use -m 5600 for NetNTLMv2, -a 0 for dictionary mode. If no success, add -r rules.txt for mutations or switch to -a 3 for brute-force. Monitor GPU/CPU usage for progress.

**Expected Output**: Progress bar showing attempts, and upon success: "<hash>:password" lines, e.g., "JDOE::DOMAIN:...:MyWeakPass123". Use --show to list all cracked if session restored.
