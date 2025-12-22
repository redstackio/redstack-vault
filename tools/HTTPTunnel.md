---
id: f90a07af-7dda-4430-af48-7edc68efc62d
type: tool
verified: true
created_at: '2019-08-28T21:17:30.366693+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - tunneling
  - proxy
  - evasion
  - post-exploitation
url: 'http://http-tunnel.sourceforge.net/'
commands:
  - '[[commands/httptunnel-start-standalone-server]]'
  - '[[commands/httptunnel-start-client-portmap]]'
  - '[[commands/httptunnel-start-client-socks]]'
validated: true
---

# HTTPTunnel

**Status**: Unverified

## Overview

HTTPTunnel is a tunneling tool designed to encapsulate network connections within HTTP GET and POST requests, allowing traffic to bypass restrictive firewalls and HTTP proxies. It is commonly used in penetration testing for command and control (C2) communications, data exfiltration, or accessing internal resources from behind corporate firewalls.

## Description

HTTPTunnel operates with two main components: a client (htc) that runs behind the firewall and accepts local connections, and a server (hts) that runs on an external host and translates HTTP requests into actual network connections. The client can function in port-mapping mode to forward specific ports or as a SOCKS v4/v5 proxy for broader application support. Authentication for SOCKS can integrate with fixed user lists, LDAP, or MySQL directories. Configuration is managed via a web-based GUI, and SOCKS proxy cascading is supported. Two server variants exist: a hosted PHP script for web servers and a standalone Perl/Win32 binary for full control.

## Features

- Feature 1: Tunneling over pure HTTP to evade proxy restrictions
- Feature 2: SOCKS v4/v5 proxy support with authentication (LDAP/MySQL)
- Feature 3: Port mapping for direct local-to-remote forwarding
- Feature 4: Web-based GUI for configuration
- Feature 5: Standalone server avoids web host limitations like timeouts

## Installation

### Requirements

- Perl 5 (for script versions)
- Compiler for building from source (if needed)
- For hosted server: PHP-enabled web server

### Install Commands

```bash
# On Ubuntu/Debian (install via apt if available, or download source)
sudo apt update
sudo apt install libwww-perl  # Dependencies for Perl version

# Download and extract source from official site
wget http://http-tunnel.sourceforge.net/releases/httptunnel-3.3.tar.gz
tar -xzf httptunnel-3.3.tar.gz
cd httptunnel-3.3
make
sudo make install

# For Windows: Download pre-built Win32 binaries from SourceForge
```

For Kali Linux, it may be available in repositories or install via the above source build.

## Basic Usage

```bash
hts --help  # Server help
htc --help  # Client help
```

### Common Options

| Option | Description |
|--------|-------------|
| -F | Forward to a program (server) |
| -p | Local port to listen on |
| -s | Server host for client |
| -S | Enable SOCKS mode (client) |
| -A | Authentication source (e.g., LDAP) |

## Examples

### Example 1: Basic Usage

Start server:

```bash
[[commands/httptunnel-start-standalone-server]]
```

Start client for port mapping:

```bash
[[commands/httptunnel-start-client-portmap]]
```

### Example 2: Advanced Usage

Start SOCKS client:

```bash
[[commands/httptunnel-start-client-socks]]
```

Configure via web GUI after starting components.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy (for tunneling through proxies)
- [[Protocol Tunneling]] Protocol Tunneling (HTTP encapsulation)
- [[Communication Through Removable Media]] Communication Through Removable Media (if used with proxies)

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP traffic patterns (e.g., repeated GET/POST with binary data) via proxy logs
- Detection method 2: Network connections to non-standard HTTP ports or unexpected hosts
- Detection method 3: Process monitoring for hts/htc binaries or Perl scripts with HTTP tunneling signatures
- Detection method 4: SOCKS proxy traffic anomalies in firewall logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Socat]]
- [[Ngrok]]

## References

- Official website: http://http-tunnel.sourceforge.net/
- SourceForge repository for downloads and documentation
