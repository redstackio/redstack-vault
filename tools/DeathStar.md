---
id: 370b72b6-a3cd-4589-bfa9-4343ad4a9e8e
type: tool
verified: true
created_at: '2019-08-28T21:17:40.562988+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
tags:
  - active-directory
  - privilege-escalation
  - automation
  - empire
url: 'https://github.com/byt3bl33d3r/DeathStar'
commands:
  - '[[commands/deathstar-basic-attack]]'
  - '[[commands/deathstar-install-and-setup]]'
validated: true
---

# DeathStar

**Status**: Unverified

## Overview

DeathStar is a Python-based automation tool designed for offensive security operations in Active Directory environments. It integrates with PowerShell Empire's RESTful API to orchestrate a multi-stage attack chain aimed at escalating privileges from initial low-level access to full Domain Admin rights. Common use cases include red team engagements simulating advanced persistent threats (APTs) targeting Windows domains.

## Description

DeathStar automates the deployment of Empire stagers to infect target machines, followed by enumeration of domain users, groups, and service accounts. It then executes techniques such as Kerberoasting, AS-REP Roasting, and resource-based constrained delegation to crack credentials and move laterally. The tool assumes a running Empire server and handles agent management, module execution, and cleanup, making complex AD compromises more efficient and repeatable.

## Features

- **Automated Workflow**: Chains reconnaissance, exploitation, and persistence without manual intervention.
- **Empire Integration**: Uses REST API for seamless control of listeners, stagers, and post-exploitation modules.
- **Multiple Attack Paths**: Supports techniques like Kerberoasting (T1558.003), unconstrained delegation (T1097), and more.
- **Configurable Options**: Adjustable delays, listener selection, and targeting for stealthy operations.
- **Logging and Reporting**: Outputs detailed logs of each phase for analysis and debriefing.

## Installation

### Requirements

- Python 3.6+
- Git
- A running PowerShell Empire server (version 3.0+ recommended)
- pip and virtualenv for dependency management

### Install Commands

Use [[commands/deathstar-install-and-setup]] for standard installation:

```bash
git clone https://github.com/byt3bl33d3r/DeathStar.git && cd DeathStar && pip3 install -r requirements.txt
```

For virtual environment setup:

```bash
python3 -m venv deathstar_env && source deathstar_env/bin/activate && pip install -r requirements.txt
```

Supported platforms include Kali Linux (pre-requisites available) and Ubuntu. Ensure Empire is installed separately via its official documentation.

## Basic Usage

```bash
python3 DeathStar.py --help
```

This displays available options, including authentication credentials, domain targeting, and Empire connection details.

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --username` | Initial domain username |
| `-p, --password` | Password for the username |
| `-d, --domain` | Target domain name |
| `--url` | Empire REST API URL |
| `--listener` | Empire listener name |
| `--delay` | Delay between actions (seconds) |

## Examples

### Example 1: Basic Usage

Run a standard attack using [[commands/deathstar-basic-attack]]:

```bash
python3 DeathStar.py -u jdoe -p Password123 -d corp.local --url http://127.0.0.1:1337 --listener http
```

This initiates the full automation sequence.

### Example 2: Advanced Usage

```bash
python3 DeathStar.py -u jdoe -p Password123 -d corp.local --url http://127.0.0.1:1337 --listener http --delay 30 --no-cleanup
```

Includes delay for evasion and skips cleanup for persistence testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Kerberoasting]] Kerberoasting
- [[AS-REP Roasting]] AS-REP Roasting
- [[Pass the Ticket]] Account Manipulation (Unconstrained Delegation)
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Empire server on non-standard ports (e.g., 1337).
- Unusual PowerShell executions or Empire stager downloads on endpoints.
- Logs showing Kerberos ticket requests for service accounts (Event ID 4769).
- Python processes spawning child processes with Empire modules.
- Monitor for API calls to Empire endpoints from automation scripts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[PowerShell-Empire]]
- [[tools/Impacket]]

## References

- Official GitHub Repository: https://github.com/byt3bl33d3r/DeathStar
- PowerShell Empire Documentation: https://bc-security.gitbook.io/empire-wiki
- MITRE ATT&CK for Enterprise: https://attack.mitre.org
