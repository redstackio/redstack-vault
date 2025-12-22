---
id: 05d7c53e-9d16-4829-b860-7913a701a8b5
name: efs-potato-privilege-escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.245336+00:00'
updated_at: '2023-04-10T20:37:54.190558+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/EFSPotato (MS-EFSR EfsRpcOpenFileRaw)]]'
  - '[[tags/EoP - Impersonation Privileges]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/compile-efs-potato-cs-dotnet-4x-default]]'
  - '[[commands/compile-efs-potato-cs-dotnet-4x-x86]]'
  - '[[commands/compile-efs-potato-cs-dotnet-35-default]]'
  - '[[commands/compile-efs-potato-cs-dotnet-35-x86]]'
  - '[[commands/execute-efs-potato-elevate-process]]'
platforms:
  - Windows
tools: []
validated: true
---

# efs-potato-privilege-escalation

## Summary

EFSPotato is a privilege escalation technique that exploits a vulnerability in the Microsoft Encrypting File System Remote Protocol (EFSRPC) to impersonate other users and open files with SYSTEM privileges. This allows attackers to bypass User Account Control (UAC) and execute arbitrary code with elevated privileges on Windows systems, typically from a medium integrity level process.

## Description

EFSPotato exploits a race condition in the EFSRPC protocol, specifically the EfsRpcOpenFileRaw function. The attacker creates a hard link to a target file, opens it via EFSRPC, and then races to replace the hard link with a symbolic link pointing to a file controlled by the attacker. This impersonates the file owner (often SYSTEM) and enables spawning elevated processes. It is effective on unpatched Windows 7 through Windows 10 systems where .NET Framework is installed. This technique is useful in post-exploitation scenarios to gain administrator or SYSTEM access from a standard user context, enabling further actions like persistence or lateral movement.

## Requirements

1. Windows 7-10 (unpatched for EFSRPC vulnerability)
2. .NET Framework 2.0/3.5 or 4.x installed for compilation
3. EfsPotato.cs source code available on the target or transferable system
4. Medium integrity access (standard user privileges) to execute the compiled binary
5. SeImpersonatePrivilege or equivalent for the impersonation to succeed

## Defense

Defensive measures and detection strategies:

- Apply the latest security patches to mitigate the EFSRPC vulnerability (e.g., MS17-010 and later for related issues)
- Implement the principle of least privilege to restrict user escalation capabilities
- Monitor for suspicious activity, such as unusual hard link or symbolic link creations, EFSRPC calls, or execution of compiled .NET binaries from temporary locations
- Enable UAC with secure desktop and monitor for UAC bypass attempts via process monitoring tools like Sysmon

## Objectives

1. Gain elevated privileges on the target system
2. Bypass User Account Control (UAC)
3. Achieve persistence on the target system

## Instructions

### Step 1: Obtain EfsPotato Source Code

**Context**: The EfsPotato.cs C# source must be present on the target system. This step ensures the file is available for compilation. Why: Without the source, compilation cannot proceed.

Download or transfer EfsPotato.cs from a trusted repository (e.g., GitHub hfiref0x/EfsPotato) to a writable directory like %TEMP%.

**Expected Output**: EfsPotato.cs file saved in the current directory.

**Success Indicators**:
- File exists and is readable: `dir EfsPotato.cs`
- No download errors or access denied messages

### Step 2: Compile EfsPotato

**Context**: Compile the C# source into an executable using the system's .NET compiler (csc.exe). Select the version based on the target's .NET installation—use .NET 4.x for modern systems or .NET 3.5 for older/compatibility. Why: The compiled binary is required to exploit the EFSRPC vulnerability; 32-bit (x86) may be needed if targeting 32-bit processes.

For .NET 4.x (default 64-bit):

**Command** ([[commands/compile-efs-potato-cs-dotnet-4x-default]]):
```cmd
csc EfsPotato.cs
```

> Compiles EfsPotato.cs into EfsPotato.exe (64-bit). If successful, no output is shown; check for EfsPotato.exe file creation.

For .NET 4.x (32-bit):

**Command** ([[commands/compile-efs-potato-cs-dotnet-4x-x86]]):
```cmd
csc /platform:x86 EfsPotato.cs
```

> Compiles a 32-bit version. Success: EfsPotato.exe created without errors.

For .NET 3.5 (default 64-bit, if .NET 4.x unavailable):

**Command** ([[commands/compile-efs-potato-cs-dotnet-35-default]]):
```cmd
C:\Windows\Microsoft.Net\Framework\v3.5\csc.exe EfsPotato.cs
```

> Uses legacy compiler. Success: No compiler errors, EfsPotato.exe generated.

For .NET 3.5 (32-bit):

**Command** ([[commands/compile-efs-potato-cs-dotnet-35-x86]]):
```cmd
C:\Windows\Microsoft.Net\Framework\v3.5\csc.exe /platform:x86 EfsPotato.cs
```

> 32-bit legacy compile. Success: EfsPotato.exe (x86) created.

If compilation fails (e.g., missing references), ensure .NET is installed and path is correct.

**Expected Output**: EfsPotato.exe file in the current directory; no error messages like "error CSxxxx".

**Success Indicators**:
- `dir EfsPotato.exe` shows the file
- File size ~10-20 KB

### Step 3: Execute for Privilege Escalation

**Context**: Run the compiled EfsPotato.exe to impersonate SYSTEM via EFSRPC and spawn an elevated process. Specify the target program (e.g., cmd.exe for a shell). Why: This triggers the race condition exploit to bypass UAC and gain high integrity.

**Command** ([[commands/execute-efs-potato-elevate-process]]):
```cmd
EfsPotato.exe cmd.exe
```

> Launches an elevated cmd.exe. The exploit runs silently; if successful, a new process spawns with elevated token.

Decision point: If targeting PowerShell, use `EfsPotato.exe powershell.exe`. For silent execution, pipe output or run hidden.

**Expected Output**: A new command prompt window opens with elevated privileges (title: "Administrator: C:\Windows\system32\cmd.exe" or similar). Run `whoami /priv` to confirm SYSTEM-level privileges.

**Success Indicators**:
- New process runs with high integrity (check via Task Manager or `whoami /groups` shows Mandatory Label\High Mandatory Level)
- No error like "Access denied" or exploit failure

## Expected Output

Successful execution results in an elevated process running as SYSTEM or Administrator, bypassing UAC without prompts. Sample output from elevated cmd: `C:\Windows\system32> whoami` returns `nt authority\system`.
