---
id: 810c215f-61f2-4613-b7e3-5fb4cf8987d3
type: tool
verified: true
created_at: '2019-08-28T21:17:37.666310+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - voip
  - iax
  - enumeration
  - brute-force
  - reconnaissance
url: 'https://github.com/EnableSecurity/enumIAX'
validated: true
---

# enumiax

**Status**: Unverified

## Overview

enumIAX is a specialized tool for enumerating usernames on Inter-Asterisk eXchange (IAX) protocol services, commonly used in VoIP systems like Asterisk PBX. It supports two modes: sequential numerical guessing (e.g., user100 to user999) and dictionary-based attacks using a wordlist. This tool is valuable in penetration testing for discovering valid accounts during reconnaissance phases of VoIP security assessments.

## Description

enumIAX operates by sending IAX authentication requests to a target server and analyzing responses to determine valid usernames. In sequential mode, it iterates through a range of numeric extensions, ideal for environments with predictable naming conventions. Dictionary mode loads usernames from a file, allowing for more customized attacks based on common VoIP usernames (e.g., admin, extension, sipuser). The tool includes rate-limiting options to evade basic detection. It is lightweight, written in Perl, and focuses solely on IAXv2 protocol enumeration without broader VoIP support.

## Features

- Feature 1: Sequential username brute-forcing with customizable start/end ranges.
- Feature 2: Dictionary-based enumeration from text files.
- Feature 3: Configurable delays between attempts to reduce detection risk.
- Feature 4: Simple output logging valid/invalid users for further analysis.

## Installation

### Requirements

- Perl 5 (standard on most Linux distributions).
- Network access to target IAX ports (default UDP 4569).

### Install Commands

```bash
# On Kali Linux (pre-installed in some VoIP toolkits, or install via package)
sudo apt update && sudo apt install enumiax

# From source (if not available via package manager)
git clone https://github.com/EnableSecurity/enumIAX.git
cd enumIAX
chmod +x enumiax.pl
sudo cp enumiax.pl /usr/local/bin/enumiax
```

## Basic Usage

```bash
enumiax --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -s, --start | Start number for sequential mode |
| -e, --end | End number for sequential mode |
| -u, --users | Path to username dictionary file |
| -d, --delay | Delay between requests in seconds |
| -h, --help | Show usage help |

## Examples

### Example 1: Basic Usage (Sequential Mode)

```bash
enumiax -s 100 -e 200 192.168.1.100
```

### Example 2: Advanced Usage (Dictionary Mode)

```bash
enumiax -u /usr/share/wordlists/usernames.txt -d 1 target.example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual UDP traffic spikes on port 4569 (IAX default).
- Detection method 2: Failed authentication logs in Asterisk showing sequential or dictionary-based attempts.
- Detection method 3: Network IDS alerts for IAX protocol abuse.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[sipvicious]]
- [[tools/svmap]]

## References

- Official GitHub: https://github.com/EnableSecurity/enumIAX
- VoIP Security Testing Guide: https://www.owasp.org/index.php/OWASP_VoIP_Project
