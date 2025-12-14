---
id: tool-zap
url: 'https://www.zaproxy.org/'
tags:
  - proxy
  - web
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.645Z'
validated: true
submitted: true
---
# ZAP

**Status**: Unverified

## Overview

OWASP ZAP (Zed Attack Proxy) is an open-source web app scanner and proxy for finding vulnerabilities, used here for SSRF testing via request manipulation.

## Description

ZAP proxies traffic, breaks for editing (e.g., injecting %0A in URLs), and supports scripting for automated tests on endpoints like /help_docs.

## Features

- Feature 1: Active/passive scanning
- Feature 2: Request breakpoint
- Feature 3: HUD for in-browser testing

## Installation

### Requirements

- Java 8+

### Install Commands

```bash
# Download and run
java -jar zap.jar
# Or via package manager: apt install zaproxy
```

## Basic Usage

```bash
# Configure proxy to 127.0.0.1:8080
# Use Breakpoints tab
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Help |
| `-cmd` | Command line mode |

## Examples

### Example 1: Basic Usage

Proxy browser traffic.

### Example 2: Advanced Usage

Break, edit URL for AWS metadata, continue.

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Tactics

- [[Discovery]]

## Detection

- Traffic routed through 8080

## Related Procedures

- [[procedures/Access-AWS-Metadata-Existing-Endpoint-via-SSRF]]

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]

## References

- Official documentation: https://www.zaproxy.org/docs/
