---
id: cmd-uuid-1
data: >-
  import base64

  from urllib.parse import unquote

  import re

  token =
  "BAhbCGkD5+gCVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ1qVh%2FA51yK3Ak6DW5hbm9fbnVtaQH7Og1uYW5vX2RlbmkGOg1zdWJtaWNybyIHJRA6CXpvbmVJIghVVEMGOgZFRkkiCFVUQwY7C1RJdTsGDWpWH8DnXIrcCTsHaQH7OwhpBjsJIgclEDsKQAlJIiFtYW50dWhhY2tlcm9uZTE3MzhAZ21haWwuY29tBjsLVA==--5d75e1da7fbede4b6285f61f758e5dbed8d62604"

  decoded_token = base64.b64decode(unquote(token))

  print(re.findall(rb"[a-zA-Z0-9.\_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
  decoded_token))
tags:
  - decoding
  - pii-extraction
type: command
output: '[b''mantuhackerone1738@gmail.com'']'
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.997Z'
verified: false
validated: true
submitted: true
---
# python-decode-base64-token-extract-email

## Command

```python
import base64
from urllib.parse import unquote
import re
token = "BAhbCGkD5+gCVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ1qVh%2FA51yK3Ak6DW5hbm9fbnVtaQH7Og1uYW5vX2RlbmkGOg1zdWJtaWNybyIHJRA6CXpvbmVJIghVVEMGOgZFRkkiCFVUQwY7C1RJdTsGDWpWH8DnXIrcCTsHaQH7OwhpBjsJIgclEDsKQAlJIiFtYW50dWhhY2tlcm9uZTE3MzhAZ21haWwuY29tBjsLVA==--5d75e1da7fbede4b6285f61f758e5dbed8d62604"
decoded_token = base64.b64decode(unquote(token))
print(re.findall(rb"[a-zA-Z0-9.\_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", decoded_token))
```

## Description

This Python script decodes a URL-encoded Base64 token from an email confirmation URL and extracts embedded email addresses using regex, useful for identifying PII exposure in archived or live application tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `token` | The Base64-encoded token string from the URL | Yes |
| `unquote(token)` | Handles URL percent-encoding in the token | Yes |
| `base64.b64decode` | Performs Base64 decoding to bytes | Yes |
| `re.findall` | Regex pattern to match emails in decoded bytes | Yes |

## Examples

### Basic Usage

```python
import base64
from urllib.parse import unquote
import re
token = "<your_token_here>"
decoded_token = base64.b64decode(unquote(token))
print(re.findall(rb"[a-zA-Z0-9.\_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", decoded_token))
```

### Advanced Usage

For multiple tokens or file input, extend the script to loop over a list:

```python
tokens = ["token1", "token2"]
for token in tokens:
    decoded = base64.b64decode(unquote(token))
    emails = re.findall(rb"[a-zA-Z0-9.\_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", decoded)
    print(emails)
```

## Expected Output

A list of byte-encoded email addresses, e.g., [b'mantuhackerone1738@gmail.com'] or [b'big.dogs1979@gmail.com'].

## Related

- [[procedures/Decode-Base64-Token-to-Extract-Email-PII]]
