---
type: tool
description: >-
  Hamster is a sidejacking tool that acts as a proxy server to hijack web
  sessions by replacing user cookies with stolen ones sniffed from network
  traffic.
url: 'https://github.com/digininja/Hamster'
verified: true
created_at: '2019-08-28T21:17:37.678563+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - sidejacking
  - session-hijacking
  - proxy
  - credential-access
validated: true
---

# hamster

**Status**: Unverified

## Overview

Hamster is a specialized proxy tool designed for sidejacking attacks in offensive security testing. It intercepts HTTP traffic from a user's browser and transparently replaces the session cookies with stolen ones, typically obtained from network sniffing tools like Ferret. This allows testers to hijack active web sessions without needing to crack passwords or exploit vulnerabilities directly. Commonly used in wireless network assessments where unencrypted cookies can be captured.

## Description

Hamster operates as a local proxy server that sits between the user's browser and the target website. When configured, it monitors outgoing requests and substitutes the browser's cookies with those from a stolen session file (e.g., output from Ferret). This technique exploits the use of HTTP cookies for session management, particularly in scenarios where HTTPS is not enforced or during man-in-the-middle attacks on open networks. Hamster does not perform the sniffing itself but relies on external tools for cookie capture; it focuses on the hijacking via proxying. It's lightweight, Python-based, and ideal for red team exercises demonstrating session management flaws.

## Features

- Feature 1: Transparent cookie replacement in proxied HTTP traffic
- Feature 2: Support for session files from sniffers like Ferret (cookie.txt format)
- Feature 3: Configurable listening interface and port for flexible deployment
- Feature 4: No modification to target application required; works on any cookie-based session

## Installation

### Requirements

- Python 2.7 or 3.x (depending on version)
- Network sniffing tool like Ferret for cookie capture
- Root/admin privileges for interface sniffing

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# Manual installation from source
sudo apt update
sudo apt install python3 git

git clone https://github.com/digininja/Hamster.git
cd Hamster
sudo python3 setup.py install

# Or via pip (if available)
pip3 install hamster-sidejacking
```

For Ubuntu/Debian, ensure libpcap is installed for sniffing: `sudo apt install libpcap-dev`.

## Basic Usage

```bash
hamster --help
```

Displays available options, including interface selection and session file loading.

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface for proxying (e.g., -i eth0) |
| -p, --port | Proxy listening port (default: 8080) |
| -c, --cookies | Path to stolen cookies file (e.g., -c cookies.txt from Ferret) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
hamster -i wlan0
```

Starts the proxy on wlan0 interface. Configure your browser to use localhost:8080 as proxy. Provide a cookies.txt file from Ferret for replacement.

### Example 2: Advanced Usage

```bash
hamster -i eth0 -p 3128 -c /path/to/stolen_cookies.txt
```

Runs Hamster on eth0, port 3128, using a specific stolen cookies file for session replacement.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Pass the Hash]] Pass the Cookie

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic on localhost ports (e.g., 8080, 3128) via network monitoring
- Detection method 2: Anomalous cookie values in web requests not matching user sessions (via WAF logs)
- Detection method 3: Presence of Hamster processes or Python scripts with proxy behavior in process lists
- Detection method 4: Increased HTTP traffic patterns indicative of session replay on open networks

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[ferret]]
- [[tools/Wireshark]]
- [[tools/Burp-Suite]]

## References

- Official GitHub Repository: https://github.com/digininja/Hamster
- Kali Linux Tools Page: https://www.kali.org/tools/hamster-sidejacking/
- Related Technique Documentation: MITRE ATT&CK T1539
