---
id: 123e4567-e89b-12d3-a456-426614174010
name: me-sh
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.885Z'
platforms:
  - Web
tags:
  - oauth2
url: null
validated: true
submitted: true
---

# me-sh

**Status**: Unverified

## Overview

Shell script to verify OAuth2 access tokens by querying Vimeo's /me endpoint, returning user info on success or errors on invalidation.

## Description

This tool uses curl with Authorization: Bearer header to fetch current user data, ideal for validating tokens in auth bypass scenarios.

## Features

- Feature 1: Bearer token authentication
- Feature 2: HTTP status checking
- Feature 3: JSON response display

## Installation

### Requirements

- bash and curl

### Install Commands

```bash
# Create or download
wget https://example.com/me.sh
chmod +x me.sh
```

## Basic Usage

```bash
./me.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Help |
| -t, --token | Access token |

## Examples

### Example 1: Basic Usage

```bash
./me.sh d3ac3bb53d1c4ebc3de7d28e4ed801c0
```

### Example 2: Advanced Usage

```bash
./me.sh 9eabdc746910ea39c07395ee1b69a2b9
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- API calls to /me with various tokens
- 401 errors indicating revocation tests

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/getAccessToken-sh]]

## References

- Vimeo API Docs
