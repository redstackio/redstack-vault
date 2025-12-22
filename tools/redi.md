---
id: b72b120a-d60e-4c61-aac9-437354bb0796
name: redi
type: tool
verified: true
created_at: '2019-08-28T21:17:27.567336+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - c2
  - redirector
  - nginx
  - cobalt-strike
  - ssl
url: ''
commands:
  - '[[commands/redi-setup-cobalt-strike-redirector]]'
validated: true
---

# redi

**Status**: Unverified

## Overview

Redi is an automated bash script designed for red team operators to quickly set up redirectors for Cobalt Strike command and control (C2) infrastructure. It configures nginx as a reverse proxy to forward traffic to the C2 server while integrating Let's Encrypt for free SSL/TLS certificates, helping to blend malicious traffic with legitimate HTTPS communications.

## Description

In offensive security engagements, especially those involving Cobalt Strike, direct connections to C2 servers can be easily detected and blocked. Redi simplifies the deployment of domain-fronted redirectors by automating nginx installation, configuration, and SSL setup. This tool is particularly useful for operational security (OPSEC) in prolonged red team exercises, allowing attackers to route beacon traffic through what appears to be a normal web server. It supports custom domains and can be run on cloud instances or VPS for rapid deployment.

## Features

- Automated nginx reverse proxy configuration for HTTP/HTTPS traffic
- Integration with Certbot for Let's Encrypt SSL certificate issuance and renewal
- Support for custom target IPs/ports for C2 servers
- Basic firewall adjustments (e.g., opening port 80/443)
- Logging and error handling for troubleshooting setups
- Idempotent runs to allow reconfiguration without reinstallation

## Installation

### Requirements

- Linux distribution with apt package manager (e.g., Ubuntu/Debian, Kali Linux)
- Root or sudo access
- Internet connectivity for domain resolution and certificate issuance
- A registered domain name pointed to the server's IP (DNS A record required)

### Install Commands

```bash
# Clone the repository (assuming GitHub source; adjust if different)
git clone https://github.com/anthemtotheego/Redi.git redi
cd redi

# Make the script executable
chmod +x redi.sh

# Install dependencies (Certbot and nginx)
sudo apt update
sudo apt install -y nginx certbot python3-certbot-nginx
```

On Kali Linux, nginx and certbot are often pre-installed or available via `apt install`.

## Basic Usage

```bash
./redi.sh --help
```

This displays available options, including domain, target, port, and email parameters.

### Common Options

| Option | Description |
|--------|-------------|
| -d, --domain | Specify the domain for the redirector |
| -t, --target | Target IP/hostname for proxying |
| -p, --port | Target port (default: 80) |
| -e, --email | Email for Let's Encrypt |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Set up a redirector for a local C2 server:

```bash
sudo ./redi.sh -d myredirect.com -t 127.0.0.1 -p 8080 -e ops@team.com
```

### Example 2: Advanced Usage

Deploy on a VPS with custom config:

```bash
sudo ./redi.sh -d secure-site.com -t 10.10.10.5 -p 443 -e admin@domain.com
```

After execution, verify with `sudo nginx -t` and `sudo systemctl status nginx`.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Defanged Indicators of Compromise (for masking C2 via proxies)
- [[Internal Proxy]] Proxy (nginx as reverse proxy for C2)

### Tactics

- [[Command and Control]] Command And Control

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of redi.sh or similar scripts in /tmp or user directories
- Nginx configs with unusual upstream targets (e.g., internal IPs on port 8080)
- Certbot logs showing rapid certificate issuances for suspicious domains
- Traffic patterns: High HTTPS to a new domain proxying to non-standard ports
- File artifacts: /etc/nginx/sites-enabled/ with proxy_pass to C2 IPs

## Related Procedures

- [[procedures/Deploy-C2-Infrastructure]]
- [[procedures/Configure-Redirectors-for-OPSEC]]

## Related Tools

- [[tools/Cobalt-Strike]]
- [[tools/Nginx]]
- [[tools/Certbot]]

## References

- Cobalt Strike documentation on redirectors
- Let's Encrypt rate limits and best practices
