---
id: cdd9123c-25fb-43a7-9b6a-eadc3ccff0cf
name: SMB-Credential-Enumeration-for-SAMAccountName-Spoofing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.069604+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/AS-REP-Roasting|T1558.004 - AS-REP Roasting]]'
  - '[[techniques/Valid-Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/samAccountName spoofing]]'
  - '[[tags/credential enumeration]]'
commands:
  - '[[commands/crackmapexec-smb-nopac]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
validated: true
---

# SMB-Credential-Enumeration-for-SAMAccountName-Spoofing

## Summary

This procedure uses CrackMapExec to perform SMB credential enumeration via the NoPac module, targeting Active Directory environments to extract AS-REP hashes from users without Kerberos pre-authentication enabled. These hashes can be cracked offline to obtain plaintext passwords, enabling SAMAccountName spoofing attacks where an attacker creates a duplicate user account with the same samAccountName but a different SID to intercept authentication and impersonate privileged users, ultimately leading to privilege escalation and potential SYSTEM access on domain controllers.

## Description

In Active Directory, SAMAccountName spoofing exploits the fact that authentication can be influenced by matching usernames before SID resolution. By enumerating credentials via SMB using the NoPac technique (abusing Kerberos AS-REP roasting on accounts without pre-auth), attackers obtain crackable hashes. Once cracked, these credentials allow creation of spoofed accounts in a controlled domain or forest, bypassing access controls. This is particularly effective in multi-forest setups or misconfigured trusts. The target environment is typically Windows Server with Active Directory Domain Services (AD DS) exposed over SMB (port 445). Prerequisites include network access to the domain controller or member server and basic domain knowledge (e.g., usernames). Success enables lateral movement and escalation, but requires follow-on actions like hash cracking and account creation not covered here.

## Requirements

1. Network access to the target Windows machine (SMB port 445 open).
2. Valid domain context (e.g., known usernames or null sessions for anonymous enumeration).
3. CrackMapExec tool installed on the attacker's machine.
4. Optional: Wordlist for offline cracking of obtained hashes.

## Defense

- Enforce Kerberos pre-authentication on all user accounts to prevent AS-REP roasting.
- Monitor for anomalous Kerberos AS-REP requests and SMB connections from unauthorized sources using tools like Windows Event Logs (Event ID 4768) or SIEM.
- Implement least privilege for account creation and monitor for duplicate SAMAccountName attempts via auditing.
- Use network segmentation to limit SMB exposure and enable SMB signing.

## Objectives

1. Enumerate AS-REP hashes from target accounts via SMB using NoPac.
2. Obtain crackable credential material for offline analysis.
3. Enable subsequent SAMAccountName spoofing for user impersonation and privilege escalation.

## Instructions

### Step 1: Enumerate SMB Credentials with NoPac Module

**Context**: This step uses CrackMapExec's SMB module with the NoPac option to request Kerberos AS-REP responses without pre-authentication, targeting accounts vulnerable to roasting. It simulates a legitimate authentication attempt over SMB to dump hashes. Run this from a Linux-based attacker machine with domain visibility; use null credentials for initial probes or known low-priv creds for broader access. If successful, hashes are output in crackable format (e.g., Hashcat mode 18200).

**Command** ([[commands/crackmapexec-smb-nopac]]):
```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -M nopac
```

> This command probes the target IP for vulnerable accounts, requesting AS-REP tickets. Replace placeholders with actual values (e.g., null session: -u '' -p ''). The -M nopac flag triggers the NoPac module, which exploits the absence of pre-auth requirements. Expected output includes a list of vulnerable users and their AS-REP hashes if found. Verify by checking for 'ASREPRoastable' indicators. If no hashes are returned, the accounts may require pre-auth or the probe failed due to firewall rules—retry with valid creds or scan multiple hosts.

### Step 2: Verify and Prepare Hashes for Cracking

**Context**: After enumeration, validate the output hashes and prepare them for offline cracking. This step ensures the extracted material is usable for obtaining plaintext passwords needed for spoofing. Decision point: If hashes are obtained, export them to a file; otherwise, pivot to alternative enumeration methods like LDAP queries.

**Command** ([[commands/crackmapexec-smb-nopac]]):
```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -M nopac --output-file $_OUTPUT_FILE
```

> Append the --output-file flag to save results. Expected output: A file containing lines like 'username:asrep_hash'. Success is confirmed if the file populates with at least one hash. Use tools like Hashcat next (not covered here) with a wordlist to crack: hashcat -m 18200 hashes.txt rockyou.txt. If cracking succeeds, use the password to create a spoofed account matching a target user's SAMAccountName.
