---
data: curl -i $URL
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.214Z'
id: ebecba5a-ec60-42c8-9b18-443e99248f0c
verified: false
validated: true
submitted: true
---
# curl-browse

## Command

```bash
curl -i $URL
```

## Description

Basic curl command to fetch and inspect HTTP responses, including headers and body, for web reconnaissance and path testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `$URL` | Target URL to browse | Yes |

## Examples

### Basic Usage

```bash
curl -i http://www.example.starbucks.com.sg/
```

### Advanced Usage

```bash
curl -i -L http://www.example.starbucks.com.sg/xxxx
```

## Expected Output

HTTP status, headers, and page body, e.g., 404 with custom message and footer.

## Related

- [[commands/curl-traversal]]
