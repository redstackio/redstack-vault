---
id: 343d81ac-f42c-473a-868e-793cfdf58600
type: tool
verified: true
created_at: '2019-08-28T21:17:24.129204+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - password-cracking
  - gui
  - john-the-ripper
url: 'https://www.openwall.com/john/'
validated: true
---

# johnny

**Status**: Unverified

## Overview

Johnny is a graphical user interface (GUI) frontend for John the Ripper, a popular password cracking tool. It simplifies the process of loading hash files, selecting wordlists, configuring cracking rules, and monitoring progress, making it accessible for users who prefer a visual interface over command-line operations. Commonly used in penetration testing for offline password analysis after hash extraction.

## Description

Johnny integrates directly with John the Ripper's backend, allowing users to perform dictionary attacks, brute-force cracking, and rule-based mutations without needing to construct complex command lines. It supports session management, real-time status updates, and export of results. Ideal for red teamers and security analysts who need to crack passwords from various formats like NTLM, MD5, SHA, and Kerberos tickets. Note that Johnny requires John the Ripper to be installed as its core engine.

## Features

- **Session Management**: Load, save, and resume cracking sessions.
- **Hash Loading**: Import hashes from files in multiple formats supported by John.
- **Wordlist Selection**: Choose from built-in or custom dictionaries.
- **Rule Configuration**: Apply mutation rules for advanced attacks.
- **Progress Monitoring**: Real-time ETA, speed, and cracked password display.
- **Export Results**: Save cracked passwords and session logs.

## Installation

### Requirements

- John the Ripper (core dependency)
- Qt libraries for GUI rendering
- Supported on Linux distributions like Kali or Ubuntu

### Install Commands

```bash
# On Kali Linux (pre-installed with John the Ripper)
# No additional installation needed if John is present

# On Ubuntu/Debian
sudo apt update
sudo apt install john johnny

# From source (if needed)
git clone https://github.com/openwall/john.git
cd john/src
./configure && make -s clean && make -sj4
sudo make install
# Johnny is included in the run/ directory
```

## Basic Usage

```bash
johnny
```

This launches the GUI. Once open, use the menu to load a hash file (e.g., via File > Load Hashes), select a wordlist, and start cracking.

### Common Options

Johnny primarily operates via GUI, but can be launched with basic CLI flags for automation:

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and available options |
| `--session=SESSION_NAME` | Load a specific saved session |
| `-g` | Run in graphics mode (default) |

## Examples

### Example 1: Basic Launch

```bash
johnny
```

Opens the main GUI window for interactive use.

### Example 2: Load Specific Session

```bash
johnny --session=my-crack-session
```

Resumes a previously saved cracking session named 'my-crack-session'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'johnny' or 'john' executables with high CPU usage.
- File system artifacts: Temporary session files in ~/.john/ or user directories.
- Network indicators: None (offline tool), but watch for hash file transfers.
- Log analysis: Audit logs showing GUI launches or John subprocesses.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/john-the-ripper]]
- [[tools/Hashcat]]

## References

- Official John the Ripper documentation: https://www.openwall.com/john/
- Kali Tools page: https://www.kali.org/tools/johnny/
