---
id: c4796d49-c5df-402f-ab40-dab968fd6b3f
type: tool
verified: true
created_at: '2020-03-07T02:03:16.469422+00:00'
updated_at: '2023-05-30T01:08:15.809339+00:00'
platforms:
  - Windows
tags:
  - exploit-dev
url: 'https://github.com/corelan/mona'
commands:
  - '[[commands/mona-jmp-esp-search]]'
validated: true
---

# mona

**Status**: ✓ Verified

## Overview

Mona is an Immunity Debugger plugin developed by Corelan Team, designed to assist in exploitation development and debugging tasks. It provides a suite of utilities for tasks such as searching memory for specific patterns, generating cyclic patterns for buffer overflows, finding ROP/JOP gadgets, and analyzing modules for exploitation opportunities. Commonly used in offensive security for developing exploits against Windows applications, particularly in scenarios involving stack overflows, SEH overwrites, and advanced exploitation techniques.

## Description

Mona extends the capabilities of Immunity Debugger by offering specialized commands for exploit developers. It automates repetitive tasks like locating useful instructions (e.g., jmp esp), identifying safe modules without ASLR/SafeSEH, and building ROP chains. Key features include memory searching, pattern generation, and gadget discovery, making it invaluable for crafting reliable exploits in controlled environments like vulnerability research and red teaming.

## Features

- **Pattern Tools**: Generate cyclic patterns (`pattern_create`) and calculate offsets (`pattern_offset`) for buffer overflow exploitation.
- **Search Functions**: Find strings, bytes, instructions, or pointers in memory and files (`find`, `jmp`, `seh`, `jop`, `rop`).
- **Memory Analysis**: Locate references to cyclic patterns (`findmsp`), list process heaps (`heap`), and inspect loaded modules (`modules`).
- **Gadget Building**: Discover gadgets for ROP/JOP chains and egghunters (`egg`).
- **Module Filtering**: Identify exploitable modules based on protections like ASLR, SafeSEH, and DEP.

## Installation

### Requirements

- Immunity Debugger installed on Windows.
- Python support enabled in Immunity Debugger.

### Install Commands

1. Download the latest mona.py from the official repository:
   ```bash
   # Use browser or wget/curl to download from https://github.com/corelan/mona
   git clone https://github.com/corelan/mona.git
   ```
2. Copy `mona.py` to Immunity Debugger's PyCommands directory (typically `C:\Program Files (x86)\Immunity Inc\Immunity Debugger\PyCommands`).
3. Restart Immunity Debugger and type `!mona` in the command bar to verify installation.

## Basic Usage

Load a target process in Immunity Debugger, then use mona commands prefixed with `!` (e.g., `!mona jmp -r esp`).

```immunity
!mona help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help for a specific mona command |
| `-cpb` | Filter modules by protections (e.g., no ASLR, no SafeSEH) |
| `-module` | Specify a module to search within |

## Examples

### Example 1: Basic Usage

Search for jmp esp instructions:

```immunity
!mona jmp -r esp
```

### Example 2: Advanced Usage

Generate a 500-byte cyclic pattern:

```immunity
!mona pattern_create 500
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Injection]] Process Injection (for debugging injected code)
- [[Remote Services]] Remote Services (in conjunction with debugging remote processes)

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of `mona.py` in Immunity Debugger directories.
- Debugger processes (e.g., `ImmunityDebugger.exe`) running on production systems.
- Memory patterns or cyclic data indicative of exploit development testing.
- Network logs showing downloads from Corelan GitHub repository.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Immunity Debugger]]
- [[pwntools]]

## References

- Official GitHub Repository: https://github.com/corelan/mona
- Corelan Exploit Writing Tutorial: https://www.corelan.be/index.php/2009/07/19/exploit-writing-tutorial-part-1-stack-based-overflows/
- Immunity Debugger Documentation: https://debugger.immunityinc.com/
