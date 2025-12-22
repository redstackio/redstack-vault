---
url: null
tags:
  - server
  - custom
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.850Z'
id: 39e18a69-96f4-4ad7-8845-b14e2688e841
validated: true
submitted: true
---
# Custom Kotlin Ktor Server

**Status**: Unverified

## Overview

Local server serving dynamic CSS for exfiltration.

## Description

Built with Ktor to return CSS with attribute selectors logging hits to /hit?char=%s&position=%d.

## Features

- Feature 1: Dynamic CSS generation
- Feature 2: Request logging
- Feature 3: Embedded Netty

## Installation

### Requirements

- Kotlin, Ktor deps

### Install Commands

```bash
# Compile and run in IntelliJ
```

## Basic Usage

```bash
# Run on port 8080
```

### Common Options

| Option | Description |
|--------|-------------|
| Port | Listen port |

## Examples

### Example 1: Basic Usage

Serve CSS endpoint.

### Example 2: Advanced Usage

Log exfil params.

## MITRE ATT&CK Mapping

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Collection]] Collection

## Detection

Local server traffic.

## Related Procedures

- [[procedures/Exfiltrate-2FA-Code-Using-CSS-Selectors]]

## Related Tools

- [[tools/ngrok]]

## References

- Ktor docs
