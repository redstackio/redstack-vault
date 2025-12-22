---
id: 66701752-cc1e-4a5b-add9-1055d4d27633
type: tool
verified: true
created_at: '2019-08-28T21:17:41.832977+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - command-injection
  - web-exploitation
  - automation
  - pentesting
url: 'https://github.com/commixproject/commix'
validated: true
---

# Commix

**Status**: Unverified

## Overview

Commix is a fast and thorough automated command injection exploitation tool written in Python. It is designed for web developers, penetration testers, and security researchers to identify and exploit command injection vulnerabilities in web applications. Commix automates the detection and exploitation process, supporting various injection techniques and providing an interactive shell upon success.

## Description

Commix (short for [comm]and [i]njection e[x]ploiter) simplifies the testing of web applications for command injection flaws. It can detect vulnerabilities in parameters or strings within HTTP requests and exploit them to execute arbitrary OS commands on the target server. The tool supports classic, time-based, file-based, and other blind injection methods, making it versatile for different scenarios. It is particularly useful in black-box testing where direct feedback is limited.

## Features

- Automatic detection of command injection vulnerabilities using multiple techniques (classic, time-based, file-based, error-based).
- Interactive post-exploitation shell for executing commands on the target.
- Tamper scripts to bypass web application firewalls (WAFs) and filters.
- Support for various HTTP methods (GET, POST, PUT, etc.) and encodings.
- Session management and proxy integration for advanced testing.
- Detailed logging and reporting of exploitation attempts.

## Installation

### Requirements

- Python 2.7 or Python 3.x
- Git (for cloning the repository)
- Standard Python libraries (urllib, etc.)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/commixproject/commix.git

# Navigate to the directory
cd commix

# Run the installer (optional, sets up dependencies)
python commix.py --install

# Verify installation
python commix.py --version
```

For pip installation (if available via PyPI):
```bash
pip install commix
```

## Basic Usage

```bash
python commix.py -u "http://target.com/vulnerable_page.php?id=1"
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target URL to test for injection |
| `-r, --request-file` | Load HTTP request from file |
| `--technique` | Specify injection technique (classic, time, file, etc.) |
| `-t, --tamper` | Use tamper scripts to bypass filters |
| `--proxy` | Use a proxy server (e.g., --proxy=http://127.0.0.1:8080) |
| `-v, --verbose` | Increase verbosity level |
| `--os-cmd` | Execute a specific OS command |

## Examples

### Example 1: Basic Usage

Test a URL for command injection:

```bash
python commix.py -u "http://example.com/page.php?param=test" --batch
```

This runs in non-interactive mode and automatically confirms actions.

### Example 2: Advanced Usage

Use time-based technique with a tamper script and proxy:

```bash
python commix.py -u "http://example.com/page.php?param=test" --technique=time --tamper=space2comment --proxy=socks://127.0.0.1:1080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] - Command and Scripting Interpreter: Unix Shell
- [[Exploit Public-Facing Application]] - Exploit Public-Facing Application
- [[Web Shell]] - Server Software Component: Web Shell

### Tactics

- [[Execution]] - Execution
- [[Initial Access]] - Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP requests with encoded payloads (e.g., base64, URL encoding) targeting parameters.
- Network traffic anomalies, such as repeated requests to the same endpoint with varying payloads.
- Server-side logs showing command execution attempts (e.g., ping, sleep, or file reads).
- Presence of Python processes or commix.py on compromised systems (if uploaded).
- Integration with proxies like Burp Suite may show tool-specific headers.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]] - For SQL injection testing
- [[Burp-Suite]] - Web proxy and scanner
- [[ZAP]] - OWASP Zed Attack Proxy

## References

- Official GitHub: https://github.com/commixproject/commix
- Documentation: https://commixproject.com
- Blog posts on command injection techniques
