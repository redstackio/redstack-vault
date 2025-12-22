---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.854354+00:00'
updated_at: '2023-04-10T20:26:27.002499+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active-Directory-Attacks]]'
  - '[[tags/Dumping-AD-Domain-Credentials]]'
  - '[[tags/Using-Vshadow]]'
commands:
  - '[[commands/create-volume-shadow-copy-vssadmin]]'
  - '[[commands/copy-ntds-dit-from-shadow-copy]]'
  - '[[commands/copy-system-hive-from-shadow-copy]]'
platforms:
  - Windows
tools:
  - '[[tools/vssadmin]]'
validated: true
---

# Dump-AD-Domain-Credentials-Using-VSSAdmin

## Summary

This procedure uses the built-in Volume Shadow Copy Service (VSS) via vssadmin to create a snapshot of the Active Directory database on a Domain Controller, allowing extraction of the NTDS.DIT file containing user hashes without directly accessing the locked original. It also copies the SYSTEM registry hive needed for decryption. Hashes can then be extracted offline using tools like impacket-secretsdump for cracking and lateral movement.

## Description

In an Active Directory environment, the NTDS.DIT file stores all domain user credentials in hashed form but is locked by the LSASS process on Domain Controllers. This procedure bypasses that by creating a point-in-time shadow copy of the system volume, enabling read-only access to copy the file and related registry hives. This technique is stealthy as it leverages native Windows tools, evading many AV solutions. It targets Windows Server Domain Controllers and requires local admin privileges. Once copied, the files enable offline credential dumping, supporting further attacks like pass-the-hash or golden ticket creation. Note: After dumping, clean up shadows to avoid detection.

## Requirements

1. Local Administrator privileges on the target Domain Controller.
2. Command Prompt executed as Administrator.
3. Target environment: Windows Server (2008+ ) acting as a Domain Controller with NTDS installed.
4. Sufficient disk space on the target for shadow copies (typically 1-5 GB for NTDS.DIT + SYSTEM).
5. Optional: Remote access via RDP, WinRM, or psexec for execution.

## Defense

- Monitor for vssadmin.exe executions via Sysmon (Event ID 1: ProcessCreate with Image vssadmin.exe) or Windows Event Logs (Security Event ID 4688).
- Restrict shadow copy creation using Group Policy: Computer Configuration > Administrative Templates > System > Shadow Copy > Disable Volume Shadow Copy service on non-essential servers.
- Implement privileged access management (PAM) to limit admin logons to DCs.
- Enable LSASS protection (Credential Guard) to complicate dumping, though shadow copy still works.
- Regularly audit shadow copies with vssadmin list shadows and alert on unexpected creations.

## Objectives

1. Create a volume shadow copy of the system drive to access locked AD files.
2. Copy NTDS.DIT and SYSTEM hive from the shadow copy for offline analysis.
3. Extract and crack domain credential hashes to enable lateral movement and persistence.
4. Maintain stealth by using native tools and cleaning up artifacts post-extraction.

## Instructions

### Step 1: Create Volume Shadow Copy

**Context**: Initiate a shadow copy of the C: drive (or system drive) where NTDS is located. This creates a snapshot without affecting the live system. Capture the output to identify the shadow path for the next steps.

**Command** ([[commands/create-volume-shadow-copy-vssadmin]]):
```cmd
vssadmin create shadow /for=C:
```

> This command uses vssadmin to snapshot the C: drive. Run it in an elevated Command Prompt. The output will include the Shadow Copy Volume path, which is essential for accessing files in the snapshot. If the drive is not C:, adjust /for= accordingly. Success is indicated by a confirmation message; failure may occur due to quota limits or service issues—verify VSS service is running with `sc query vss`.

### Step 2: Copy NTDS.DIT from Shadow Copy

**Context**: Using the Shadow Copy Volume path from Step 1 (e.g., \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2), copy the NTDS.DIT database file. This file contains all domain hashes but requires the SYSTEM hive for decryption.

**Command** ([[commands/copy-ntds-dit-from-shadow-copy]]):
```cmd
copy $_SHADOW_PATH\Windows\NTDS\ntds.dit $_OUTPUT_PATH\ntds.dit
```

> Replace $_SHADOW_PATH with the exact volume path from vssadmin output (include the trailing backslash if needed for navigation). Set $_OUTPUT_PATH to a writable directory like C:\temp. This copies the ~100-500MB file. Expected success: "1 file(s) copied." Verify with `dir $_OUTPUT_PATH` to confirm the file exists and size matches expectations. If access denied, ensure admin context.

### Step 3: Copy SYSTEM Hive from Shadow Copy

**Context**: The SYSTEM registry hive contains the boot key needed to decrypt NTDS.DIT hashes. Copy it from the same shadow to enable full credential extraction using tools like secretsdump.py.

**Command** ([[commands/copy-system-hive-from-shadow-copy]]):
```cmd
copy $_SHADOW_PATH\Windows\System32\config\SYSTEM $_OUTPUT_PATH\SYSTEM
```

> Use the same $_SHADOW_PATH and $_OUTPUT_PATH as Step 2. This copies the registry file (~10-50MB). Expected: "1 file(s) copied." Post-copy, you can exfiltrate both files or process locally. For extraction: Use `secretsdump.py -ntds $_OUTPUT_PATH/ntds.dit -system $_OUTPUT_PATH/SYSTEM LOCAL` (requires Impacket tools).

### Step 4: Clean Up Shadow Copy

**Context**: Delete the shadow copy to reduce footprint and free space. This prevents easy detection via `vssadmin list shadows`.

**Command**:
```cmd
vssadmin delete shadows /for=C: /quiet
```

> The /quiet flag suppresses prompts. Expected: "No items found to delete" if already gone, or confirmation. Verify cleanup with `vssadmin list shadows /for=C:` showing no entries.
