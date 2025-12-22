---
id: 6ba0bee0-c6c3-4f37-abcb-25eb215efdb0
type: tool
verified: true
created_at: '2020-02-20T07:17:13.475860+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - network
  - pivot
  - proxy
  - tunnel
url: 'https://github.com/jpillora/chisel'
commands:
  - '[[commands/chisel-client-reverse-port-forward]]'
  - '[[commands/chisel-server-enable-reverse-tunneling]]'
validated: true
---

# Chisel

**Status**: ✓ Verified

## Overview

Chisel is a fast TCP/UDP tunnel over HTTP, secured with SSH-like authentication. It is written in Go and compiles to a single binary that includes both client and server modes. Chisel is particularly useful for bypassing firewalls by disguising traffic as HTTP, creating secure endpoints into networks, and enabling port forwarding for pivoting during security assessments.

## Description

Chisel transports tunnel traffic over HTTP using WebSockets, making it stealthy and effective for restricted environments. It supports both forward and reverse port forwarding, SOCKS5 proxying, and authentication via username/password or keys. The tool is lightweight, cross-platform, and ideal for red team operations involving network pivoting, C2 infrastructure, or accessing internal services from compromised hosts.

## Features

- Feature 1: HTTP/WebSocket transport for firewall evasion
- Feature 2: Reverse and dynamic (SOCKS5) port forwarding
- Feature 3: Built-in authentication and fingerprint verification
- Feature 4: Multi-platform support (Windows, Linux, macOS, ARM)
- Feature 5: UDP tunneling for DNS or other protocols

## Installation

### Requirements

- Go 1.13 or later (for building from source)
- Network access to download binaries

### Install Commands

For Kali Linux/Ubuntu (download pre-built binary):

```bash
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_linux_amd64.gz
 gunzip chisel_1.9.1_linux_amd64.gz
 chmod +x chisel
 sudo mv chisel /usr/local/bin/
```

For building from source:

```bash
go install github.com/jpillora/chisel@latest
```

For Windows: Download the .exe from GitHub releases and add to PATH.

For cross-compilation (e.g., Windows from Linux):

```bash
export GOOS=windows
 export GOARCH=amd64
go build -o chisel.exe github.com/jpillora/chisel
```

Common GOOS: windows, linux, darwin, android
Common GOARCH: 386, amd64, arm, arm64

## Basic Usage

```bash
chisel --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --version | Display version |
| --auth | Enable authentication (username:password) |
| --fingerprint | Show server fingerprint |
| --keep-alive | Set keep-alive interval |

## Examples

### Example 1: Basic Usage (Server Mode)

Start server with reverse tunneling enabled:

```bash
./chisel server -p :9000 --reverse
```

### Example 2: Advanced Usage (Client SOCKS Proxy)

```bash
./chisel client server.example.com:9000 R:1080:socks
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling
- [[Connection Proxy]] Proxy
- [[Communication Through Removable Media]] Communication Through Removable Media (for binary transfer)

### Tactics

- [[Command and Control]] Command and Control
- [[Lateral Movement]] Lateral Movement

## Detection

- Unusual HTTP/WebSocket traffic to non-standard ports
- Presence of chisel binary or Go-related artifacts
- Anomalous outbound connections with low entropy payloads
- Network logs showing persistent TCP/UDP tunnels
- Process monitoring for chisel.exe or chisel processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Socat]]
- [[tools/Ncat]]

## References

- Official GitHub: https://github.com/jpillora/chisel
- Documentation: https://github.com/jpillora/chisel#usage
