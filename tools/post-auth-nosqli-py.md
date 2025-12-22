---
url: null
tags:
  - exploit
  - nosql
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.397Z'
id: f1d4109f-646c-4a1f-b9b3-63aea6ecefff
validated: true
submitted: true
---
# post-auth-nosqli-py

**Status**: Unverified

## Overview

Custom Python exploit script for blind NoSQL injection in Rocket.Chat, handling authentication, oracle construction, data leakage, account takeover, and RCE via webhooks.

## Description

The script automates the attack chain, using requests for API interactions, bcrypt for any hashing, and implements functions like users_nosqli_blind_leak for character guessing.

## Features

- Feature 1: Auth and session management
- Feature 2: Blind injection oracles with $where
- Feature 3: Automated token/email/2FA leakage
- Feature 4: Webhook creation and interactive shell

## Installation

### Requirements

- Python 3
- requests, bcrypt libraries

### Install Commands

```bash
pip3 install requests bcrypt
```

## Basic Usage

```bash
python3 post_auth_nosqli.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --user | Username for auth |
| -p, --pass | Password |
| Target URL | Instance base URL |

## Examples

### Example 1: Basic Usage

```bash
python3 post_auth_nosqli.py -u attacker -p attacker http://target:3000
```

### Example 2: Advanced Usage

```bash
python3 post_auth_nosqli.py -u user -p pass http://target:3000 --leak-only
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

- Network logs showing repetitive API queries to users.list
- Anomalous webhook creations
- Child process spawns from Node.js

## Related Procedures

- [[procedures/Identify-Admin-Users-via-Blind-NoSQL-Injection]]

## Related Tools

- [[tools/requests]]

## References

- HackerOne Report #1130874
