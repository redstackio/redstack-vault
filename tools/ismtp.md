---
id: c4418930-98ba-443f-b80d-25b113944263
type: tool
verified: true
created_at: '2019-08-28T21:17:36.862139Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smtp
  - enumeration
  - relay
  - spoofing
  - reconnaissance
url: 'https://github.com/nulltr0py/ismtp'
commands:
  - '[[commands/ismtp-vrfy-user-enumeration]]'
  - '[[commands/ismtp-rcpt-user-enumeration]]'
  - '[[commands/ismtp-relay-test]]'
  - '[[commands/ismtp-spoofing-test]]'
validated: true
---

# iSMTP

**Status**: Unverified

## Overview

iSMTP is a specialized tool for testing SMTP servers, focusing on user enumeration via VRFY and RCPT TO commands, detecting open relays, and assessing internal spoofing vulnerabilities. It is commonly used in penetration testing to identify weaknesses in email infrastructure that could lead to account discovery or abuse for phishing campaigns.

## Description

iSMTP automates interactions with SMTP services to probe for misconfigurations. It supports modes for verifying users (VRFY), checking recipient acceptance (RCPT TO), testing relay permissions, and simulating spoofed emails from internal sources. This makes it valuable for reconnaissance in Active Directory environments or any setup with exposed SMTP servers. The tool outputs detailed responses from the server, helping testers interpret security postures without manual telnet sessions.

## Features

- Feature 1: User enumeration using VRFY and RCPT TO commands to identify valid accounts.
- Feature 2: Open relay detection by attempting cross-domain email routing.
- Feature 3: Internal spoofing tests to check if forged sender addresses are accepted.
- Feature 4: Customizable wordlists and domains for targeted testing.
- Feature 5: Verbose logging of SMTP transaction responses for analysis.

## Installation

### Requirements

- Linux environment (Kali Linux recommended).
- Python 2/3 (depending on version).
- Access to wordlists for enumeration.

### Install Commands

```bash
# On Kali Linux: Pre-installed or update repos
git clone https://github.com/nulltr0py/ismtp.git
cd ismtp
chmod +x ismtp.py
sudo cp ismtp.py /usr/local/bin/ismtp

# On Ubuntu/Debian:
sudo apt update
sudo apt install python3
# Then clone as above
```

## Basic Usage

```bash
ismtp --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and usage |
| -v, --verbose | Enable verbose output for detailed SMTP responses |
| -t | Specify target SMTP server |
| -m | Set mode (vrfy, rcpt, relay, spoof) |
| -u | User wordlist file |

## Examples

### Example 1: Basic Usage

```bash
ismtp -t 192.168.1.100 -m vrfy -u users.txt
```

### Example 2: Advanced Usage

```bash
ismtp -t mail.example.com -m relay -f external@domain.com -r victim@gmail.com -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Network Service Scanning]] Network Service Scanning
- [[Exploitation of Remote Services]] Exploitation of Remote Services

### Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual volume of VRFY or RCPT TO commands from a single source IP in SMTP logs.
- Detection method 2: Failed relay attempts or spoofed MAIL FROM in server transaction logs.
- Detection method 3: Network monitoring for connections to port 25/465/587 with enumeration patterns.
- Detection method 4: Enable SMTP logging (e.g., via Postfix or Exchange) to capture command sequences.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/smtp-user-enum]]
- [[Swaks]]

## References

- Official GitHub Repository: https://github.com/nulltr0py/ismtp
- Kali Linux Tools Page: https://tools.kali.org/information-gathering/ismtp
- SMTP Security Best Practices: RFC 5321
