---
id: 0ae46660-1add-455b-b9b9-e437d37be3c2
type: tool
verified: true
created_at: '2019-08-28T21:17:24.506769+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - disassembly
  - reverse-engineering
  - binary-analysis
url: 'https://github.com/gdabah/distorm'
commands:
  - '[[commands/distorm3-disassemble-file]]'
  - '[[commands/distorm3-disassemble-bytes]]'
validated: true
---

# diStorm3

**Status**: Unverified

## Overview

diStorm3 is a lightweight, high-performance binary disassembler library focused on x86 and x86-64 architectures. It supports disassembly in 16-bit, 32-bit, and 64-bit modes, covering a wide range of instruction sets including legacy FPU, MMX, SSE/SSE2/SSE3/SSSE3/SSE4, AVX, VMX, and AMD SVM extensions. Primarily used in reverse engineering, malware analysis, and security research to convert machine code into readable assembly instructions.

## Description

diStorm3 excels in speed and accuracy for decomposing binary code, making it suitable for both static and dynamic analysis in offensive security operations. The library outputs structured data that can be formatted into text, enabling integration into custom tools for exploit development, vulnerability research, or binary patching. Written in portable C, it includes bindings for Python, Ruby, and Java, ensuring ease of use across different environments. It is backward compatible with diStorm64 and requires minimal dependencies, allowing deployment in constrained settings like embedded systems or kernel modules.

## Features

- **Multi-Mode Support**: Disassembles 16/32/64-bit x86 code with full instruction set coverage (FPU, MMX, SSE family, AVX, etc.).
- **High Performance**: Optimized for speed, outperforming many competitors in disassembly throughput.
- **Structured Output**: Returns a parseable structure for each instruction, including offset, size, mnemonic, and operands.
- **Language Bindings**: Native C API plus wrappers for Python (distorm3 package), Ruby, and Java.
- **Portability**: Platform-independent, supports little and big endian, no external dependencies beyond standard C library.
- **Custom Formatting**: Tools for generating human-readable or custom-formatted assembly output.

## Installation

### Requirements

- C compiler (gcc or equivalent) for building from source.
- Python 3.x for the Python binding.
- Git for cloning the repository.

### Install Commands

For Python binding (recommended for quick use):

```bash
pip install distorm3
```

For C library from source (Linux/Ubuntu):

```bash
sudo apt update
sudo apt install build-essential git
git clone https://github.com/gdabah/distorm.git
distorm$ cd distorm
sudo make install
```

For Windows (using MSVC):

```cmd
git clone https://github.com/gdabah/distorm.git
distorm> nmake -f Makefile.msvc
# Copy distorm.dll and headers to your project
```

For macOS:

```bash
brew install automake
git clone https://github.com/gdabah/distorm.git
distorm$ ./autogen.sh
./configure
make
sudo make install
```

## Basic Usage

```python
from distorm3 import *

# Basic disassembly example
code = b'\x90\x90\x90'  # NOP instructions
for instruction in Decode(0x1000, code, Decode64Bits):
    print(FormatInstruction(instruction, False))
```

### Common Options

diStorm3 is a library, so options are set via API parameters:

| Option | Description |
|--------|-------------|
| `Decode16Bits` / `Decode32Bits` / `Decode64Bits` | Mode selector for bit width |
| `FormatInstruction` | Formats output with/without offset and bytes |
| `JustText` flag | Outputs only mnemonic and operands without offset/bytes |

## Examples

### Example 1: Basic Usage

Disassemble a simple binary snippet using Python:

```python
from distorm3 import *
code = b'\xb8\x01\x00\x00\x00'  # mov eax, 1
for i in Decode(0x1000, code, Decode32Bits):
    print(FormatInstruction(i, False))
```

Output:

```
0000000000001000 B801000000         MOV EAX,0x1
```

### Example 2: Advanced Usage

Disassemble from a file (see [[commands/distorm3-disassemble-file]] for full command):

```python
from distorm3 import *;
with open('binary.exe', 'rb') as f:
    code = f.read();
for i in Decode(0x400000, code, Decode64Bits):
    if i[3] != '':  # Skip invalid instructions
        print(FormatInstruction(i, True))
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (for analyzing packed/malware binaries)
- [[PowerShell]] PowerShell (if used in scripting for dynamic analysis)

### Tactics

- [[Discovery]] Discovery (binary reconnaissance)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of distorm3 Python package in environments (`pip list | grep distorm`).
- Process monitoring for custom scripts importing distorm3 during binary analysis.
- File system artifacts like cloned distorm repositories or built libraries.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official GitHub: https://github.com/gdabah/distorm
- Python Binding Documentation: https://pypi.org/project/distorm3/
