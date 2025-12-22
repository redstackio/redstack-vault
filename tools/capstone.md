---
id: 2b68a811-2119-4540-916f-7da628c75352
type: tool
verified: true
created_at: '2019-08-28T21:17:28.747740+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - disassembly
  - reversing
  - binary-analysis
  - framework
url: 'https://www.capstone-engine.org/'
validated: true
---

# capstone

**Status**: Unverified

## Overview

Capstone is a lightweight, multi-platform disassembly framework designed for binary analysis and reverse engineering in the security community. It provides a clean API for disassembling code across multiple architectures, making it essential for malware analysis, exploit development, and understanding obfuscated binaries during red team operations.

## Description

Developed by Nguyen Anh Quynh and maintained by a community, Capstone excels in parsing and disassembling machine code into human-readable assembly. Its architecture-neutral API allows easy integration into tools for security testing, such as custom disassemblers or scripts for analyzing payloads. Key strengths include detailed instruction decomposition (mnemonics, operands, implicit registers) and support for semantics like read/write registers. Implemented in C with bindings for Python, C++, and others, it's thread-safe and native to Windows and Unix-like systems.

## Features

- **Multi-Architecture Support**: Handles ARM, ARM64 (AArch64), Mips, X86 (16/32/64-bit), PowerPC, Sparc, SystemZ, and more.
- **Clean API**: Simple, intuitive interface for disassembly without architecture-specific complexities.
- **Instruction Details**: Provides mnemonics, operands, and semantics (e.g., registers read/written).
- **Lightweight Bindings**: Wrappers for Python, Ruby, C#, Java, Go, etc., for easy scripting.
- **Thread-Safe**: Designed for concurrent use in multi-threaded applications.
- **Cross-Platform**: Works on Windows, Linux, macOS, and BSD.

## Installation

### Requirements

- C compiler (gcc/clang)
- Python 3 (for bindings)
- Build tools (make, cmake)

### Install Commands

```bash
# On Ubuntu/Debian (for library and Python binding)
sudo apt update
sudo apt install libcapstone4 libcapstone-dev python3-capstone

# Or via pip for Python binding only
pip install capstone

# From source (recommended for latest features)
git clone https://github.com/capstone-engine/capstone.git
cd capstone
make
sudo make install
# For Python bindings
sudo make install-bindings
```

For Windows, use vcpkg or build from source with Visual Studio. On macOS, use Homebrew: `brew install capstone`.

## Basic Usage

```bash
python3 -c "from capstone import *; print('Capstone installed successfully')"
```

### Common Options

Capstone is primarily a library, so options are set via API calls (e.g., Cs(CS_ARCH_X86, CS_MODE_64)). Common API options include:

| Option | Description |
|--------|-------------|
| CS_ARCH_* | Select architecture (e.g., CS_ARCH_ARM) |
| CS_MODE_* | Set mode (e.g., CS_MODE_32 for 32-bit) |
| CS_OPT_SYNTAX | Choose syntax (Intel, ATT) |
| CS_OPT_DETAIL | Enable detailed disassembly info |

## Examples

### Example 1: Basic Usage (Disassemble via Python)

Use the Python binding to disassemble a binary snippet:

```python
from capstone import *
md = Cs(CS_ARCH_X86, CS_MODE_64)
code = b'\x48\x89\xe5'  # mov rbp, rsp
for i in md.disasm(code, 0x1000):
    print(f'{i.address:08x}: {i.mnemonic} {i.op_str}')
```

Output:
```
1000: mov rbp, rsp
```

### Example 2: Advanced Usage (File Disassembly)

```python
from capstone import *
import sys
md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
with open('binary.bin', 'rb') as f:
    code = f.read()
for i in md.disasm(code, 0x1000):
    print(f'{i.address:08x}: {i.mnemonic} {i.op_str}')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (for analyzing packed malware)
- [[PowerShell]] PowerShell (via bindings for scripting disassembly)
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution (reverse engineering persistence mechanisms)

### Tactics

- [[Execution]] Execution (developing custom payloads)
- [[Impact]] Impact (analyzing destructive malware)

## Detection

- Monitor for Python processes loading capstone libraries (e.g., libcapstone.so).
- Network indicators: Downloads from capstone-engine.org or GitHub.
- File system: Presence of capstone source or bindings in user directories.
- Behavioral: Unusual disassembly scripts during incident response or red teaming.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ghidra]] (full reverse engineering suite)
- [[tools/Radare2]] (CLI disassembly and analysis)
- [[tools/IDA-Pro]] (interactive disassembler)

## References

- Official Documentation: https://www.capstone-engine.org/docs.html
- GitHub Repository: https://github.com/capstone-engine/capstone
- Python Bindings Guide: https://github.com/capstone-engine/capstone/tree/master/bindings/python
