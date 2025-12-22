---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/authentication]]'
  - '[[tags/Cryptography]]'
  - '[[tags/data exposure]]'
commands:
  - '[[commands/samdump2-dump-hashes-from-sam-system]]'
platforms:
  - Windows
tools:
  - '[[tools/samdump2]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Extract LM/NTLM Hashes from SAM/SYSTEM Hives

## Summary

This procedure extracts LM and NTLM password hashes from a Windows system's SAM and SYSTEM registry hive files, typically located in %SystemRoot%\System32\Config. These hashes can be used in pass-the-hash attacks to authenticate to other systems without knowing the plaintext passwords or subjected to offline brute-force cracking to recover passwords.

## Description

Windows stores local user account credentials in the SAM (Security Account Manager) hive, encrypted using the SYSTEM hive's boot key. Attackers with physical or administrative access to a system can copy these hive files while the system is offline or use tools to extract them from memory. The extracted hashes include LM (legacy, weak) and NTLM (stronger) variants. LM hashes are particularly vulnerable to cracking due to their storage of passwords in uppercase and split into halves. This technique is common in lateral movement and privilege escalation scenarios after initial access, allowing attackers to impersonate local accounts across the network.

## Requirements

1. Copied SAM and SYSTEM hive files from the target Windows system (e.g., via offline access or tools like Reg.exe).
2. Access to a Linux or Windows machine with samdump2 installed for extraction.
3. Basic knowledge of Windows registry structure and hash formats.
4. Optional: Hash cracking tools like Hashcat for post-extraction analysis.

## Defense

Defensive measures and detection strategies:

- Restrict physical and administrative access to systems to prevent hive file extraction.
- Enable Windows Event Logging for registry access (Event ID 4657) and monitor for unusual file copies from System32\Config.
- Use full-disk encryption (BitLocker) to protect offline hives.
- Implement credential guard features like LSA Protection to hinder in-memory extraction attempts.
- Monitor for tools like samdump2 via process auditing and network shares used for exfiltration.

## Objectives

1. Extract usable LM and NTLM hashes from offline hive files.
2. Prepare hashes for pass-the-hash attacks or offline cracking.
3. Validate extraction success through hash format recognition.

## Instructions

### Step 1: Prepare Hive Files

**Context**: Ensure the SAM and SYSTEM hive files are available on your extraction machine. These files must be from the same system and unmounted (offline).

Copy the files to your working directory if not already present. Verify file integrity to avoid corruption during transfer.

> No command needed here; manual file placement.

### Step 2: Extract Hashes Using samdump2

**Context**: Use samdump2 to decrypt the hashes from the SAM hive using the boot key derived from the SYSTEM hive. This step performs the core extraction and outputs hashes in a format suitable for tools like Hashcat or John the Ripper.

**Command** ([[commands/samdump2-dump-hashes-from-sam-system]]):
```bash
samdump2 SYSTEM SAM
```

> This command reads the SYSTEM file first to obtain the boot key, then decrypts the SAM file to dump user hashes. Run it from the directory containing both files. If successful, it will list each local user account followed by their LM and NTLM hashes (e.g., Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::).

### Step 3: Verify and Parse Output

**Context**: Review the output for valid hash formats and identify high-value accounts (e.g., Administrator). Save the output to a file for further processing.

Redirect output to a file for analysis:
```bash
samdump2 SYSTEM SAM > hashes.txt
```

> Expected: A text file with lines in the format username:RID:LM_hash:NTLM_hash. LM hashes may be 'aad3b435b51404eeaad3b435b51404ee' (empty) for accounts without LM enabled. Proceed to crack NTLM hashes if needed using external tools.
