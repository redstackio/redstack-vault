---
id: tool-pre-auth-nosqli
url: null
tags:
  - exploit
  - custom
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.828Z'
validated: true
submitted: true
---
# pre-auth-nosqli-py

**Status**: Unverified

## Overview

A custom Python exploit script implementing the full chain: NoSQL injection for token leak, password reset, account takeover, webhook creation, and interactive shell via RCE in Rocket.Chat.

## Description

The script uses requests to interact with API endpoints, automates blind regex guessing, handles auth post-takeover, and sets up webhook for command execution. Requires target URL and email as args.

## Features

- Feature 1: Automated blind token reconstruction
- Feature 2: End-to-end attack automation
- Feature 3: Interactive shell post-RCE

## Installation

### Requirements

- Python3 and requests

### Install Commands

```bash
# Assume script is available; no install needed
python3 pre_auth_nosqli.py --help
```

## Basic Usage

```bash
python3 pre_auth_nosqli.py http://target:3000 user@email.com
```

### Common Options

| Option | Description |
|--------|-------------|
| URL | Target instance | Required |
| Email | Target user | Required |

## Examples

### Example 1: Basic Usage

```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@local'
```

### Example 2: Advanced Usage

```bash
python3 pre_auth_nosqli.py --verbose 'http://target' 'user'
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

- Script name in process lists
- Pattern of API calls from single IP
- Token leak attempts in logs

## Related Procedures

- [[procedures/Leak-Password-Reset-Token-via-Blind-NoSQL-Injection]]

## Related Tools

- [[tools/Python3]]
- [[tools/requests]]

## References

- Custom tool based on HackerOne report #1130721
