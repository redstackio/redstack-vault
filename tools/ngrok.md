---
url: 'https://ngrok.com/'
tags:
  - tunneling
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.853Z'
id: 4b2445bc-1e71-444d-b7ed-f38351253e53
validated: true
submitted: true
---
# ngrok

**Status**: Unverified

## Overview

Tunneling tool for exposing local servers publicly.

## Description

Used to receive CSS exfil requests from victim browser.

## Features

- Feature 1: HTTP/HTTPS tunnels
- Feature 2: Request inspection
- Feature 3: Auth

## Installation

### Requirements

- None

### Install Commands

```bash
# Download binary
./ngrok http 8080
```

## Basic Usage

```bash
ngrok http 8080
```

### Common Options

| Option | Description |
|--------|-------------|
| http | Protocol |

## Examples

### Example 1: Basic Usage

Tunnel port.

### Example 2: Advanced Usage

With subdomain.

## MITRE ATT&CK Mapping

### Techniques

- [[Encrypted Channel]] Encrypted Channel

### Tactics

- [[Command and Control]] Command and Control

## Detection

Outbound to ngrok.io.

## Related Procedures

- [[procedures/Exfiltrate-2FA-Code-Using-CSS-Selectors]]

## Related Tools

- [[Custom Kotlin Ktor Server]]

## References

- ngrok.com
