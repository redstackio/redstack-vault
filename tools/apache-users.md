---
id: 9ad3617f-db8f-4124-8c09-31ede8aa9517
type: tool
verified: true
created_at: '2019-08-28T21:17:42.847614Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - web-enumeration
  - user-discovery
  - apache
  - reconnaissance
url: 'https://www.kali.org/tools/apache-users/'
commands:
  - '[[commands/apache-users-basic-enumeration]]'
  - '[[commands/apache-users-wordlist-enumeration]]'
validated: true
---

# apache-users

**Status**: Unverified

## Overview

apache-users is a Perl-based tool for enumerating usernames on Apache web servers that have the UserDir module enabled. It is commonly used in reconnaissance phases of penetration testing to discover valid user accounts by exploiting predictable URL patterns like http://target/~username/.

## Description

The tool works by sending HTTP GET requests to potential user directory paths and differentiating between successful (e.g., 200 OK, indicating a valid user directory) and failed (e.g., 404 Not Found) responses. This allows attackers to map out user accounts without authentication. It supports both default and custom wordlists, making it versatile for targeted enumeration. apache-users is particularly effective against misconfigured Apache servers where UserDir is enabled without restrictions.

## Features

- Username enumeration via HTTP response analysis
- Support for custom username wordlists
- Verbose mode for detailed request/response logging
- Configurable target port and protocol (HTTP/HTTPS)
- Lightweight Perl implementation with minimal dependencies

## Installation

### Requirements

- Perl 5+ with LWP::UserAgent module (for HTTP requests)
- Access to a wordlist for advanced usage (e.g., /usr/share/wordlists/)

### Install Commands

```bash
# On Kali Linux (pre-installed)

# On Ubuntu/Debian
sudo apt update
sudo apt install apache-users

# From source (if needed)
git clone https://github.com/nullsecuritynet/tools.git
cd tools/web/apache-users
chmod +x apache-users.pl
```

## Basic Usage

```bash
apache-users -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help and usage information |
| -t <target> | Specify the target host or IP |
| -p <port> | Set the target port (default: 80) |
| -w <wordlist> | Path to custom username wordlist |
| -v | Enable verbose output for debugging |
| --ssl | Use HTTPS instead of HTTP |

## Examples

### Example 1: Basic Usage

```bash
apache-users -t 192.168.1.100
```

This runs enumeration using the built-in default wordlist on port 80.

### Example 2: Advanced Usage

```bash
apache-users -t example.com -p 443 -w /usr/share/wordlists/users.txt --ssl -v
```

This targets an HTTPS server on port 443 with a custom wordlist and verbose logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.001]] Local Account
- [[Determine Physical Locations]] Gather Victim Org Information: Credentials

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Web server access logs showing repeated requests to /~<username>/ paths from a single IP
- Spike in 404 errors for non-existent user directories
- Patterns of sequential username guesses (e.g., root, admin, user1)
- Network monitoring for HTTP probes to UserDir-enabled endpoints
- WAF rules blocking enumeration attempts based on request volume

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dirbuster]]
- [[tools/Gobuster]]
- [[tools/Nikto]]

## References

- Official Kali Documentation: https://www.kali.org/tools/apache-users/
- Source Repository: https://github.com/nullsecuritynet/tools/tree/master/web/apache-users
- Apache UserDir Module: https://httpd.apache.org/docs/2.4/mod/mod_userdir.html
