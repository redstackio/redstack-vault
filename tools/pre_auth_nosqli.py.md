---
url: null
tags:
  - exploit-script
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.504Z'
id: 81e53e5d-57a1-4d90-99ad-0dd23f9a79d6
validated: true
submitted: true
---
# pre_auth_nosqli.py

**Status**: Unverified

## Overview

Custom Python exploit script for the Rocket.Chat NoSQL injection vulnerability, handling the full attack chain to RCE.

## Description

Implements password reset request, blind injection for token leak using $regex, password reset, admin login, webhook creation with script payload, and reverse shell setup.

## Features

- Feature 1: Automated token guessing
- Feature 2: API session management
- Feature 3: Payload execution for RCE

## Installation

### Requirements

- Python3, requests

### Install Commands

```bash
# Download or create script
wget exploit.py -O pre_auth_nosqli.py
```

## Basic Usage

```bash
python3 pre_auth_nosqli.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --leak-token | Perform injection |
| --reset-password | Use token to reset |
| --create-webhook | Setup RCE |

## Examples

### Example 1: Basic Usage

```bash
python3 pre_auth_nosqli.py 'http://target:3000' 'admin@email.com'
```

### Example 2: Advanced Usage

```bash
python3 pre_auth_nosqli.py 'http://target:3000' 'admin@email.com' --leak-only
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious API calls from Python UA
- Regex in request bodies

## Related Procedures

## Related Tools

- [[tools/Python3]]
- [[tools/requests]]

## References

- HackerOne Report: https://hackerone.com/reports/1130721
