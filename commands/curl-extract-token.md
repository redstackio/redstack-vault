---
id: cmd-uuid-002
data: >-
  curl "http://target.com/misc.php?action=showpopups&type=friend" | grep -o
  'XOOPS_TOKEN_REQUEST[^<]*'
tags:
  - web-scrape
  - token-extract
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.924Z'
verified: false
validated: true
submitted: true
---
# curl-extract-token

## Command

```bash
curl "http://target.com/misc.php?action=showpopups&type=friend" | grep -o 'XOOPS_TOKEN_REQUEST[^<]*'
```

## Description

Fetches the misc.php page and extracts the XOOPS_TOKEN_REQUEST value using grep for token harvesting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target misc.php URL with params | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/misc.php?action=showpopups&type=friend" | grep -o 'XOOPS_TOKEN_REQUEST[^<]*'
```

### Advanced Usage

```bash
curl "http://target.com/misc.php?action=showpopups&type=friend" | grep -o 'XOOPS_TOKEN_REQUEST[^<]*' | cut -d'=' -f2
```

## Expected Output

XOOPS_TOKEN_REQUEST=abc123def456

## Related

- [[Related Procedure]]
