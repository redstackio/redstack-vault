---
id: 08d5f6b6-293f-43fb-bc85-802119f8d36d
type: tool
verified: true
created_at: '2019-08-28T21:17:23.702148+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - mitm
  - ssl-stripping
  - credential-access
  - network-attack
url: 'https://github.com/moxie0/sslstrip'
commands:
  - '[[commands/sslstrip-listen-port]]'
  - '[[commands/sslstrip-favicon-mode]]'
validated: true
---

# sslstrip

**Status**: Unverified

## Overview

sslstrip is a MITM attack tool that transparently strips HTTPS protection from HTTP traffic on a network. It intercepts HTTPS links and redirects, rewriting them as HTTP equivalents to capture sensitive data like credentials in plaintext. Commonly used in wireless network attacks or ARP spoofing scenarios for credential harvesting.

## Description

Developed by Moxie Marlinspike, sslstrip performs an adversary-in-the-middle attack by forcing browsers to connect over HTTP instead of HTTPS. It watches for HTTPS redirects and upgrades, mapping them to HTTP while optionally supplying a fake lock favicon to mimic secure connections. Supports selective logging of POST data and session denial to prevent upgrades back to HTTPS. Ideal for capturing login credentials, session cookies, or other form data in unencrypted form during network interception.

## Features

- Transparent HTTP traffic hijacking
- HTTPS link rewriting to HTTP
- Fake favicon injection for visual deception
- Selective logging of sensitive data (e.g., POST requests)
- Session killing to block HTTPS upgrades
- Support for homograph attacks on HTTPS links

## Installation

### Requirements

- Python 2.7 (legacy tool, may require compatibility mode on modern systems)
- Twisted library for networking
- iptables for traffic redirection

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install sslstrip

# Manual install from source
sudo apt install python2.7 python2.7-dev libevent-dev python-twisted-web
wget https://raw.githubusercontent.com/moxie0/sslstrip/master/sslstrip.py
chmod +x sslstrip.py
```

Note: On modern systems, use Python 2 virtualenv or compatibility wrappers due to Python 3 incompatibility.

## Basic Usage

```bash
sslstrip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l, --listen <port>` | Listen port for incoming connections (default: 8080) |
| `-f, --favicon` | Inject fake lock favicon to mimic HTTPS |
| `-k, --kill` | Kill sessions that attempt HTTPS upgrades |
| `-l, --log <file>` | Log captured data to file |
| `-w, --write <file>` | Write all traffic to file for analysis |

## Examples

### Example 1: Basic Usage

Start sslstrip listening on port 8080 for traffic redirection.

```bash
sslstrip -l 8080
```

Redirect traffic using iptables: `sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080`

### Example 2: Advanced Usage

Run with favicon injection and logging.

```bash
sslstrip -l 8080 -f -w captured_traffic.log
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] [[Adversary-in-the-Middle]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay (for ARP spoofing setup)
- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Password Filter DLL]] Modify Authentication Process: Password Filter DLL (credential capture)

### Tactics

- [[Initial Access]] Initial Access (via network access)
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP redirects from HTTPS sites in proxy logs
- Presence of fake lock favicons in traffic
- Anomalous plaintext credentials in network captures
- iptables rules redirecting port 80 to non-standard ports (e.g., 8080)
- Python processes running sslstrip.py with network listening
- Increased HTTP traffic on networks expecting HTTPS

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[ettercap]] (full MITM suite)
- [[tools/bettercap]] (modern MITM framework)
- [[tools/Wireshark]] (traffic analysis)

## References

- Official GitHub: https://github.com/moxie0/sslstrip
- Blog post by Moxie: https://www.thoughtcrime.org/software/sslstrip/
- OWASP: https://owasp.org/www-community/attacks/SSLStrip
