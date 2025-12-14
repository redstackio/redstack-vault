---
data: 'curl -X POST -d ''url=http://example.com'' https://www.apitest.io/request'
tags:
  - ssrf
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.447Z'
id: a88efb7b-acc6-4587-864a-b83ccf312925
verified: false
validated: true
submitted: true
---
# curl-identify-ssrf

## Command

```bash
curl -X POST -d 'url=http://example.com' https://www.apitest.io/request
```

## Description

Sends a POST request to the target form with a test URL to identify if SSRF is possible by checking if the server fetches and returns external content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d 'url=...'` | Data payload with URL parameter | Yes |
| `https://www.apitest.io/request` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://example.com' https://www.apitest.io/request
```

### Advanced Usage

```bash
curl -X POST -d 'url=http://httpbin.org/ip' -v https://www.apitest.io/request
```

## Expected Output

Response body containing content fetched from the provided URL, such as HTML from example.com, indicating SSRF vulnerability.

## Related

- [[Related Procedure]]
