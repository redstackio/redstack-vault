---
id: tool-1066410-001
url: 'https://www.postman.com/'
tags:
  - api-testing
  - exploit
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.468Z'
validated: true
submitted: true
---
# Postman

**Status**: Unverified

## Overview

Postman is an API development and testing platform used for sending HTTP requests, ideal for exploiting API misconfigurations like unauthorized Firebase calls.

## Description

Postman allows building, testing, and automating API requests with GUI support for headers, payloads, and authentication. In offensive security, it's used to replicate and manipulate API interactions, such as creating short links with leaked keys.

## Features

- Feature 1: Visual request builder for POST/GET with JSON payloads
- Feature 2: Environment variables for storing keys/secrets
- Feature 3: Collection runner for automated testing

## Installation

### Requirements

- Node.js (optional for CLI)
- Desktop app or web version

### Install Commands

```bash
# Download from official site or use snap
snap install postman
```

## Basic Usage

```bash
postman --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `-v, --version` | Version info |

## Examples

### Example 1: Basic Usage

Create a POST request to Firebase API in the GUI: Set URL, add key in params, JSON body with longDynamicLink.

### Example 2: Advanced Usage

```bash
# CLI example for collection run
newman run collection.json -e env.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Postman user-agent in API requests
- Anomalous POSTs to external APIs from testing IPs

## Related Procedures

- [[procedures/Exploit-Firebase-API-for-Arbitrary-Redirects]]

## Related Tools

- [[tools/curl]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://learning.postman.com/docs/getting-started/introduction/
- Related resources: API security testing guides
