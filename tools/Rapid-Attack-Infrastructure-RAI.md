---
id: 4c8a842f-f475-4f54-9cdd-f3490234bae8
type: tool
verified: true
created_at: '2019-08-28T21:17:33.810754+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - red-team
  - infrastructure
  - c2
  - phishing
url: 'https://github.com/rapid-attack-infra/rai'
validated: true
---

# Rapid-Attack-Infrastructure-RAI

**Status**: Unverified

## Overview

Rapid Attack Infrastructure (RAI) is a framework designed to streamline the setup of red team operational infrastructure. It automates the deployment of team servers, domain registrations, redirectors, and phishing servers, reducing the time and complexity involved in preparing for engagements.

## Description

In red team operations, establishing secure and obfuscated infrastructure is crucial but often time-consuming. RAI addresses this by providing scripts and tools to quickly provision components like C2 servers (e.g., Covenant or Empire integration), DNS configurations for domains, traffic redirectors to mask C2 communications, and phishing campaign servers. It supports integration with cloud providers and VPS setups, ensuring operational security through features like domain fronting and certificate management.

## Features

- Feature 1: Automated domain registration and DNS configuration for multiple providers (Cloudflare, Route53).
- Feature 2: One-click deployment of redirectors using Apache, Nginx, or custom proxies.
- Feature 3: Integration with C2 frameworks for team server setup.
- Feature 4: Phishing server templates with SSL support and payload hosting.
- Feature 5: Monitoring and logging for infrastructure health.

## Installation

### Requirements

- Linux OS (Ubuntu 20.04+ or Kali)
- Git, Python 3, and Docker
- API keys for DNS providers

### Install Commands

```bash
# Clone and install RAI
git clone https://github.com/rapid-attack-infra/rai.git
cd rai
./install.sh
```

For Docker-based install:

```bash
docker pull rai/infra:latest
docker run -v $(pwd)/config:/config rai/infra setup
```

## Basic Usage

```bash
rai --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Enable verbose logging |
| `--config FILE` | Specify config file |

## Examples

### Example 1: Basic Usage

Install and setup a basic domain:

```bash
rai install
rai domain register example.com --provider cloudflare --ip 192.168.1.100
```

### Example 2: Advanced Usage

Deploy full infrastructure:

```bash
rai setup --c2 covenant --domain evil.com --redirector nginx --phish-template evilginx
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Data Encoding for Command and Control
- [[Connection Proxy]] Proxy
- [[Phishing]] Phishing

### Tactics

- [[Command and Control]] Command and Control
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual domain registrations from red team IP ranges.
- Detection method 2: Traffic patterns to newly provisioned redirectors.
- Detection method 3: Docker containers or scripts matching RAI signatures in logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Covenant]]
- [[Evilginx]]
- [[Nginx]]

## References

- Official GitHub: https://github.com/rapid-attack-infra/rai
- Documentation: https://rai.readthedocs.io
- Related: Red Team Infrastructure Playbooks
