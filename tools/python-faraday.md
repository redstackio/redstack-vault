---
type: tool
description: >-
  Python client for interacting with the Faraday penetration testing IDE,
  enabling API-based management of workspaces, data import, and collaboration on
  security audits.
url: 'https://github.com/infobyte/faraday'
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reporting
  - collaboration
  - pentest-ide
  - api-client
validated: true
---

# python-faraday

**Status**: Unverified

## Overview

python-faraday is the Python-based CLI client for Faraday, an Integrated Penetration-Test Environment (IPE). It serves as a multiuser penetration testing IDE designed for distributing, indexing, and analyzing data generated during security audits. The client allows seamless integration of community tools into a collaborative framework, mimicking a terminal experience while providing specialized functionalities to enhance penetration testing workflows.

## Description

Faraday's python-faraday client introduces the concept of IPE, enabling teams to reuse existing security tools in a multiuser environment. It supports data import from various scanners, workspace management, and real-time collaboration without altering the user's familiar terminal interface. Developed to simplify pentesting, it acts like an IDE for security professionals, offering features for data organization, vulnerability tracking, and report generation. Ideal for red teams, bug bounty hunters, and security auditors needing centralized knowledge management.

## Features

- **Multiuser Collaboration**: Share workspaces and data in real-time across team members.
- **Tool Integration**: Import results from Nmap, Nessus, Burp, and other tools via XML/JSON.
- **API-Driven Management**: Create, update, and query hosts, services, and vulnerabilities programmatically.
- **Data Indexing**: Automatic parsing and categorization of scan outputs for quick analysis.
- **Custom Workflows**: Extend functionality with Python scripts for automated pentesting tasks.

## Installation

### Requirements

- Python 3.6+
- pip package manager
- Access to a Faraday server instance

### Install Commands

```bash
# Install via pip (Kali/Ubuntu)
pip3 install faraday-cli

# Or from source
pip3 install git+https://github.com/infobyte/faraday.git

# For Ubuntu/Debian dependencies
sudo apt update && sudo apt install python3-pip
```

On Windows/macOS, use pip in a virtual environment:

```bash
python -m venv faraday_env
source faraday_env/bin/activate  # Linux/macOS
faraday_env\Scripts\activate  # Windows
pip install faraday-cli
```

## Basic Usage

```bash
faraday-cli --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| --server | Specify Faraday server URL |

## Examples

### Example 1: Basic Usage

Login and list workspaces:

```bash
faraday-cli login --server http://localhost:5985 --username admin --password secret
faraday-cli workspace list
```

### Example 2: Advanced Usage

Create workspace and import data:

```bash
faraday-cli workspace create --name "Test Audit"
faraday-cli import --workspace "Test Audit" --file scan.xml --tool nmap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Windows Management Instrumentation]] Workflow Order

### Tactics

- [[Impact]] Impact (for reporting and analysis)
- [[Discovery]] Discovery (data indexing)

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Faraday server ports (default 5985).
- Python processes running faraday-cli with API calls.
- Log entries for XML/JSON imports in pentest environments.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Faraday Server]]
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/infobyte/faraday
- Documentation: https://faradaysec.com/docs/

*Last updated: 2023-10-01*
