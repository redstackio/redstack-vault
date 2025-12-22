---
id: 5558e8bf-6f18-443d-915d-44c0bab5daa1
type: tool
verified: true
created_at: '2019-08-28T21:17:24.990989+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
tags:
  - fuzzing
  - directory-traversal
  - vulnerability-discovery
  - perl
url: 'https://github.com/3c7oit/dotdotpwn'
validated: true
---

# DotDotPwn

**Status**: Unverified

## Overview

DotDotPwn is a flexible, intelligent fuzzing tool designed to discover directory traversal vulnerabilities in various services and applications, including HTTP/FTP/TFTP servers and web platforms like CMSs, ERPs, and blogs. It supports protocol-specific modules and a protocol-independent payload sender, making it versatile for penetration testing and vulnerability assessment. Category: Vulnerability Scanning / Fuzzing.

## Description

Written in Perl, DotDotPwn runs on both *NIX and Windows systems. It was the first Mexican tool included in BackTrack Linux (BT4 R2). The tool intelligently crafts and sends payloads with escalating numbers of '../' sequences to test for path traversal weaknesses. It can output results to files or STDOUT for scripting integration. Supported fuzzing modules include HTTP, HTTP URL, FTP, TFTP, Payload (protocol-independent), and STDOUT.

## Features

- **Modular Fuzzing**: Dedicated modules for HTTP, FTP, TFTP, and generic payload sending.
- **Intelligent Payload Generation**: Automatically escalates traversal depth to find the breaking point.
- **Protocol Independence**: Payload module works with any TCP service.
- **Scripting Support**: STDOUT mode for generating payloads without network interaction.
- **Cross-Platform**: Perl-based, runs on Linux, Windows, and other Perl-supported environments.
- **Output Logging**: Saves results to files for analysis and reporting.

## Installation

### Requirements

- Perl 5.x (with core modules; no additional CPAN modules typically needed).
- Network access to target services.

### Install Commands

```bash
# Clone from GitHub (recommended)
git clone https://github.com/3c7oit/dotdotpwn.git
cd dotdotpwn

# Or download and extract the script manually
wget https://raw.githubusercontent.com/3c7oit/dotdotpwn/master/dotdotpwn.pl
chmod +x dotdotpwn.pl

# On Kali/Debian-based systems, it may be available via apt (check repositories)
# apt search dotdotpwn  # If available
```

For Windows, use Strawberry Perl or ActivePerl, then run via command prompt.

## Basic Usage

```perl
perl dotdotpwn.pl --help
```

This displays available modules, options, and syntax.

### Common Options

| Option | Description |
|--------|-------------|
| -m, --mode | Specify fuzzing module (http, ftp, tftp, payload, stdout) |
| -h, --host | Target hostname/IP |
| -p, --port | Target port |
| -f, --fuzz | Fuzzing depth (number of ../) |
| -o, --output | Output file for results |
| -u, --user | Username (for auth modules like FTP) |
| -P, --pass | Password (for auth) |
| -P, --payload | Custom payload string |
| -v, --verbose | Increase verbosity |

## Examples

### Example 1: Basic Usage (HTTP Fuzzing)

```perl
perl dotdotpwn.pl -m http -h example.com -p 80 -f 10 -o http_traversal_results.txt
```

### Example 2: Advanced Usage (FTP with Auth)

```perl
perl dotdotpwn.pl -m ftp -h ftp.target.com -u anonymous -P guest -f 8 -v -o ftp_results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks (for service discovery leading to fuzzing)
- [[File and Directory Discovery]] File and Directory Discovery (via traversal testing)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic**: Unusual sequences of requests with multiple '../' in paths to web/FTP/TFTP services.
- **Process Monitoring**: Perl processes (perl.exe or perl) with network connections and high CPU from fuzzing loops.
- **Logs**: Server access logs showing repeated traversal attempts from a single source IP.
- **IDS Signatures**: Alerts for directory traversal patterns (e.g., Snort rules for ../ payloads).
- **File System**: Presence of dotdotpwn.pl script or output files with fuzzing results.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for initial port scanning before fuzzing)
- [[Ffuf]] (alternative web fuzzer)
- [[Metasploit]] (for exploiting discovered traversals)

## References

- Official GitHub: https://github.com/3c7oit/dotdotpwn
- Original BackTrack inclusion notes
- Perl documentation for networking modules
