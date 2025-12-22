---
id: 41dd7b40-f9bc-4923-8145-f7dc29eff57d
name: Remote-DPAPI-Credential-Dumping-with-DonPAPI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.357768+00:00'
updated_at: '2023-04-10T20:37:13.628747+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Data Protection API]]'
  - '[[tags/DonPAPI - Dumping DPAPI credz remotely]]'
  - '[[tags/Windows - DPAPI]]'
commands:
  - '[[commands/donpapi-extract-all-hashes]]'
  - '[[commands/donpapi-extract-hashes-with-ntlm]]'
  - '[[commands/dpapi-export-backup-keys]]'
  - '[[commands/donpapi-decrypt-with-pvk-and-extract-hashes]]'
platforms:
  - Windows
tools:
  - '[[tools/DonPAPI]]'
validated: true
---

# Remote-DPAPI-Credential-Dumping-with-DonPAPI

## Summary

This procedure outlines how to remotely dump credentials protected by the Windows Data Protection API (DPAPI) using the DonPAPI tool. It enables attackers with valid domain credentials to extract sensitive data, such as passwords and master keys, from remote Windows systems without needing physical or local access, facilitating further lateral movement and privilege escalation in Active Directory environments.

## Description

DPAPI is a cryptographic API built into Windows that protects sensitive data like passwords, cookies, and encryption keys using symmetric encryption tied to the user's login credentials. DonPAPI exploits remote access protocols (e.g., SMB/RPC) to retrieve DPAPI blobs, master keys, and backup keys from domain controllers or member servers. This technique is particularly effective in domain-joined environments where an attacker has compromised low-privilege credentials. The process involves authenticating to the target, extracting keys, and optionally decrypting using domain backup keys. Prerequisites include network connectivity to the target and valid credentials; success yields plaintext credentials or crackable hashes for offline analysis. This maps to credential access and lateral movement tactics, commonly used post-initial compromise to expand access.

## Requirements

1. Valid domain user credentials with network access to the target Windows machine (e.g., via SMB/RPC ports 445, 135).
2. Python 3 environment with Impacket library installed (DonPAPI depends on it for protocol handling).
3. Network connectivity to the target domain controller or member server running Windows Server 2008+.
4. Optional: Pre-obtained NTLM hashes for pass-the-hash authentication to avoid plaintext passwords.

## Defense

- Enable LSA protection and Credential Guard on Windows systems to prevent DPAPI key extraction.
- Restrict SMB/RPC access using firewalls and group policies; monitor for anomalous authentication attempts from compromised accounts.
- Implement endpoint detection rules for Python executions involving Impacket tools and unusual RPC calls to LSASS.
- Regularly rotate credentials and use privileged access workstations (PAWs) to limit exposure.

## Objectives

1. Authenticate remotely to the target and extract DPAPI-protected credential hashes.
2. Retrieve domain backup keys for decrypting user-specific DPAPI data across the network.
3. Decrypt and export sensitive credentials for offline cracking or direct use.
4. Achieve persistence or escalation by leveraging dumped credentials.

## Instructions

### Step 1: Extract All Available DPAPI Hashes

**Context**: Begin by using valid domain credentials to remotely connect to the target and dump all accessible DPAPI credential hashes. This step retrieves master keys and blobs without specifying hash types, providing a broad extraction for analysis.

**Command** ([[commands/donpapi-extract-all-hashes]]):
```python
DonPAPI.py domain/user:passw0rd@target
```

> This command authenticates to the target using the provided credentials and enumerates DPAPI structures via RPC. It outputs hashes in a format suitable for tools like Hashcat. If successful, expect a list of extracted hashes (e.g., NTLM, Kerberos tickets) saved to stdout or a file; failures may indicate insufficient privileges or network issues.

### Step 2: Extract Specific Hashes Using NTLM Authentication

**Context**: If plaintext passwords are unavailable or for stealth, use pre-compromised NTLM hashes to authenticate and extract targeted DPAPI hashes. This avoids password spraying detection while focusing on specific credential types.

**Command** ([[commands/donpapi-extract-hashes-with-ntlm]]):
```python
DonPAPI.py --hashes <LM>:<NT> domain/user@target
```

> Replace <LM>:<NT> with the LM and NTLM hashes (LM can be empty as :000000...). The tool performs pass-the-hash over SMB/RPC to dump hashes. Successful output includes the requested hashes; monitor for authentication logs on the target to verify.

### Step 3: Export Domain Backup Keys

**Context**: To decrypt user DPAPI data network-wide, export the domain's backup keys from the domain controller. This requires credentials with access to the DC and uses the Impacket dpapi module.

**Command** ([[commands/dpapi-export-backup-keys]]):
```python
dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip
```

> This exports the backup key (domain_backupkey.pvk) used by DCs to recover user keys. Output is a .pvk file; success is indicated by the file creation without errors. Use this key in subsequent steps for broader decryption.

### Step 4: Decrypt with Backup Key and Extract Network Hashes

**Context**: Using the exported backup key, decrypt DPAPI structures across the domain network list to retrieve additional credentials. This final step ties together key recovery and dumping for comprehensive access.

**Command** ([[commands/donpapi-decrypt-with-pvk-and-extract-hashes]]):
```python
python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list
```

> Provide the path to the .pvk file and a list of targets (e.g., comma-separated IPs or a file). The tool decrypts using the backup key and outputs hashes. Expect decrypted credential details; validate by checking for plaintext or crackable outputs.
