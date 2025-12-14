---
id: tool-uuid-3
url: 'https://github.com/portswigger/burp-jwt-support'
tags:
  - extension
  - jwt
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.251Z'
validated: true
submitted: true
---
# Burp JSON Web Token Extension

**Status**: Unverified

## Overview

This Burp Suite extension provides support for handling JWTs, highlighting requests containing them for easy identification.

## Description

In the Remitly attack, it highlights JWT-bearing requests in green, aiding in pinpointing the correct /password_reset/start endpoint and analyzing token contents during capture and swap.

## Features

- Feature 1: JWT decoding and validation
- Feature 2: Request highlighting
- Feature 3: Payload modification assistance

## Installation

### Requirements

- Burp Suite Professional or Community

### Install Commands

```bash
# In Burp: Extender > BApp Store > Search 'JSON Web Token' > Install
```

## Basic Usage

No CLI; load in Burp Extender tab.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Auto-highlights JWTs |

## Examples

### Example 1: Basic Usage

Load extension; intercept requests—JWTs show in green.

### Example 2: Advanced Usage

Right-click request > 'Decode JWT' for payload inspection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Extension-specific behaviors not directly detectable; infer from Burp usage

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- GitHub: https://github.com/portswigger/burp-jwt-support
