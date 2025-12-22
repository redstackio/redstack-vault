---
id: cd1cdde9-9b3b-4538-af13-5ca2b3c4c57a
name: smtp-user-enum
type: tool
verified: true
created_at: '2019-08-28T21:17:22.266188+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/smtp-user-enum-enumerate-users-rcpt-mode]]'
tags:
  - enumeration
  - network
  - smtp
platforms:
  - Linux
url: 'http://pentestmonkey.net/tools/smtp-user-enum'
validated: true
---

# smtp-user-enum

**Status**: Unverified

## Overview

smtp-user-enum is a specialized tool for enumerating OS-level user accounts on systems running SMTP services like sendmail. It performs enumeration by sending SMTP commands such as VRFY, EXPN, and RCPT TO, then inspecting the server's responses to identify valid users. This is commonly used in reconnaissance phases to discover valid usernames for further attacks like brute-force or credential stuffing.

## Description

The tool supports multiple enumeration modes (VRFY, EXPN, RCPT) and can handle multi-threaded scanning for efficiency. It works against unprotected SMTP servers that respond differently to valid vs. invalid recipients, allowing attackers to infer user existence. Use it during network enumeration when SMTP port 25 (or 587) is open and the service is not hardened against such probes.

## Features

- Feature 1: Multiple SMTP command modes (VRFY, EXPN, RCPT) for flexible enumeration
- Feature 2: Multi-threaded workers for faster scanning of large username lists
- Feature 3: Support for target domains and custom timeouts to handle varied SMTP implementations
- Feature 4: Verbose output and result counting for easy analysis

## Installation

### Requirements

- Linux distribution with Perl (for the script-based tool)
- Network access to target SMTP servers

### Install Commands

```bash
# On Kali Linux (pre-installed or via apt)
apt update && apt install smtp-user-enum

# Manual installation from source
wget http://pentestmonkey.net/tools/smtp-user-enum/smtp-user-enum-1.2.tar.gz
tar -xzf smtp-user-enum-1.2.tar.gz
cd smtp-user-enum-1.2
chmod +x smtp-user-enum.pl
sudo mv smtp-user-enum.pl /usr/local/bin/smtp-user-enum
```

## Basic Usage

```bash
smtp-user-enum --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -M, --mode | Enumeration mode: VRFY, EXPN, or RCPT |
| -U, --users | File containing usernames to test |
| -t, --target | Target IP or hostname |
| -d, --domain | Domain to append to usernames |
| -p, --port | SMTP port (default: 25) |
| -w, --workers | Number of worker processes (default: 5) |
| -T, --timeout | Query timeout in seconds (default: 5) |
| -v, --verbose | Enable verbose output |

## Examples

### Example 1: Basic Usage

```bash
smtp-user-enum -M RCPT -U /path/to/users.txt -t 192.168.1.100
```

### Example 2: Advanced Usage

```bash
smtp-user-enum -M VRFY -U users.txt -t mail.example.com -p 25 -d example.com -w 10
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor SMTP logs for repeated VRFY/EXPN/RCPT queries from a single source IP
- Detection method 2: High volume of failed SMTP recipient checks in server logs
- Detection method 3: Network IDS rules for SMTP enumeration patterns (e.g., Snort rules for smtp-user-enum signatures)

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

- Official website: http://pentestmonkey.net/tools/smtp-user-enum
- GitHub mirror: https://github.com/pentestmonkey/smtp-user-enum
