---
url: null
tags:
  - custom-script
  - ssrf
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.142Z'
id: 131c4fcb-2e12-48c9-86b0-59a13d8aad94
validated: true
submitted: true
---
# Custom-B64search-Script

**Status**: Unverified

## Overview

A custom bash script (b64search.sh) for performing SSRF-based directory brute forcing by manipulating base64-encoded cookies.

## Description

The script encodes paths into base64 tokens, sends SSRF requests via curl, and checks responses for valid paths.

## Features

- Feature 1: Base64 token modification
- Feature 2: Multithreading support via xargs
- Feature 3: Response code checking

## Installation

### Requirements

- Bash and curl

### Install Commands

Create script: #!/bin/bash; curl with modified cookie $1
chmod +x b64search.sh

## Basic Usage

```bash
./b64search.sh /path
```

### Common Options

Script args for path.

## Examples

### Example 1: Basic Usage

As in command with xargs.

### Example 2: Advanced Usage

Customize for different endpoints.

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Lateral Movement]] Lateral Movement

## Detection

- Anomalous internal requests
- Base64 patterns in logs

## Related Procedures

- [[procedures/API-SSRF-Exploitation-for-Internal-Access]]

## Related Tools

- [[tools/Curl]]

## References

Custom, based on attack.
