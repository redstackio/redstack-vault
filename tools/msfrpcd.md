---
id: 05924519-4de2-4a54-b2fb-7dce716f9a93
type: tool
verified: true
created_at: '2019-08-28T21:17:29.212053+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - metasploit
  - rpc
  - exploitation
  - framework
url: >-
  https://docs.metasploit.com/docs/using-metasploit/basics/using-the-metasploit-rpc-api.html
validated: true
---

# msfrpcd

**Status**: Unverified

## Overview

msfrpcd is the RPC daemon for the Metasploit Framework, enabling remote control and automation of Metasploit sessions, modules, and exploits via a JSON-RPC API. It is commonly used in penetration testing to integrate Metasploit with custom scripts, CI/CD pipelines, or other tools for automated vulnerability scanning, exploitation, and post-exploitation activities.

## Description

msfrpcd allows external applications to interact with Metasploit's console, database, and module library without requiring direct msfconsole access. It supports authentication via username/password or tokens, and listens on a specified port for RPC calls. This facilitates scripting complex attack chains, managing multiple sessions, and integrating with tools like Armitage or custom Python clients using libraries such as pymetasploit3.

## Features

- **Remote Module Execution**: Load and run exploits, auxiliaries, and payloads remotely.
- **Session Management**: Control interactive shells, Meterpreter sessions, and console output.
- **Database Integration**: Query and manipulate the Metasploit database for hosts, services, and vulnerabilities.
- **Authentication Options**: Supports SSL/TLS, username/password, and token-based auth.
- **API Methods**: Core, Auth, Client, Console, Session, Module, Job, and Database methods for comprehensive control.

## Installation

### Requirements

- Metasploit Framework installed (includes msfrpcd).
- Ruby 2.7+ and PostgreSQL for full functionality.
- Network access to the target port (default 55553).

### Install Commands

```bash
# On Kali Linux (pre-installed with Metasploit)
sudo apt update && sudo apt install metasploit-framework

# On Ubuntu
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall

# On Windows/macOS: Download from https://www.metasploit.com/download and follow installer
```

## Basic Usage

```bash
msfrpcd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-P, --password` | Set password for authentication |
| `-u, --user` | Set username (default: msf) |
| `-p, --port` | Listen on specified port (default: 55553) |
| `-S, --ssl` | Enable SSL/TLS |
| `-f, --foreground` | Run in foreground (no daemonize) |
| `-a, --address` | Bind to IP address (default: 127.0.0.1) |

## Examples

### Example 1: Basic Usage

Start msfrpcd in foreground with password auth:

```bash
msfrpcd -P mypassword -f -a 0.0.0.0 -p 55553
```

### Example 2: Advanced Usage

Start with SSL enabled and custom user:

```bash
msfrpcd -u admin -P securepass -S -f -a 0.0.0.0 -p 55554
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Execution through API]] Native API
- [[Encrypted Channel]] Encrypted Channel

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on non-standard ports (e.g., 55553/TCP) with JSON-RPC payloads.
- Process monitoring for msfrpcd.exe or ruby processes binding to unusual IPs/ports.
- Log analysis for Metasploit database connections or RPC auth attempts.
- SSL certificate anomalies if TLS is enabled.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit Framework]]
- [[tools/armitage]]

## References

- Official Documentation: https://docs.metasploit.com/docs/using-metasploit/basics/using-the-metasploit-rpc-api.html
- GitHub Repository: https://github.com/rapid7/metasploit-framework
