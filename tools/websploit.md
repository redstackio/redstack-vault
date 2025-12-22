---
id: 4386529f-16a3-43f7-bd44-04727701dfdb
name: websploit
type: tool
verified: true
created_at: '2019-08-28T21:17:38.383701+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - web-exploitation
  - scanning
  - social-engineering
  - network-attacks
url: 'https://github.com/AliasIO/WebSploit'
validated: true
---

# websploit

**Status**: Unverified

## Overview

WebSploit is an open-source penetration testing framework focused on web application exploitation, scanning, crawling, and analysis. It supports automated exploitation, social engineering attacks, and network-based attacks, integrating elements from Metasploit for enhanced functionality. Commonly used in red team operations for identifying and exploiting web vulnerabilities like LFI, SQL injection, and phpMyAdmin weaknesses.

## Description

WebSploit provides a modular framework for offensive security testing, emphasizing web-specific attacks. It includes tools for reconnaissance, exploitation, and post-exploitation, such as Autopwn for automated scanning and exploitation using Metasploit's wmap plugin, format infectors for embedding payloads in files, and specialized scanners for common web apps like phpMyAdmin. The framework also supports network attacks like ARP spoofing, WiFi jamming, and MITM setups. It's particularly useful for targeting web services in internal or external networks, bypassing protections like CloudFlare, and conducting social engineering via fake updates or access points.

## Features

- **Autopwn**: Metasploit-integrated scanner and automatic exploiter for target services.
- **wmap**: Web application mapping and crawling using Metasploit's wmap plugin.
- **Format Infector**: Injects reverse/bind payloads into file formats for exploitation.
- **phpMyAdmin Scanner**: Detects and scans for vulnerabilities in phpMyAdmin installations.
- **CloudFlare Resolver**: Bypasses CloudFlare protections to resolve real IP addresses.
- **LFI Bypasser**: Tests and bypasses local file inclusion filters.
- **Apache Users Scanner**: Enumerates Apache users via server headers.
- **Dir Bruter and Admin Finder**: Brute-forces directories and admin panels.
- **MLITM and MITM Attacks**: Man-in-the-middle setups for XSS phishing.
- **Java Applet and MFOD Attacks**: Browser-based exploitation vectors.
- **USB Infection, ARP Dos, Web Killer**: Physical and network denial-of-service attacks.
- **Fake Update/Access Point, WiFi Honeypot/Jammer/Dos**: Wireless social engineering and disruption.
- **Bluetooth POD Attack**: Bluetooth proximity-based attacks.

## Installation

### Requirements

- Python 2.7 or 3.x (some modules may require Python 2)
- Git
- Metasploit Framework (for Autopwn and wmap modules)
- Dependencies: Install via pip (e.g., requests, beautifulsoup4)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/AliasIO/WebSploit.git /opt/websploit
cd /opt/websploit

# Make executable
chmod +x wsf.py

# Install Python dependencies (if needed)
pip3 install -r requirements.txt

# For Kali Linux: Often available in repos, but git clone recommended for latest
sudo apt update && sudo apt install websploit-framework
```

For Ubuntu:

```bash
sudo apt install git python3-pip
# Then follow clone steps above
```

For macOS (via Homebrew):

```bash
git clone https://github.com/AliasIO/WebSploit.git
cd WebSploit
brew install python3
pip3 install -r requirements.txt
```

## Basic Usage

```bash
python3 wsf.py
```

This launches the interactive shell:

wsf > help  # Show available modules
wsf > use phpmyadmin_scanner  # Load a module
wsf > show options  # View module options
wsf > set URL http://target.com  # Configure
wsf > run  # Execute

### Common Options

| Option | Description |
|--------|-------------|
| `use <module>` | Loads a specific module (e.g., autopwn, lfi_bypasser) |
| `set <option> <value>` | Configures module parameters (e.g., RHOSTS, URL) |
| `show options` | Displays current module settings |
| `run` or `exploit` | Executes the loaded module |
| `back` | Returns to main menu |
| `exit` | Quits WebSploit |

## Examples

### Example 1: Basic Usage

Start and list modules:

```bash
python3 wsf.py
wsf > ls
```

### Example 2: Advanced Usage

Scan with phpMyAdmin module:

```bash
python3 wsf.py
wsf > use phpmyadmin_scanner
wsf > set URL http://192.168.1.100
wsf > run
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript (for XSS modules)
- [[Network Service Scanning]] Network Service Scanning (via wmap)

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic patterns: Unusual scans from Metasploit-integrated modules (e.g., wmap probes).
- Process monitoring: python3 wsf.py or suspicious Python processes with web requests.
- Log analysis: Web server logs showing directory brute-forcing or LFI attempts.
- File system: Presence of WebSploit directory (/opt/websploit) or cloned repo artifacts.
- Behavioral: Automated exploitation attempts correlating with module features like fake AP setups.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/metasploit-framework]]
- [[tools/sqlmap]]
- [[tools/Nikto]]

## References

- Official GitHub: https://github.com/AliasIO/WebSploit
- Documentation: Included in repo README
- Related: Metasploit wmap plugin docs
