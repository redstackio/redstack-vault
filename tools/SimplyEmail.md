---
id: 6130af51-14b0-476d-bdd1-b56d21d493e8
type: tool
verified: true
created_at: '2019-08-28T21:17:25.876515+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - osint
  - email-recon
  - reconnaissance
url: 'https://github.com/securitygeneration/SimplyEmail'
validated: true
---

# SimplyEmail

**Status**: Unverified

## Overview

SimplyEmail is an open-source email reconnaissance framework designed for fast and efficient OSINT gathering of email addresses associated with target domains. It automates searches across multiple sources like search engines (Bing, Google), PGP key servers, and more, making it ideal for initial reconnaissance phases in penetration testing and threat intelligence.

## Description

SimplyEmail provides a modular framework for email harvesting, allowing users to run individual modules or all at once. It supports output to various formats and can deduplicate results. Commonly used in red teaming for identifying potential phishing targets or valid email addresses for social engineering attacks.

## Features

- Feature 1: Modular design with support for Bing, Google, PGP, and custom modules
- Feature 2: Automated deduplication and sorting of email results
- Feature 3: Configurable timeouts and output directories for large-scale recon
- Feature 4: Integration with other OSINT tools via file outputs

## Installation

### Requirements

- Python 3.6+
- pip and git
- Internet access for API/search queries

### Install Commands

```bash
# Clone the repository
git clone https://github.com/securitygeneration/SimplyEmail.git
cd SimplyEmail

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (often pre-configured)
# SimplyEmail is available via apt or manual install as above
```

## Basic Usage

```python
python simplyemail.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -m, --module | Specify module(s) to run (e.g., bing, all) |
| -t, --target | Target domain for reconnaissance |
| -o, --output | Output directory for results |
| --timeout | Set query timeout in seconds |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Run Bing module on a target domain:

```python
python simplyemail.py -m bing -t example.com -o results/
```

### Example 2: Advanced Usage

Run all modules with custom timeout:

```python
python simplyemail.py -m all -t example.com -o results/ --timeout 120
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing for Information]] Phishing for Information
- [[Email Addresses]] Gather Victim Identity Information: Email Addresses

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of search engine queries from a single IP (Bing/Google APIs)
- Detection method 2: Network traffic to PGP key servers (keys.openpgp.org)
- Detection method 3: Log analysis for Python processes named simplyemail.py

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/theHarvester]]
- [[tools/MailSniper]]

## References

- Official GitHub: https://github.com/securitygeneration/SimplyEmail
- Documentation: Included in repo README

## Related Commands

- [[commands/simplyemail-run-bing-module]]
- [[commands/simplyemail-run-all-modules]]
- [[commands/simplyemail-run-pgp-module]]
