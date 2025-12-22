---
id: bc4e5b82-e7fa-4963-9886-5b21da1c3246
name: remote-command-execution-via-wmi-using-impacket
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.964543+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - >-
    [[techniques/Windows Management Instrumentation|T1047 - Windows Management
    Instrumentation]]
sub_techniques: []
tags:
  - Impacket
  - WMI
  - lateral-movement
  - remote-execution
  - windows-credentials
commands:
  - '[[commands/impacket-wmiexec-execute-command]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Remote Command Execution via WMI Using Impacket

## Summary

This procedure uses Impacket's wmiexec.py tool to execute commands on a remote Windows machine via Windows Management Instrumentation (WMI). It enables lateral movement by leveraging valid credentials to run semi-interactive commands or scripts remotely, with output retrieved via SMB shares. This is useful for post-exploitation scenarios where direct interactive access is restricted but credentialed SMB/WMI access is available.

## Description

WMIExec.py from the Impacket suite exploits the Windows Management Instrumentation interface to create a semi-interactive shell on the target. It authenticates using provided domain credentials and executes commands through WMI's process creation capabilities. Output is captured by redirecting it to a specified SMB share (defaulting to ADMIN$ if available), allowing retrieval without leaving persistent artifacts like uploaded binaries. This technique is stealthy as it uses native Windows protocols (WMI over DCERPC on port 135, SMB on 445) and avoids tools like PsExec that might trigger more alerts. It maps to MITRE ATT&CK techniques for execution via WMI and use of valid accounts for lateral movement. Prerequisites include network access to the target, valid credentials, and an accessible SMB share. Success results in command execution and output retrieval, enabling further enumeration or control.

## Requirements

1. Impacket suite installed on the attacker's machine (see [[tools/Impacket]] for installation).
2. Valid domain or local credentials (username/password or hash) for a user with execute privileges on the target.
3. Network connectivity to the target on ports 135 (WMI) and 445 (SMB).
4. An accessible SMB share on the target (e.g., ADMIN$) for output retrieval; custom shares can be specified if needed.
5. Python 3 environment on the attacker's machine.

## Defense

- Implement least privilege: Restrict user accounts from having remote execution rights via WMI.
- Enable WMI filtering and logging: Use Group Policy to audit WMI events and block unauthorized remote WMI calls.
- Network segmentation: Isolate segments to limit lateral movement; monitor SMB and WMI traffic for anomalous patterns (e.g., unusual DCERPC requests).
- Credential protection: Use protected users groups, LAPS for local admins, and monitor for credential dumping.
- Endpoint detection: Tools like Sysmon can log WMI process creation; EDR solutions often flag Impacket-like traffic.

## Objectives

1. Execute arbitrary commands on a remote Windows host using native WMI protocols.
2. Retrieve command output via SMB without uploading files or establishing interactive shells.
3. Facilitate lateral movement in domain environments with valid credentials.
4. Maintain stealth by mimicking legitimate administrative activities.

## Instructions

### Step 1: Prepare Output Redirection Command

**Context**: WMIExec executes non-interactive commands, so prepare a Windows command that redirects output to a temporary file in an accessible SMB share (e.g., ADMIN$) for later retrieval. This prevents output loss and allows verification. Use a random directory name to avoid conflicts.

**Code** ([[codes/windows-admin-share-output-redirection]]):

```cmd
cmd.exe /Q /c cd 1> \\127.0.0.1\ADMIN$\__RANDOM 2>&1
```

> This command changes the directory (or any diagnostic command) and redirects stdout (1>) and stderr (2>&1) to a file in the ADMIN$ share. Replace `__RANDOM` with a unique identifier (e.g., a timestamp or UUID). After execution, retrieve the file via SMB: `smbclient \\$TARGET\ADMIN$ -U $USERNAME%$PASSWORD` and look for the output file. Expected: A file created in the share containing the command's output, confirming redirection works.

### Step 2: Execute Remote Command Using WMIExec

**Context**: Use Impacket's wmiexec.py to authenticate and execute the prepared command via WMI. Specify credentials, target, and the command. If using a non-default share, include the -share option. This step accomplishes remote execution and output staging.

**Command** ([[commands/impacket-wmiexec-execute-command]]):

```bash
python3 /path/to/impacket/examples/wmiexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET "$_REMOTE_COMMAND" -share $_SHARE
```

> Replace placeholders: $_DOMAIN (e.g., DOMAIN), $_USERNAME/$_PASSWORD (credentials), $_TARGET (IP/hostname), $_REMOTE_COMMAND (e.g., the output redirection from Step 1 or `whoami`), $_SHARE (e.g., ADMIN$). The tool connects via WMI, spawns the command, and stages output in the share. Expected: Console output showing command execution (e.g., "Impacket v0.x.x" followed by command results if interactive, or success message). No errors like "Access denied" indicate success. Retrieve output from the share post-execution.

### Step 3: Retrieve and Verify Output

**Context**: After execution, access the SMB share to fetch the output file. This verifies success and provides results for further actions like parsing or chaining commands.

**Instructions**: Use smbclient or similar to connect: `smbclient //$_TARGET/$_SHARE -U $_DOMAIN\\$_USERNAME%$_PASSWORD`. Navigate to the temporary directory (e.g., __RANDOM) and download the file (e.g., `get output.txt`). Analyze the file contents.

> Expected: File contains the remote command's output (e.g., current directory path for `cd`). If empty or errored, check credentials/share access.
