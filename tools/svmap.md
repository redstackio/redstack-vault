---
id: 8bbd7fe4-0e98-4134-ad7a-87b01d33e0b0
type: tool
verified: true
created_at: '2019-08-28T21:17:41.639467+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - voip
  - sip
  - reconnaissance
  - scanning
url: 'https://github.com/EnableSecurity/sipvicious'
validated: true
---

# svmap

**Status**: Unverified

## Overview

svmap is a SIP scanner from the SIPVicious suite, designed to audit SIP-based VoIP systems by identifying SIP devices and servers within a specified IP range. It is commonly used in penetration testing and security assessments to discover VoIP infrastructure, map potential attack surfaces, and enumerate SIP endpoints for further exploitation or analysis.

## Description

The SIPVicious suite is a collection of open-source tools for auditing Session Initiation Protocol (SIP) devices in VoIP environments. svmap specifically performs network scans to detect SIP servers by sending SIP requests (such as OPTIONS or INVITE) to a range of IP addresses and ports. It helps identify active SIP devices, their responses, and basic configuration details without requiring authentication. This tool is particularly useful in reconnaissance phases of red team engagements targeting unified communications systems, allowing testers to map out PBX systems, softphones, and gateways.

## Features

- IP range scanning for SIP devices on default ports (5060 UDP/TCP)
- Support for custom SIP methods (e.g., OPTIONS, INVITE)
- Rate limiting to avoid detection or overwhelming targets
- Output in various formats for further analysis (e.g., CSV, text)
- Integration with other SIPVicious tools like svwar for extension enumeration

## Installation

### Requirements

- Python 2.7 or 3.x (though Python 2 is deprecated; use a virtual environment)
- Git for cloning the repository
- No additional dependencies beyond standard Python libraries

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3 -y
git clone https://github.com/EnableSecurity/sipvicious.git
cd sipvicious

# For Python 3 (recommended)
pip3 install -r requirements.txt

# Or for legacy Python 2 (if needed)
sudo apt install python2
pip2 install -r requirements.txt
```

On Kali Linux, SIPVicious is available in the repositories:

```bash
sudo apt update && sudo apt install sipvicious
```

For macOS with Homebrew:

```bash
brew install sipvicious
```

For Windows, use a Python environment and clone as above.

## Basic Usage

```bash
python3 svmap.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m, --method` | Specify SIP method to use (default: OPTIONS) |
| `-p, --port` | Target port (default: 5060) |
| `-r, --rate` | Packets per second (default: 100) |
| `-o, --output` | Output file format (e.g., csv) |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Scan an IP range for SIP devices using default OPTIONS method:

```bash
python3 svmap.py 192.168.1.0/24
```

### Example 2: Advanced Usage

Scan with INVITE method, custom port, and rate limiting, outputting to CSV:

```bash
python3 svmap.py -m INVITE -p 5060 -r 50 -o results.csv 10.0.0.0/16
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SIP OPTIONS or INVITE requests from scanning IPs
- High volume of UDP/TCP traffic on port 5060
- Log entries in SIP servers (e.g., Asterisk, FreePBX) showing probe attempts
- Network IDS alerts for SIP protocol abuse

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/svwar]]
- [[tools/svcrack]]
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/EnableSecurity/sipvicious
- SIPVicious Documentation: Included in repo README
- VoIP Security Best Practices: OWASP VoIP Guide
