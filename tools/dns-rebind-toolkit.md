---
url: 'https://github.com/malware-dev/dns-rebind-toolkit'
tags:
  - dns
  - rebinding
  - ssrf
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.621Z'
id: f8cdb855-8fa4-4c82-af13-16237be57461
validated: true
submitted: true
---
# dns-rebind-toolkit

**Status**: Unverified

## Overview

dns-rebind-toolkit is an open-source Python-based tool for setting up DNS rebinding attacks, commonly used in security testing to bypass network restrictions like DNS pinning in applications such as Nextcloud.

## Description

The toolkit provides a simple DNS server implementation that allows dynamic IP resolution changes, enabling attackers to trick server-side applications into making requests to internal resources. It's particularly useful for SSRF exploitation in web applications by simulating rapid DNS TTL changes.

## Features

- Feature 1: Customizable rebinding intervals and TTL
- Feature 2: Support for multiple target IPs and ports
- Feature 3: Logging of DNS queries and HTTP requests

## Installation

### Requirements

- Python 3.x
- No additional dependencies beyond standard library

### Install Commands

```bash
# Clone and run
 git clone https://github.com/malware-dev/dns-rebind-toolkit.git
 cd dns-rebind-toolkit
 python setup.py install
```

## Basic Usage

```bash
python dns_rebind_server.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output for queries |

## Examples

### Example 1: Basic Usage

```bash
python dns_rebind_server.py --domain example.com --target-ip 127.0.0.1
```

### Example 2: Advanced Usage

```bash
python dns_rebind_server.py --domain example.com --bind-ip 1.2.3.4 --target-ip 169.254.169.254 --interval 1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual DNS server traffic on non-standard ports
- Rapid TTL changes in DNS responses from external domains
- Anomalous outbound HTTP requests from web servers

## Related Procedures

- [[procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]

## Related Tools

- [[Related Tool 1|tools/Burp-Suite]]
- [[Related Tool 2|tools/Wireshark]]

## References

- Official documentation: https://github.com/malware-dev/dns-rebind-toolkit
- Related resources: HackerOne Report #2115212
