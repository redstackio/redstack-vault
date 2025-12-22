---
id: 722437f0-ce25-4c5d-8bcb-008dc3996629
type: tool
verified: true
created_at: '2023-10-01T12:00:00+00:00'
updated_at: '2023-10-01T12:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - pivoting
  - tunneling
  - proxy
  - post-exploitation
  - socks
url: 'https://github.com/sensepost/reGeorg'
commands:
  - '[[commands/regeorg-tunnel-connect]]'
  - '[[commands/regeorg-socks-proxy]]'
validated: true
---

# reGeorg

**Status**: Unverified

## Overview

reGeorg is a Python-based tool for creating SOCKS proxies through compromised web servers. As the successor to reDuh, it enables network pivoting by tunneling traffic via HTTP requests to a bastion or DMZ web server, allowing access to internal networks without direct connectivity.

## Description

reGeorg works by deploying a small tunnel servlet (e.g., in JSP, PHP, or ASP) to a vulnerable web application on the target server. The attacker then connects to this servlet using reGeorg.py to establish a bidirectional tunnel. A SOCKS proxy can be layered on top to route arbitrary traffic through the tunnel. This is particularly useful in scenarios where the web server has access to internal resources but the attacker does not, such as pivoting from a DMZ host to backend databases or services.

## Features

- Feature 1: Supports multiple web languages for tunnel servlets (JSP, PHP, ASP, Python)
- Feature 2: Creates SOCKS4/SOCKS5 proxies for easy integration with standard tools
- Feature 3: HTTP-based tunneling to evade firewalls that block non-HTTP traffic
- Feature 4: Lightweight and scriptable for automation in red team operations
- Feature 5: Handles encoding to bypass basic WAFs and IDS

## Installation

### Requirements

- Python 2.7 or 3.x (with urllib for HTTP handling)
- Git for cloning the repository
- No additional dependencies beyond standard library

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3 -y
git clone https://github.com/sensepost/reGeorg.git
cd reGeorg

# For Python 2 (if needed)
sudo apt install python -y
```

On Windows, use Git Bash or download the ZIP from GitHub and extract.

## Basic Usage

```python
python reGeorg.py --help
```

First, deploy a tunnel servlet to the target (manually upload a template like tunnel.jsp). Then establish the tunnel and SOCKS proxy.

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | URL to the tunnel servlet |
| -p, --port | Local port for tunnel or SOCKS |
| -t, --target | Tunnel endpoint for SOCKS |
| -v | Verbose output for debugging |
| --proxy | Upstream proxy for the connection |

## Examples

### Example 1: Basic Usage

Establish a tunnel:

```python
python reGeorg.py -u http://target.com/tunnel.jsp tunnel -p 8080
```

Then start SOCKS:

```python
python reGeorgSocks.py -p 1080 -t 127.0.0.1:8080
```

### Example 2: Advanced Usage

With upstream proxy:

```python
python reGeorg.py -u http://target.com/tunnel.jsp tunnel -p 8080 --proxy http://corporate-proxy:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy (Command and Control via proxy for internal pivoting)
- [[Encrypted Channel]] Encrypted Channel (HTTP tunneling to blend with legitimate traffic)

### Tactics

- [[Command and Control]] Command and Control
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP POST requests to web servlets with base64-encoded payloads (tunnel traffic)
- Detection method 2: Web server logs showing repeated connections from the same IP to tunnel endpoints
- Detection method 3: Network monitoring for SOCKS-like traffic patterns originating from web servers
- Detection method 4: File integrity checks on web directories for uploaded tunnel servlets (e.g., tunnel.jsp)
- Detection method 5: Python process monitoring on attacker machines for reGeorg.py executions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Chisel]] (Alternative tunneling tool)
- [[Socat]] (General-purpose relay for pivoting)

## References

- Official GitHub: https://github.com/sensepost/reGeorg
- SensePost Blog: https://sensepost.com/blog/2013/regeorg-the-successor-to-reduh/
- Related: Original reDuh tool documentation
