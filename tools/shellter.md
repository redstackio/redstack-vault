---
id: 5ba5ca85-d5cf-4eff-a17e-4808038f825e
type: tool
verified: true
created_at: '2019-08-28T21:17:32.913504+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - shellcode-injection
  - pe-infection
  - evasion
url: 'https://github.com/shellterproject/Shellter'
validated: true
---

# Shellter

**Status**: Unverified

## Overview

Shellter is a dynamic shellcode injection tool designed for offensive security testing. It is the first truly dynamic PE (Portable Executable) infector, allowing users to inject shellcode into legitimate 32-bit Windows executables on-the-fly without permanently modifying the original file until execution. Commonly used for creating undetectable payloads that evade antivirus detection during red team engagements.

## Description

Shellter operates by hooking API calls and injecting shellcode dynamically at runtime, preserving the original executable's functionality while adding malicious behavior. It supports integration with Metasploit payloads, such as Meterpreter reverse shells, and includes built-in evasion techniques like API hashing and indirect calls to bypass static analysis. Ideal for post-exploitation scenarios where blending malicious code into trusted binaries is required.

## Features

- Feature 1: Dynamic injection - Infects PE files without static modifications, activating only upon execution.
- Feature 2: AV evasion - Supports multiple evasion methods including syscall invocation, code caves, and entropy reduction.
- Feature 3: Metasploit integration - Directly generates and injects MSFvenom payloads.
- Feature 4: Interactive mode - Allows real-time selection of injection and evasion options.
- Feature 5: 32-bit PE support - Targets Windows executables on x86 architecture.

## Installation

### Requirements

- Windows OS (x86 or x64 host, targets 32-bit PE files)
- .NET Framework 4.0 or later
- Metasploit Framework (optional, for payload generation)

### Install Commands

Shellter is distributed as a standalone executable. Download from the official GitHub repository:

```cmd
# Download the latest release
# Visit: https://github.com/shellterproject/Shellter/releases
# Extract shellter.exe to a working directory, e.g., C:\Tools\Shellter\
```

No formal installation required; run directly from the extracted folder.

## Basic Usage

```cmd
shellter.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Specify the PE file to infect |
| --evade-all | Apply all evasion techniques |
| --metasploit | Use Metasploit for shellcode generation |
| --shellcode | Load custom shellcode file |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```cmd
shellter.exe -f C:\Windows\System32\notepad.exe
```

This launches interactive mode to inject a default shellcode.

### Example 2: Advanced Usage

```cmd
shellter.exe -f C:\path\to\app.exe --evade-all --metasploit
```

Generates and injects a Metasploit payload with full evasion.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Dynamic-link Library Injection]] - Dynamic-link Library Injection (for shellcode execution)
- [[Obfuscated Files or Information]] - Obfuscated Files or Information (via dynamic infection)
- [[Hijack Execution Flow]] - Hijack Execution Flow (API hooking)

### Tactics

- [[Execution]] - Execution
- [[Privilege Escalation]] - Privilege Escalation
- [[Defense Evasion]] - Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual API hooking in running processes (e.g., via Sysmon Event ID 8).
- Detection method 2: Scan for modified PE sections or high entropy in executables using tools like PEiD or Detect It Easy.
- Detection method 3: Behavioral analysis - Look for processes spawning reverse shells from legitimate binaries.
- Detection method 4: YARA rules targeting Shellter's code caves or syscall patterns.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]
- [[tools/msfvenom]]

## References

- Official GitHub: https://github.com/shellterproject/Shellter
- Documentation: Included in release ZIP or wiki on GitHub
- Blog Post: Original announcement on shellterproject.com
