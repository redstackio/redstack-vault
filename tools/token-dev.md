---
id: tool-001
url: 'https://token.dev'
tags:
  - jwt
  - token-generation
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.858Z'
validated: true
submitted: true
---
# token.dev

**Status**: Unverified

## Overview

token.dev is an online JWT generator and debugger, used in security testing to create custom tokens for exploitation, particularly unsigned ones for bypass scenarios.

## Description

This web-based tool allows users to encode/decode JWTs, set payloads, and generate tokens without signatures, ideal for testing auth vulnerabilities like in WordPress plugins.

## Features

- Feature 1: Custom payload editing (e.g., add 'email' field)
- Feature 2: Token encoding/decoding
- Feature 3: Algorithm selection (e.g., HS256, none for unsigned)

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation needed; access via browser.

## Basic Usage

```bash
# Open in browser
https://token.dev
```

### Common Options

| Option | Description |
|--------|-------------|
| Payload Editor | JSON input for custom claims |
| Algorithm | Select 'none' for unsigned |
| Generate | Button to create token |

## Examples

### Example 1: Basic Usage

Enter payload {"email": "target@example.com"}, select no signing, click Generate. Copy output token.

### Example 2: Advanced Usage

Set expiration (exp) and issued-at (iat) timestamps for validity window.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to token.dev from testing environments
- Presence of freshly generated JWTs in logs

## Related Procedures

- [[procedures/Generate-Unsigned-JWT-Token]]
- [[procedures/Create-Arbitrary-User-Account]]

## Related Tools

- [[jwt.io]]

## References

- Official site: https://token.dev
- JWT RFC: https://tools.ietf.org/html/rfc7519
