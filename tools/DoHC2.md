---
id: a5a70857-d3ce-42d0-8deb-51de7c571c54
name: DoHC2
type: tool
verified: true
created_at: '2019-08-28T21:17:43Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - c2
  - doh
  - cobalt-strike
  - external-c2
  - command-and-control
url: 'https://github.com/ryanhanson/DoHC2'
commands:
  - '[[commands/dohc2-start-server]]'
  - '[[commands/dohc2-generate-profile]]'
validated: true
---

# DoHC2

**Status**: Unverified

## Overview

DoHC2 is an external command and control (C2) framework that enables DNS over HTTPS (DoH) communication for Cobalt Strike. It leverages the ExternalC2 library to tunnel C2 traffic through encrypted DNS queries, evading traditional network defenses that monitor unencrypted DNS. Commonly used in red team operations for stealthy beaconing in environments with strict outbound filtering.

## Description

DoHC2 integrates with Cobalt Strike by providing a DoH-based external C2 server and malleable profiles. Attackers run the DoHC2 server to handle incoming DNS queries from compromised hosts, which are encoded as DoH POST requests. This allows for bidirectional communication without relying on standard HTTP/HTTPS or DNS protocols that might be blocked or inspected. It's particularly effective for persistence and data exfiltration in air-gapped or heavily monitored networks.

## Features

- Feature 1: Full DoH protocol support for encrypted C2 over DNS (RFC 8484 compliant)
- Feature 2: Integration with Cobalt Strike ExternalC2 for malleable profile generation
- Feature 3: Customizable jitter, sleep, and encoding to mimic legitimate DNS traffic
- Feature 4: TLS certificate management for secure DoH endpoints
- Feature 5: Support for multiple domains and subdomains for traffic obfuscation

## Installation

### Requirements

- Go 1.18 or later
- Cobalt Strike 4.0 or later with ExternalC2 enabled
- TLS certificates (self-signed or CA-issued)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ryanhanson/DoHC2.git
cd DoHC2

# Build the binary
go build -o DoHC2 .

# For Kali/Ubuntu (install Go if needed)
sudo apt update && sudo apt install golang-go

# For Windows (using MSYS2 or WSL)
# Follow Go installation, then build as above
```

## Basic Usage

```bash
./DoHC2 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Enable verbose logging |
| `--config` | Path to configuration file (TOML/JSON) |

## Examples

### Example 1: Basic Usage

Start the server and generate a profile:

```bash
# Start server
./DoHC2 server --cert server.crt --key server.key --listen 0.0.0.0:443 --domain doh.example.com

# In another terminal, generate profile
./DoHC2 profile generate --output dohc2.profile --server-url https://doh.example.com/dns-query --domain example.com
```

### Example 2: Advanced Usage

Configure with jitter and custom user-agent:

```bash
./DoHC2 profile generate --output advanced.profile --server-url https://doh.example.com/dns-query --domain example.com --jitter 30 --user-agent "Cloudflare-DNS/1.0"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (DoH for C2)
- [[Encrypted Channel]] Encrypted Channel (TLS over DNS)
- [[Communication Through Removable Media]] Communication Through Removable Media (adapted for network evasion)

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual DoH traffic volumes to non-standard resolvers (monitor for POST requests to /dns-query endpoints)
- Detection method 2: Anomalous DNS query patterns (high entropy in subdomains, periodic jittered queries)
- Detection method 3: Cobalt Strike process spawning with ExternalC2 loaded; check for DoH library imports in binaries
- Detection method 4: TLS certificate mismatches or self-signed certs on DoH ports (443/TCP)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cobalt Strike]]
- [[dns2tcp]]

## References

- Official GitHub: https://github.com/ryanhanson/DoHC2
- ExternalC2 Documentation: https://github.com/rapid7/cobaltstrike-external-c2
- RFC 8484: DNS over HTTPS
