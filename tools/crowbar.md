---
type: tool
description: >-
  Crowbar is a brute-forcing tool for penetration testing, supporting key-based
  and password-based attacks on protocols like SSH, VNC, RDP, and OpenVPN.
url: 'https://github.com/galkan/crowbar'
verified: true
tags:
  - brute-force
  - network
platforms:
  - Linux
commands:
  - '[[commands/crowbar-ssh-brute-with-key]]'
  - '[[commands/crowbar-ssh-password-brute]]'
  - '[[commands/crowbar-vnc-password-brute]]'
  - '[[commands/crowbar-rdp-password-brute]]'
  - '[[commands/crowbar-openvpn-password-brute]]'
validated: true
---

# crowbar

**Status**: Unverified

## Overview

Crowbar (formerly known as Levye) is a specialized brute-forcing tool designed for penetration testing. It differentiates itself by supporting alternative authentication methods, such as using SSH private keys for brute-forcing SSH servers, in addition to traditional username/password dictionary attacks. It's particularly useful for testing weak credentials or keys on remote services like SSH, VNC, RDP, and OpenVPN.

## Description

Crowbar was developed to provide brute-forcing capabilities that go beyond standard tools. For instance, while many tools rely solely on username/password pairs for SSH, Crowbar allows the use of obtained private keys to attempt logins against a list of potential usernames. This makes it valuable in red team scenarios where keys have been extracted from compromised systems. It supports multi-threading for efficiency and works with wordlists for scalable attacks. Common use cases include lateral movement testing and credential validation during engagements.

## Features

- Key-based brute forcing for SSH using private keys against username lists
- Password dictionary attacks for SSH, VNC, RDP, and OpenVPN
- Multi-threaded execution to speed up attempts
- Support for single credentials or file-based lists
- Integration with underlying tools like Paramiko for SSH and FreeRDP for RDP
- Verbose logging for monitoring progress and results

## Installation

### Requirements

- Python 3.6+
- pip
- Git
- For RDP: FreeRDP installed (on Debian/Ubuntu: apt install freerdp2-x11)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/galkan/crowbar.git
cd crowbar

# Install Python dependencies
pip3 install -r requirements.txt

# On Debian/Ubuntu, ensure system deps
sudo apt update
sudo apt install python3-paramiko freerdp2-x11
```

For other platforms like macOS, use Homebrew for dependencies: `brew install freerdp`.

## Basic Usage

```bash
python3 crowbar.py -h
```

This displays help with all options and supported services.

### Common Options

| Option | Description |
|--------|-------------|
| -b, --bruteforce | Protocol to target (ssh, vnc, rdp, openvpn) |
| -s, --site | Target IP address or hostname |
| -u, --user | Username or path to user list file |
| -c, --pass | Password or path to password list file |
| -k, --key | Path to SSH private key file (for key-based attacks) |
| -t, --thread | Number of threads (default: 10) |
| -v, --verbose | Enable detailed output |

## Examples

### Example 1: Basic SSH Password Brute Force

```bash
python3 crowbar.py -b ssh -s 192.168.1.100 -u users.txt -c passwords.txt
```

### Example 2: SSH Key Brute Force

```bash
python3 crowbar.py -b ssh -s target.com -u /path/to/users.txt -k id_rsa -t 20
```

For more specific examples, see the related commands below.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Password Spraying]] Password Spraying

### Tactics

- [[Credential Access]] Credential Access

## Detection

- Monitor for high volumes of failed authentication attempts on targeted services (e.g., SSH logs showing rapid logins from single source)
- Detect unusual SSH key authentications or key mismatches in auth logs
- Network traffic analysis for repeated connection attempts to ports 22 (SSH), 5900 (VNC), 3389 (RDP), 1194 (OpenVPN)
- Endpoint detection for Python processes spawning network connections with brute-force patterns
- Use tools like Fail2Ban or IDS rules for brute-force signatures

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hydra]]
- [[tools/medusa]]

## References

- Official GitHub: https://github.com/galkan/crowbar
- Documentation in repo README
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1110/
