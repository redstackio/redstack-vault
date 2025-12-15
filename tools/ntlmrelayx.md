---
id: tool-ntlmrelayx
url: 'https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py'
tags:
  - ntlm-relay
  - rce
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.358Z'
validated: true
submitted: true
---
# ntlmrelayx

**Status**: Unverified

## Overview

ntlmrelayx is an Impacket tool for relaying NTLM authentication from captured challenges to other services, enabling lateral movement and RCE without cracking hashes.

## Description

Part of the Impacket suite, it listens for auth attempts (e.g., from Responder) and forwards them to targets like SMB shares, HTTP, or LDAP. In this context, relays NetNTLM from Burp's SMB trigger to internal vulnerable services for RCE in the pentester's context.

## Features

- Feature 1: Relays to SMB, HTTP, MSSQL, LDAP
- Feature 2: Executes commands via relayed SMBExec
- Feature 3: Supports SMB2/3 and signing bypass

## Installation

### Requirements

- Python 3.x
- Impacket library

### Install Commands

```bash
# Install Impacket
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip install .
```

## Basic Usage

```bash
python examples/ntlmrelayx.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | Target host for relay |
| -tf | Target file with hosts |
| -smb2support | Enable SMB2 |

## Examples

### Example 1: Basic Usage

```bash
python ntlmrelayx.py -t smb://internal-host
```

### Example 2: Advanced Usage

```bash
python ntlmrelayx.py -tf targets.txt -smb2support -i
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and Relay
- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual auth relays in event logs (4624/4768)
- Impacket processes or Python scripts
- Failed logons from relay IPs

## Related Procedures


## Related Tools

- [[tools/Responder]]
- [[tools/CrackMapExec]]

## References

- Official documentation: https://github.com/SecureAuthCorp/impacket
- Related resources: NTLM relay attacks guide
