---
type: tool
description: >-
  A advanced library injection technique that loads DLLs directly from memory
  into a host process without relying on the Windows file system or standard
  loader APIs, enhancing stealth and evasion.
url: 'https://www.advancedpersistentthreat.com/2011/07/reflective-dll-injection.html'
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - injection
  - dll
  - reflective
  - code-execution
  - evasion
commands:
  - '[[commands/powershell-invoke-reflective-pe-injection-dll]]'
validated: true
---

# reflective-dll-injection

**Status**: Unverified

## Overview

Reflective DLL Injection is a sophisticated code injection technique that enables the loading and execution of a Dynamic Link Library (DLL) entirely within the memory space of a target process. Unlike traditional DLL loading methods that write files to disk and use LoadLibrary, this approach performs all operations in memory, reducing forensic footprints and evading common detection mechanisms. It is commonly used in red team operations, malware development, and penetration testing for privilege escalation, persistence, and lateral movement.

## Description

The technique leverages reflective programming principles where the DLL contains its own loader code to resolve imports, relocate addresses, and execute its entry point without external dependencies on the host's loader. Originally developed by Stephen Fewer, it maps the DLL as a raw PE (Portable Executable) file into memory and uses custom parsing to handle sections, imports, and TLS callbacks. This makes it ideal for scenarios requiring in-memory execution to avoid antivirus signatures on disk artifacts. Implementations exist in C/C++, PowerShell (via PowerSploit), and .NET (C# reflective loaders).

## Features

- Feature 1: In-memory loading to avoid disk writes and file-based detection
- Feature 2: Self-contained relocation and import resolution for portability across processes
- Feature 3: Support for both reflective DLLs and PE executables (via extensions like Reflective PE Injection)
- Feature 4: Evasion of API monitoring by avoiding calls to LoadLibrary or CreateRemoteThread
- Feature 5: Customizable for specific architectures (x86/x64)

## Installation

### Requirements

- Windows OS (XP or later, tested on Windows 7-11)
- Development environment for custom loaders (Visual Studio for C/C++, or PowerShell for scripting)
- PowerSploit module for PowerShell-based implementations

### Install Commands

For PowerShell implementation using PowerSploit:

```powershell
# Clone PowerSploit repository
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/CodeExecution/Invoke-ReflectivePEInjection.ps1' -OutFile 'Invoke-ReflectivePEInjection.ps1'
# Or import the module
Import-Module .\PowerSploit\CodeExecution\Invoke-ReflectivePEInjection.ps1
```

For C/C++ implementation:

```bash
# Clone original reflective DLL loader (requires Visual Studio)
git clone https://github.com/stephenfewer/ReflectiveDLLInjection
# Build with MSVC
cl /DUNICODE /D_UNICODE ReflectiveLoader.c dll.c /link /DLL /OUT:reflective.dll
```

On Kali Linux for cross-compilation:

```bash
# Install MinGW-w64 for Windows cross-compile
apt install mingw-w64
# Compile (example)
i686-w64-mingw32-gcc -c ReflectiveLoader.c -o ReflectiveLoader.o
```

## Basic Usage

```powershell
Get-Help Invoke-ReflectivePEInjection -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -PEBytes | Byte array of the PE file to inject |
| -LHost | For network-based delivery (if extended) |
| -ForceASLR | Enable ASLR for the injected module |
| -ExeArgs | Arguments for the PE entry point |

## Examples

### Example 1: Basic Usage

Inject a DLL into the current process using PowerShell:

```powershell
$DLLBytes = Get-Content -Path 'C:\path\to\reflective.dll' -Encoding Byte
Invoke-ReflectivePEInjection -PEBytes $DLLBytes -ExeArgs ''
```

### Example 2: Advanced Usage

Inject into a remote process (requires process handle):

```powershell
# First, get process ID and handle (via other means)
$ProcId = 1234
$ProcHandle = OpenProcess 0x1F0FFF 0 $ProcId
Invoke-ReflectivePEInjection -PEBytes $DLLBytes -ProcId $ProcId -ProcHandle $ProcHandle
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Dynamic-link Library Injection]] Process Injection: DLL Injection
- [[DLL Search Order Hijacking]] Hijack Execution Flow: DLL Search Order Hijacking (variant)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual memory allocations (VirtualAllocEx) without corresponding file I/O
- Detection method 2: Hook API calls to GetProcAddress and LoadLibrary; look for reflective patterns in memory dumps
- Detection method 3: Behavioral analysis: Sudden process code changes without module loads in process lists (via tools like Process Hacker)
- Detection method 4: PowerShell logging for Invoke-ReflectivePEInjection module loads or reflective execution
- Detection method 5: EDR rules for PE parsing in non-loader contexts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerSploit]]
- [[tools/cobalt-strike]]

## References

- Original implementation: https://github.com/stephenfewer/ReflectiveDLLInjection
- PowerSploit documentation: https://github.com/PowerShellMafia/PowerSploit
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1055/001/
