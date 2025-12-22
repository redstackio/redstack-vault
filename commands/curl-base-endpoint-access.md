---
data: 'curl -i http://51.83.253.82/item/default'
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.346Z'
id: 54d7d101-8694-4fc8-ba02-40435862261e
verified: false
validated: true
submitted: true
---
# curl-base-endpoint-access

## Command

```bash
curl -i http://51.83.253.82/item/default
```

## Description

Sends a GET request to the base /item/default endpoint to verify normal 200 OK response and establish baseline behavior for SQL injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in output | Yes |
| `http://51.83.253.82/item/default` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -i http://51.83.253.82/item/default
```

### Advanced Usage

```bash
curl -i -H "User-Agent: Mozilla/5.0" http://51.83.253.82/item/default
```

## Expected Output

HTTP/1.1 200 OK followed by headers and HTML content for skin editing page.

## Related

- [[Related Procedure: Access-Base-Endpoint-for-Normal-Behavior]]
