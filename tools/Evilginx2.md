---
url: 'https://github.com/kgretzky/evilginx2'
tags:
  - mitm
  - phishing
  - 2fa-bypass
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:47.920Z'
id: 92c0932a-1353-4381-b024-1a77c838573e
validated: true
submitted: true
---
# Evilginx2

**Status**: Unverified

## Overview

Evilginx2 is an open-source man-in-the-middle attack framework for phishing login credentials and session cookies, specifically designed to bypass 2FA by capturing post-auth tokens.

## Description

It acts as a reverse proxy to intercept traffic between victim and target site (e.g., HackerOne), phish credentials, relay 2FA, and steal resulting session cookies. Used in offensive security for real-time session hijacking without alerting the user.

## Features

- Feature 1: Automatic cookie and token capture during login flows
- Feature 2: Support for custom phishing sites and subdomains
- Feature 3: Real-time session replay and persistence

## Installation

### Requirements

- Go 1.13+ installed
- Linux/macOS environment
- Domain for phishing (with DNS control)

### Install Commands

```bash
# Clone and build
go get github.com/kgretzky/evilginx2
go build
# Or from source
mkdir evilginx2 && cd evilginx2
go mod init evilginx2
make
```

## Basic Usage

```bash
./evilginx --help
```

Configure phishlets for targets like HackerOne.

### Common Options

| Option | Description |
|--------|-------------|
| -p | Path to config file |
| -v | Verbose logging |
| --phishlet | Load specific phishlet |

## Examples

### Example 1: Basic Usage

```bash
./evilginx -p ./phishlets/hackerone.yaml
# Set up lures and monitor captures
```

### Example 2: Advanced Usage

```bash
./evilginx --phishlet hackerone --lure https://fake-hackerone.com/login
# Relay traffic and capture cookies
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious proxy traffic or DNS queries to attacker domains
- Mismatched TLS certificates in login flows
- Anomalous session cookie origins in logs

## Related Procedures


## Related Tools

- [[tools/Browser-Cookie-Editor]]

## References

- GitHub repository: https://github.com/kgretzky/evilginx2
- Documentation on phishlet configuration
