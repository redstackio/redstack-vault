---
id: 94ab0e4c-7341-435b-9e3f-f699e45274c5
type: tool
verified: true
created_at: '2019-08-28T21:17:34.185790+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - osint
  - credential-access
  - breach-check
url: 'https://github.com/thewhiteh4t/pwnedOrNot'
commands:
  - '[[commands/pwnedOrNot-check-single-email]]'
  - '[[commands/pwnedOrNot-check-multiple-emails]]'
validated: true
---

# pwnedOrNot

**Status**: Unverified

## Overview

pwnedOrNot is a Python-based OSINT tool for checking if email addresses have been compromised in data breaches via the Have I Been Pwned (HIBP) service. If a breach is detected, it can search for associated passwords using services like Dehashed, aiding in credential reconnaissance during security assessments.

## Description

This tool automates breach checks and password discovery, making it useful for red teamers, penetration testers, and security researchers to identify weak or reused credentials. It supports single email checks or batch processing from files and requires API keys for full functionality. Common use cases include pre-engagement reconnaissance and validating credential hygiene.

## Features

- Feature 1: Breach detection using HIBP API
- Feature 2: Password searching via Dehashed integration
- Feature 3: Support for single or multiple email inputs
- Feature 4: Color-coded output for quick analysis

## Installation

### Requirements

- Python 3.6+
- requests library
- API keys for HIBP and Dehashed (optional for basic checks)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/thewhiteh4t/pwnedOrNot.git
cd pwnedOrNot

# Install dependencies
pip3 install -r requirements.txt

# Set API keys (optional)
export HIBP_API_KEY=your_hibp_key
export DEHASHED_API_KEY=your_dehashed_key
```

## Basic Usage

```python
python pwnedOrNot.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -e, --email | Check a single email |
| -f, --file | Check emails from a file |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```python
python pwnedOrNot.py -e victim@example.com
```

### Example 2: Advanced Usage

```python
python pwnedOrNot.py -f emails_list.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery
- [[System Information Discovery]] System Information Discovery (for credential context)

### Tactics

- [[Credential Access]] Credential Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: API requests to HIBP endpoints (api.pwnedpasswords.com, haveibeenpwned.com)
- Detection method 2: Network traffic to Dehashed API
- Detection method 3: Python process spawning with 'pwnedOrNot.py' in arguments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Have-I-Been-Pwned]]
- [[tools/Dehashed]]

## References

- Official GitHub: https://github.com/thewhiteh4t/pwnedOrNot
- HIBP Documentation: https://haveibeenpwned.com/API/v3
