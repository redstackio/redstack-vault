---
id: e75cc3e2-168b-48ef-9402-09be06423349
name: msfd
type: tool
verified: true
created_at: '2019-08-28T21:17:33.384167+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - metasploit
  - rpc
  - penetration-testing
  - exploitation
url: 'https://docs.metasploit.com/docs/using-metasploit/interacting-rpc.html'
validated: true
---

# msfd

**Status**: Unverified

## Overview

msfd is the RPC (Remote Procedure Call) daemon for the Metasploit Framework, a popular open-source penetration testing platform. It allows external applications and scripts to control Metasploit remotely via an RPC interface, enabling automation of exploits, payload generation, and session management without direct console interaction.

## Description

The Metasploit Framework provides infrastructure, exploits, payloads, and auxiliary modules for penetration testing and security auditing. msfd specifically exposes these capabilities over RPC, supporting JSON-RPC for programmatic access. This is ideal for integrating Metasploit into custom tools, CI/CD pipelines for security testing, or remote team operations. Developed by Rapid7 and the open-source community, it receives frequent updates with new modules for emerging vulnerabilities.

## Features

- Feature 1: RPC interface for remote control of exploits, sessions, and modules
- Feature 2: Supports SSL/TLS for secure connections
- Feature 3: Authentication via username/password to prevent unauthorized access
- Feature 4: Integration with msfconsole and external clients like Armitage or custom scripts

## Installation

### Requirements

- Ruby 2.7+ and dependencies (bundler, etc.)
- PostgreSQL for database (optional but recommended)
- Network access for binding ports

### Install Commands

```bash
# On Kali Linux (pre-installed Metasploit)
sudo apt update && sudo apt install metasploit-framework

# On Ubuntu
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall

# On Windows (via installer)
# Download from https://windows.metasploit.com/metasploitframework-latest.msi

# Verify installation
msfconsole -v
```

## Basic Usage

```bash
msfd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -a, --address HOST | Bind to a specific IP address |
| -p, --port PORT | Listen on specified port (default 55552) |
| -S, --ssl | Enable SSL |
| -U, --user USER | Set RPC username |
| -P, --pass PASS | Set RPC password |
| -f, --foreground | Run in foreground for debugging |

## Examples

### Example 1: Basic Usage

```bash
msfd -a 127.0.0.1 -p 55553 -U msf -P password
```

### Example 2: Advanced Usage

```bash
msfd -a 0.0.0.0 -p 55553 -S -U msf -P strongpass -f
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation of Remote Services]] Exploitation of Remote Services
- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network monitoring for RPC traffic on non-standard ports (e.g., 55553)
- Detection method 2: Process monitoring for msfd.exe or ruby processes with RPC flags
- Detection method 3: Log analysis for Metasploit module loads or exploit attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/metasploit-framework]]
- [[tools/armitage]]

## References

- Official documentation: https://docs.metasploit.com/
- RPC API: https://github.com/rapid7/metasploit-rpc

*Last updated: 2023-10-01T00:00:00Z*
