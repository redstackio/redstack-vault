---
url: 'https://github.com/SpiderLabs/Responder'
tags:
  - ntlm-capture
  - relay-attack
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.742Z'
id: 72e0c97c-c752-4f99-806a-5bfa25d4bfc2
validated: true
submitted: true
---
# Responder

**Status**: Unverified

## Overview

Responder is a LLMNR, NBT-NS, MDNS, and DNS poisoner for capturing NTLM hashes in network attacks.

## Description

It poisons name resolution protocols to relay authentication attempts, capturing hashes for cracking. Used here via UNC paths to steal Windows logins from subdomain visitors.

## Features

- Feature 1: Multi-protocol poisoning (LLMNR/NBT-NS)
- Feature 2: Hash relay and capture
- Feature 3: WPAD rogue server

## Installation

### Requirements

- Python 3

### Install Commands

```bash
git clone https://github.com/SpiderLabs/Responder.git
cd Responder
pip install -r requirements.txt
```

## Basic Usage

```bash
python Responder.py -I eth0
```

### Common Options

| Option | Description |
|--------|-------------|
| `-I` | Interface |
| `-w` | Enable WPAD |

## Examples

### Example 1: Basic Usage

```bash
python Responder.py -I eth0
```

### Example 2: Advanced Usage

```bash
python Responder.py -I eth0 -r -d
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning

### Tactics

- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous SMB/HTTP traffic
- NTLM auth failures in logs

## Related Procedures

- [[procedures/Perform-Subdomain-Takeover-and-Host-Content]]

## Related Tools


## References

- GitHub: https://github.com/SpiderLabs/Responder
