---
id: 46403ca8-0c6c-48ff-a7f3-e94c63287028
type: tool
verified: true
created_at: '2019-08-28T21:17:24.907959Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Embedded Devices
tags:
  - exploitation
  - routers
  - iot
  - embedded
  - scanning
url: 'https://github.com/threat9/routersploit'
validated: true
---

# RouterSploit

**Status**: Unverified

## Overview

RouterSploit is an open-source penetration testing framework specifically designed for exploiting vulnerabilities in embedded devices, such as routers, IP cameras, and other IoT hardware. It mirrors the structure of Metasploit but focuses on network-attached devices commonly found in home and enterprise environments.

## Description

The framework includes a collection of modules categorized into exploits (for taking advantage of known vulnerabilities), creds (for testing credentials against network services), and scanners (for checking if targets are vulnerable to exploits). It supports a wide range of router vendors like D-Link, Cisco, TP-Link, and others, making it ideal for red team assessments of network perimeters and internal IoT segments.

## Features

- **Exploit Modules**: Pre-built exploits for CVEs affecting embedded devices, such as buffer overflows, command injections, and authentication bypasses.
- **Credential Testing**: Automated brute-force and default credential checks for common router admin panels.
- **Scanner Modules**: Automated vulnerability detection, including autopwn for comprehensive checks across multiple modules.
- **Modular Architecture**: Easy extension with custom modules for new vulnerabilities.
- **Interactive Shell**: Command-line interface similar to Metasploit for module selection, configuration, and execution.

## Installation

### Requirements

- Python 3.6 or higher
- Git
- pip

### Install Commands

```bash
# Clone the repository
git clone https://github.com/threat9/routersploit.git

# Navigate to the directory
cd routersploit

# Install dependencies
pip3 install -r requirements.txt
```

On Kali Linux, it may be available via apt: `sudo apt install routersploit`.

## Basic Usage

```bash
python3 rsf.py
```

This launches the interactive shell. Common commands inside the shell:
- `search <keyword>`: Find modules (e.g., `search dlink`).
- `use <module>`: Load a module (e.g., `use exploits/routers/dlink/dir_300_1_3_1_command_injection`).
- `set <option> <value>`: Configure options (e.g., `set target 192.168.1.1`).
- `check`: Verify if the target is vulnerable.
- `exploit` or `run`: Execute the module.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help and available commands |
| `--target <IP>` | Set target IP for non-interactive runs |
| `--run-module <path>` | Execute a specific module non-interactively |

## Examples

### Example 1: Basic Usage

Launch the framework and search for D-Link modules:

```bash
python3 rsf.py
rsf > search dlink
```

### Example 2: Advanced Usage

Non-interactively scan a target with autopwn:

```bash
python3 rsf.py --target 192.168.1.1 --run-module scanners/autopwn
```

### Example 3: Credential Testing

Test default creds on a Cisco router:

```bash
python3 rsf.py --target 192.168.1.254 --run-module creds/routers/cisco/default_creds
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Password Guessing]] Password Guessing
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious Python processes (rsf.py) on assessment machines connecting to device management ports (80, 443, 8080).
- High volume of HTTP/HTTPS requests to router admin interfaces from a single source.
- Failed login attempts or anomalous credential probes logged on devices.
- Network traffic patterns matching known RouterSploit user agents or module signatures.

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
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/threat9/routersploit
- Documentation: https://docs.routersploit.com/

*Last updated: 2023-10-01T00:00:00Z*
