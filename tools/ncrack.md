---
id: 881a4582-4699-4873-924b-62eb405a9054
type: tool
verified: true
created_at: '2019-08-28T21:17:30.434071+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - bruteforce
  - credential-access
  - network-authentication
url: 'https://nmap.org/ncrack/'
commands:
  - '[[commands/ncrack-ssh-password-bruteforce]]'
  - '[[commands/ncrack-rdp-password-bruteforce]]'
  - '[[commands/ncrack-http-basic-auth-bruteforce]]'
  - '[[commands/ncrack-ftp-password-bruteforce]]'
validated: true
---

# ncrack

**Status**: Unverified

## Overview

Ncrack is a high-speed network authentication cracking tool designed for proactive security testing. It targets weak passwords across multiple protocols and hosts, aiding in network audits and vulnerability assessments by simulating brute-force attacks.

## Description

Ncrack was built to help companies secure their networks by proactively testing all their hosts and networking devices for poor passwords. Security professionals also rely on Ncrack when auditing their clients. Ncrack was designed using a modular approach, a command-line syntax similar to Nmap, and a dynamic engine that can adapt its behavior based on network feedback. It allows for rapid, yet reliable large-scale auditing of multiple hosts. Ncrack’s features include a very flexible interface granting the user full control of network operations, allowing for very sophisticated bruteforcing attacks, timing templates for ease of use, runtime interaction similar to Nmap’s, and many more. Protocols supported include SSH, RDP, FTP, Telnet, HTTP(S), POP3(S), IMAP, SMB, VNC, SIP, Redis, PostgreSQL, MySQL, MSSQL, MongoDB, Cassandra, WinRM, and OWA.

## Features

- Modular design supporting over 15 protocols for authentication cracking
- Dynamic timing engine that adjusts speed based on network conditions
- User interaction during runtime for pausing, resuming, or adjusting attacks
- Support for pairwise and combinatorial password guessing
- Flexible input/output handling for user and password lists
- Parallel processing for multi-host and multi-protocol attacks

## Installation

### Requirements

- Standard build tools (gcc, make)
- Network libraries (libssh, libssl)

### Install Commands

```bash
# Kali Linux (pre-installed)
sudo apt update && sudo apt install ncrack

# Ubuntu
sudo apt update && sudo apt install ncrack

# From source (all platforms)
git clone https://github.com/nmap/ncrack.git
cd ncrack
./configure
make
sudo make install

# Windows/macOS: Use pre-built binaries from nmap.org or compile with MSYS2/Brew
brew install ncrack  # macOS with Homebrew
```

## Basic Usage

```bash
ncrack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Increase verbosity level |
| -p <port> | Specify port(s) to scan |
| -U <file> | Username list file |
| -P <file> | Password list file |
| -T <level> | Timing template (1-5, default 3) |

## Examples

### Example 1: Basic Usage

```bash
ncrack -p 22 192.168.1.100
```

Attempts default credentials on SSH port 22.

### Example 2: Advanced Usage

```bash
ncrack -p 22,3389 192.168.1.0/24 -U users.txt -P passwords.txt -T4
```

Brute-forces SSH and RDP across a subnet using custom lists.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Guessing]] Password Guessing
- [[Password Cracking]] Password Cracking
- [[Password Spraying]] Brute Force

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of failed authentication attempts in logs (e.g., /var/log/auth.log for SSH)
- Unusual network traffic patterns to authentication ports (22, 3389, 21, etc.) from a single source
- Connection attempts to multiple protocols/hosts in short bursts
- Monitor for ncrack process signatures or similar tools via EDR
- Rate limiting and account lockouts on services can mitigate and alert on brute-force attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/Hydra]]

## References

- Official website: https://nmap.org/ncrack/
- GitHub repository: https://github.com/nmap/ncrack
- Nmap Project documentation
