---
id: a6df01bd-c86e-4af6-96c4-1e060beef4fe
name: WMI-Remote-Process-Creation-via-WMIC
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.258203+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Windows Management Instrumentation|T1047 - Windows Management
    Instrumentation]]
sub_techniques: []
tags:
  - '[[tags/Windows - Using credentials]]'
  - '[[tags/WMI Protocol]]'
commands:
  - '[[commands/wmic-remote-process-create]]'
platforms:
  - Windows
tools: []
validated: true
---

# WMI-Remote-Process-Creation-via-WMIC

## Summary

This procedure demonstrates how to use the Windows Management Instrumentation Command-line (WMIC) tool to create and execute a process on a remote Windows machine, such as launching the Calculator application (calc.exe). It leverages the WMI protocol for remote command execution, requiring valid credentials for the target system. This technique is commonly used in lateral movement scenarios within Windows environments.

## Description

WMI Remote Process Creation via WMIC allows attackers with valid domain credentials to execute arbitrary commands on remote Windows hosts without needing additional tools. The WMIC utility interacts with the WMI service (winmgmt) to invoke the Win32_Process class's Create method, spawning a new process on the target. This is particularly effective in Active Directory environments where domain admin or local admin credentials are available. The technique assumes the WMI service is enabled on the target (default on Windows) and that firewall rules permit DCOM/WMI traffic over ports 135 and dynamic RPC ports. Success results in the remote execution of the specified binary, enabling further post-exploitation activities like shell spawning or payload delivery. Note that modern Windows versions may log this activity via Event ID 19 in the Microsoft-Windows-WMI-Activity/Operational log.

## Requirements

1. Valid domain or local administrator credentials for the target machine.
2. Network connectivity to the target over WMI ports (TCP 135 and high-range RPC ports 49152-65535).
3. WMIC tool available on the attacker's machine (pre-installed on Windows; can be installed on Linux via Samba tools).
4. Target machine running Windows with WMI service enabled (default).

## Defense

- Restrict WMI access using Group Policy to limit remote execution to authorized users only (e.g., enable WMI firewall rules selectively).
- Monitor WMI activity through Windows Event Logs (Event IDs 5857, 5858 for WMI connections; 19 for process creation).
- Implement Just Enough Administration (JEA) and constrained delegation to prevent credential abuse.
- Use network segmentation and endpoint detection tools to alert on anomalous WMIC usage from non-administrative hosts.

## Objectives

1. Remotely execute a process on a target Windows machine to establish command execution capability.
2. Facilitate lateral movement within a domain environment using stolen credentials.
3. Verify remote access for further privilege escalation or persistence.
4. Demonstrate execution without dropping additional binaries on the target.

## Instructions

### Step 1: Verify WMI Connectivity

**Context**: Before executing the remote process, confirm that WMI communication is possible with the target to avoid authentication errors. This step uses a simple query to test the connection without creating processes.

**Command** ([[commands/wmic-remote-process-create]] with query variation):
```cmd
wmic /node:$_TARGET_HOST /user:$_DOMAIN\$_USERNAME /password:$_PASSWORD process list brief
```

> This command lists running processes on the remote host to validate credentials and WMI access. Replace placeholders with actual values. If successful, it returns a table of processes; errors indicate credential or network issues.

### Step 2: Create Remote Process

**Context**: Once connectivity is confirmed, use WMIC to invoke the creation of a new process on the target, such as calc.exe for testing. This step directly maps to the Win32_Process.Create WMI method.

**Command** ([[commands/wmic-remote-process-create]]):
```cmd
wmic /node:$_TARGET_HOST /user:$_DOMAIN\$_USERNAME /password:$_PASSWORD process call create "$_PROCESS_PATH"
```

> This launches the specified executable (e.g., calc.exe) on the remote machine. The command outputs a process ID if successful. For calc.exe, use "C:\Windows\System32\calc.exe" as the path. If the process requires interaction, it may not be visible remotely, but non-interactive binaries (e.g., cmd.exe /c whoami > C:\output.txt) can be used for verification.

### Step 3: Verify Process Execution

**Context**: After creation, query the target to confirm the process started and check for any output or side effects, ensuring the technique succeeded.

**Command** ([[commands/wmic-remote-process-create]] with query):
```cmd
wmic /node:$_TARGET_HOST /user:$_DOMAIN\$_USERNAME /password:$_PASSWORD process where "name='$_PROCESS_NAME.exe'" get processid
```

> This retrieves the process ID of the launched executable (e.g., name='calc'). A non-zero PID indicates success. For file-output payloads, retrieve the file via SMB or additional WMI queries.
