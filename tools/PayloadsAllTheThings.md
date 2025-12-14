---
id: tool-payloadsallthethings
url: >-
  https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery
tags:
  - ssrf
  - payloads
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.031Z'
validated: true
submitted: true
---
# PayloadsAllTheThings

**Status**: Unverified

## Overview

PayloadsAllTheThings is a comprehensive GitHub repository providing a collection of payloads, scripts, and techniques for various web vulnerabilities, including Server-Side Request Forgery (SSRF). It serves as a reference for security researchers and pentesters to quickly access tested payloads for exploitation scenarios like IPv6 embedding bypasses in SSRF attacks.

## Description

This tool is not an executable application but a curated knowledge base of payloads organized by vulnerability type. The SSRF section includes examples for bypassing filters using techniques such as IPv6 address embedding, decimal/hex IP encodings, and cloud metadata service accesses. It's commonly used in offensive security operations to prototype attacks without building payloads from scratch, accelerating vulnerability discovery and exploitation in web applications like Infogram's API.

## Features

- Feature 1: Extensive SSRF payload list, including IPv6-to-IPv4 mappings for localhost bypass
- Feature 2: Coverage of multiple bypass techniques (e.g., URL shorteners, redirects)
- Feature 3: Integration-friendly format for tools like Burp Suite or custom scripts

## Installation

### Requirements

- Git installed on the system
- Basic file system access for cloning

### Install Commands

```bash
# Clone the repository
git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git
cd PayloadsAllTheThings
```

## Basic Usage

```bash
# Browse SSRF payloads
ls Server\ Side\ Request\ Forgery/
cat Server\ Side\ Request\ Forgery/Payloads.md
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | This is a static repo; no CLI options |
| Git commands | Standard git for updates (e.g., git pull) |

## Examples

### Example 1: Basic Usage

```bash
# View SSRF payloads
cat PayloadsAllTheThings/Server\ Side\ Request\ Forgery/README.md
```

This displays an overview of SSRF techniques, including IPv6 embedding examples like [0:0:0:0:0:ffff:127.0.0.1].

### Example 2: Advanced Usage

```bash
# Extract specific payload for testing
grep -i "ipv6" PayloadsAllTheThings/Server\ Side\ Request\ Forgery/Payloads.md
```

Use the output to construct requests, e.g., integrating into curl for Infogram testing.

## Expected Output

Text files containing payload lists; no runtime output as it's a reference repo.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Git clone activity to the PayloadsAllTheThings repository in logs
- Presence of cloned repo files in pentest environments
- Usage patterns in scripts referencing payload files

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/curl]]

## References

- Official GitHub: https://github.com/swisskyrepo/PayloadsAllTheThings
- SSRF-specific: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery
