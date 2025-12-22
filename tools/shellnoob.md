---
id: 3b13d2e1-5f78-46ad-a103-21f39a48bf9c
type: tool
verified: true
created_at: '2019-08-28T21:17:29.237387+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - FreeBSD
tags:
  - shellcode
  - exploitation
  - conversion
  - assembly
url: 'https://github.com/angea/shellnoob'
validated: true
---

# shellnoob

**Status**: Unverified

## Overview

ShellNoob is a Python-based tool designed to simplify shellcode development and manipulation by automating the conversion between various shellcode formats and providing interactive features for assembly-to-opcode translation. It is particularly useful in offensive security operations for generating, modifying, and testing shellcode payloads across different architectures and syntaxes without manual error-prone conversions.

## Description

ShellNoob focuses on the creative aspects of shellcode writing by handling repetitive tasks like format conversions and opcode validation. It supports conversions from and to formats such as assembly (asm), binary (bin), hexadecimal (hex), object files (obj), executables (exe), C arrays, Python bytearrays, Ruby arrays, pretty-printed hex, safe assembly, complete C programs, and ShellStorm archives. The tool also offers an interactive mode for real-time asm-to-opcode and vice-versa conversions, which helps identify problematic bytes in shellcode. It accommodates both AT&T and Intel syntax, 32-bit and 64-bit architectures, and includes features like syscall resolution, breakpoint prepending, stdin/stdout piping, and debugging aids like strace/gdb output generation. ShellNoob is portable, requiring only Python 2.7+ or 3+ and standard tools like gcc, as, and objdump, making it ideal for on-target development during penetration tests.

## Features

- **Format Conversion**: Supports asm, bin, hex, obj, exe, C, python, ruby, pretty, safeasm, completec, shellstorm.
- **Interactive Mode**: Real-time assembly to opcode conversion and vice versa to avoid bad bytes.
- **Syntax Support**: AT&T and Intel (via --intel switch).
- **Architecture Support**: 32/64-bit on Linux/x86, x86_64, ARM; FreeBSD/x86, x86_64.
- **Syscall Resolution**: Automatically resolves syscall numbers, constants, and errors.
- **Portability**: Single Python script, no complex dependencies; works on Python 2.7+ and 3+.
- **Debugging Aids**: Options for strace/gdb output (--to-strace, --to-gdb), verbose mode for step-by-step tracing.
- **Plugins**: Binary patching (--file-patch), VM patching (--vm-patch), no-operation forking (--fork-nopper).
- **I/O Flexibility**: Read from stdin/write to stdout using "-" as filename; prepend breakpoints (-c).
- **Library Usage**: Can be imported as a Python module for scripting.

## Installation

### Requirements

- Python 2.7+ or 3+
- gcc, as (assembler), objdump (for certain conversions)

### Install Commands

```bash
# Download the script from GitHub
wget https://raw.githubusercontent.com/angea/shellnoob/master/shellnoob.py

# Make it executable
chmod +x shellnoob.py

# For Kali/Ubuntu (Python and binutils are pre-installed or available via apt)
# No additional installation needed if Python and binutils are present
```

## Basic Usage

```bash
python shellnoob.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-v, --verbose` | Enable verbose output to show conversion steps |
| `--intel` | Use Intel syntax instead of AT&T |
| `--64` | Target 64-bit architecture |
| `-c` | Prepend a breakpoint (INT3) to the shellcode |
| `--from FORMAT` | Input format (e.g., asm, bin, hex) |
| `--to FORMAT` | Output format (e.g., bin, C, python) |
| `-` | Read from stdin or write to stdout |
| `--interactive` | Enter interactive asm/opcode mode |
| `--to-strace` | Generate strace-compatible output for debugging |
| `--to-gdb` | Generate GDB script for debugging |

## Examples

### Example 1: Basic Usage

Convert assembly shellcode to binary format:

```bash
python shellnoob.py --from asm --to bin input.asm
```

### Example 2: Advanced Usage

Interactive mode for 64-bit Intel syntax conversion with verbose output:

```bash
python shellnoob.py --interactive --64 --intel -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Injection]] Process Injection (shellcode injection into processes)
- [[PowerShell]] PowerShell (via generated Python/C payloads)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (shellcode obfuscation and format changes)

### Tactics

- [[Execution]] Execution (delivering and executing shellcode payloads)
- [[Persistence]] Persistence (via injected shellcode)
- [[Command and Control]] Command and Control (custom shellcode for C2)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of shellnoob.py script or its downloads in logs.
- Python processes executing shellnoob.py with arguments like --from asm --to bin.
- Unusual assembly or binary file generations in temp directories.
- objdump or as invocations in process trees during payload development.
- Network or file system anomalies from generated shellcode executions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/msfvenom]] (Metasploit payload generator)
- [[pwntools]] (Python exploit development framework)

## References

- Official GitHub Repository: https://github.com/angea/shellnoob
- Formats Description: Included in tool's help output or README
