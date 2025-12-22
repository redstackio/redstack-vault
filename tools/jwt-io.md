---
url: 'https://jwt.io'
tags:
  - jwt
  - authentication
type: tool
platforms:
  - Web
description: 'Online tool for decoding, verifying, and generating JWT tokens'
id: 55608e54-33e8-472b-a91b-47799ef83529
created_at: '2025-12-13T09:01:26.678Z'
updated_at: '2025-12-13T09:01:26.678Z'
verified: false
validated: true
submitted: true
---
# jwt.io

**Status**: Unverified

## Overview

jwt.io is a web-based tool for working with JSON Web Tokens (JWTs), allowing users to decode tokens, verify signatures, and generate new tokens for testing purposes in security assessments.

## Description

The tool provides an interactive interface to paste JWTs, view their decoded header and payload, and sign new tokens with provided secrets. It's commonly used in offensive security to analyze and tamper with authentication tokens in web applications.

## Features

- Feature 1: JWT decoding without signature verification
- Feature 2: Token signing with various algorithms (e.g., HMAC, RSA)
- Feature 3: Payload editing and real-time encoding

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation required; access via https://jwt.io.

## Basic Usage

```bash
# Not applicable; web-based tool
```

### Common Options

| Option | Description |
|--------|-------------|
| Paste JWT | Decode existing token |
| Edit Payload | Modify claims and sign |

## Examples

### Example 1: Basic Usage

Paste a JWT string into the interface to decode it.

### Example 2: Advanced Usage

Edit the payload, input a secret, and generate a signed token.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]]
- [[Valid Accounts]]

### Tactics

- [[Initial Access]]
- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for traffic to jwt.io domain
- Detection method 2: Log unusual JWT-related activities in applications

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- Official site: https://jwt.io
- JWT documentation: https://jwt.io/introduction
