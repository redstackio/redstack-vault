---
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reconnaissance
  - wordpress
  - fingerprinting
  - passive-recon
url: 'https://github.com/carloslado/plecost'
validated: true
---

# plecost

**Status**: Unverified

## Overview

Plecost is a WordPress fingerprinting tool designed for security testing and reconnaissance. It identifies installed plugins and their versions on WordPress sites, either by directly analyzing a single URL or by leveraging Google search results for passive discovery. It also highlights associated CVEs for vulnerable plugins, aiding in vulnerability assessment during penetration testing or red team operations.

## Description

Plecost automates the detection of WordPress plugins by parsing site content, headers, and common plugin footprints. In single-URL mode, it actively probes the target for plugin indicators. In Google mode, it uses search engine dorks to find indexed WordPress instances related to a domain, making it useful for broad reconnaissance without direct interaction. Results include plugin names, versions, and CVE references, helping prioritize exploitation targets. It's particularly valuable in web application testing phases for mapping the attack surface of WordPress deployments.

## Features

- Feature 1: Single URL fingerprinting with direct probing for plugin detection
- Feature 2: Google-based passive reconnaissance for domain-wide WordPress discovery
- Feature 3: CVE lookup and reporting for identified plugins
- Feature 4: JSON output support for integration with other tools
- Feature 5: Silent mode for stealthy operations

## Installation

### Requirements

- Python 2.7 or 3.x
- pip (for dependencies like requests, beautifulsoup4)
- Git (for cloning the repository)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/carloslado/plecost.git
cd plecost

# Install dependencies
pip install -r requirements.txt

# Or install directly via pip (if available)
pip install plecost
```

On Kali Linux, it may be available via apt: `apt install plecost`.

## Basic Usage

```python
python plecost.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -u URL | Fingerprint a single URL |
| -g DOMAIN | Use Google to find and fingerprint WordPress instances for a domain |
| -o FILE | Output results to a JSON file |
| --silent | Suppress console output for stealth |
| --update | Update the plugin database |

## Examples

### Example 1: Basic Usage

```python
python plecost.py -u http://example.com
```

### Example 2: Advanced Usage

```python
python plecost.py -g example.com -o results.json --silent
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Client Configurations]] Gather Victim Host Information: Software (identifies WordPress plugins and versions)
- [[Vulnerability Scanning]] Active Scanning: Vulnerability (probes for plugin details and CVEs)

### Tactics

- [[Reconnaissance]] Reconnaissance (gathers information on target web applications)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual requests to WordPress sites with patterns matching plugin enumeration (e.g., probing /wp-content/plugins/ paths)
- Detection method 2: Google API or search query spikes related to dorking for WordPress footprints (e.g., inurl:wp-content site:example.com)
- Detection method 3: Network logs showing Python requests library traffic to WordPress endpoints
- Detection method 4: Presence of plecost.py or its dependencies in process lists or file systems

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/WPScan]]
- [[tools/Nikto]]

## References

- Official GitHub: https://github.com/carloslado/plecost
- WordPress Security Documentation: https://wordpress.org/support/article/hardening-wordpress/
