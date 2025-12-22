---
id: 309b8128-bfae-4f82-b76b-2c584d14fea2
name: Copy-File-to-Remote-Windows-Machine-via-Xcopy
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T22:19:00.525565+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Lateral Movement]]'
  - '[[Command and Control]]'
techniques:
  - '[[Remote File Copy]]'
sub_techniques: []
tags:
  - '[[tags/file-transfer]]'
  - '[[tags/lateral-movement]]'
commands:
  - '[[commands/Map-Remote-Share-as-Network-Drive]]'
  - '[[commands/Copy-File-to-Mapped-Drive-using-Xcopy]]'
platforms:
  - Windows
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Copy-File-to-Remote-Windows-Machine-via-Xcopy

## Summary

This procedure uses built-in Windows commands to copy a file from a local machine to a remote Windows host in a domain environment. It authenticates to an administrative share (C$) using net use to map a network drive, then transfers the file via xcopy. This technique is commonly used for lateral movement or staging payloads without relying on external tools.

## Description

In Windows domains, administrative shares like C$ allow authenticated users with sufficient privileges to access remote file systems. This procedure leverages net use to establish a persistent connection to the target's C$\Users\Public directory (a common drop location), followed by xcopy for the file transfer. It assumes the attacker has valid domain credentials and network access to the target. The approach minimizes detection by using native cmd.exe utilities, but it requires interactive prompts for xcopy confirmation. Success enables file placement for further exploitation, such as executing malware on the remote host.

## Requirements

1. Valid domain credentials (username and password) with administrative access to the target machine's C$ share.
2. Network connectivity to the target machine over SMB (port 445 open).
3. Local Windows machine with command prompt (cmd.exe) access.
4. The source file must exist on the local machine (e.g., in C:\).
5. Target path should be a writable location like Users\Public to avoid permission issues.

## Defense

Defensive measures and detection strategies:

- Enable SMB signing and auditing on domain controllers to log unauthorized share access.
- Monitor Event ID 5145 (network share access) and 4624 (logon events) for suspicious net use authentications.
- Restrict administrative share access via Group Policy (e.g., disable C$ for non-admins).
- Use endpoint detection tools to alert on xcopy executions from unusual processes or to admin shares.
- Implement least privilege: Limit domain user accounts from having admin rights on remote hosts.

## Objectives

1. Authenticate to the remote machine and map its administrative share as a local drive.
2. Transfer the specified file to the remote machine's public directory.
3. Verify the file was copied successfully without errors.

## Instructions

### Step 1: Map Remote Share

**Context**: Authenticate to the target's C$ share using domain credentials and map it to a local drive letter (T:). This creates a temporary network connection for file access. The Users\Public path is used as it's often writable without additional privileges.

**Command** ([[commands/Map-Remote-Share-as-Network-Drive]]):
```cmd
net use T: \\$_DOMAIN\C$\Users\Public /user:$_DOMAIN\$_USERNAME $_PASSWORD
```

> This command initiates an SMB connection. If successful, the drive is mounted for subsequent use. Disconnect with 'net use T: /delete' after transfer. Common errors include access denied (insufficient privileges) or network path not found (firewall/SMB disabled).

### Step 2: Copy File to Mapped Drive

**Context**: With the share mapped, use xcopy to transfer the file from the local path to the remote public directory. xcopy prompts to confirm if the target specifies a file or directory; select 'F' for file. This step assumes the source file is in C:\; adjust paths as needed.

**Command** ([[commands/Copy-File-to-Mapped-Drive-using-Xcopy]]):
```cmd
xcopy C:\$_FILENAME T:\$_FILENAME
```

> The command copies the file and reports the number of files transferred. If the target path is ambiguous, it prompts for clarification. Verify success by checking the remote directory or attempting to access the file via the mapped drive. Use /Y flag to suppress prompts in scripts: xcopy /Y source target.
