---
id: tool-reuse-signature-gatecoin
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/362/493/3a53d6b8bdd503df00223293b31c7b9d924fb158/reuse_signature_gatecoin.py
name: reuse_signature_gatecoin.py
tags:
  - exploit-script
  - api-replay
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.788Z'
description: Python script demonstrating Gatecoin API signature reuse exploit.
validated: true
submitted: true
---
# reuse_signature_gatecoin.py

**Status**: Unverified

## Overview

A Python script that automates the Gatecoin API signature reuse attack by generating a read-only key request with a future timestamp, waiting 299 seconds for cache expiration, and replaying with modified payload for full privileges. Used in offensive security testing for auth bypass demonstrations.

## Description

The script handles API authentication, timestamp calculation (3 seconds future), signature generation (excluding payload), sleep for cache expiry, payload modification (add trade/withdraw permissions), and replay. It requires Gatecoin API credentials and assumes client clock ahead. Outputs the escalated key details.

## Features

- Feature 1: Automatic future timestamp generation
- Feature 2: 299-second wait with cache testing
- Feature 3: Payload modification for privilege escalation
- Feature 4: Error handling for 401 responses (duplicate or timestamp)

## Installation

### Requirements

- Python 3.x
- requests library: `pip install requests`
- Valid Gatecoin API token

### Install Commands

```bash
# No installation needed; download script
wget 'https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/362/493/3a53d6b8bdd503df00223293b31c7b9d924fb158/reuse_signature_gatecoin.py'

# Install dependencies
pip install requests
```

## Basic Usage

```bash
python reuse_signature_gatecoin.py --token YOUR_API_TOKEN --wait 299
```

### Common Options

| Option | Description |
|--------|-------------|
| `--token` | Gatecoin API token |
| `--wait` | Seconds to wait for cache (default 299) |
| `-v, --verbose` | Verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
python reuse_signature_gatecoin.py --token abc123
```

Runs the full exploit: generates request, waits, modifies, replays.

### Example 2: Advanced Usage

```bash
python reuse_signature_gatecoin.py --token abc123 --wait 300 -v
```

Verbose mode with custom wait time.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual API key creations with mismatched permissions
- Patterns of delayed requests with same signatures
- Network logs showing repeated POST to /api/v1/keys
- Python process with requests to Gatecoin API

## Related Procedures

- [[procedures/Replay-Modified-API-Request-for-Privilege-Escalation]]
- [[procedures/Generate-Initial-API-Request-with-Future-Timestamp]]

## Related Tools

- [[Burp Suite]]
- [[Wireshark]]

## References

- HackerOne Report #425314
- Gatecoin API Documentation
