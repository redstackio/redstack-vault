---
id: 535a2404-714d-434a-9164-a12661fd262b
type: tool
verified: true
created_at: '2019-08-28T21:17:41.523281+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - dos
  - ssl
  - denial-of-service
  - network-attack
url: 'https://github.com/vanhoefm/thc-ssl-dos'
validated: true
---

# thc-ssl-dos

**Status**: Unverified

## Overview

THC-SSL-DOS is a specialized tool for testing the resilience of SSL/TLS servers against denial-of-service (DoS) attacks. It exploits the computational asymmetry in SSL handshakes, where establishing a secure connection demands significantly more processing power from the server (up to 15 times more than the client). By initiating thousands of SSL renegotiations over a single TCP connection, the tool can overload the target server, potentially rendering it unresponsive. This is particularly useful in penetration testing to assess SSL implementation vulnerabilities and server performance under stress.

## Description

THC-SSL-DOS targets the SSL/TLS renegotiation feature, a mechanism allowing clients to renegotiate connection parameters mid-session. The tool abuses this by triggering excessive renegotiations, amplifying the load on the server's CPU and cryptographic resources. This affects virtually all SSL implementations, a known issue since 2003 that has been discussed in security communities but remains exploitable in many environments. It is commonly used in red team exercises to simulate DoS scenarios against web servers, APIs, or any service relying on SSL/TLS. Note that this tool should only be used on systems you own or have explicit permission to test, as it can cause real service disruptions.

## Features

- Exploits SSL renegotiation for amplified DoS impact
- Operates over a single TCP connection to evade rate-limiting
- Supports targeting specific ports and IP addresses
- Configurable connection and renegotiation parameters for customized attacks
- Lightweight and fast, requiring minimal client resources

## Installation

### Requirements

- Linux environment (tested on Debian-based distros like Ubuntu/Kali)
- GCC compiler and make utilities
- libssl-dev for OpenSSL dependencies

### Install Commands

```bash
# Clone the repository
git clone https://github.com/vanhoefm/thc-ssl-dos.git

# Navigate to the directory
cd thc-ssl-dos

# Compile the tool
make

# The binary 'ssl-dos' will be generated in the current directory
```

On Kali Linux, it may be available via apt: `sudo apt install thc-ssl-dos`.

## Basic Usage

```bash
./ssl-dos <target_ip> <target_port>
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage |
| `-c <count>` | Number of renegotiations per connection (default: 30000) |
| `-p <port>` | Target port (default: 443) |
| `-f <file>` | Read targets from a file (one IP:port per line) |
| `-t <threads>` | Number of parallel connections (default: 1) |

## Examples

### Example 1: Basic Usage

Perform a basic SSL DoS attack on a target server:

```bash
./ssl-dos 192.168.1.100 443
```

This initiates renegotiations on port 443 until interrupted (Ctrl+C).

### Example 2: Advanced Usage

Attack multiple targets with increased renegotiations and threads:

```bash
./ssl-dos -c 50000 -t 5 -f targets.txt
```

Where `targets.txt` contains lines like `10.0.0.1:443`.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Direct Network Flood]] Direct Network Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Sudden spikes in SSL/TLS renegotiation requests from a single IP
- High CPU utilization on the server correlated with incomplete SSL handshakes
- Network logs showing repeated TCP connections to port 443 (or custom) with minimal data transfer
- Use tools like Wireshark to inspect for renegotiation packets or server-side monitoring (e.g., Apache/Nginx access logs) for anomalous handshake patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hping3]] (for general network flooding)
- [[tools/slowloris]] (for HTTP DoS attacks)

## References

- Official GitHub Repository: https://github.com/vanhoefm/thc-ssl-dos
- THC Documentation: Included in the tool's README
- Related Research: SSL Renegotiation Attacks (vanhoefm.org)
