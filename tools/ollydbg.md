---
id: f14749dc-d556-4b9a-bb36-e4c2e576be04
type: tool
verified: true
created_at: '2019-08-28T21:17:36.286591+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - debugger
  - reverse-engineering
  - malware-analysis
  - binary-analysis
url: 'http://www.ollydbg.de/'
commands:
  - '[[commands/ollydbg-launch-with-file]]'
  - '[[commands/ollydbg-attach-to-process]]'
validated: true
---

# OllyDbg

**Status**: Unverified

## Overview

OllyDbg is a 32-bit assembler-level debugging tool for Microsoft Windows, designed for analyzing binary code, particularly when source code is unavailable. It is commonly used in reverse engineering, malware analysis, vulnerability research, and software debugging to trace execution, inspect registers, and identify code structures.

## Description

OllyDbg emphasizes binary code analysis with an intuitive graphical user interface that avoids cryptic commands. It supports debugging of executables and DLLs, multithreaded applications, and provides advanced features like code disassembly, breakpoint management, and plugin extensibility. Ideal for offensive security operations involving exploit development, unpacking malware, or patching binaries.

## Features

- Intuitive user interface with no cryptic commands
- Code analysis: traces registers, recognizes procedures, loops, API calls, switches, tables, constants, and strings
- Direct loading and debugging of DLLs
- Object file scanning to locate routines from object files and libraries
- User-defined labels, comments, and function descriptions
- Support for Borland debugging information format
- Saves patches between sessions and applies them to executable files
- Open architecture with third-party plugins
- No installation required; runs portably without registry changes
- Debugging of multithreaded applications and attachment to running programs
- Configurable disassembler supporting MASM and IDEAL formats
- Support for MMX, 3DNow!, SSE instructions, and Athlon extensions
- Full UNICODE support and dynamic recognition of ASCII/UNICODE strings (including Delphi format)
- Recognition of complex code constructs like calls to jumps
- Decoding of over 1900 standard API calls and 400 C functions
- Context-sensitive help for API functions
- Conditional, logging, memory, and hardware breakpoints
- Program execution tracing and logging of function arguments
- Fixup display and dynamic stack frame tracing
- Search for imprecise commands, masked binary sequences, and references to constants or addresses
- Memory examination/modification, on-the-fly breakpoints, and command assembly into binary form
- Can run from a floppy disk for portable use

## Installation

### Requirements

- Microsoft Windows (32-bit applications; compatible with 64-bit Windows in WoW64 mode)
- No additional dependencies; fully standalone

### Install Commands

OllyDbg does not require installation and can be run portably. Download the ZIP archive from the official website and extract to a directory.

```cmd
# Download manually from http://www.ollydbg.de/
# Extract ZIP to C:\OllyDbg\
# No installer; run ollydbg.exe directly
```

For portable use:

```cmd
cd C:\OllyDbg\
ollydbg.exe
```

## Basic Usage

```cmd
ollydbg.exe
```

Launches the OllyDbg GUI. Use the menu or toolbar for debugging actions like loading files or attaching to processes.

### Common Options

OllyDbg has limited command-line options, primarily for launching with a file:

| Option | Description |
|--------|-------------|
| `[filename]` | Load and debug the specified executable or DLL on startup |
| `/attach [pid]` | Attach to the process with the given PID (non-standard; use GUI for reliability) |
| `-p` | Portable mode (default) |

## Examples

### Example 1: Basic Usage

Launch OllyDbg:

```cmd
ollydbg.exe
```

In the GUI, go to File > Open and select an executable to debug.

### Example 2: Advanced Usage

Launch and load a specific file:

```cmd
ollydbg.exe C:\path\to\target.exe
```

This opens the executable in the debugger for analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (for unpacking and deobfuscating malware)
- [[Process Discovery]] Process Discovery (during debugging of processes)
- [[Create or Modify System Process]] Create or Modify System Process (for analyzing persistence mechanisms)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of ollydbg.exe in process lists or file system
- Debugger-related artifacts like conditional breakpoints or memory patches in target binaries
- Anti-debugging bypass attempts in malware samples
- Network downloads from ollydbg.de domain
- Registry or filesystem changes if plugins are installed (though minimal by default)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/IDA-Pro]] (Advanced disassembler and debugger)
- [[tools/x64dbg]] (Open-source alternative for 64-bit debugging)
- [[tools/Ghidra]] (NSA's free reverse engineering suite)

## References

- Official website: http://www.ollydbg.de/
- Plugin repository: http://www.ollydbg.de/plugins.html
- Documentation: Included in the download or available on the website
