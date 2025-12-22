---
id: f0f0ded8-b91e-4f93-90a9-846784cc7d33
name: Recon-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:17.792449+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - recon
  - osint
  - framework
url: 'https://github.com/lanmaster53/recon-ng'
validated: true
---

# Recon-ng

**Status**: Unverified

## Overview

Recon-ng is an open-source, full-featured reconnaissance framework written in Python, designed for web-based open-source intelligence (OSINT) gathering. It is commonly used in penetration testing and red team operations to perform automated reconnaissance on targets, such as discovering subdomains, hosts, contacts, and vulnerabilities through modular workflows.

## Description

Recon-ng provides a Metasploit-like console interface with a vast library of modules for tasks including passive reconnaissance, active scanning, and data harvesting from public sources. It supports workspace management to organize projects, integrates with external APIs (e.g., Shodan, Bing, Google), and allows scripting for automation. The framework is platform-agnostic but excels in Linux environments like Kali, making it a staple tool for mapping attack surfaces without direct interaction with targets.

## Features

- Modular architecture with 80+ built-in modules for reconnaissance tasks (e.g., domain brute-forcing, email harvesting, host discovery).
- Workspace and database management for storing and querying reconnaissance data.
- Support for API keys to leverage third-party services for enriched intelligence.
- Export options including CSV, HTML, and XML for reporting.
- Scriptable execution via .rc files for automated runs.
- Built-in help system and module documentation within the console.

## Installation

### Requirements

- Python 3.7+ (or Python 2.7 for legacy versions).
- pip and git.
- Optional: API keys for modules (e.g., Shodan, VirusTotal).

### Install Commands

On Kali Linux (pre-installed in Kali 2020+):

```bash
# Update and install if missing
sudo apt update
sudo apt install recon-ng
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3-pip git
git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng
pip3 install -r REQUIREMENTS
./recon-ng --update
```

On macOS (using Homebrew):

```bash
brew install python
pip3 install recon-ng
```

On Windows (via WSL or Git Bash):

Use the Ubuntu instructions within WSL.

## Basic Usage

```bash
recon-ng
```

This launches the interactive console. From there, use commands like `help`, `modules search <keyword>`, `use <module>`, `set <option> <value>`, and `run`.

### Common Options

Recon-ng is primarily interactive, but CLI options include:

| Option | Description |
|--------|-------------|
| -h, --help | Display help message |
| -r <script>, --run <script> | Execute commands from a script file |
| -w <workspace>, --workspace <workspace> | Load a specific workspace |
| --no-banner | Suppress the startup banner |
| --no-check | Skip version check |

## Examples

### Example 1: Basic Usage

Launch and create a workspace:

```bash
recon-ng
[recon-ng][default] > workspace -a project1
[recon-ng][project1] > help
```

### Example 2: Advanced Usage

Run a script for automated subdomain enumeration:

```bash
recon-ng -r subdomain_enum.rc
```

Where `subdomain_enum.rc` contains:

```
workspace -a target
add domains
set domains example.com
use recon/domains-hosts/brute_hosts
set SOURCE example.com
run
exit
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Gather Victim Network Information]] Gather Victim Network Information
- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Console processes named `recon-ng` or Python scripts accessing OSINT APIs.
- Network traffic to reconnaissance services (e.g., Shodan queries from unusual IPs).
- Database files (SQLite) in user directories with reconnaissance data.
- Log entries for API key usage or module executions in EDR tools.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Maltego]]
- [[tools/theHarvester]]

## References

- Official GitHub: https://github.com/lanmaster53/recon-ng
- Documentation: https://recon-ng.readthedocs.io/en/master/
- Usage Guide: https://www.offensive-security.com/metasploit-unleashed/recon-ng/
