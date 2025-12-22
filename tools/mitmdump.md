---
id: 3e80f9de-ed8c-4381-afd9-08497061c321
type: tool
verified: true
created_at: '2019-08-28T21:17:36.473994+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - proxy
  - traffic-interception
  - mitm
  - http-https
url: 'https://mitmproxy.org/'
validated: true
---

# mitmdump

**Status**: Unverified

## Overview

mitmdump is the command-line companion to mitmproxy, an interactive HTTPS proxy for capturing, inspecting, and modifying HTTP/HTTPS traffic. It provides the core functionality of mitmproxy without the graphical console interface, making it suitable for scripted, automated, or headless environments. Commonly used in penetration testing for traffic analysis, request tampering, and replay attacks.

## Description

mitmdump acts as a man-in-the-middle proxy that intercepts SSL/TLS-encrypted traffic by generating on-the-fly certificates. It allows real-time inspection and editing of HTTP flows, saving conversations for later analysis, and replaying client or server responses. Unlike the full mitmproxy console, mitmdump focuses on batch processing and scripting via Python addons, akin to tcpdump but specialized for HTTP.

## Features

- Intercept and modify HTTP/HTTPS traffic on the fly
- Save HTTP conversations in .mitm format for replay and analysis
- Replay both HTTP clients and servers
- Make scripted changes using Python scripts
- Automatic SSL interception with dynamically generated certificates

## Installation

### Requirements

- Python 3.7+
- pip package manager

### Install Commands

```bash
# On Kali Linux (pre-installed as part of mitmproxy)
# No action needed if mitmproxy is already installed

# On Ubuntu/Debian
sudo apt update
sudo apt install python3-pip
pip3 install mitmproxy

# On macOS with Homebrew
brew install mitmproxy

# From source (optional)
pip3 install --upgrade git+https://github.com/mitmproxy/mitmproxy.git
```

After installation, generate certificates with `mitmdump` (it will prompt on first run).

## Basic Usage

```bash
mitmdump --help
```

Configure your browser or application to use the proxy at localhost:8080 (default port).

### Common Options

| Option | Description |
|--------|-------------|
| -p, --listen-port PORT | Set the listening port (default: 8080) |
| -s, --script SCRIPT | Load a Python script for automation |
| -w, --write FILENAME | Write flows to a file |
| --set OPTION=VALUE | Set configuration options (e.g., --set confdir=~/.mitmproxy/) |
| --flow-filter EXPR | Filter flows (e.g., ~u /api/ for URLs matching /api/) |

## Examples

### Example 1: Basic Usage

```bash
mitmdump -p 8080
```

Starts listening on port 8080 and displays traffic in real-time.

### Example 2: Advanced Usage

```bash
mitmdump -s tamper.py -w session.mitm --flow-filter "~d example.com"
```

Runs with a script to tamper requests, saves to file, and filters for a specific domain.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Initial Access]] Initial Access
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on non-standard ports (e.g., 8080)
- Presence of mitmproxy certificates in client trust stores
- Python processes running mitmdump or mitmproxy
- Network logs showing intercepted/modified HTTP flows

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/mitmproxy]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://docs.mitmproxy.org/stable/
- GitHub repository: https://github.com/mitmproxy/mitmproxy

## Related Commands

- [[commands/mitmdump-start-basic-listener]]
- [[commands/mitmdump-run-with-script]]
- [[commands/mitmdump-dump-to-file]]
