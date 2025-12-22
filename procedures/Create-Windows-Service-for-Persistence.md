---
id: 4478d6f9-3c4a-4103-9662-a3838c4c99df
name: Create-Windows-Service-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.968713+00:00'
updated_at: '2023-04-10T20:37:24.622346+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Service Execution|T1035 - Service Execution]]'
  - >-
    [[techniques/Service Registry Permissions Weakness|T1058 - Service Registry
    Permissions Weakness]]
sub_techniques: []
tags:
  - '[[tags/Serviceland]]'
  - '[[tags/Windows - Persistence]]'
  - '[[tags/Windows Service]]'
commands:
  - '[[commands/sharpersist-add-service-persistence]]'
platforms:
  - Windows
tools:
  - '[[tools/SharPersist]]'
validated: true
---

# Create-Windows-Service-for-Persistence

## Summary

This procedure demonstrates how to establish persistence on a Windows system by creating a malicious service that executes a benign process like the Calculator (calc.exe) to mask activity. Using the SharPersist tool, it configures the service to run automatically on system startup, allowing attackers to maintain long-term access for data exfiltration, malware deployment, or further compromise.

## Description

In this technique, attackers leverage Windows service mechanisms to achieve persistence. A new service is registered in the Windows Registry using the 'sc' command or tools like SharPersist, pointing to a command execution chain that launches calc.exe as a disguise. The service starts automatically upon boot, executing the payload without user interaction. This is particularly effective in environments with weak service registry permissions (T1058), enabling execution (T1035) for persistence (TA0003). The target environment is a Windows workstation or server with administrative privileges. Success results in the service running indefinitely, providing a foothold for subsequent actions like lateral movement or data collection.

## Requirements

1. Administrator-level access to the target Windows system.
2. SharPersist tool available and executable on the system (downloaded or compiled C# binary).
3. The target executable (e.g., calc.exe) must exist in the system path (C:\Windows\System32).
4. PowerShell execution policy allowing script runs (or bypass if restricted).

## Defense

- Implement and enforce the principle of least privilege to restrict access to critical systems and services.
- Regularly monitor system logs (Event ID 7045 for service installations) and network traffic for signs of suspicious activity.
- Use endpoint protection software to detect and prevent the installation of malicious services, including behavioral analysis for unusual process spawning.

## Objectives

1. To maintain persistent access to a compromised system across reboots.
2. To exfiltrate sensitive data without detection.
3. To install additional malware for further compromise.
4. To carry out other malicious activities under the guise of legitimate processes.

## Instructions

### Step 1: Prepare SharPersist Tool

**Context**: Ensure the SharPersist executable is available on the target system. This tool simplifies service creation for persistence by handling registry modifications and service configuration.

Download or transfer SharPersist.exe to a temporary location, such as C:\temp\SharPersist.exe. Verify it runs without errors by checking its help output.

### Step 2: Create the Persistent Service

**Context**: Use SharPersist to register a new service that executes cmd.exe with arguments to launch calc.exe. This step configures the service for automatic startup, achieving persistence.

**Command** ([[commands/sharpersist-add-service-persistence]]):

```powershell
SharPersist.exe -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Service" -m add
```

> This command specifies the service type (-t service), the executable to run (-c cmd.exe), arguments to pass (-a /c calc.exe for launching Calculator), service name (-n), and mode to add the service (-m add). Expected output includes confirmation of service creation, such as "Service 'Some Service' added successfully." Verify by checking services.msc or running `sc query "Some Service"`, which should show STATE: 1 STOPPED (or 4 RUNNING if started).

### Step 3: Verify and Start the Service

**Context**: Confirm the service is installed and test its execution to ensure persistence works as intended.

Use the built-in `sc start "Some Service"` command to start it manually. Observe calc.exe launching. Reboot the system and check if the service auto-starts (via Event Viewer or process monitoring). If issues arise, check registry at HKLM\SYSTEM\CurrentControlSet\Services\Some Service for modifications.
