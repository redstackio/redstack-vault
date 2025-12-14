---
url: 'http://www.jwt.io/'
tags:
  - jwt
  - decoder
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:18.990Z'
id: 0d8e415b-6a7a-4c4a-9031-fc1f59ffdb93
validated: true
submitted: true
---
# jwt.io

**Status**: Unverified

## Overview

jwt.io is an online debugger for JSON Web Tokens (JWTs), allowing creation, decoding, and modification of token payloads and headers for testing auth vulnerabilities.

## Description

It provides a UI to input JWTs, view parsed sections (header, payload, signature), and experiment with algorithms/secrets, useful for crafting forged tokens in exploits like this one.

## Features

- Feature 1: Token decoding and validation
- Feature 2: Payload editing
- Feature 3: Library integration examples

## Installation

### Requirements

- Web browser

### Install Commands

```bash
# Web-based, no install
# Access via browser
```

## Basic Usage

```bash
# Open https://jwt.io and paste token
```

### Common Options

N/A (web UI)

## Examples

### Example 1: Basic Usage

Paste JWT into debugger to decode payload.

### Example 2: Advanced Usage

Modify payload, regenerate (without verify) for forgery.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Not directly detectable; monitor for tampered tokens in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]

## References

- Official site: http://www.jwt.io/
