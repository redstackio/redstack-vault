---
id: tool-calsignature-js-001
name: calSignature-js
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.175Z'
platforms:
  - Linux
  - macOS
  - Windows
  - Browser
tags:
  - signature-generation
  - javascript
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/045/220/7c77c82f6c7b0247597f1e37b0dab9bb7fa5987c/calSignature.js
validated: true
submitted: true
---

# calSignature-js

**Status**: Unverified

## Overview

calSignature.js is a JavaScript script extracted from the Romit app, used to generate authorization signatures for API requests based on apiKey, apiSecret, Location-ID, and additional parameters like PIN and timestamp. It's key for client-side auth in brute-force attacks.

## Description

This tool enables the creation of valid Bearer tokens for Romit API calls without server dependency, exploiting client-side generation. Commonly used in web pentesting for auth bypass scenarios involving signed requests. Features include HMAC-based signing and timestamp integration for replay protection (though ineffective here due to no rate limits).

## Features

- Feature 1: HMAC-SHA256 signature computation using apiSecret
- Feature 2: Integration of PIN, phone, and timestamp into payload
- Feature 3: Output as Bearer token compatible with HTTP headers

## Installation

### Requirements

- Node.js (for CLI use) or browser console
- No additional deps; pure JS

### Install Commands

```bash
# Download script
wget https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/045/220/7c77c82f6c7b0247597f1e37b0dab9bb7fa5987c/calSignature.js

# Or save as file and run with node
node calSignature.js <apiKey> <apiSecret> <locationId> <pin>
```

## Basic Usage

```bash
node calSignature.js
```

### Common Options

| Option | Description |
|--------|-------------|
| `<apiKey>` | Romit API key string |
| `<apiSecret>` | Secret for HMAC |
| `<locationId>` | Wallet/Location UUID |
| `<pin>` | 4-digit PIN guess |

## Examples

### Example 1: Basic Usage

```bash
node calSignature.js ABC123 secret123 loc-uuid 1234
```

Output: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... (Bearer token)

### Example 2: Advanced Usage

Integrate in script:

```bash
TOKEN=$(node calSignature.js $API_KEY $API_SECRET $LOC_ID $PIN)
curl -H "Authorization: Bearer $TOKEN" ...
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Cloud Instance Metadata API]] Credentials from Password Stores (client-side creds)
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for anomalous signature patterns in API logs (e.g., sequential PIN timestamps)
- Detect Node.js or browser console executions generating Romit-specific tokens

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]

## References

- HackerOne Report #75702
- Romit API Documentation (if public)
