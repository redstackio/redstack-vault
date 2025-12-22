---
id: df411125-df65-4113-8d37-1c4545ae30dd
name: Automated Password Extraction from SYSVOL and Group Policy Preferences
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.542823+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
  - '[[techniques/Network Share Discovery|T1135 - Network Share Discovery]]'
sub_techniques:
  - >-
    [[sub-techniques/Group Policy Preferences|T1555.006 - Group Policy
    Preferences]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/SYSVOL Password Extraction]]'
  - '[[tags/Group Policy Preferences]]'
commands:
  - '[[commands/metasploit-enum-smb-shares]]'
  - '[[commands/metasploit-enum-windows-shares]]'
  - '[[commands/metasploit-enum-gpp-credentials]]'
  - '[[commands/crackmapexec-extract-gpp-autologin]]'
  - '[[commands/crackmapexec-extract-gpp-password]]'
  - '[[commands/get-gpp-password-null-session]]'
  - '[[commands/get-gpp-password-cleartext-creds]]'
  - '[[commands/get-gpp-password-pass-the-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Impacket]]'
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Automated Password Extraction from SYSVOL and Group Policy Preferences

## Summary

This procedure automates the discovery and extraction of plaintext passwords stored in SYSVOL shares and Group Policy Preferences (GPP) XML files within a Windows Active Directory environment. It leverages tools like Metasploit modules, CrackMapExec, and Impacket's Get-GPPPassword.py to enumerate network shares, access SYSVOL, and decrypt embedded credentials, enabling attackers to obtain service account or local admin passwords for further compromise.

## Description

In legacy Active Directory setups, Group Policy Preferences often store passwords in unencrypted XML files within the SYSVOL share, accessible to authenticated domain users. This procedure begins with share enumeration to identify SYSVOL access, followed by targeted extraction of GPP files containing credentials like autologon passwords or scheduled task accounts. These passwords are decrypted using built-in AES keys (publicly known since 2012). The technique targets domain controllers or file servers hosting SYSVOL, requiring at minimum domain user credentials. Successful execution yields plaintext credentials usable for lateral movement or privilege escalation. Note: Microsoft patched GPP password storage in 2012, but legacy policies may persist.

## Requirements

1. Domain user credentials (or null session where possible) with read access to SYSVOL shares.
2. Network connectivity to domain controllers or SYSVOL hosts (ports 445/TCP for SMB).
3. Installed tools: Metasploit Framework, CrackMapExec, Impacket suite (Get-GPPPassword.py).
4. Python 2/3 environment for Impacket tools.

## Defense

- Remove legacy GPP XML files containing passwords from SYSVOL and migrate to secure alternatives like LAPS or managed service accounts.
- Restrict SYSVOL read access to Domain Users group and monitor for anomalous SMB access via tools like Microsoft ATA or Sysmon.
- Enable Advanced Audit Policy for file share access and review Event ID 5145 for SYSVOL enumerations.
- Use endpoint detection to block execution of tools like CrackMapExec or Impacket on compromised hosts.

## Objectives

1. Enumerate accessible SMB shares to confirm SYSVOL availability.
2. Extract and decrypt GPP passwords from XML files in SYSVOL.
3. Obtain plaintext credentials for use in lateral movement or privilege escalation.

## Instructions

### Step 1: Enumerate SMB Shares Using Metasploit

**Context**: Start by identifying accessible network shares, including SYSVOL, to confirm the target hosts SYSVOL exposure. This uses Metasploit's SMB enumeration module to list shares without deep exploitation.

**Command** ([[commands/metasploit-enum-smb-shares]]):
```bash
use scanner/smb/smb_enumshares; set RHOSTS <TARGET_IP>; run
```

> This module connects via SMB and lists all shares on the target. Replace <TARGET_IP> with the domain controller IP. If successful, look for 'SYSVOL' in the output shares list.

### Step 2: Enumerate Windows Shares Post-Exploitation

**Context**: If you have a foothold on a Windows host (e.g., via Meterpreter session), use this module to gather share information locally or remotely, focusing on domain-level shares like SYSVOL.

**Command** ([[commands/metasploit-enum-windows-shares]]):
```bash
use post/windows/gather/enum_shares; set SESSION <SESSION_ID>; run
```

> Run within a Meterpreter session. <SESSION_ID> is the ID from 'sessions -l'. Output includes share paths; verify SYSVOL presence for GPP access.

### Step 3: Enumerate GPP Credentials Using Metasploit

**Context**: Directly pull GPP credentials from SYSVOL using Metasploit's post module, which parses XML files for encrypted passwords and decrypts them on-the-fly.

**Command** ([[commands/metasploit-enum-gpp-credentials]]):
```bash
use post/windows/gather/credentials/gpp; set SESSION <SESSION_ID>; run
```

> Execute in a Meterpreter session on a domain-joined host. It accesses \\<DC>\SYSVOL and extracts cpassword fields, decrypting with the known AES key. Output shows usernames and plaintext passwords.

### Step 4: Extract GPP Autologin Passwords with CrackMapExec

**Context**: Use CrackMapExec to target GPP autologin XML files specifically, authenticating with provided credentials or hashes to pull SYSVOL data remotely.

**Command** ([[commands/crackmapexec-extract-gpp-autologin]]):
```bash
crackmapexec smb <TARGET_IP> -u <USERNAME> -H <NTLM_HASH> -M gpp_autologin
```

> <TARGET_IP> is the DC IP, <USERNAME> a domain user, <NTLM_HASH> the NTLM hash (optional if using password with -p). Output displays extracted autologon credentials if present in SYSVOL.

### Step 5: Extract Standard GPP Passwords with CrackMapExec

**Context**: Similar to autologin but targets general GPP password XML files (e.g., for services or tasks), providing another vector for credential recovery.

**Command** ([[commands/crackmapexec-extract-gpp-password]]):
```bash
crackmapexec smb <TARGET_IP> -u <USERNAME> -H <NTLM_HASH> -M gpp_password
```

> Use the same parameters as Step 4. Success yields passwords from Groups.xml or Services.xml in SYSVOL.

### Step 6: Extract GPP Passwords with Impacket (Null Session)

**Context**: Attempt extraction without credentials using a null SMB session, ideal for anonymous access if SYSVOL is exposed.

**Command** ([[commands/get-gpp-password-null-session]]):
```bash
Get-GPPPassword.py -no-pass <DOMAIN_CONTROLLER>
```

> <DOMAIN_CONTROLLER> is the FQDN or IP. If SYSVOL allows guest access, it dumps all GPP passwords.

### Step 7: Extract GPP Passwords with Cleartext Credentials

**Context**: Authenticate with known domain credentials to access restricted SYSVOL shares and retrieve GPP data.

**Command** ([[commands/get-gpp-password-cleartext-creds]]):
```bash
Get-GPPPassword.py <DOMAIN>/<USERNAME>:<PASSWORD>@<DOMAIN_CONTROLLER>
```

> Provide full creds in the format shown. Output includes decrypted passwords from all GPP files.

### Step 8: Extract GPP Passwords with Pass-the-Hash

**Context**: Use stolen NTLM hashes for authentication without plaintext passwords, common in lateral movement scenarios.

**Command** ([[commands/get-gpp-password-pass-the-hash]]):
```bash
Get-GPPPassword.py -hashes <LMHASH>:<NTHASH> <DOMAIN>/<USERNAME>@<DOMAIN_CONTROLLER>
```

> <LMHASH> is often 'aad3b435b51404eeaad3b435b51404ee' for empty LM; <NTHASH> is the NT hash. This bypasses password prompts.
