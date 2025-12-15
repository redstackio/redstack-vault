---
url: 'https://portswigger.net/burp/documentation/desktop/repeater'
tags:
  - repeater
  - request-modification
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.791Z'
id: 17e1ad01-978d-4dfc-b1c5-066880a337d7
validated: true
submitted: true
---
# Burp-Repeater

**Status**: Unverified

## Overview

Burp Repeater is a Burp Suite tool for manually sending and modifying HTTP requests, perfect for replaying captured requests with altered headers like cookies to test authentication bypasses.

## Description

Repeater allows precise control over request parameters, enabling testers to paste stolen cookies into new sessions and forward them to the server, simulating attacks like session hijacking.

## Features

- Feature 1: Manual request editing and resending
- Feature 2: Response comparison across sends
- Feature 3: Support for raw HTTP editing

## Installation

### Requirements

- Included in Burp Suite installation
- Java runtime

### Install Commands

```bash
# Launched via Burp Suite GUI; no separate install
java -jar burpsuite_pro_v2023.x.x.jar
```

## Basic Usage

```bash
# In Burp: Right-click intercepted request > Send to Repeater
```

### Common Options

| Option | Description |
|--------|-------------|
| Send | Forward the request once |
| Repeater tabs | Manage multiple requests |
| Raw view | Edit full HTTP message |

## Examples

### Example 1: Basic Usage

Send a captured request to Repeater, modify Cookie header, and send to replay.

### Example 2: Advanced Usage

```bash
# GUI: Paste cookies into header, update CSRF token if needed, send multiple times to test
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Pass the Hash]] Pass the Ticket

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Repeated identical requests from same IP
- Modified headers in server logs

## Related Procedures


## Related Tools

- [[tools/Burp-Proxy]]
- [[tools/Postman]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: Burp Suite extensions
