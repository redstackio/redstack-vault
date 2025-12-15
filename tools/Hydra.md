---
id: tool-hydra-001
url: 'https://github.com/vanhauser-thc/thc-hydra'
tags:
  - brute-force
  - password-cracking
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.721Z'
validated: true
submitted: true
---
# Hydra

**Status**: Unverified

## Overview

Hydra is a parallelized login cracker supporting numerous protocols, ideal for brute-forcing web services like HTTP Basic Auth or forms, commonly used in penetration testing to exploit weak credentials on endpoints without rate limits.

## Description

THC-Hydra performs high-speed dictionary attacks against login pages, including WebDAV over HTTP/HTTPS. It supports modules for various auth types and can handle SSL, making it suitable for targeting Nextcloud's vulnerable WebDAV interface. In offensive security, it's used to automate credential guessing where defenses are absent, but ethical use requires authorization.

## Features

- Feature 1: Supports over 50 protocols including HTTP, HTTPS, and form-based auth
- Feature 2: Multi-threaded for fast parallel attempts
- Feature 3: Verbose output and session resumption for long-running attacks

## Installation

### Requirements

- Kali Linux or similar distro (pre-installed on Kali)
- libssl-dev, libssh-dev for compilation

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install hydra

# Or from source
git clone https://github.com/vanhauser-thc/thc-hydra.git
cd thc-hydra
./configure
make
sudo make install
```

## Basic Usage

```bash
hydra -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l username` | Single login name | 
| `-L file` | Login names file | 
| `-p password` | Single password | 
| `-P file` | Passwords file | 
| `-t tasks` | Number of parallel tasks | 
| `-V` | Verbose mode | 

## Examples

### Example 1: Basic Usage

```bash
hydra -l admin -p password target.com http-get /
```

### Example 2: Advanced Usage

```bash
hydra -L users.txt -P pass.txt -t 10 target.com https-post-form "/login:username=^USER^&password=^PASS^:Invalid" -V
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of failed HTTP 401 requests from a single IP in server logs
- Detection method 2: Network IDS alerts on rapid auth attempts (e.g., Snort rules for Hydra signatures)

## Related Procedures

- [[procedures/Exploit-WebDAV-Authentication-Bypass]]

## Related Tools

- [[Medusa]]
- [[Ncrack]]

## References

- Official documentation: https://github.com/vanhauser-thc/thc-hydra
- Related resources: OWASP Brute Force Attack page
