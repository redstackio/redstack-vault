---
id: 5535be2e-95ed-4328-9c9f-55971a831645
type: tool
verified: true
created_at: '2019-08-28T21:17:32.392724+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - opsec
  - key-serving
  - c2-infrastructure
  - http
  - dns
url: 'https://github.com/example/keyserver'
commands:
  - '[[commands/keyserver-start-http-server]]'
  - '[[commands/keyserver-start-dns-server]]'
  - '[[commands/keyserver-add-key]]'
validated: true
---

# keyserver

**Status**: Unverified

## Overview

keyserver is a lightweight utility for serving encryption keys, configuration data, or other sensitive payloads over HTTP and DNS protocols. It is commonly used in offensive security operations to provide dynamic access to keys for implants or payloads, improving operational security by avoiding hardcoded secrets.

## Description

The tool supports both HTTP endpoints for direct key retrieval and DNS TXT records for stealthy, protocol-agnostic key delivery. This makes it suitable for red team scenarios where payloads need to fetch keys post-deployment without relying on static configurations. keyserver handles key storage in simple JSON or text files and can run as a standalone server.

## Features

- HTTP serving: Expose keys via REST-like endpoints (e.g., /keys/{name})
- DNS serving: Respond to TXT queries for domain-based key retrieval
- Key management: Add, list, and update keys via CLI
- Lightweight and cross-platform: Minimal dependencies, runs on major OSes
- OPSEC-focused: No logging by default, configurable bind addresses

## Installation

### Requirements

- Go 1.16+ (for building from source)
- Network privileges for DNS port 53 (if using DNS mode)

### Install Commands

```bash
# On Kali/Ubuntu (build from source)
go install github.com/example/keyserver@latest

# Or clone and build
mkdir -p $GOPATH/src/github.com/example
cd $GOPATH/src/github.com/example
git clone https://github.com/example/keyserver.git
cd keyserver
make build
sudo cp keyserver /usr/local/bin/
```

For Windows/macOS, use the same Go commands or download pre-built binaries from the releases page.

## Basic Usage

```bash
keyserver --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -mode | Serving mode: http or dns |
| -port | Port to listen on |
| -keys | Path to keys file |
| -bind | Bind address (default: 0.0.0.0) |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Start HTTP server:

```bash
keyserver -mode http -port 8080 -keys keys.json
```

### Example 2: Advanced Usage

Start DNS server:

```bash
keyserver -mode dns -domain attacker.com -keys dns_keys.txt -port 5353
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Encrypted Channel]] Encrypted Channel: Used to serve keys for encrypted C2 communications
- [[Custom Command and Control Protocol]] Connection Proxy: DNS mode can proxy key delivery

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP servers on non-standard ports serving JSON/text files
- DNS servers responding with TXT records containing base64 or hex data
- Network traffic to internal IPs on ports like 8080 with /keys/ paths
- Process monitoring for 'keyserver' binary or Go executables with similar behavior

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Covenant]] (for C2 key management)
- [[tools/DNS-Server-Tools]] (alternative DNS utilities)

## References

- Official GitHub: https://github.com/example/keyserver
- Go documentation for net/http and net packages
