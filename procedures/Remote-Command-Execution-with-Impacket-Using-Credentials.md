---
id: 1d5706bb-b899-46cc-a6d5-cf1ce92b19fd
name: Remote-Command-Execution-with-Impacket-Using-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.853585+00:00'
updated_at: '2023-10-10T20:37:57.917393+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Pass the Hash|T1550.002 - Pass the Hash]]'
  - '[[techniques/SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
  - >-
    [[techniques/Windows Management Instrumentation|T1047 - Windows Management
    Instrumentation]]
sub_techniques: []
tags:
  - Impacket
  - Windows
  - Lateral Movement
  - Remote Execution
  - Credentials
commands:
  - '[[commands/set-local-account-token-filter-policy]]'
  - '[[commands/enable-administrator-token-filter]]'
  - '[[commands/impacket-atexec-execute-command]]'
  - '[[commands/impacket-dcomexec-execute-command]]'
  - '[[commands/impacket-wmiexec-execute-with-ntlm-hash]]'
  - '[[commands/impacket-wmiexec-execute-with-password]]'
  - '[[commands/impacket-psexec-execute-command]]'
  - '[[commands/impacket-smbexec-execute-command]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Remote-Command-Execution-with-Impacket-Using-Credentials

## Summary

This procedure uses Impacket tools to execute remote commands on Windows targets via protocols like SMB, DCOM, WMI, and Task Scheduler, leveraging valid credentials or NTLM hashes for authentication. It enables lateral movement and remote administration in a Windows domain environment, bypassing some UAC restrictions through registry modifications.

## Description

Impacket provides Python-based implementations for interacting with Windows network protocols, allowing attackers with stolen credentials to perform remote command execution without dropping additional binaries on the target. This technique is commonly used post-credential acquisition for lateral movement, such as from a compromised workstation to a domain controller. The procedure covers multiple execution methods (PsExec-like, SMBExec, AtExec, DComExec, WmiExec) and preparatory registry changes to ensure compatibility with non-elevated accounts. It assumes the attacker has domain or local admin credentials and network access to the target over ports 445 (SMB), 135 (RPC/DCOM/WMI). Success results in command output returned to the attacker, enabling further actions like privilege escalation or data exfiltration.

## Requirements

1. Valid domain or local administrator credentials (username/password) or NTLM hash for the target.
2. Network access to the target Windows machine (ports 445/TCP for SMB, 135/TCP for RPC, dynamic high ports for WMI/DCOM).
3. Impacket suite installed on the attacker's Kali Linux or similar machine.
4. Python 3 environment with required dependencies (e.g., pyasn1, cryptography).

## Defense

- Implement least privilege access and monitor for anomalous remote executions via Windows Event Logs (ID 4688, 5145 for SMB).
- Enable UAC remote restrictions and monitor registry changes to Policies\System keys.
- Use network segmentation, credential guard (LSA Protection), and tools like Microsoft Defender for Endpoint to detect Impacket traffic patterns (e.g., unusual SMB/RPC over non-standard ports).
- Rotate credentials regularly and enforce MFA for admin accounts.

## Objectives

1. Establish remote command execution capability on the target Windows machine.
2. Facilitate lateral movement using valid or hashed credentials.
3. Bypass UAC remote execution filters if necessary.
4. Retrieve command output for situational awareness or further exploitation.

## Instructions

### Step 1: Set Local Account Token Filter Policy

**Context**: Modify the registry to disable UAC remote token filtering, allowing non-RID 500 local admins to perform remote administrative tasks via SMB/WMI without full elevation prompts. This is a prerequisite for tools like PsExec and WmiExec when using non-built-in admin accounts.

**Command** ([[commands/set-local-account-token-filter-policy]]):
```bash
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1
```

> This command adds or sets the LocalAccountTokenFilterPolicy DWORD to 1, which relaxes remote UAC restrictions. Run this on the target if you have initial access, or remotely if credentials allow. Expected: "The operation completed successfully." Verify with `reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy` showing value 0x1 (1).

### Step 2: Enable Administrator Token Filter

**Context**: Optionally enable token filtering for the built-in Administrator account to restrict its remote capabilities, but in offensive contexts, this may be adjusted or checked to understand target hardening. Note: Setting to 1 enables filtering (restricts), but the procedure uses it to assess or modify for compatibility.

**Command** ([[commands/enable-administrator-token-filter]]):
```bash
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken /t REG_DWORD /f /d 1
```

> This sets FilterAdministratorToken to 1, enabling UAC filtering for admin tokens. In attacks, confirm it's 0 (disabled) for easier remote access. Expected: "The operation completed successfully." If set to 1, remote execution with built-in admin may fail, requiring workarounds.

### Step 3: Execute via PsExec Equivalent

**Context**: Use psexec.py to upload and execute a service binary (RemComSvc) for interactive shell access, mimicking Sysinternals PsExec. Ideal for initial remote shell establishment.

**Command** ([[commands/impacket-psexec-execute-command]]):
```bash
psexec.py DOMAIN/username:password@10.10.10.10
```

> Authenticates via SMB and deploys a temporary service for command execution. Expected: Interactive shell prompt (e.g., "C:\Windows\system32> ") where you can run commands like `whoami`. Output includes target info and shell interaction. Use `-debug` for verbose logging.

### Step 4: Execute via SMBExec

**Context**: Leverage SMB for semi-interactive execution without file drops, using named pipes for command relay. Useful when service installation is blocked.

**Command** ([[commands/impacket-smbexec-execute-command]]):
```bash
smbexec.py DOMAIN/username:password@10.10.10.10
```

> Establishes SMB connection and executes commands via pipe. Expected: Shell-like interface with command output (e.g., "dir" lists files). Includes share creation/cleanup logs. Less detectable than PsExec as no persistent service.

### Step 5: Execute via AtExec (Task Scheduler)

**Context**: Schedule tasks via AT service for command execution, retrieving output through SMB pipes. Bypasses some EDR monitoring on direct execution.

**Command** ([[commands/impacket-atexec-execute-command]]):
```bash
atexec.py DOMAIN/username:password@10.10.10.10
```

> Creates temporary scheduled tasks and captures stdout. Expected: Command prompt and output (e.g., `net user` shows users). Tasks auto-delete post-execution. Note: AT service deprecated in newer Windows; falls back if unavailable.

### Step 6: Execute via DComExec

**Context**: Use DCOM/RPC for remote execution via WMI or CLSID, providing semi-interactive shell. Effective against hosts with SMB restricted but RPC open.

**Command** ([[commands/impacket-dcomexec-execute-command]]):
```bash
dcomexec.py DOMAIN/username:password@10.10.10.10
```

> Authenticates via RPC and spawns cmd.exe. Expected: Interactive DOS prompt (e.g., "Microsoft Windows [Version...]> ") with command output. Uses dynamic ports post-135.

### Step 7: Execute via WmiExec with Password

**Context**: WMI-based execution for stealthy, fileless command running. Returns output via WMI queries; supports both password and hash auth.

**Command** ([[commands/impacket-wmiexec-execute-with-password]]):
```bash
wmiexec.py DOMAIN/username:password@10.10.10.10
```

> Connects via WMI (ports 135 + high port) for command execution. Expected: Non-interactive output (e.g., `whoami /all` results prefixed with [*]). Cleaner than shells; no prompt but pipes output directly.

### Step 8: Execute via WmiExec with NTLM Hash

**Context**: Same as above but using pass-the-hash for credentialless password exposure. Preferred when only hashes are available (e.g., from LSASS dump).

**Command** ([[commands/impacket-wmiexec-execute-with-ntlm-hash]]):
```bash
wmiexec.py DOMAIN/username@10.10.10.10 -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

> Uses NTLM hash for auth instead of password. Expected: Same WMI output as password variant. Replace hash with target-specific LM:NTLM values. If hash invalid, fails with auth error.
