---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567895
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.880Z'
validated: true
submitted: true
---
# Burp-Suite-Professional

**Status**: Unverified

## Overview

Burp Suite Professional is a comprehensive web vulnerability scanner and proxy tool used for security testing, including CSRF POC generation and parameter extraction.

## Description

It intercepts HTTP traffic, allows manipulation of requests, and aids in crafting exploits like CSRF forms. In this attack, it's used to parse confirmation links and test the HTML POC. Features include repeater for testing POSTs and intruder for fuzzing.

## Features

- Feature 1: Proxy interception for traffic analysis
- Feature 2: Repeater module for request modification
- Feature 3: Decoder for URL parameter extraction

## Installation

### Requirements

- Java 8+ runtime
- 4GB+ RAM

### Install Commands

```bash
# Download from official site and run installer
java -jar burpsuite_pro.jar
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

Launch and configure proxy to intercept browser traffic.

### Example 2: Advanced Usage

Use Repeater: Intercept login request, send to Repeater, modify parameters, and forward.

```bash
# No CLI; GUI-based
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic routed through localhost:8080 (default proxy)
- Unusual HTTP modifications in logs

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP CSRF Guide
