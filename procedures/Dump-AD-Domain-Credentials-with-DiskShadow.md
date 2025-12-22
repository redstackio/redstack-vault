---
type: procedure
tactics:
  - '[[tactics/Credential-Access]]'
techniques:
  - '[[techniques/Credential-Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active-Directory-Attacks]]'
  - '[[tags/Dumping-AD-Domain-Credentials]]'
  - '[[tags/Using-DiskShadow]]'
commands:
  - '[[commands/diskshadow-execute-extraction-script]]'
  - '[[commands/dir-list-exfil-directory]]'
  - '[[commands/reg-save-system-hive-to-exfil]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Dump-AD-Domain-Credentials-with-DiskShadow

## Summary

This procedure uses the built-in Windows tool DiskShadow to create a volume shadow copy of the system drive, expose it temporarily, and extract the NTDS.dit file containing Active Directory domain user hashes. It also backs up the SYSTEM registry hive for use with tools like secretsdump.py to decrypt the hashes. This technique bypasses direct file access monitoring by leveraging legitimate Windows volume shadow copy services.

## Description

In Active Directory environments, the NTDS.dit file stores hashed credentials for all domain users and is protected on Domain Controllers. DiskShadow, a signed Microsoft binary available on Windows Server 2008 and later, allows creation of persistent shadow copies without Volume Shadow Copy Service (VSS) writers, enabling extraction of NTDS.dit from C:\Windows\NTDS\ without alerting file integrity monitoring tools. The procedure involves scripting DiskShadow commands to mount the shadow copy as a virtual drive (Z:), copying NTDS.dit to an exfiltration directory, and cleaning up the shadow. The SYSTEM hive backup provides boot key data needed for hash extraction. This is typically executed post-compromise on a Domain Controller with SYSTEM privileges, aiding lateral movement or persistence via cracked credentials.

## Requirements

1. Administrative or SYSTEM privileges on a Domain Controller (e.g., via psexec or scheduled task).
2. Local access to the target system (e.g., interactive shell or RDP).
3. Knowledge of the NTDS.dit location (default: C:\Windows\NTDS\ntds.dit).
4. Write access to a staging directory like C:\exfil for output files.
5. Windows Server 2008 or later with DiskShadow.exe in C:\Windows\System32.

## Defense

- Enable advanced auditing for process creation and file access on Domain Controllers, specifically monitoring diskshadow.exe executions and VSS events (Event ID 8222 for shadow copy creation).
- Implement application whitelisting (e.g., AppLocker) to restrict unsigned scripts or block shadow copy creation for non-admin processes.
- Use protected file access controls and monitor for anomalous registry saves or copies from protected paths like C:\Windows\NTDS.
- Deploy endpoint detection rules for shadow copy exposure (e.g., via Sysmon Event ID 1 for cmd.exe /c copy involving ntds.dit).

## Objectives

1. Create a shadow copy of the system volume containing NTDS.dit without triggering VSS writers.
2. Extract NTDS.dit and the SYSTEM registry hive to a local directory for offline analysis.
3. Enable subsequent hash dumping using tools like Impacket's secretsdump for credential recovery.
4. Maintain operational security by deleting the shadow copy post-extraction.

## Instructions

### Step 1: Prepare the DiskShadow Extraction Script

**Context**: Create a script file containing the DiskShadow commands to automate shadow copy creation, exposure, NTDS.dit extraction, and cleanup. This avoids manual input and ensures repeatability. Use the provided script content to populate the file.

Use [[codes/DiskShadow-Script-for-NTDS-Extraction]] to generate the content for C:\diskshadow.txt. Save it using notepad or echo commands:

```cmd
echo set context persistent nowriters > C:\diskshadow.txt
echo add volume c: alias someAlias >> C:\diskshadow.txt
# ... (append full script from code)
```

> This step sets up the automation; verify the file contents with type C:\diskshadow.txt to ensure no syntax errors.

### Step 2: Execute the DiskShadow Script to Extract NTDS.dit

**Context**: Run DiskShadow from the System32 directory to process the script, creating the shadow copy, copying NTDS.dit, and deleting the shadow. This performs the core extraction without direct access to the protected file.

**Command** ([[commands/diskshadow-execute-extraction-script]]):
```cmd
diskshadow.exe /s $_SCRIPT_PATH
```

> Execute from C:\Windows\System32. The command processes the script: sets context, adds the C: volume, creates the shadow, exposes it as Z:, copies ntds.dit via cmd.exe, and resets/deletes the shadow.

### Step 3: Verify the Exfiltration

**Context**: List the contents of the exfil directory to confirm NTDS.dit was successfully copied. This validates the extraction before proceeding to registry backup.

**Command** ([[commands/dir-list-exfil-directory]]):
```cmd
dir $_EXFIL_PATH
```

> Expected output includes ntds.dit in the directory, indicating successful shadow copy and copy operation.

### Step 4: Backup the SYSTEM Registry Hive

**Context**: Save the SYSTEM hive to pair with NTDS.dit for hash decryption (provides the boot key). This is essential for tools like secretsdump to process the dump.

**Command** ([[commands/reg-save-system-hive-to-exfil]]):
```cmd
reg.exe save hklm\system $_EXFIL_PATH\system.bak
```

> The command exports the hive; success is indicated by a non-zero file size for system.bak.
