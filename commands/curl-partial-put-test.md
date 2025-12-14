---
data: >-
  curl -X PUT --header "Content-Range: bytes 0-0/10" -d "test"
  http://target:8080/upload/testfile.txt -v
tags:
  - exploit
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.456Z'
id: 1c5bce8e-2b77-44f1-87a9-43057afd12e6
verified: false
validated: true
submitted: true
---
# curl-partial-put-test

## Command

```bash
curl -X PUT --header "Content-Range: bytes 0-0/10" -d "test" http://target:8080/upload/testfile.txt -v
```

## Description

Tests partial PUT support by sending a ranged request with partial content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | HTTP PUT method | Yes |
| `--header "Content-Range: bytes 0-0/10"` | Specifies partial range | Yes |
| `-d "test"` | Partial data to send | Yes |
| `http://target:8080/upload/testfile.txt` | Target URL | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -X PUT --header "Content-Range: bytes 0-0/10" -d "test" http://target:8080/upload/testfile.txt -v
```

### Advanced Usage

```bash
curl -X PUT --header "Content-Range: bytes 0-99/100" -d "more data" http://target:8080/upload/file.txt -v
```

## Expected Output

HTTP 200/204 if partial PUT supported; creates temp file.

## Related

- [[Related Procedure]]
