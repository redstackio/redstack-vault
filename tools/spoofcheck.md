---
id: 86a48516-25e6-4852-a28e-25a85c9ffae5
type: tool
verified: true
created_at: '2019-08-28T21:17:30.454897+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - email
  - spoofing
  - spf
  - dmarc
  - reconnaissance
url: 'https://github.com/example/spoofcheck'
validated: true
---

# spoofcheck

**Status**: Unverified

## Overview

spoofcheck is a command-line tool designed to assess email spoofing vulnerabilities for a given domain. It queries and analyzes SPF (Sender Policy Framework) and DMARC (Domain-based Message Authentication, Reporting, and Conformance) DNS records to identify weak configurations that could enable unauthorized email spoofing, such as missing or lax policies.

## Description

The tool performs automated DNS lookups to retrieve SPF and DMARC records, then evaluates them against best practices for preventing spoofing. It flags issues like soft fails (~all in SPF), absent DMARC policies, or monitoring-only setups (p=none). Commonly used in reconnaissance phases of penetration testing to identify phishing opportunities or misconfigurations in target organizations' email security.

## Features

- Feature 1: Automatic SPF record retrieval and parsing for authorization mechanisms.
- Feature 2: DMARC policy analysis, including rua/ruf reporting URIs and pct (percentage) settings.
- Feature 3: Recommendations for remediation, such as tightening policies to reject spoofed emails.

## Installation

### Requirements

- Go 1.16+ (if building from source)
- DNS resolution capabilities (standard on most systems)

### Install Commands

```bash
# Clone and build from source (assuming GitHub repo)
go install github.com/example/spoofcheck@latest

# Or download pre-built binary from releases
wget https://github.com/example/spoofcheck/releases/download/v1.0/spoofcheck-linux-amd64
chmod +x spoofcheck-linux-amd64
sudo mv spoofcheck-linux-amd64 /usr/local/bin/spoofcheck
```

On Kali Linux, it may not be pre-installed; use the build method above. For Ubuntu: Install Go first with `sudo apt install golang-go`, then follow the go install steps.

## Basic Usage

```bash
spoofcheck --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for detailed record parsing |
| `--spf` | Focus analysis on SPF records only |
| `--dmarc` | Focus analysis on DMARC records only |

## Examples

### Example 1: Basic Usage

```bash
spoofcheck example.com
```

### Example 2: Advanced Usage

```bash
spoofcheck -v --dmarc example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for email configurations)
- [[Email Addresses]] Gather Victim Identity Information: Email Addresses

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- DNS query logs showing lookups for TXT records on target domains (e.g., _dmarc.target.com)
- Network traffic to DNS resolvers with patterns for SPF/DMARC queries during recon phases

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dig]]
- [[tools/nslookup]]

## References

- Official GitHub: https://github.com/example/spoofcheck
- DMARC.org: https://dmarc.org/
- SPF Records: https://www.openspf.org/
