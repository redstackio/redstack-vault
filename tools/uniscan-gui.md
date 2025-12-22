---
id: b616c69d-ac71-4872-8700-5b7d67beac10
type: tool
verified: true
created_at: '2019-08-28T21:17:26.316004+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - web-scanning
  - rfi
  - lfi
  - rce
  - vulnerability-scanner
url: 'https://github.com/j0hnnyw3/Uniscan'
validated: true
---

# uniscan-gui

**Status**: Unverified

## Overview

Uniscan GUI is a graphical user interface for the Uniscan vulnerability scanner, designed to detect Remote File Inclusion (RFI), Local File Inclusion (LFI), and Remote Command Execution (RCE) vulnerabilities in web applications. It simplifies the scanning process for penetration testers by providing an intuitive interface to configure targets, select vulnerability types, and review results, making it suitable for both beginners and experienced users in web security assessments.

## Description

Uniscan GUI wraps the core Uniscan engine, a Perl-based tool that automates the testing of common web vulnerabilities by sending crafted HTTP requests to identify inclusion flaws and command injection points. It supports scanning multiple URLs, using custom wordlists for payloads, and generating reports on discovered vulnerabilities. Commonly used in offensive security operations for reconnaissance and exploitation phases, particularly against PHP-based applications prone to these issues. The GUI enhances usability by visualizing scan progress, displaying real-time results, and allowing easy export of findings.

## Features

- **Graphical Interface**: Point-and-click configuration for scan parameters, reducing the need for command-line expertise.
- **Vulnerability Detection**: Automated testing for RFI (e.g., external file inclusion), LFI (e.g., path traversal), and RCE (e.g., command injection via web interfaces).
- **Customizable Payloads**: Integration with wordlists for protocol fuzzing (HTTP, HTTPS, FTP) and file path testing.
- **Reporting**: Generates HTML or text reports summarizing vulnerabilities, including proof-of-concept requests.
- **Multi-Threading**: Supports concurrent scanning to speed up large target lists.
- **Proxy Support**: Compatible with tools like Burp Suite for request interception and modification.

## Installation

### Requirements

- Perl 5.10 or higher
- GTK+ libraries for GUI (libgtk2.0-dev on Debian-based systems)
- Git for cloning the repository
- Optional: Custom wordlists for advanced scanning

### Install Commands

```bash
# Clone the repository (Uniscan includes GUI components)
git clone https://github.com/j0hnnyw3/Uniscan.git
cd Uniscan

# Install dependencies on Ubuntu/Debian/Kali
sudo apt update
sudo apt install perl libgtk2.0-dev libnet-ssleay-perl libwww-mechanize-perl

# Make scripts executable (GUI launcher)
chmod +x uniscan-gui

# For Kali Linux (often pre-configured or via apt)
sudo apt install uniscan
```

After installation, verify by running `uniscan-gui` from the Uniscan directory.

## Basic Usage

```bash
uniscan-gui
```

This launches the GUI. In the interface:
1. Enter the target URL (e.g., http://example.com/vulnerable.php).
2. Select vulnerability types (RFI, LFI, RCE).
3. Configure options like threads (default 10) or wordlist path.
4. Click "Start Scan" to begin testing.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message (CLI fallback if GUI fails) |
| `-v, --verbose` | Enable verbose logging in GUI console |
| `--wordlist` | Path to custom payload wordlist (GUI file picker alternative) |

## Examples

### Example 1: Basic GUI Launch and Scan

```bash
uniscan-gui
```

In GUI: Input `http://target.com/index.php?page=`, select LFI, use default paths wordlist, start scan. Results show if paths like `../../../etc/passwd` succeed.

### Example 2: Advanced Scan with Custom Wordlist

Launch GUI, then in options: Set wordlist to `/usr/share/wordlists/rfi.txt`, target `https://target.com/search.php?q=`, enable RFI and RCE, proxy to localhost:8080 for Burp integration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application (for identifying RFI/LFI/RCE entry points)
- [[Upload Malware]] Dynamic Resolution (indirectly via protocol fuzzing in scans)

### Tactics

- [[Reconnaissance]] Reconnaissance (scanning for web vulnerabilities)
- [[Initial Access]] Initial Access (exploiting discovered flaws)

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: High volume of HTTP requests with suspicious payloads (e.g., `http://evil.com/shell.txt` for RFI tests) from a single source IP.
- Process monitoring: Perl processes (uniscan.pl) or GTK windows titled "Uniscan" on compromised systems.
- Logs: Web server access logs showing repeated 200/403 responses to inclusion attempts.
- File artifacts: Presence of Uniscan directory or wordlist files in temp directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]] (for proxying Uniscan traffic)
- [[tools/sqlmap]] (complementary for SQLi testing alongside inclusion vulns)

## References

- Official GitHub: https://github.com/j0hnnyw3/Uniscan
- Documentation: Included README in repository
- Related: OWASP Testing Guide for Injection Flaws
