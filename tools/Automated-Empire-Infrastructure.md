---
id: 92736707-bc3f-4214-855b-c5e8bf916be0
type: tool
description: >-
  A automation script for deploying and managing PowerShell Empire
  infrastructure, simplifying setup for post-exploitation operations in red team
  engagements.
verified: true
created_at: '2019-08-28T21:17:18.714636+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - post-exploitation
  - empire
  - automation
  - red-team
url: 'https://github.com/EmpireProject/Empire'
commands:
  - '[[commands/automated-empire-setup-infrastructure]]'
  - '[[commands/automated-empire-create-listener]]'
  - '[[commands/automated-empire-generate-stager]]'
validated: true
---

# Automated-Empire-Infrastructure

**Status**: Unverified

## Overview

The Automated Empire Infrastructure tool is a Python-based automation script designed to streamline the deployment and management of the PowerShell Empire post-exploitation framework. It handles the installation of Empire, database setup, listener configuration, and stager generation, making it ideal for red teamers who need to quickly spin up infrastructure for simulated attacks without manual configuration.

## Description

PowerShell Empire is an open-source framework for post-exploitation operations, focusing on evasion techniques and agent management across Windows, Linux, and macOS targets. This automation tool addresses the complexity of Empire's setup by providing scripted commands for end-to-end infrastructure management. It's commonly used in controlled environments for training, penetration testing, and adversary emulation, aligning with MITRE ATT&CK post-exploitation phases.

## Features

- Feature 1: One-click setup of Empire server, including dependency installation and database initialization.
- Feature 2: Automated listener creation and management for various protocols (HTTP, HTTPS, TCP).
- Feature 3: Stager payload generation tailored to target platforms and delivery methods.
- Feature 4: Integration with Empire's RESTful API for scripted operations.

## Installation

### Requirements

- Ubuntu 20.04+ or Kali Linux
- Python 3.8 or higher
- Git
- PostgreSQL (optional, for advanced DB setups)

### Install Commands

```bash
# Clone Empire repository (prerequisite)
git clone https://github.com/EmpireProject/Empire.git
cd Empire

# Install Empire dependencies
./setup/install.sh
pip3 install -r requirements.txt

# Download and setup the automation script (assuming it's a separate repo or included)
wget https://example.com/automated_empire.py
chmod +x automated_empire.py
```

## Basic Usage

```bash
python3 automated_empire.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available commands |
| -v, --verbose | Enable verbose logging for troubleshooting |
| --config | Path to custom configuration file |

## Examples

### Example 1: Basic Usage

Setup the full infrastructure:

```bash
python3 automated_empire.py --setup --db sqlite
```

### Example 2: Advanced Usage

Create a listener and generate a stager:

```bash
python3 automated_empire.py --listener create --type http --port 8080
python3 automated_empire.py --stager generate --listener http --output windows_stager.ps1 --platform windows
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Web Protocols]] Web Protocols
- [[Asymmetric Cryptography]] Non-Standard Port

### Tactics

- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Python processes spawning Empire-related binaries (e.g., teamserver.py) on non-standard ports.
- Detection method 2: Look for Git clones of the Empire repository or unusual pip installs of Empire dependencies.
- Detection method 3: Network traffic to listeners on ports like 8080/8443 with HTTP payloads resembling stagers.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Empire]]
- [[tools/Cobalt Strike]]

## References

- Official Empire Documentation: https://bc-security.gitbook.io/empire-wiki
- GitHub Repository: https://github.com/EmpireProject/Empire
