---
url: ''
tags:
  - ssl-test
  - debug
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.028Z'
id: af223ee3-4b90-4fbc-b200-b0dbf0411046
validated: true
submitted: true
---
# openssl-s-client

**Status**: Unverified

## Overview

OpenSSL command for establishing SSL/TLS client connections to test handshakes, certificates, and ciphers in security testing.

## Description

Used to verify anonymous ciphers on SMTP ports by restricting to aNULL, simulating MITM without auth on targets like apps.owncloud.com.

## Features

- Feature 1: Custom cipher specification
- Feature 2: Certificate inspection
- Feature 3: STARTTLS support

## Installation

### Requirements

- OpenSSL package

### Install Commands

```bash
# On Ubuntu
apt install openssl
# On macOS
brew install openssl
```

## Basic Usage

```bash
openssl s_client --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -connect | Host:port |
| -cipher | Cipher list |

## Examples

### Example 1: Basic Usage

```bash
openssl s_client -connect target:443
```

### Example 2: Advanced Usage

```bash
openssl s_client -connect target:465 -cipher aNULL
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Logs of incomplete handshakes or cipher mismatches
- Specific error patterns in SSL logs

## Related Procedures

- [[procedures/Test-Anonymous-Cipher-Handshake-with-OpenSSL]]

## Related Tools

- [[tools/testssl-sh]]
- [[tools/sslyze]]

## References

- OpenSSL docs: https://www.openssl.org/docs/man1.1.1/man1/s_client.html
