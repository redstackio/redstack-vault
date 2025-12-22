---
id: tool-001
url: >-
  https://github.com/mozilla/fxa/blob/fd716ec3f3461d22b847f337f6b1e899d671ee0d/packages/fxa-auth-client/lib/crypto.ts#L18
tags:
  - script
  - hashing
type: tool
verified: false
platforms:
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.076Z'
validated: true
submitted: true
---
# calculate-authpw-ts

**Status**: Unverified

## Overview

A TypeScript script derived from Mozilla's fxa-auth-client to compute authPW using PBKDF2, useful for exploiting password-derived authentication in Firefox Accounts.

## Description

This custom script implements the client-side authPW generation logic exposed in public source code, allowing attackers to derive hashes from leaked passwords for API abuse like account deletion.

## Features

- Feature 1: PBKDF2 hashing with email salt and 1000 iterations
- Feature 2: Base64 encoding of 32-byte output
- Feature 3: Email normalization for consistent derivation

## Installation

### Requirements

- Node.js or TypeScript runtime
- crypto module (built-in)

### Install Commands

```bash
# Clone or create script from GitHub source
git clone https://github.com/mozilla/fxa.git
# Or download calculate_authpw.ts attachment
```

## Basic Usage

```bash
node calculate_authpw.js --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--email` | Input email |
| `--password` | Input password |
| `-h, --help` | Show usage |

## Examples

### Example 1: Basic Usage

```bash
node calculate_authpw.js --email victim@example.com --password pass123
```

### Example 2: Advanced Usage

```bash
node calculate_authpw.js --email victim@example.com --password 'pass' --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to fxa-auth-client GitHub
- Execution of TypeScript/Node scripts with credential-like inputs
- Anomalous PBKDF2 computations in logs

## Related Procedures

- [[procedures/Compute-AuthPW-from-Password]]

## Related Tools

- [[tools/playcode-io-typescript]]

## References

- https://github.com/mozilla/fxa
- HackerOne Report #2197244
