---
id: 1f29e6e5-06d9-49bf-875e-786c7219385f
name: windows-elevated-services-backdoor-persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.105024+00:00'
updated_at: '2023-04-10T20:37:29.706530+00:00'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Service Execution]]'
  - '[[Windows Service]]'
sub_techniques: []
tags:
  - elevated
  - services-elevated
  - windows-persistence
commands:
  - '[[commands/create-backdoor-service-powershell]]'
  - '[[commands/start-backdoor-service-sc]]'
  - '[[commands/create-backdoor-persistence-sharpersist]]'
  - '[[commands/create-backdoor-service-sc]]'
  - '[[commands/start-backdoor-service-sc]]'
platforms:
  - Windows
tools:
  - '[[tools/sharpersist]]'
validated: true
---

# windows-elevated-services-backdoor-persistence

## Summary

This procedure creates a backdoor Windows service that runs with elevated (SYSTEM) privileges to establish persistent access on a compromised host. It covers multiple methods including native PowerShell cmdlets, the sc utility, and the SharPersist tool, allowing attackers to maintain access across reboots for further post-exploitation activities like data exfiltration or lateral movement.

## Description

In a Windows environment, services can be configured to run automatically with high privileges, making them an ideal persistence mechanism. This procedure assumes the attacker has already obtained administrative access and a backdoor executable (e.g., backdoor.exe) placed on the target. The backdoor service executes this payload upon startup or on-demand, evading basic detection if disguised properly. It targets the Service Registry Permissions Weakness by leveraging weak default permissions on service keys and uses Service Execution to run malicious code. Success provides a reliable foothold for long-term compromise, but requires careful configuration to avoid triggering endpoint detection.

## Requirements

1. Administrative privileges (LocalSystem or equivalent) on the target Windows system.
2. A backdoor executable (e.g., backdoor.exe) uploaded to a writable path like C:\Windows\Temp\.
3. PowerShell execution policy allowing script execution (or bypass if restricted).
4. For SharPersist method: The SharPersist.exe binary downloaded and executed on the target.

## Defense

- Regularly audit service configurations using tools like Authoritas or PowerShell's Get-Service/Get-WmiObject Win32_Service to detect unauthorized services.
- Implement least-privilege principles by tightening service registry permissions (e.g., via Group Policy) to prevent weak access controls.
- Enable Windows Defender Application Control (WDAC) or AppLocker to block unsigned executables from running as services.
- Monitor event logs for service creation events (Event ID 7045 in System log) and anomalous process executions from svchost.exe or services.exe.

## Objectives

1. Create a new elevated service that executes a backdoor payload with persistence.
2. Ensure the service starts automatically or on-demand to maintain access post-reboot.
3. Verify service creation and execution without immediate detection.

## Instructions

### Step 1: Prepare Backdoor Executable

**Context**: Ensure the backdoor payload is in place on the target. This step assumes prior file transfer (e.g., via SMB or initial shell). The executable should be a silent, non-interactive binary that performs the desired actions (e.g., reverse shell).

Upload backdoor.exe to C:\Windows\Temp\backdoor.exe using an existing shell or tool like certutil.

### Step 2: Create Service Using PowerShell

**Context**: Use native PowerShell to register a new service pointing to the backdoor executable. This method is stealthy as it mimics legitimate service creation and runs under SYSTEM.

**Command** ([[commands/create-backdoor-service-powershell]]):

```powershell
New-Service -Name "Backdoor" -BinaryPathName "C:\Windows\Temp\backdoor.exe" -Description "Nothing to see here." -StartupType Automatic
```

> This registers the service with automatic startup. If successful, the service will execute the binary on boot or manual start.

### Step 3: Start the Service Using SC

**Context**: Manually start the newly created service to immediately activate the backdoor. Use the sc command for compatibility across methods.

**Command** ([[commands/start-backdoor-service-sc]]):

```cmd
sc start Backdoor
```

> The service process spawns, executing the backdoor. Monitor for errors like invalid binary path.

### Step 4: Alternative - Create Service Using SC Utility

**Context**: If PowerShell is restricted, use the built-in sc.exe to create the service directly via command line. This wraps the backdoor in cmd.exe for execution.

**Command** ([[commands/create-backdoor-service-sc]]):

```cmd
sc create Backdoor binpath= "cmd.exe /k C:\temp\backdoor.exe" start= "auto" obj= "LocalSystem"
```

> Creates the service with auto-start and SYSTEM privileges. The /k flag keeps cmd open to run the executable.

### Step 5: Alternative - Create Persistence Using SharPersist

**Context**: For advanced persistence, use the SharPersist tool to create a service-based backdoor. This tool handles registry modifications securely and can be more evasive.

**Command** ([[commands/create-backdoor-persistence-sharpersist]]):

```cmd
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c backdoor.exe" -n "Backdoor" -m add
```

> Adds the service via SharPersist, which executes cmd.exe to run the backdoor. Verify with sc query Backdoor.

### Step 6: Verify Persistence

**Context**: Confirm the service is registered and functional. Reboot the system (if possible) to test auto-start.

Run `sc query Backdoor` to check status. Expected: STATE: 4 RUNNING or similar.
