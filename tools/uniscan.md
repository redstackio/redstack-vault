---
id: aebb66a7-6498-4f9a-bf51-b390d7b3928e
type: tool
verified: true
created_at: '2019-08-28T21:17:43.116906+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - web-scanning
  - lfi
  - rfi
  - rce
  - vulnerability-scanner
url: 'https://sourceforge.net/projects/uniscan/'
validated: true
---

# uniscan

**Status**: Unverified

## Overview

Uniscan is a lightweight web vulnerability scanner designed to detect Remote File Inclusion (RFI), Local File Inclusion (LFI), and Remote Command Execution (RCE) flaws in web applications. It is particularly useful during reconnaissance and initial vulnerability assessment phases of penetration testing.

## Description

Uniscan operates by sending crafted HTTP requests to target URLs, testing parameters for inclusion vulnerabilities and command injection points. It supports various modes, including basic scanning, extension-based testing, and focused include scanning. The tool is written in Perl and is command-line based, making it suitable for automated scripts or manual testing in offensive security operations.

## Features

- Feature 1: Detection of LFI via path traversal payloads (e.g., ../../../etc/passwd)
- Feature 2: RFI testing with external file references (e.g., http://attacker.com/shell.txt)
- Feature 3: RCE probing through command injection in parameters
- Feature 4: Support for multiple file extensions (PHP, ASP, JSP, etc.)
- Feature 5: Custom wordlists for payload customization
- Feature 6: Modes for include-specific scanning and full vulnerability checks

## Installation

### Requirements

- Perl 5.x
- wget or curl for downloading payloads if needed
- Linux environment (Kali Linux recommended)

### Install Commands

```bash
# Clone or download from SourceForge
wget https://sourceforge.net/projects/uniscan/files/uniscan.pl/download -O uniscan.pl
chmod +x uniscan.pl

# Or on Kali (if available in repos)
sudo apt update && sudo apt install uniscan
```

## Basic Usage

```perl
./uniscan.pl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Specify target URL |
| -e, --extensions | Test specific file extensions (comma-separated) |
| -i, --include | Include scanner mode for LFI/RFI |
| -w, --wordlist | Custom wordlist for payloads |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```perl
./uniscan.pl -u http://example.com/vulnerable.php
```

### Example 2: Advanced Usage

```perl
./uniscan.pl -u http://example.com -e php,asp -i -w /path/to/payloads.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP requests with path traversal patterns (e.g., multiple ../ in URLs)
- Detection method 2: Logs showing requests to external domains for RFI tests
- Detection method 3: Perl process spawning with uniscan.pl arguments in process lists
- Detection method 4: Web server access logs with repeated parameter fuzzing

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nikto]]
- [[tools/dirb]]

## References

- Official SourceForge page: https://sourceforge.net/projects/uniscan/
- Perl documentation for HTTP requests
