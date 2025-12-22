---
id: e6dca8f4-f55f-4938-8e81-46e48015cddc
name: NTDS-Hash-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.962770+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
  - '[[techniques/Credential Dumping/LSASS Memory|T1003.001]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/Extract hashes from ntds.dit]]'
commands:
  - '[[commands/secretsdump-extract-ntds-local]]'
  - '[[commands/secretsdump-dump-ntlm-with-vss]]'
  - '[[commands/secretsdump-dump-dc-hashes-with-ntlm]]'
  - '[[commands/hashcat-crack-ntlm-hashes]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# NTDS-Hash-Extraction

## Summary

NTDS Hash Extraction is a post-exploitation technique to dump password hashes from the Active Directory database (ntds.dit) on a Domain Controller. This procedure uses the secretsdump.py tool from the Impacket suite to extract NTLM hashes for all domain users and computers, either locally from copied files or remotely via network access with administrative credentials or hashes. The resulting hashes enable offline cracking to recover plaintext passwords for further attacks like pass-the-hash or lateral movement.

## Description

The ntds.dit file on a Windows Domain Controller stores hashed credentials for all Active Directory objects, including users, computers, and trusts. Attackers with admin access to the DC can extract this file along with the SYSTEM registry hive (which provides boot keys for decryption) to parse and retrieve NTLM hashes. Secretsdump.py automates this by handling the extraction, decryption, and formatting of hashes into crackable formats. This can be done locally if the attacker has physical or offline access to the files (e.g., via shadow copy), or remotely over SMB using valid domain admin credentials, NTLM hashes, or Volume Shadow Copy Service (VSS) to bypass file locks. Once extracted, hashes are cracked using tools like Hashcat against wordlists. This technique is high-impact in AD environments as it compromises the entire domain if successful.

## Requirements

1. Administrative privileges on the Domain Controller or valid domain admin credentials/NTLM hashes for remote access.
2. Network connectivity to the DC (SMB ports 445 open) for remote dumping; local file access for offline extraction.
3. Impacket suite installed on the attacker's machine (includes secretsdump.py).
4. For cracking: Hashcat or similar tool, a wordlist (e.g., rockyou.txt), and sufficient compute resources for offline cracking.

## Defense

- Restrict administrative access to Domain Controllers using just-in-time privileges and monitor logon events (Event ID 4624) for suspicious admin logins.
- Enable Volume Shadow Copy protection and monitor for VSS usage (Event ID 7045 for service installations).
- Implement strong password policies, LAPS (Local Administrator Password Solution), and Protected Users group to increase cracking difficulty.
- Use Windows Defender Credential Guard to isolate LSASS and prevent dumping; monitor for tools like secretsdump via EDR signatures.
- Regularly audit SYSVOL and ntds.dit access, and deploy network segmentation to limit SMB exposure.

## Objectives

1. Dump NTLM hashes from ntds.dit for all domain accounts.
2. Extract supplemental data like password last set times and account status.
3. Crack recovered hashes offline to obtain plaintext credentials for domain compromise.

## Instructions

### Step 1: Prepare Files for Local Extraction

**Context**: If the attacker has already copied the ntds.dit and SYSTEM files (e.g., from a VSS snapshot or offline DC), use local extraction to parse hashes without network access. This avoids detection from remote connections.

**Command** ([[commands/secretsdump-extract-ntds-local]]):
```bash
secretsdump.py -system $_SYSTEM_HIVE -ntds $_NTDS_FILE LOCAL
```

> This command parses the provided SYSTEM hive and ntds.dit file locally, outputting hashes in the format 'username:rid:lmhash:nthash'. Replace $_SYSTEM_HIVE with the path to the SYSTEM registry file (e.g., /root/SYSTEM) and $_NTDS_FILE with ntds.dit (e.g., /root/ntds.dit). Run this on the attacker's machine. Expected output includes a header like 'Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation' followed by credential listings.

### Step 2: Remote Dump Using Domain Admin Credentials with VSS

**Context**: For live DCs, use valid domain admin credentials to remotely dump hashes via SMB, leveraging VSS to create a shadow copy and avoid file locks on ntds.dit. This method includes password last-set times and user status for targeting crackable accounts.

**Command** ([[commands/secretsdump-dump-ntlm-with-vss]]):
```bash
secretsdump.py -dc-ip $_DC_IP $_DOMAIN/$_USERNAME@$_DOMAIN -use-vss -pwd-last-set -user-status
```

> Authenticate as a domain admin (e.g., $_USERNAME = administrator, $_DOMAIN = AD) to the DC at $_DC_IP. The -use-vss flag creates a shadow copy, -pwd-last-set adds last password change timestamps, and -user-status shows account states (enabled/disabled). Output mirrors local extraction but fetched remotely; save to a file with > output.txt for cracking.

### Step 3: Targeted DC Hash Dump Using NTLM Pass-the-Hash

**Context**: If plaintext credentials are unavailable but an NTLM hash is known (e.g., from prior dumping), use pass-the-hash to dump only the DC's hashes quickly and with less noise, focusing on machine accounts.

**Command** ([[commands/secretsdump-dump-dc-hashes-with-ntlm]]):
```bash
secretsdump.py -hashes :$_NTLM_HASH -just-dc $_DOMAIN/dc$@$_DC_IP
```

> Specify the NTLM hash in the format 'aad3b435b51404eeaad3b435b51404ee:$_NTLM_HASH' (LM hash is empty). The -just-dc flag limits to DC credentials, reducing output size. This authenticates without passwords, outputting DC-specific hashes.

### Step 4: Crack Extracted NTLM Hashes Offline

**Context**: Use the dumped hashes (in hashcat format) with a wordlist to recover plaintext passwords. Focus on weak or recently changed passwords first by sorting output from prior steps.

**Command** ([[commands/hashcat-crack-ntlm-hashes]]):
```bash
hashcat -m 1000 -a 0 $_HASH_FILE $_WORDLIST
```

> Mode -m 1000 is for NTLM; -a 0 for dictionary attack. $_HASH_FILE contains lines like 'username::nthash', $_WORDLIST is e.g., /usr/share/wordlists/rockyou.txt. Run on GPU-enabled machine for speed. Successful cracks show 'Cracked' status; use --show to list recovered passwords.
