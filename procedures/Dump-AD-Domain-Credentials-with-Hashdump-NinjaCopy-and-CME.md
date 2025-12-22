---
id: 019d9286-1588-469f-8b94-15fd7f3b43e9
name: Dump-AD-Domain-Credentials-with-Hashdump-NinjaCopy-and-CME
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.998564+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
  - '[[sub-techniques/LSA Secrets|T1003.004 - LSA Secrets]]'
  - '[[sub-techniques/NTDS|T1003.003 - NTDS]]'
  - >-
    [[sub-techniques/Security Account Manager|T1003.002 - Security Account
    Manager]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/Credential Access]]'
commands:
  - '[[commands/msfconsole-run-domain-hashdump]]'
  - '[[commands/invoke-ninjacopy-copy-ntds-dit]]'
  - '[[commands/crackmapexec-smb-ntds-vss]]'
  - '[[commands/crackmapexec-smb-ntds-drsuapi]]'
platforms:
  - Windows
tools:
  - '[[tools/metasploit-framework]]'
  - '[[tools/PowerSploit]]'
  - '[[tools/CrackMapExec]]'
validated: true
---

# Dump-AD-Domain-Credentials-with-Hashdump-NinjaCopy-and-CME

## Summary

This procedure outlines multiple methods to dump Active Directory domain credentials, including password hashes from the SAM database, LSA secrets, and the NTDS.dit file. Attackers use these techniques post-compromise on a domain controller or with sufficient privileges to extract hashes for offline cracking or pass-the-hash attacks, enabling lateral movement and privilege escalation in Windows environments.

## Description

Dumping AD domain credentials targets sensitive data stored in Windows systems, such as the local SAM database for workstation hashes or the NTDS.dit file on domain controllers for full domain user hashes. This procedure covers three complementary approaches: using Metasploit's domain_hashdump module to remotely dump hashes via WMI, Invoke-NinjaCopy to stealthily copy the NTDS.dit file without triggering alerts, and CrackMapExec to extract NTDS data using Volume Shadow Copy Service (VSS) or Directory Replication Service (DRS) APIs. These methods require administrative access or domain credentials and are typically executed after initial foothold or privilege escalation. Success provides NTLM hashes, which can be cracked with tools like Hashcat to reveal plaintext passwords, compromising the entire domain.

## Requirements

1. Administrative privileges on a domain-joined Windows system or valid domain credentials with DCSync rights.
2. Network access to the domain controller (ports 445/TCP for SMB, 135/TCP for RPC).
3. Installed tools: Metasploit Framework, PowerSploit (for Invoke-NinjaCopy), and CrackMapExec.
4. PowerShell execution policy set to allow scripts (Bypass or Unrestricted).
5. Target environment: Windows Server 2008+ with Active Directory.

## Defense

- Enable Protected Users group and restrict NTDS.dit access via filesystem permissions.
- Implement credential guard (LSA protection) and disable WMI remotely if possible.
- Monitor for anomalous SMB/RPC traffic, process creation (e.g., wmic.exe, powershell.exe), and Event ID 4662 (object access on sensitive files).
- Use tools like Microsoft ATA or EDR solutions to detect DCSync replication attempts and hash dumping.

## Objectives

1. Extract password hashes from SAM, LSA, or NTDS.dit for offline analysis.
2. Enable pass-the-hash or password cracking to access additional systems.
3. Achieve domain dominance by compromising administrator accounts.

## Instructions

This procedure provides alternative methods; select based on access level and evasion needs. All methods assume you have a shell or PowerShell session on a compromised host with domain admin creds.

### Step 1: Dump Hashes Using Metasploit Domain Hashdump

**Context**: Use this for remote hash extraction from the domain controller via WMI without direct file access. It targets SAM and LSA secrets, providing local and domain hashes.

**Command** ([[commands/msfconsole-run-domain-hashdump]]):
```bash
msfconsole -q -x "use windows/gather/credentials/domain_hashdump; set RHOSTS $_TARGET_IP; set SMBUser $_USERNAME; set SMBPass $_PASSWORD; run"
```

> This launches Metasploit in quiet mode, loads the domain_hashdump module, configures the target DC IP, credentials, and executes the dump. It queries WMI to retrieve hashes without alerting typical file monitors. If successful, hashes are saved to loot for cracking.

### Step 2: Copy NTDS.dit Using Invoke-NinjaCopy

**Context**: For direct NTDS.dit extraction, use this PowerShell tool to copy the file from the DC's %SystemRoot%\NTDS folder to a local path, bypassing some AV by mimicking legitimate file operations.

**Command** ([[commands/invoke-ninjacopy-copy-ntds-dit]]):
```powershell
Invoke-NinjaCopy -Path "c:\windows\NTDS\ntds.dit" -Verbose -LocalDestination "c:\temp\ntds.dit"
```

> Run this in a PowerShell session with DA privileges. The -Path specifies the remote NTDS.dit location, -Verbose logs progress, and -LocalDestination saves the file locally. Verify the copy with file size checks (NTDS.dit is typically 10-100MB). Post-copy, use ntdsutil or secretsdump.py to parse hashes.

### Step 3: Extract NTDS Using CrackMapExec VSS Method

**Context**: If direct copy fails, use CME's VSS method to create a shadow copy and dump NTDS.dit remotely over SMB without physical file access.

**Command** ([[commands/crackmapexec-smb-ntds-vss]]):
```bash
cme smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --ntds vss
```

> This connects to the target DC via SMB, authenticates, and uses VSS to snapshot and extract NTDS.dit hashes. Output includes username:rid:LMHASH:NTHASH format. Decision point: If VSS fails due to permissions, fallback to DRSUAPI.

### Step 4: Extract NTDS Using CrackMapExec DRSUAPI Method (Fallback)

**Context**: As an alternative to VSS, DRSUAPI mimics legitimate replication to pull NTDS data without shadow copies, useful if VSS is monitored or disabled.

**Command** ([[commands/crackmapexec-smb-ntds-drsuapi]]):
```bash
cme smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --ntds drsuapi
```

> This is the default method in CME, leveraging Directory Replication Service to fetch user objects and hashes. It requires replication rights (e.g., DA). Output mirrors VSS: crackable hash files. Verify by checking for SID::RID:username:lm:nt format in the generated .ntds file.
