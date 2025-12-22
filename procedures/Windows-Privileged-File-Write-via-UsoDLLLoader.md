---
id: 9df4bfb6-b9cc-4781-892c-a3c835aa6e75
name: Windows-Privileged-File-Write-via-UsoDLLLoader
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.353930+00:00'
updated_at: '2023-04-10T20:37:40.964274+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
  - >-
    [[techniques/File Permissions Modification|T1222 - File Permissions
    Modification]]
sub_techniques: []
tags:
  - '[[tags/EoP - Privileged File Write]]'
  - '[[tags/UsoDLLLoader]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/PowerShell-Get-DLL-Properties]]'
  - '[[commands/CMD-List-System32-Contents]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Privileged-File-Write-via-UsoDLLLoader

## Summary

This procedure exploits the UsoDLLLoader COM interface on Windows systems to achieve privileged file writes by loading a malicious DLL into a SYSTEM-privileged process. By manipulating the DLL search order, an attacker with low-privileged access can force the system to load and execute arbitrary code as SYSTEM, enabling writes to protected directories like System32 for persistence or further escalation.

## Description

The UsoDLLLoader interface, part of Windows Update services, runs with high privileges and searches for DLLs in user-writable locations before system paths. An attacker can place a malicious DLL in such a location (e.g., current working directory or %PATH%), then trigger the interface via COM invocation. When loaded, the DLL executes in the context of the svchost.exe process running as SYSTEM, allowing file operations on restricted areas. This technique is effective on Windows 7 through 11, provided the attacker has local execution rights. It combines DLL hijacking with COM abuse for privilege escalation and evasion, bypassing standard file permission checks.

## Requirements

1. Local access to a Windows system (user-level privileges sufficient for execution).
2. Ability to write files to a directory in the DLL search order (e.g., current directory or a writable PATH entry).
3. A compiled malicious DLL that performs the desired file write operation (e.g., using C++ or a tool like msfvenom for shellcode injection).
4. PowerShell or CMD access for COM invocation and verification.

## Defense

- Apply least privilege principles: Restrict user accounts from executing unsigned binaries or modifying PATH.
- Monitor COM interface invocations and DLL loads via ETW (Event Tracing for Windows) or Sysmon (Event ID 7 for ImageLoad).
- Harden DLL search order by setting SafeDLLSearchMode registry key and removing writable directories from PATH.
- Regularly audit file creations in protected directories like System32 using file integrity monitoring tools.
- Keep Windows updated to mitigate known COM-related vulnerabilities.

## Objectives

1. Achieve SYSTEM-level file write access to protected system directories.
2. Establish persistence by planting malicious DLLs or executables in System32.
3. Facilitate further privilege escalation or lateral movement post-exploitation.

## Instructions

### Step 1: Verify Target DLL and System Environment

**Context**: Confirm the presence of the vulnerable DLL (e.g., windowscoredeviceinfo.dll or similar in the chain) and check its properties to ensure the target environment supports the exploit. This step identifies if the system is patchable or if search order hijacking is feasible.

**Command** ([[commands/PowerShell-Get-DLL-Properties]]):
```powershell
Get-ItemProperty -Path "C:\Windows\System32\windowscoredeviceinfo.dll"
```

> This PowerShell command retrieves file properties like version, size, and last modified date. Use it to verify the DLL exists and note its location for hijacking planning. If the file is missing or protected, abort or pivot to another DLL in the UsoDLLLoader chain.

### Step 2: Inspect System32 Directory for Write Feasibility

**Context**: Examine the contents and permissions of the System32 directory to identify potential write targets and confirm low-priv write restrictions. This informs where to place the output of the privileged write.

**Command** ([[commands/CMD-List-System32-Contents]]):
```cmd
dir C:\Windows\System32
```

> Run this in CMD to list files in System32. Look for writable subpaths or confirm protections. Success is indicated by the directory listing without access denied errors; note key system files for targeting in the malicious DLL payload.

### Step 3: Prepare Malicious DLL Placement

**Context**: Compile or obtain a malicious DLL that, when loaded, performs the file write (e.g., copies a payload to System32\malicious.exe). Place it in a hijackable location like the current directory, which precedes System32 in the search order when UsoDLLLoader is triggered.

**Instructions**: Use a development tool to build the DLL with DllMain exporting the file write logic (e.g., CreateFile with SYSTEM privileges). Copy the DLL to %CD%\windowscoredeviceinfo.dll. No command reference here as this is manual preparation; verify placement with Step 1 command.

### Step 4: Trigger UsoDLLLoader via COM

**Context**: Invoke the UsoDLLLoader interface to force loading of the hijacked DLL as SYSTEM, executing the file write.

**Instructions**: In PowerShell, use New-Object to instantiate the COM object:
```powershell
$uso = [activator]::CreateInstance([type]::GetTypeFromCLSID("{some-guid-for-usodllloader}"))
$uso.SomeMethod()
```

> Replace with actual CLSID and method for UsoDLLLoader (research via regsvr32 or OLEView). The interface call loads the DLL from the search path, running the payload. Monitor with ProcMon for confirmation.

### Step 5: Verify Privileged Write

**Context**: Confirm the file write succeeded by checking for the new file in System32 using the listing command from Step 2.

**Instructions**: Re-run the directory list command. If the malicious file appears, the exploit worked; execute it for persistence or escalation.

## Expected Output

Successful execution results in a new file (e.g., backdoor.dll) appearing in C:\Windows\System32, verifiable via directory listing showing creation time matching the exploit timestamp. No errors in COM invocation, and Event Viewer may log DLL load events under SYSTEM.
