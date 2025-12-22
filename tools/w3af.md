---
id: be0d842e-5b17-47be-b791-e82789b58581
type: tool
verified: true
created_at: '2019-08-28T21:17:37.009400+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - web
  - scanner
  - exploitation
  - vulnerability-assessment
url: 'https://w3af.org/'
commands:
  - '[[commands/w3af-start-console]]'
  - '[[commands/w3af-run-audit]]'
  - '[[commands/w3af-grep-scan]]'
validated: true
---

# w3af

**Status**: Unverified

## Overview

w3af (Web Application Attack and Audit Framework) is an open-source tool designed to identify and exploit vulnerabilities in web applications. It functions as a comprehensive framework for automated security testing, similar to Metasploit but focused on web environments. w3af supports black-box scanning techniques to discover issues like SQL injection, XSS, and remote file inclusion through its extensive plugin architecture.

## Description

w3af provides both a graphical user interface (GUI) and a command-line console for conducting web vulnerability audits. The core is written in Python, featuring over 130 plugins categorized into types such as audit (for exploitation), grep (for information gathering), and infrastructure (for evasion). It crawls web applications, identifies entry points, and attempts exploits, generating detailed reports on findings. This tool is particularly useful in penetration testing for mapping attack surfaces and validating vulnerabilities in production-like environments without requiring source code access.

## Features

- **Plugin-Based Architecture**: Modular plugins for reconnaissance, auditing, and exploitation.
- **Automated Crawling**: Discovers URLs, forms, and parameters dynamically.
- **Vulnerability Exploitation**: Attempts to confirm and exploit detected issues like SQLi and XSS.
- **Reporting**: Outputs results in multiple formats (HTML, XML, text) for easy analysis.
- **Evasion Techniques**: Supports proxies, tamperers, and encoding to bypass WAFs.
- **GUI and CLI Support**: Visual interface for beginners and scriptable console for automation.

## Installation

### Requirements

- Python 2.7 or 3.x (depending on version)
- Git for source installation
- Dependencies: libxml2, libxslt, nmap (for some plugins)

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install w3af

# On Ubuntu (from repositories)
sudo apt update && sudo apt install w3af

# From source (latest version)
git clone https://github.com/andresriancho/w3af.git
cd w3af
pip install -r requirements.txt
python w3af_console
```

For macOS, use Homebrew: `brew install w3af` (may require additional setup).

## Basic Usage

```bash
w3af_console --help
```

This displays available options for the console.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help and usage information |
| -s, --script | Run in non-interactive script mode |
| -p, --plugins | Specify plugins to load (e.g., -p audit,grep) |
| -t, --target | Set the target URL |
| -o, --output | Specify output plugin (e.g., -o html) |

## Examples

### Example 1: Basic Usage

Start the interactive console:

```bash
w3af_console
```

Inside the console:

```
w3af>>> set target http://example.com
w3af>>> plugins
w3af/plugins>>> start audit
```

### Example 2: Advanced Usage

Non-interactive audit scan:

```bash
w3af_console -s -p audit,output.html -t http://example.com
```

This runs an automated scan and saves results to HTML.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript (for XSS testing)
- [[Exploit Public-Facing Application]] (for SQL injection and other injection flaws)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: High volume of HTTP requests from a single source with varying User-Agents or paths mimicking w3af signatures.
- Process monitoring: Presence of `w3af_console` or Python processes with w3af modules on compromised hosts.
- Logs: Web server logs showing probing for common vulnerabilities (e.g., /admin, SQL error patterns).
- IDS/IPS alerts: Signatures for known w3af plugin behaviors, like fuzzing parameters.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/ZAP]]
- [[tools/sqlmap]]

## References

- Official website: https://w3af.org/
- GitHub repository: https://github.com/andresriancho/w3af
- Documentation: https://w3af.org/documentation/
- Kali Linux tools page: https://www.kali.org/tools/w3af/
