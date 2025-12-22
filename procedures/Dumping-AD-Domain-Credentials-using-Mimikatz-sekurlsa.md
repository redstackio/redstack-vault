---
id: 06f21c46-686a-4db0-a4b8-deec197b1290
name: Dumping-AD-Domain-Credentials-using-Mimikatz-sekurlsa
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.072472+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/active-directory-attacks]]'
  - '[[tags/dumping-ad-domain-credentials]]'
  - '[[tags/mimikatz-sekurlsa]]'
commands:
  - '[[commands/mimikatz-sekurlsa-dump-krbtgt]]'
  - '[[commands/mimikatz-lsadump-lsa-inject-krbtgt]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Dumping-AD-Domain-Credentials-using-Mimikatz-sekurlsa

## Summary

This procedure uses the Mimikatz sekurlsa module to extract password hashes and LSA secrets from a Windows system's memory, targeting Active Directory domain credentials such as the krbtgt account hash. It enables attackers to perform pass-the-hash attacks, escalate privileges, and move laterally in a network after gaining local administrator access.

## Description

In an Active Directory environment, attackers often target the Local Security Authority (LSA) subsystem to dump credentials stored in memory. The sekurlsa module of Mimikatz interacts with the LSASS process to retrieve Kerberos tickets, NTLM hashes, and other secrets without needing to inject code in some cases. This is particularly effective against the krbtgt account, whose hash can compromise the entire domain by allowing golden ticket forging. The procedure assumes execution on a domain-joined Windows machine with admin rights and is commonly used post-initial access for credential harvesting. Success provides hashes usable in tools like Hashcat for cracking or direct replay in attacks.

## Requirements

1. Local administrator privileges on a domain-joined Windows system (e.g., via UAC bypass or prior escalation).
2. Mimikatz binary downloaded and executed from a trusted source (run as administrator).
3. Windows OS (Server 2008+ or Windows 7+), with LSASS protection potentially disabled (e.g., via registry or group policy).
4. Network connectivity if lateral movement follows, but not required for dumping.

## Defense

- Enable Credential Guard and LSA protection on Windows systems to prevent LSASS access.
- Monitor for Mimikatz signatures via EDR tools (e.g., process injection into LSASS, unusual memory reads).
- Implement application whitelisting to block unsigned executables like Mimikatz.
- Regularly rotate the krbtgt password to invalidate dumped hashes.
- Use Sysmon logging to detect command-line arguments matching Mimikatz modules (e.g., 'sekurlsa' or 'lsadump').

## Objectives

1. Extract the NTLM hash of the krbtgt account for potential domain compromise.
2. Dump LSA secrets containing sensitive domain information like passwords and keys.
3. Enable subsequent attacks such as pass-the-hash or Kerberos ticket forging.
4. Verify successful credential extraction for lateral movement planning.

## Instructions

### Step 1: Launch Mimikatz and Access sekurlsa Module

**Context**: Start Mimikatz with elevated privileges to interact with LSASS. This step prepares the environment for credential dumping by elevating to the sekurlsa context, which handles in-memory credential extraction.

Execute the Mimikatz executable as administrator. Once in the Mimikatz prompt (!#), privilege::elevate if needed, then enter the sekurlsa module.

**Command** ([[commands/mimikatz-sekurlsa-dump-krbtgt]]):
```cmd
sekurlsa::krbtgt
```

> This command retrieves the Kerberos keys and NTLM hash for the krbtgt account from LSASS memory. It succeeds if admin rights allow LSASS access, providing the hash immediately usable for attacks.

### Step 2: Dump LSA Secrets Using lsadump

**Context**: After extracting the krbtgt hash, use the lsadump module to inject and retrieve additional LSA secrets, focusing on krbtgt-related data. This step uncovers stored secrets like service account passwords.

From the Mimikatz prompt, switch to lsadump module and run the injection command targeting krbtgt.

**Command** ([[commands/mimikatz-lsadump-lsa-inject-krbtgt]]):
```cmd
lsadump::lsa /inject /name:krbtgt
```

> The /inject flag forces credential extraction via process injection if direct access is blocked. Expected output includes decrypted secrets; if krbtgt name is specified, it filters for relevant domain keys.

### Step 3: Verify and Export Credentials

**Context**: Review the dumped output for validity and save hashes for offline cracking or immediate use. This ensures the procedure's success before proceeding to exploitation.

Manually inspect the console output for hashes (e.g., starting with $krbtgt or NTLM format). Optionally, use Mimikatz's log or redirect output to a file: log (or > output.txt in cmd).

> No specific command here, but cross-reference with known krbtgt hash formats (32 hex chars for NTLM). Success is confirmed by presence of usable hashes without errors like 'access denied'.
