---
data: 'curl -H "Header: Value" http://target.com'
tags:
  - web
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 045ed168-f0a5-48d5-b58b-6400d1fc0b07
created_at: '2025-12-13T09:01:17.271Z'
updated_at: '2025-12-13T09:01:17.271Z'
verified: false
validated: true
submitted: true
---
# Curl HTTP Request

## Command

```bash
curl -H "Header: Value" http://target.com
```

## Description
Sends an HTTP request with custom headers, useful for testing vulnerabilities like request smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Custom header | Yes |
| `url` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://target.com
```

### Advanced Usage

```bash
curl -H "Transfer-Encoding: chunked" http://target.com
```

## Expected Output
HTTP response headers and body.

## Related
- [[procedures/Craft-Multi-line-Transfer-Encoding-Request]]
