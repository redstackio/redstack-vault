---
id: 0b0f3185-0d70-444e-8851-e5d2da9b492f
type: tool
verified: true
created_at: '2019-08-28T21:17:27.543333+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
tags:
  - c2
  - post-exploitation
  - rootkit
  - com
url: 'https://github.com/zerosum0x0/koadic'
commands:
  - '[[commands/koadic-start-server]]'
  - '[[commands/koadic-create-http-listener]]'
  - '[[commands/koadic-generate-stager]]'
  - '[[commands/koadic-interact-zombie]]'
validated: true
---

# Koadic

**Status**: Unverified

## Overview

Koadic (Or COM Command & Control) is a Python-based post-exploitation framework designed for Windows environments. It leverages native COM interfaces to establish command and control (C2) over compromised hosts, functioning as a rootkit similar to Meterpreter or PowerShell Empire. Commonly used in red team engagements for maintaining persistence, executing modules, and evading detection without requiring additional binaries on the target.

## Description

Koadic operates by generating stagers (small payloads) that connect back to a C2 server via protocols like HTTP, HTTPS, or DNS. Once connected, 'zombies' (compromised systems) can be interacted with to run modules for tasks such as keylogging, screenshot capture, privilege escalation, and lateral movement. It emphasizes living off the land by using Windows built-ins, making it stealthy and effective against endpoint detection tools.

## Features

- Feature 1: Modular architecture with 20+ post-exploitation modules (e.g., mimikatz integration, process injection)
- Feature 2: Multiple C2 protocols (HTTP, HTTPS, DNS) for flexible communication
- Feature 3: Obfuscated payloads using JScript/VBScript to bypass AV
- Feature 4: Native Windows COM abuse for rootkit-like persistence without files
- Feature 5: Cross-platform controller (runs on Linux/Windows) targeting Windows victims

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- Windows target with Internet Explorer/Edge for stager execution

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python -y
git clone https://github.com/zerosum0x0/koadic.git
cd koadic
pip install -r requirements.txt
```

On Kali Linux, it's available via apt: `sudo apt install koadic`.

For Windows controller: Use Python installer and run the clone commands in Command Prompt.

## Basic Usage

```python
python koadic.py --help
```

This displays the help menu with options for listeners, generation, and interaction.

### Common Options

| Option | Description |
|--------|-------------|
| -l, --listener | Create or manage listeners (e.g., -l http) |
| -g, --generate | Generate stagers or implants |
| --url | Specify URL path for web-based C2 |
| -p, --port | Set listener port |
| --help | Show help for subcommands |

## Examples

### Example 1: Basic Usage

Start the server and create a listener:

```python
python koadic.py
# In console: listeners
# Then: use http /news
# set port 80
# run
```

Or use CLI for listener:

```python
python koadic.py -l http -p 80 --url /news
```

### Example 2: Advanced Usage

Generate and deploy a stager, then interact:

```python
python koadic.py generate stager jscript http stager.js
# Deliver stager.js to target (e.g., via phishing)
# Once connected: python koadic.py interact zombie1
# In console: use gather/env
# run
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Protocols]] - Application Layer Protocol: Web Protocols (HTTP/HTTPS C2)
- [[Process Injection]] - Process Injection (via COM)
- [[Boot or Logon Autostart Execution]] - Boot or Logon Autostart Execution (persistence modules)
- [[Credential Dumping]] - OS Credential Dumping (mimikatz-like modules)

### Tactics

- [[Command and Control]] - Command And Control
- [[Privilege Escalation]] - Privilege Escalation
- [[Persistence]] - Persistence
- [[Collection]] - Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP traffic from Windows hosts to internal C2 servers, especially with obfuscated JScript payloads
- Detection method 2: COM object instantiation anomalies (e.g., monitoring for scripted COM abuse via Sysmon Event ID 1)
- Detection method 3: Network connections on non-standard ports with user-agent strings mimicking browsers
- Detection method 4: PowerShell or WMI execution of encoded scripts (if modules trigger them)
- Detection method 5: Fileless indicators: No dropped binaries, but increased registry reads/writes for COM persistence

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Covenant]]
- [[PowerShell Empire]]
- [[Meterpreter]]

## References

- Official GitHub: https://github.com/zerosum0x0/koadic
- Documentation: https://koadic.readthedocs.io/
- Related resources: Offensive Security blogs on COM abuse
