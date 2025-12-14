---
url: null
tags:
  - oob
  - detection
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.481Z'
id: 5a9e272d-d9aa-4ae3-afd3-2e43de07aca2
validated: true
submitted: true
---
# Burp-Collaborator

**Status**: Unverified

## Overview

Burp Collaborator is an OOB interaction tool integrated with Burp Suite to detect external callbacks like DNS/HTTP requests from exploited vulnerabilities.

## Description

It generates unique domains/URLs for payloads, polling for interactions to confirm exploits like redirects in smuggling attacks, capturing headers with stolen cookies.

## Features

- Feature 1: HTTP and DNS polling
- Feature 2: Detailed interaction logs
- Feature 3: Integration with Burp payloads

## Installation

### Requirements

- Burp Suite installed

### Install Commands

```bash
# Launched from Burp GUI: Burp > Burp Collaborator Client
```

## Basic Usage

```bash
# GUI-based, poll via client interface
```

### Common Options

| Option | Description |
|--------|-------------|
| Poll now | Manual check for interactions |
| Copy URL | Generate payload URL |

## Examples

### Example 1: Basic Usage

Launch client and copy URL for smuggling payload.

### Example 2: Advanced Usage

Poll after exploit to capture request with cookies.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Queries to collaborator-like domains
- Unexpected outbound HTTP from servers

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- PortSwigger documentation
