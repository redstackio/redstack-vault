---
url: 'https://ngrok.com'
tags:
  - tunneling
  - exfiltration
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.998Z'
id: f0266619-9200-43b2-be8b-95af97a59d37
validated: true
submitted: true
---
# ngrok

**Status**: Unverified

## Overview

Ngrok is a tunneling tool that exposes local servers to the internet via secure tunnels, commonly used in security testing for receiving callbacks from XSS exfiltration or webhook testing.

## Description

Ngrok creates a public URL (e.g., 8a7b2695.ngrok.io) forwarding to a local port, ideal for capturing data sent from exploited applications like review URLs in XSS attacks. It supports HTTP/HTTPS and TCP tunnels with authentication options.

## Features

- Feature 1: Secure public endpoints for local services
- Feature 2: Request inspection and replay
- Feature 3: Custom subdomains and auth

## Installation

### Requirements

- Go 1.11+ or pre-built binaries

### Install Commands

```bash
# Download binary
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

tar xvzf ngrok-v3-stable-linux-amd64.tgz

sudo mv ngrok /usr/local/bin
```

## Basic Usage

```bash
ngrok http 80
```

### Common Options

| Option | Description |
|--------|-------------|
| -config | Path to config file |
| --log | Log level |

## Examples

### Example 1: Basic Usage

```bash
ngrok http 8080
```

### Example 2: Advanced Usage

```bash
ngrok http --subdomain=mytunnel 3000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound connections to ngrok.io domains
- Unusual HTTP traffic patterns to dynamic subdomains

## Related Procedures


## Related Tools

- [[tools/localtunnel]]
- [[tools/serveo]]

## References

- Official documentation: https://ngrok.com/docs
