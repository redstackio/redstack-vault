---
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - web-exploit
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Web vulnerability scanner and proxy for intercepting and modifying HTTP/S
  traffic
id: 1f5759fa-5be7-4503-b717-a040c97722ad
created_at: '2025-12-13T09:01:26.735Z'
updated_at: '2025-12-13T09:01:26.735Z'
verified: false
validated: true
submitted: true
---
# Burp Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, used for intercepting requests, analyzing responses, and exploiting vulnerabilities like XML wrapping in SAML.

## Description

It includes tools like Proxy, Repeater, and Intruder for manipulating traffic, making it ideal for forging and submitting SAML responses in attacks against GHES.

## Features
- Feature 1: Traffic interception and modification
- Feature 2: Automated vulnerability scanning
- Feature 3: Extensible with plugins for custom exploits

## Installation

### Requirements
- Java Runtime Environment
- Compatible OS

### Install Commands

```bash
# Download from official site and run the installer
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
burp-suite
```

### Example 2: Advanced Usage

```bash
burp-suite --project-file exploit.burp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques
- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Tactics
- [[Initial Access]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:
- Unusual proxy traffic in network logs
- Anomalous HTTP requests to SAML endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools
- [[tools/XML-Editor]]

## References
- Official documentation: https://portswigger.net/burp/documentation
