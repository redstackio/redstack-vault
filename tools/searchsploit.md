---
id: 256b11f7-72cd-4d8d-8338-fe7c3e52f2c9
type: tool
verified: true
created_at: '2019-08-28T21:17:29.078391+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - exploitation
  - search
  - exploit-db
url: 'https://www.exploit-db.com/'
description: Command-line tool for searching the Exploit Database offline.
validated: true
---

# searchsploit

**Status**: Unverified

## Overview

Searchsploit is a command-line tool that provides offline access to the Exploit Database (Exploit-DB), an archive of public exploits, shellcode, and vulnerability research materials. It is designed for penetration testers, vulnerability researchers, and security professionals to quickly search for exploits related to specific software, vulnerabilities, or keywords without needing an internet connection after initial setup.

## Description

The Exploit Database serves as a comprehensive collection of exploits gathered from direct submissions, mailing lists, and public sources. Searchsploit allows users to query this database locally, making it an essential tool for red teaming, vulnerability assessment, and exploit development. It supports searching by keyword, application, CVE, EDB-ID, and more, with options to view exploit details, download files, or access web URLs.

## Features

- Feature 1: Offline searching of over 30,000 exploits and shellcodes
- Feature 2: Support for case-sensitive searches, exact matching, and JSON output
- Feature 3: Integration with Exploit-DB updates to keep the local database current
- Feature 4: Display of exploit metadata including author, type, platform, and reference links

## Installation

### Requirements

- Python 2.7 or 3.x (though primarily Python 2 compatible)
- Git (for cloning the database)
- Internet access for initial download and updates

### Install Commands

```bash
# On Kali Linux (pre-installed)
# Already available as part of the kali-linux-default metapackage

# On Ubuntu/Debian
sudo apt update
sudo apt install exploitdb

# Manual installation from GitHub
cd /opt
git clone https://gitlab.com/exploit-database/exploitdb.git
ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit

# Update the database after installation
searchsploit -u
```

## Basic Usage

```bash
searchsploit --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -u | Update the local Exploit-DB copy |
| -w | Show full paths/URLs for exploits |
| --case | Case-sensitive search |
| -j | Output results in JSON format |
| -p EDB-ID | Show details for a specific exploit ID |

## Examples

### Example 1: Basic Usage

Search for exploits related to Apache:

```bash
searchsploit apache
```

### Example 2: Advanced Usage

Search for Struts exploits and show URLs:

```bash
searchsploit -w struts
```

Update the database:

```bash
searchsploit -u
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (for researching vulnerabilities)
- [[Stage Capabilities]] Install/Remove Software (for exploit acquisition during operations)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for 'searchsploit' executions in security tools directories
- Detection method 2: Network traffic to Exploit-DB servers during updates (e.g., gitlab.com/exploit-database)
- Detection method 3: File system artifacts like /usr/share/exploitdb or cloned repositories in /opt

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[metasploit-framework]]
- [[tools/Nmap]]

## References

- Official GitLab Repository: https://gitlab.com/exploit-database/exploitdb
- Exploit Database Website: https://www.exploit-db.com/
- Kali Tools Documentation: https://www.kali.org/tools/searchsploit/
