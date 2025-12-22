---
url: null
tags:
  - exploit-script
type: tool
verified: false
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.715Z'
id: 9b3ddf54-0fb7-40f7-9d27-679ea94dd29f
validated: true
submitted: true
---
# post_auth_nosqli.py

**Status**: Unverified

## Overview

Custom exploit script implementing blind NoSQL injection, account takeover, and RCE via webhook in Rocket.Chat.

## Description

The script automates the full chain: auth, injection with functions like users_nosqli_blind_leak, reset, webhook creation, and shell.

## Features

- Feature 1: Blind char-by-char extraction
- Feature 2: API session handling
- Feature 3: Webhook RCE payloads

## Installation

### Requirements

- Python3, requests, bcrypt

### Install Commands

Download or create the script; no formal install.

## Basic Usage

```bash
python3 post_auth_nosqli.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | Username |
| -p | Password |
| target | URL |

## Examples

### Example 1: Basic Usage

```bash
python3 post_auth_nosqli.py -u user -p pass 'http://target'
```

### Example 2: Advanced Usage

```bash
python3 post_auth_nosqli.py -u user -p pass 'http://target' --leak-only
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

- Script name in process lists or logs

## Related Procedures

- [[procedures/Execute-Commands-via-Webhook-for-RCE]]

## Related Tools

- [[tools/Python3]]

## References

- Custom tool from HackerOne report
