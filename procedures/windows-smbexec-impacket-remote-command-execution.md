---
id: d7943250-fd0a-4f3f-bf5d-e1de4cd25c8f
name: windows-smbexec-impacket-remote-command-execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.998840+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[sub-techniques/SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin
    Shares]]
tags:
  - '[[tags/Impacket]]'
  - '[[tags/SMBExec]]'
  - '[[tags/Windows - Using credentials]]'
commands:
  - '[[commands/impacket-smbexec-interactive-shell]]'
  - '[[commands/windows-batch-dir-listing]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# windows-smbexec-impacket-remote-command-execution

## Summary

This procedure demonstrates how to use Impacket's SMBExec tool to execute commands on a remote Windows machine via SMB admin shares, leveraging valid administrator credentials for lateral movement or post-exploitation activities such as information gathering or privilege escalation.

## Description

SMBExec exploits the SMB protocol to create a semi-interactive shell on a target Windows system by uploading and executing a service binary that communicates back via named pipes. It requires administrative credentials and network access to the target's SMB port (445). This technique is useful in domain environments for moving laterally between hosts without dropping persistent files, as the service is removed after execution. Common use cases include running reconnaissance commands like directory listings or deploying further payloads. Note that while effective, it generates detectable network traffic and service creation events on the target.

## Requirements

1. Valid domain or local administrator credentials for the target Windows machine.
2. Network connectivity to the target on TCP port 445 (SMB).
3. Impacket suite installed on the attacker's machine (Python 3 environment).
4. Target must have administrative shares (e.g., ADMIN$) enabled and not restricted by SMB signing policies.

## Defense

- Enforce strong, unique passwords and multi-factor authentication for admin accounts.
- Implement network segmentation to restrict lateral SMB traffic between hosts.
- Enable SMB signing and disable NTLMv1; monitor for anomalous SMB connections and service creations via Windows Event Logs (Event ID 7045 for service installs).
- Use endpoint detection tools to alert on unexpected command executions from SMB-related processes.

## Objectives

1. Establish a semi-interactive shell on the remote Windows host for command execution.
2. Perform lateral movement within a network using compromised credentials.
3. Gather system information or execute payloads without direct RDP or PsExec access.
4. Maintain operational security by avoiding persistent artifacts on the target.

## Instructions

### Step 1: Launch SMBExec for Interactive Shell

**Context**: Initiate the connection to the target using SMBExec, which will create a temporary service to pipe commands and output back to your attacker machine. This provides a cmd.exe-like interface for executing commands remotely.

**Command** ([[commands/impacket-smbexec-interactive-shell]]):
```bash
python3 smbexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

> This command authenticates to the target and opens a semi-interactive shell. Replace placeholders with actual values (e.g., DOMAIN=corp, USERNAME=admin, PASSWORD=Passw0rd, TARGET_IP=192.168.1.100). If no domain, use . for local. The shell prompt will appear as '{+} \TARGET_IP\ADMIN$::', allowing you to type commands directly.

**Expected Output**: Successful authentication message followed by a shell prompt. Errors include 'Access Denied' for invalid creds or 'Connection Refused' for network/firewall issues.

### Step 2: Execute Reconnaissance Command via Batch Payload

**Context**: Within the SMBExec shell, execute a batch command to list directory contents and redirect output to a file for exfiltration or review. This demonstrates non-interactive command execution and uses a temporary batch file to chain actions while cleaning up afterward.

**Code** ([[codes/windows-batch-dir-listing-payload]]):
```bash
%COMSPEC% /Q /c echo dir > \\127.0.0.1\C$\__output 2>&1 > %TEMP%\execute.bat & %COMSPEC% /Q /c %TEMP%\execute.bat & del %TEMP%\execute.bat
```

> Paste this payload directly into the SMBExec shell. It creates a batch file in TEMP, runs 'dir' to output to C$\__output (accessible via SMB), executes it quietly, and deletes the batch file. The /Q flag suppresses output, and 2>&1 captures errors.

**Expected Output**: No visible output in the shell if successful (due to /Q), but check the __output file on the target via SMB share for directory listing contents.

### Step 3: Retrieve and Review Output

**Context**: After execution, access the output file created on the target to verify success and gather information. This step confirms the command ran and provides data for further analysis.

**Command** ([[commands/windows-batch-dir-listing]]):
```bash
smbclient \\_TARGET_IP\C$ -U $_DOMAIN/$_USERNAME%$_PASSWORD
```

> Use smbclient (from Impacket or Samba) to connect to the ADMIN$ share and download __output. Navigate with 'cd \', then 'get __output' to retrieve the file locally. Delete it afterward with 'rm __output' to clean up.

**Expected Output**: Successful share mount and file download. The __output file contains the 'dir' listing, e.g., ' Volume in drive C is Windows ... Directory of C:\\ ...'. If file not found, the payload failed.
