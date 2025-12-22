---
id: proc-uuid-2
tags:
  - decoding
  - pii-extraction
  - base64
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/python-decode-base64-token-extract-email]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:18.007Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Decode-Base64-Token-to-Extract-Email-PII

## Summary

This procedure decodes Base64-encoded tokens from email confirmation URLs to extract embedded personally identifiable information (PII), such as user email addresses, demonstrating information disclosure in applications like Omise's dashboard.

## Description

Applications often encode session or confirmation data in Base64 without additional protection, making it trivial to decode and reveal sensitive data like emails. This procedure targets tokens in archived or live URLs, using Python to unquote URL-encoded characters, Base64-decode the payload, and apply regex to identify email patterns. Prerequisites include the raw token string and a Python environment. Outcomes include plaintext PII, enabling risks like user enumeration or phishing.

## Requirements

1. Extracted Base64 token from the confirmation URL
2. Python 3.x installed with standard libraries (base64, urllib.parse, re)
3. Basic scripting knowledge

## Defense

Defensive measures and detection strategies:

- Encrypt or hash PII in tokens instead of plain Base64 encoding
- Use token signing (e.g., JWT with encryption) to prevent tampering/decoding
- Audit logs for unusual decoding attempts or token access patterns

## Objectives

1. Decode the token to access embedded data
2. Extract and validate PII like email addresses
3. Assess exposure impact for reporting

## Instructions

### Step 1: Prepare the Token

**Context**: Isolate the Base64 portion from the full URL and handle any URL encoding.

No command required.

> From the URL, copy the token after /confirm_email/, e.g., "BAhbCGkD5+gCVTog...". Note any % encodings.

### Step 2: Execute Decoding Script

**Context**: Run the Python script to unquote, decode, and search for emails.

**Command** ([[commands/python-decode-base64-token-extract-email]]):
```python
import base64
from urllib.parse import unquote
import re
token = "BAhbCGkD5+gCVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ1qVh%2FA51yK3Ak6DW5hbm9fbnVtaQH7Og1uYW5vX2RlbmkGOg1zdWJtaWNybyIHJRA6CXpvbmVJIghVVEMGOgZFRkkiCFVUQwY7C1RJdTsGDWpWH8DnXIrcCTsHaQH7OwhpBjsJIgclEDsKQAlJIiFtYW50dWhhY2tlcm9uZTE3MzhAZ21haWwuY29tBjsLVA==--5d75e1da7fbede4b6285f61f758e5dbed8d62604"
decoded_token = base64.b64decode(unquote(token))
print(re.findall(rb"[a-zA-Z0-9.\_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", decoded_token))
```

> This script unquotes the token, decodes it to bytes, and uses regex to find email matches. Expected output: [b'mantuhackerone1738@gmail.com'].

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/python-decode-base64-token-extract-email]]

## Tools Used

- [[tools/Python]]

## Tags

- [[decoding]]
- [[pii-extraction]]
