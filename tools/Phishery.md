---
type: tool
verified: true
description: >-
  A simple SSL-enabled HTTP server designed for phishing credentials via Basic
  Authentication in security testing scenarios.
url: 'https://github.com/ryleyangus/phishery'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - phishing
  - credential-access
  - http-server
  - ssl
validated: true
---

# Phishery

**Status**: Unverified

## Overview

Phishery is a lightweight, Go-based HTTP server that supports SSL/TLS and is primarily used for hosting phishing pages to capture credentials through Basic Authentication. It is commonly employed in red team exercises and penetration testing to simulate phishing attacks by serving fake login interfaces.

## Description

Phishery allows security professionals to quickly set up a server that mimics legitimate login portals, prompting users for credentials via HTTP Basic Auth. Captured credentials are logged for analysis. The tool supports custom templates for realistic phishing scenarios and can operate over HTTPS to avoid interception warnings. It is not intended for malicious use but for authorized testing environments.

## Features

- Feature 1: Basic Authentication credential capture with real-time logging
- Feature 2: SSL/TLS support for secure (HTTPS) phishing simulations
- Feature 3: Customizable HTML templates for target-specific phishing pages
- Feature 4: Simple command-line interface for easy deployment
- Feature 5: Cross-platform compatibility via Go runtime

## Installation

### Requirements

- Go 1.13 or later installed
- Access to GitHub for downloading the source

### Install Commands

```bash
# Install via Go
GO111MODULE=on go install github.com/ryleyangus/phishery/cmd/phishery@latest

# Or clone and build manually
git clone https://github.com/ryleyangus/phishery.git
cd phishery/cmd/phishery
go build
```

For Kali Linux or Ubuntu, ensure Go is installed via `sudo apt install golang-go`.

## Basic Usage

```bash
phishery --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --version | Display version information |
| -p | Specify listening port |
| -a | Bind address |
| -s | Enable SSL |
| -t | Custom template directory |

## Examples

### Example 1: Basic Usage

```bash
phishery -p 8080
```

This starts a basic HTTP server on port 8080, serving a default phishing page.

### Example 2: Advanced Usage

```bash
phishery -p 443 -s -c cert.pem -k key.pem -t ./custom-templates
```

Starts an HTTPS server with custom templates.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[T1566.002]] Phishing: Spearphishing Link
- [[Reversible Encryption]] Modify Authentication Process: Multi-Factor Authentication

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network monitoring for unusual HTTP/HTTPS servers on non-standard ports with Basic Auth prompts
- Detection method 2: Log analysis for credential capture patterns or Go binary executions (phishery)
- Detection method 3: SSL certificate anomalies or self-signed certs in phishing contexts

## Related Commands

- [[commands/phishery-start-basic-server]]
- [[commands/phishery-ssl-phishing-server]]
- [[commands/phishery-custom-template-server]]

## References

- Official GitHub Repository: https://github.com/ryleyangus/phishery
- Go Documentation for building: https://golang.org/doc/
