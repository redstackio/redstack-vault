---
id: 91166105-7aa7-4e3c-a0e2-6d5fcab3044e
name: SMB Relay Attack via Disabled SMB Signing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.372255+00:00'
updated_at: '2023-04-10T20:26:21.811002+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Windows Admin Shares|T1077 - Windows Admin Shares]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[SMB Signing Disabled and IPv4]]'
commands:
- '[[Check if SMB signing is enabled]]'
- '[[Enable SMB signing]]'
- '[[Enumerate Targets]]'
- '[[Exploit]]'
---

# SMB Relay Attack via Disabled SMB Signing

## Summary

A SMB relay attack is a type of man-in-the-middle attack that allows an attacker to intercept and relay SMB authentication requests to gain access to a target system. This specific attack targets systems with SMB signing disabled and IPv4 enabled. The attacker can use the SMB Signing Command to che

## Description

# Description

A SMB relay attack is a type of man-in-the-middle attack that allows an attacker to intercept and relay SMB authentication requests to gain access to a target system. This specific attack targets systems with SMB signing disabled and IPv4 enabled. The attacker can use the SMB Signing Command to check if SMB signing is disabled and then use the Disable Command to disable it. Once SMB signing is disabled, the attacker can use the NTLMv2 Hashes Relay Attack to relay authentication requests to a target system and gain access to sensitive resources.

This attack can be used to gain access to sensitive information, such as user credentials, and to move laterally within a network.

## Requirements

1. Access to a network with SMB signing disabled and IPv4 enabled

1. Tools for SMB relay attacks, such as Responder or Inveigh

## Defense

1. Enable SMB signing to prevent SMB relay attacks

1. Use IPsec to secure SMB traffic

1. Monitor network traffic for signs of SMB relay attacks

## Objectives

1. Gain access to sensitive information

1. Move laterally within a network

# Instructions

1. To enable SMB signing, run the following command: 

Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" RequireSecuritySignature -Value 1

To disable SMB signing, run the following command: 

Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" RequireSecuritySignature -Value 0

**Code**: [[SMB signing]]

> SMB signing is a security mechanism in the SMB protocol that ensures the authenticity of the sender and receiver of a message. When SMB signing is enabled, a digital signature is added to each SMB packet, which prevents attackers from tampering with the packet in transit. The command provided enables or disables SMB signing on a machine. The 'RequireSecuritySignature' parameter is set to 1 to enable SMB signing and 0 to disable it.

**Command** ([[Check if SMB signing is enabled]]):

```bash
Get-SmbServerConfiguration | Select-Object -ExpandProperty 'EnableSMBSigning'
```

**Command** ([[Enable SMB signing]]):

```bash
Set-SmbServerConfiguration -EnableSMBSigning $true
```

2. COMMANDS

**Code**: [[disabled]]

> This command disables multiple commands at once. To use this command, provide a list of the commands you want to disable separated by spaces after the 'COMMANDS' keyword. For example, 'COMMANDS command1 command2 command3'. The disabled commands will no longer be available for use until they are re-enabled.

3. To perform an NTLMv2 Hashes Relay Attack, follow these steps:
1. Set up a rogue SMB server using Responder.
2. Use the Multirelay.py script to relay authentication requests to a target system.
3. Capture the NTLMv2 hashes and crack them to obtain the plaintext password.

**Code**: [[NTLMv2 hashes relay]]

> This attack takes advantage of the fact that many systems still use the outdated NTLMv2 authentication protocol. By relaying authentication requests from a target system to a rogue SMB server, an attacker can capture the NTLMv2 hashes and crack them to obtain the plaintext password. This attack can be particularly effective in environments where users have local administrator privileges on their machines, as the stolen credentials can be used to move laterally through the network and gain access to sensitive resources.

**Command** ([[Enumerate Targets]]):

```bash
nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args smbuser='Guest',smbpass='' -oN nmap.txt 192.168.0.0/24
```

**Command** ([[Exploit]]):

```bash
ntlmrelayx.py -tf targets.txt -smb2support
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Windows Admin Shares|T1077 - Windows Admin Shares]]

## Commands Used

- [[Check if SMB signing is enabled]]
- [[Enable SMB signing]]
- [[Enumerate Targets]]
- [[Exploit]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[SMB Signing Disabled and IPv4]]
