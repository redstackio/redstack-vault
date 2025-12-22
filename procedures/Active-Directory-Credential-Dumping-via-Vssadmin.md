---
id: a264143b-c7cd-4f33-8855-2068bab0b911
name: Active-Directory-Credential-Dumping-via-Vssadmin
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.882957+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/Using vssadmin]]'
commands:
  - '[[commands/vssadmin-create-volume-shadow-copy]]'
  - '[[commands/copy-ntds-dit-from-shadow-copy]]'
  - '[[commands/copy-system-hive-from-shadow-copy]]'
platforms:
  - Windows
tools:
  - '[[tools/Vssadmin]]'
validated: true
---

# Active-Directory-Credential-Dumping-via-Vssadmin

## Summary

This procedure uses the built-in Windows Volume Shadow Copy Service (VSS) via the vssadmin tool to create a shadow copy of the system volume, allowing extraction of the NTDS.dit database file and the SYSTEM registry hive without directly accessing the protected files on a live domain controller. These files contain hashed Active Directory credentials that can be processed offline for password recovery, enabling lateral movement or privilege escalation in AD environments.

## Description

In Active Directory environments, the NTDS.dit file stores all domain user hashes (including NTLM and Kerberos keys), while the SYSTEM hive contains the necessary boot key for decryption. Direct access to these files is restricted on live systems, but vssadmin can create a point-in-time shadow copy, providing a consistent snapshot that bypasses some locks. Once copied, tools like secretsdump.py from Impacket can extract and crack the hashes. This technique is commonly used post-compromise on domain controllers or systems with NTDS replication. It requires administrative privileges and is detectable via event logs for shadow copy creation.

## Requirements

1. Administrative privileges on a Windows domain controller or system with NTDS installed.
2. Access to the C: drive (system volume).
3. A destination directory (e.g., C:\ShadowCopy) with write permissions.
4. Built-in vssadmin tool (available on Windows Server 2008+).
5. Optional: Offline cracking tools like Hashcat for post-extraction.

## Defense

- Restrict administrative access to domain controllers via least privilege principles.
- Monitor Event ID 7036 (Service Control Manager) for VSS service starts and Event ID 8222 for shadow copy creations.
- Disable volume shadow copies on DCs via Group Policy if not needed for backups.
- Enable Sysmon logging for process creation involving vssadmin.exe.
- Use protected processes and credential guard to limit hash exposure.

## Objectives

1. Create a shadow copy to access locked NTDS.dit and SYSTEM files.
2. Extract credential hashes for offline cracking and domain compromise.
3. Enable lateral movement using recovered domain admin credentials.

## Instructions

### Step 1: Create Volume Shadow Copy

**Context**: Use vssadmin to generate a shadow copy of the C: drive, which provides a mountable snapshot for accessing protected files without disrupting the live system.

**Command** ([[commands/vssadmin-create-volume-shadow-copy]]):
```cmd
vssadmin create shadow /for=C:
```

> This command initiates the shadow copy service and creates a snapshot. The shadow copy ID (e.g., HarddiskVolumeShadowCopy1) will be outputted, which is used in subsequent copy operations. Verify the copy exists by checking the output for success and the volume GUID.

### Step 2: Copy NTDS.dit from Shadow Copy

**Context**: Access the shadow copy path to retrieve the NTDS.dit file, which holds all AD user hashes. Replace the shadow copy volume name with the one from Step 1 output.

**Command** ([[commands/copy-ntds-dit-from-shadow-copy]]):
```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\ShadowCopy
```

> This copies the database file to a local directory. Success is indicated by no errors and the file appearing in C:\ShadowCopy with the correct size (~MBs depending on domain size). If the volume name differs, update it accordingly.

### Step 3: Copy SYSTEM Hive from Shadow Copy

**Context**: Extract the SYSTEM registry hive, which contains the decryption key needed to process NTDS.dit hashes. This step ensures the credentials can be decrypted offline.

**Command** ([[commands/copy-system-hive-from-shadow-copy]]):
```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM C:\ShadowCopy
```

> This retrieves the hive file. Expected output is a successful copy confirmation. The file should match the original size and be usable with tools like secretsdump for hash extraction.

### Step 4: Clean Up Shadow Copy (Optional but Recommended)

**Context**: Delete the shadow copy to minimize footprint and avoid storage bloat or detection.

**Command**:
```cmd
vssadmin delete shadows /for=C: /oldest
```

> This removes the oldest shadow copy. Confirm deletion via output showing the shadow removed. Always perform cleanup to evade forensics.
