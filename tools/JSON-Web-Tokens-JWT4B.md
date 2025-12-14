---
id: tool-736522-jwt4b
url: 'https://github.com/PortSwigger/jwt-support'
tags:
  - jwt
  - extension
  - burp-plugin
type: tool
verified: false
platforms:
  - Burp Suite
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.814Z'
validated: true
submitted: true
---
# JSON-Web-Tokens-JWT4B

**Status**: Unverified

## Overview

JWT4B is a Burp Suite extension for handling JSON Web Tokens, providing decode, edit, sign, and verify capabilities directly within Burp for testing token-based vulnerabilities like the authmagic improper validation.

## Description

This plugin integrates into Burp to parse JWTs in requests/responses, allowing easy payload inspection and modification without external tools. In the attack, it's used to alter the 'u' field in the access token during interception, exploiting the module's failure to verify access token integrity.

## Features

- Feature 1: Decode/encode JWT headers, payloads, signatures
- Feature 2: Sign with various algorithms (HS256, etc.)
- Feature 3: Validate token integrity and expiration

## Installation

### Requirements

- Burp Suite Community/Professional

### Install Commands

In Burp: Extender > BApp Store > Search 'JWT Support' > Install.

```bash
# Or manual: Download BApp, load in Extender > Add
```

## Basic Usage

Right-click request in Proxy/Repeater > 'Send to JWT Editor'.

### Common Options

| Option | Description |
|--------|-------------|
| Decode | View token components |
| Sign | Re-sign after edits |

## Examples

### Example 1: Basic Usage

Intercept request, right-click 'token' > JWT Editor > Edit payload > Change 'u' > Apply.

### Example 2: Advanced Usage

Verify signature validity post-modification to confirm bypass.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Burp logs showing JWT extension activity
- Tampered tokens with mismatched payloads/signatures in traffic

## Related Procedures

- [[procedures/Intercept-and-Modify-JWT-Token-Refresh-Request]]

## Related Tools

- [[tools/Burp-Suite]]
- jwt.io (online alternative)

## References

- Official documentation: https://github.com/PortSwigger/jwt-support
- Related resources: JWT.io
