---
id: 246494e9-c0d5-4e4c-bf2e-bff365526604
type: tool
verified: true
created_at: '2019-08-28T21:17:30.697871+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - credential-access
  - password-dumping
  - post-exploitation
url: 'https://github.com/AlessandroZ/LaZagne'
commands:
  - '[[commands/lazagne-dump-all-credentials]]'
  - '[[commands/lazagne-dump-browser-passwords]]'
  - '[[commands/lazagne-dump-wifi-profiles]]'
  - '[[commands/lazagne-dump-windows-credentials]]'
validated: true
---

# LaZagne

**Status**: Unverified

## Overview

LaZagne is an open-source application designed to retrieve passwords and credentials stored on a local computer. It supports a wide range of modules for extracting data from browsers, WiFi profiles, Windows credential stores, databases, and more. Commonly used in penetration testing for credential access during post-exploitation phases.

## Description

LaZagne automates the recovery of various credentials by targeting application-specific storage mechanisms. It works on multiple platforms and does not require administrative privileges for many modules, though elevated access enhances results. Key use cases include harvesting saved passwords for lateral movement, privilege escalation, or data exfiltration in red team engagements.

## Features

- **Multi-Module Support**: Extracts from browsers (Chrome, Firefox, etc.), WiFi, Windows (SAM, LSA), Apple iCloud, databases (SQL Server, PostgreSQL), and chat apps (Pidgin, Thunderbird).
- **Cross-Platform**: Compatible with Windows, Linux, and macOS.
- **No Dependencies for Core Modules**: Most extractions use built-in libraries.
- **Output Formatting**: Credentials displayed in console or exportable to files.
- **Stealth Options**: Runs quietly without GUI prompts.

## Installation

### Requirements

- Python 3.x
- Git (for cloning the repository)

### Install Commands

```bash
# Clone the repository
 git clone https://github.com/AlessandroZ/LaZagne.git
 cd LaZagne

# For Windows executable (pre-built)
# Download from releases: https://github.com/AlessandroZ/LaZagne/releases

# Run directly with Python (no install needed)
 python laZagne.py --help
```

On Kali Linux, it may be available via apt, but cloning ensures the latest version:

```bash
apt update && apt install python3 git
# Then clone as above
```

## Basic Usage

```python
python laZagne.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and available modules |
| `-p, --path` | Specify a path for modules (e.g., custom browsers) |
| `-o, --output` | Output results to a file |
| `--json` | Export results in JSON format |

## Examples

### Example 1: Basic Usage

Dump all credentials:

```python
python laZagne.py all
```

### Example 2: Advanced Usage

Dump browser passwords and output to JSON:

```python
python laZagne.py browsers --json > browsers.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials from Password Stores]] Credentials from Password Stores
- [[Credential Dumping]] OS Credential Dumping
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for `laZagne.py` or `LaZagne.exe` executions via EDR tools.
- **File Access**: Anomalous reads from browser profile directories (e.g., `%APPDATA%\Google\Chrome`) or WiFi config files.
- **Registry Queries**: Access to Windows credential hives (SAM, SYSTEM).
- **Network**: No direct network activity, but follow-up actions like credential use may trigger alerts.
- **Logging**: Enable PowerShell/Python logging; check for script block executions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]] (Advanced Windows credential dumping)
- [[SharpDPAPI]] (DPAPI credential extraction)

## References

- Official GitHub: https://github.com/AlessandroZ/LaZagne
- Documentation: https://github.com/AlessandroZ/LaZagne/wiki
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1555/
