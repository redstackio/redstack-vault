---
id: 564b5cb4-1565-48a8-a47f-068925bc94e5
type: tool
verified: true
created_at: '2019-08-28T21:17:38.595478+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - evasion
  - sandbox-detection
  - htaccess
  - payload-delivery
url: 'https://github.com/RedSiege/mkhtaccess_red'
commands:
  - '[[commands/mkhtaccess-red-generate-basic]]'
  - '[[commands/mkhtaccess-red-generate-custom]]'
  - '[[commands/mkhtaccess-red-update-sandboxes]]'
validated: true
---

# mkhtaccess-red

**Status**: Unverified

## Overview

mkhtaccess_red is a specialized tool for generating Apache .htaccess configuration files to evade automated sandbox analysis during payload delivery. It automatically incorporates IP ranges and networks associated with known security research firms, malware analysis sandboxes, and AV vendors, redirecting their traffic to benign decoy content while serving malicious payloads to legitimate users. Commonly used in phishing campaigns, drive-by downloads, or web exploitation to avoid detection.

## Description

The tool parses a database of sandbox-related IP blocks (e.g., from VirusTotal, Joe Sandbox, Hybrid Analysis) and creates mod_rewrite rules in .htaccess format. This allows attackers to serve different content based on the client's IP: benign pages (e.g., a fake login form) to sandboxes, and actual exploits or downloads to real targets. It supports customization for specific campaigns and updates its sandbox intelligence periodically. Ideal for red team operations simulating advanced evasion tactics in web-based initial access vectors.

## Features

- Feature 1: Automatic generation of .htaccess rewrite rules from a curated list of 300+ sandbox IP networks.
- Feature 2: Customizable benign and malicious payload paths for targeted evasion.
- Feature 3: Option to update sandbox lists from external sources for freshness.
- Feature 4: Support for CIDR notation and regex-based IP matching in rules.
- Feature 5: Lightweight Python-based implementation, easy to integrate into deployment scripts.

## Installation

### Requirements

- Python 3.6+
- Apache mod_rewrite enabled on target server (for deployment)
- pip install requests (for updating sandbox lists)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/RedSiege/mkhtaccess_red.git
cd mkhtaccess_red
pip3 install -r requirements.txt

# Or via pip if available as package
pip3 install mkhtaccess-red
```

For Kali Linux: Pre-requisites like git and python3 are usually available; run the clone commands above.

## Basic Usage

```bash
python3 mkhtaccess_red.py --help
```

This displays available options, including generation and update flags. Always update sandboxes before generating files for the latest evasion coverage.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show detailed help message and usage |
| `-v, --verbose` | Enable verbose output for debugging generation |
| `--version` | Display tool version |
| `--update-sandboxes` | Fetch and update the sandbox IP database |

## Examples

### Example 1: Basic Usage

Generate a default .htaccess file:

```bash
python3 mkhtaccess_red.py --output evasion.htaccess
```

Deploys to a web server root to redirect sandbox traffic.

### Example 2: Advanced Usage

Custom generation with updated lists:

```bash
python3 mkhtaccess_red.py --update-sandboxes
python3 mkhtaccess_red.py --output campaign.htaccess --benign-payload /decoy.html --malicious-payload /malware.exe
```

Creates rules for a phishing campaign serving decoy to sandboxes and malware to victims.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (evasion during delivery)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (hiding payloads from analysis)
- [[Virtualization-Sandbox Evasion]] Virtualization/Sandbox Evasion (IP-based detection and redirection)

### Tactics

- [[Initial Access]] Initial Access (facilitating phishing/drive-by)
- [[Defense Evasion]] Defense Evasion (sandbox avoidance)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of suspicious .htaccess files with IP-based rewrites targeting known sandbox ranges (e.g., via log analysis or file integrity monitoring).
- Detection method 2: Anomalous redirects in web server logs from legitimate IPs but benign responses to sandbox probes.
- Detection method 3: Network traffic patterns showing differential content serving based on source IP.
- Detection method 4: Python processes or git clones related to 'mkhtaccess_red' in attacker infrastructure.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Apache-Mod-Rewrite]] (for deploying generated rules)
- [[tools/Impacket-Suite]] (for related evasion in network attacks)

## References

- Official GitHub: https://github.com/RedSiege/mkhtaccess_red
- Apache .htaccess documentation: https://httpd.apache.org/docs/2.4/howto/htaccess.html
- Sandbox IP lists: Public sources like abuseipdb or custom threat intel feeds
