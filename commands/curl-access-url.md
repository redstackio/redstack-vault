---
data: 'curl -i https://cortex-ingest.shopifycloud.com/'
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
updated_at: '2025-12-14T17:32:48.356Z'
id: 95c9a886-9602-4e09-8ab8-c3719734b6f0
verified: false
validated: true
submitted: true
---
# curl-access-url

## Command

```bash
curl -i https://cortex-ingest.shopifycloud.com/
```

## Description

Accesses the root URL of the target Cortex server to check for exposed interface, including headers for status and content type.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `https://...` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -i https://cortex-ingest.shopifycloud.com/
```

### Advanced Usage

```bash
curl -i -v https://cortex-ingest.shopifycloud.com/  # Verbose output
```

## Expected Output

HTTP/1.1 200 OK
Content-Type: text/html

[HTML or API response showing Cortex interface]

## Related

- [[Related Procedure]]
