---
id: 9d6cea28-205f-4d20-9deb-dae99bd70831
name: Modlishka
type: tool
verified: true
created_at: '2019-08-28T21:17:41.935991+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - phishing
  - reverse-proxy
  - credential-access
url: 'https://github.com/drk1wi/Modlishka'
validated: true
---

# Modlishka

**Status**: Unverified

## Overview

Modlishka is a flexible and powerful reverse proxy tool designed for advanced phishing campaigns, particularly in ethical red teaming and security training. It enables the creation of convincing phishing sites by proxying traffic to legitimate domains while intercepting credentials, session cookies, and multi-factor authentication (MFA) tokens in real-time.

## Description

Modlishka operates as a man-in-the-middle proxy that mirrors the behavior of target websites, allowing attackers to capture sensitive data without alerting victims. It supports HTTPS termination, custom domain mapping, and automated credential forwarding. Commonly used in simulated phishing exercises to test organizational defenses against sophisticated social engineering attacks. Key capabilities include bypassing common anti-phishing protections and handling complex authentication flows like OAuth and SAML.

## Features

- **Real-time Credential Capture**: Intercepts usernames, passwords, and 2FA codes during login attempts.
- **HTTPS Proxying**: Handles SSL/TLS termination to proxy secure sites seamlessly.
- **Domain Fronting**: Supports techniques to evade detection by using legitimate domains.
- **MFA Bypass**: Captures and relays one-time passwords or push notifications.
- **Customizable Hooks**: Configurable scripts for post-capture actions like forwarding credentials.
- **Logging and Reporting**: Detailed logs of interactions for analysis in training scenarios.

## Installation

### Requirements

- Go 1.13 or later
- Git
- OpenSSL for certificate generation (optional but recommended)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/drk1wi/Modlishka.git
cd Modlishka

# Build the binary
go build

# For Kali/Ubuntu, ensure Go is installed
sudo apt update && sudo apt install golang-go git
```

On macOS with Homebrew:

```bash
brew install go
git clone https://github.com/drk1wi/Modlishka.git
cd Modlishka
go build
```

## Basic Usage

```bash
./modlishka --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-config` | Path to configuration JSON file |
| `-listen` | Interface and port to listen on (e.g., :443) |
| `-cert` | Path to SSL certificate |
| `-key` | Path to private key |
| `-verbose` | Enable detailed logging |

## Examples

### Example 1: Basic Usage

Generate a config and run a simple proxy:

```bash
# Generate config
go run modlishka.go config -target https://example.com -listen 8080

# Run the proxy
./modlishka -config config.json
```

### Example 2: Advanced Usage

Run with HTTPS and custom domain:

```bash
./modlishka -config advanced-config.json -listen :443 -cert phishing.crt -key phishing.key
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Web Protocols]] Application Layer Protocol: Web Protocols

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outbound HTTPS connections from internal servers to phishing domains.
- Anomalous proxy traffic patterns or certificate mismatches in network logs.
- Presence of Go binaries or Modlishka processes in memory forensics.
- Captured logs showing credential forwarding to attacker-controlled endpoints.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Gophish]]
- [[tools/Setoolkit]]

## References

- Official GitHub: https://github.com/drk1wi/Modlishka
- Documentation: https://github.com/drk1wi/Modlishka/wiki
- Related Blog: https://blog.fox-it.com/2018/01/11/modlishka-a-go-based-phishing-toolkit/

## Related Commands

- [[commands/modlishka-generate-config]]
- [[commands/modlishka-run-phishing]]
