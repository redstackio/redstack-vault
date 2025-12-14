---
id: tool-hashpump
url: 'https://github.com/bwall/HashPump'
tags:
  - crypto
  - exploitation
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.125Z'
validated: true
submitted: true
---
# Hashpump

**Status**: Unverified

## Overview

Hashpump is a tool for performing length-extension attacks on cryptographic hashes like MD5 and SHA1, commonly used in exploiting authentication bypass vulnerabilities in web applications.

## Description

Hashpump exploits the Merkle-Damgård construction in hash functions by appending data to a message using only the hash and original length, without needing the secret key. It's particularly useful for forging signatures in APIs like WP API Key-Auth where MD5 is used insecurely. Features include support for multiple hashes, padding calculation, and output of extended messages/signatures. In offensive security, it's used to demonstrate crypto flaws and achieve auth bypass.

## Features

- Feature 1: Length-extension for MD5, SHA1, SHA256
- Feature 2: Automatic padding and block calculation
- Feature 3: Hex output for easy integration into requests

## Installation

### Requirements

- C++ compiler (g++)
- CMake

### Install Commands

```bash
# Clone and build
git clone https://github.com/bwall/HashPump.git
cd HashPump
mkdir build && cd build
cmake ..
make
```

## Basic Usage

```bash
./hashpump --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-s, --signature` | Input signature |
| `-k, --keylen` | Key length |
| `-p, --pad` | Padding string |
| `--digest` | Hash type |

## Examples

### Example 1: Basic Usage

```bash
./hashpump -s deadbeef -k 16 -p admin=1 --digest md5
```

### Example 2: Advanced Usage

```bash
./hashpump -s 5d41402abc4b2b76b9719d911017c592 -k 50 -p '}{"role":"admin"}' --digest md5 -l 64
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing unusual API requests with extended payloads
- Crypto anomaly detection in signature validation logs
- Presence of Hashpump binary or GitHub clones on attacker systems

## Related Procedures

- [[procedures/Forge-Signature-with-MD5-Length-Extension]]

## Related Tools

- [[John the Ripper]]
- [[Hashcat]]

## References

- Official GitHub: https://github.com/bwall/HashPump
- Length-Extension Attacks explanation: https://www.netsparker.com/blog/web-security/what-is-length-extension-attack/
