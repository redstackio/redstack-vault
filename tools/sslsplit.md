---
type: tool
description: >-
  SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted
  network connections, useful for penetration testing and network forensics.
url: 'https://www.roe.ch/SSLsplit'
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - mitm
  - ssl
  - tls
  - interception
  - penetration-testing
validated: true
---

# sslsplit

**Status**: Unverified

## Overview

sslsplit is a specialized tool for performing man-in-the-middle (MITM) attacks on SSL/TLS encrypted traffic. It transparently intercepts connections via network address translation (NAT) redirection, terminates the SSL/TLS session, logs all transmitted data, and establishes a new connection to the original destination. Commonly used in penetration testing to decrypt and analyze HTTPS traffic, and in forensics to capture network sessions.

## Description

sslsplit intercepts both plain TCP and SSL/TLS connections (including HTTP and HTTPS) over IPv4 and IPv6. For encrypted connections, it generates forged X.509v3 certificates on-the-fly based on the server's subject DN and SAN extension, supporting Server Name Indication (SNI). It handles RSA, DSA, ECDSA keys, and DHE/ECDHE cipher suites. Users can supply existing certificates if private keys are available. Additional features include NULL-prefix CN support, OCSP request denial, and removal of HPKP headers to bypass public key pinning. Setup typically involves iptables for traffic redirection and installing a trusted CA on clients to avoid warnings.

## Features

- Feature 1: Transparent interception of SSL/TLS connections without client modifications (with CA trust).
- Feature 2: On-the-fly certificate forging with SNI support for targeted MITM.
- Feature 3: Logging of decrypted plaintext data to files or FIFOs for analysis.
- Feature 4: Support for HTTP proxy (CONNECT method) and custom protocol filters.
- Feature 5: IPv4/IPv6 compatibility and handling of various cipher suites.

## Installation

### Requirements

- libevent-devel (for event handling)
- OpenSSL-devel (for TLS support)
- libpcap-devel (for packet capture)
- Build tools (gcc, make)

### Install Commands

```bash
# On Ubuntu/Debian (install dependencies)
sudo apt update
sudo apt install build-essential libevent-dev libssl-dev libpcap-dev

# Download and build from source
git clone https://github.com/droe/sslsplit.git
cd sslsplit
./configure
make
sudo make install
```

For Kali Linux, sslsplit is available in repositories:

```bash
sudo apt update
sudo apt install sslsplit
```

## Basic Usage

```bash
sslsplit --help
```

Generate a CA first (see related command), then redirect traffic with iptables:

```bash
sudo iptables -t nat -A PREROUTING -i eth0 --proto tcp --dport 443 -j REDIRECT --to-ports 8443
sslsplit -k ca.key -c ca.crt ssl 0.0.0.0 8443
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -D | Daemonize (run in background) |
| -l <file> | Log connections to file |
| -j <dir> | Use directory for FIFOs |
| -k <key> | CA private key file |
| -c <cert> | CA certificate file |
| -H <dir> | Log HTTP requests to directory |
| -S <dir> | Log SSL session data to directory |

## Examples

### Example 1: Basic Usage

Intercept all SSL traffic on port 443:

```bash
sslsplit -D -l /tmp/conns.log -j /tmp -k ca.key -c ca.crt ssl 0.0.0.0 443
```

### Example 2: Advanced Usage

Intercept via HTTP proxy on port 8080 with separate logs:

```bash
sslsplit -k ca.key -c ca.crt -P /tmp/proxy.log -H /tmp/http -S /tmp/ssl ssl+std 0.0.0.0 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Encrypted Channel]] Encrypted Channel: SSL/TLS

### Tactics

- [[Collection]] Collection
- [[Command and Control]] Command and Control

## Detection

- Unusual self-signed or forged certificates in traffic (monitor for CA mismatches).
- Traffic redirection via iptables/NAT rules (check firewall logs).
- Unexpected connections to local redirect ports (e.g., 8443).
- Log files or FIFOs in /tmp with sslsplit artifacts.
- Network anomalies like increased latency from double encryption.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/mitmproxy]]
- [[Burp Suite]]
- [[tools/Wireshark]]

## References

- Official website: https://www.roe.ch/SSLsplit
- GitHub repository: https://github.com/droe/sslsplit
- Documentation: Included in source or man page after install (`man sslsplit`)
