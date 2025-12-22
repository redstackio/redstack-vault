---
id: af9d0e0e-38db-4c1e-9cac-82200025e31a
name: Windows-Impacket-Psexec-Remote-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.795602+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Valid-Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Remote-Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[sub-techniques/Binary-Padding|T1027.001 - Binary Padding]]'
  - >-
    [[sub-techniques/SMB/Windows-Admin-Shares|T1021.002 - SMB/Windows Admin
    Shares]]
tags:
  - '[[tags/Impacket]]'
  - '[[tags/Windows-Using-Credentials]]'
commands:
  - '[[commands/impacket-psexec-execute-remote-command]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Windows-Impacket-Psexec-Remote-Command-Execution

## Summary

This procedure uses Impacket's psexec.py to execute commands on a remote Windows system over SMB using valid credentials. It enables lateral movement by running arbitrary commands, such as reconnaissance or payload execution, without requiring interactive access.

## Description

Impacket's psexec.py emulates the Sysinternals PsExec tool, connecting to the target via SMB to upload a temporary executable service that runs the specified command. This technique is useful in red team engagements for lateral movement after obtaining credentials, targeting Windows systems with administrative privileges. It maps to MITRE ATT&CK techniques for remote services and valid accounts, often evading detection by mimicking legitimate admin tools. Success depends on SMB access (ports 445) and admin rights on the target.

## Requirements

1. Valid domain or local credentials (username/password or NTLM hash) with administrative privileges on the target Windows system.
2. Network connectivity to the target over SMB (TCP port 445 open).
3. Impacket suite installed on the attacker's machine (Python 3 environment).
4. Target must be a Windows system (XP or later, though modern versions may require SMB signing disabled for full compatibility).

## Defense

- Enforce strong, unique passwords and multi-factor authentication for admin accounts to prevent credential reuse.
- Implement network segmentation to restrict SMB traffic between segments and monitor for anomalous connections to port 445.
- Enable SMB signing and disable NTLMv1; use Windows Defender or EDR to detect suspicious service creation and command execution.
- Log and alert on PsExec-like tools via Sysmon (Event ID 1 for process creation with psexesvc.exe) or network logs showing SMB file writes.

## Objectives

1. Establish remote command execution on the target Windows system using provided credentials.
2. Perform post-exploitation actions like reconnaissance, file transfer, or persistence without direct interactive shell.
3. Verify access and gather system information for further lateral movement.

## Instructions

### Step 1: Prepare Credentials and Target

**Context**: Ensure Impacket is installed and credentials are formatted correctly. Test SMB connectivity if possible using tools like [[commands/smbclient-connect-test]] (optional, not required here).

This step verifies prerequisites without executing the attack.

### Step 2: Execute Remote Command with Psexec

**Context**: Use psexec.py to connect to the target, upload a temporary service binary, and run the desired command. Replace placeholders with actual values; enclose commands with spaces in quotes. This accomplishes remote execution leveraging valid admin credentials.

**Command** ([[commands/impacket-psexec-execute-remote-command]]):
```bash
python3 psexec.py DOMAIN/USERNAME:PASSWORD@TARGET_IP 'cmd.exe /c whoami'
```

> This command authenticates via SMB, uploads the psexesvc.exe service, starts it to run 'whoami', and captures output. Expected output includes the remote user's context (e.g., DOMAIN\username). If using NTLM hash, format as DOMAIN/USERNAME:HASH@TARGET_IP. For hash-based auth (Pass-the-Hash), ensure the hash is in NT format.

### Step 3: Verify Execution and Clean Up

**Context**: Check the output for success and monitor for errors like access denied or SMB connection failures. Psexec automatically removes the temporary service on completion, but verify no artifacts remain.

Run a follow-up command if needed, such as dumping system info:
```bash
python3 psexec.py DOMAIN/USERNAME:PASSWORD@TARGET_IP 'cmd.exe /c systeminfo'
```

> Success is indicated by command output from the remote system without authentication errors. Errors may include 'Access denied' (insufficient privileges) or 'PIPE' issues (SMB signing enforced).
