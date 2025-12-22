---
id: c-curl-test-denied
data: 'curl -X GET "http://internal-service-endpoint?url=http://example.com"'
tags:
  - test
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.917Z'
verified: false
validated: true
submitted: true
---
# curl-test-denied-url

## Command

```bash
curl -X GET "http://internal-service-endpoint?url=http://example.com"
```

## Description

This command tests access to a denied URL through an internal service proxied by Smokescreen, expecting a block from the deny_list.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `url=http://example.com` | The denied domain to test | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://internal-service-endpoint?url=http://example.com"
```

### Advanced Usage

```bash
curl -X GET -v "http://internal-service-endpoint?url=http://example.com" > test.log
```

## Expected Output

HTTP 403 Forbidden or proxy denial message indicating domain block.

## Related

- [[commands/curl-bypass-url]]
- [[procedures/Identify-and-Test-Smokescreen-Deny-List]]
