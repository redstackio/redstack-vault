---
id: 9c1d6292-552b-4d73-ae2b-2dc8355db34e
type: tool
verified: true
created_at: '2019-08-28T21:17:32.000495+00:00'
updated_at: '2023-10-01T00:00:00.000Z'
platforms:
  - Linux
  - Windows
tags:
  - backdoor
  - shellcode-injection
  - post-exploitation
url: 'https://github.com/spyglassofthethirdage/The-Backdoor-Factory'
commands:
  - '[[commands/bdf-list-available-shellcodes]]'
  - '[[commands/bdf-patch-binary-with-reverse-tcp]]'
  - '[[commands/bdf-patch-binary-with-meterpreter]]'
validated: true
---

# The-Backdoor-Factory-BDF

**Status**: Unverified

## Overview

The Backdoor Factory (BDF) is a Python-based tool designed to inject custom shellcode into existing executable binaries (PE and ELF formats) while preserving their original functionality. It is commonly used in red team operations to create stealthy backdoors in legitimate software, enabling persistent access without altering the binary's behavior or file hashes significantly.

## Description

BDF supports a variety of shellcodes, including reverse/bind shells, Meterpreter payloads, and custom code. It identifies safe injection points (caves) in the binary's sections to insert the shellcode, ensuring the program executes normally until the injected payload is triggered. This tool is particularly useful for evading antivirus detection by modifying trusted binaries rather than deploying new malware. It works on both 32-bit and 64-bit architectures for Windows (PE) and Linux (ELF) executables.

## Features

- Feature 1: Supports multiple injection methods (small caves, large caves, jmp rpcss, etc.) to adapt to different binary structures.
- Feature 2: Built-in shellcode library including TCP reverse/bind, UDP, HTTP, and Metasploit-compatible payloads.
- Feature 3: Architecture detection and cross-compilation support for x86/x64.
- Feature 4: Output options for patched binaries with minimal footprint.
- Feature 5: Cave analysis to find optimal injection points without breaking functionality.

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- Dependencies: pefile (for PE), elftools (for ELF)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/spyglassofthethirdage/The-Backdoor-Factory.git
cd The-Backdoor-Factory

# Install dependencies (Python 2/3)
pip install -r requirements.txt

# For Kali/Ubuntu (pre-built package may be available)
sudo apt update && sudo apt install backdoor-factory

# Verify installation
python backdoorfactory.py -h
```

For Windows, use a Python environment like Anaconda and run the clone commands via Git Bash or WSL.

## Basic Usage

```bash
python backdoorfactory.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Path to the target binary file |
| -s, --shellcode | Name of the shellcode to inject (e.g., reverse_tcp) |
| -H, --host | Callback host IP for reverse shells |
| -P, --port | Callback port |
| -J, --small-cave | Use small cave injection |
| -j, --jmp-rpcss | Use jmp rpcss method for 32-bit PE |
| -o, --output-file | Specify output file name |
| -a, --architecture | Target architecture (x86, x64) |

## Examples

### Example 1: Basic Usage

List available shellcodes first:

[[commands/bdf-list-available-shellcodes]]

Then patch a binary:

[[commands/bdf-patch-binary-with-reverse-tcp]]

### Example 2: Advanced Usage

Patch with Meterpreter for Windows:

[[commands/bdf-patch-binary-with-meterpreter]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection
- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for modifications to legitimate binaries (e.g., via file integrity monitoring tools like Tripwire or OSSEC).
- Detection method 2: Analyze binaries for anomalous code caves or shellcode patterns using tools like Volatility or strings analysis.
- Detection method 3: Network monitoring for unexpected reverse connections from trusted processes.
- Detection method 4: Python process spawning with backdoorfactory.py signatures in command lines (via Sysmon or EDR).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/Donut]]
- [[tools/Invoke-Obfuscation]]

## References

- Official GitHub: https://github.com/spyglassofthethirdage/The-Backdoor-Factory
- Documentation: Included in repo README
- Related resources: Black Hat presentations on binary patching techniques
