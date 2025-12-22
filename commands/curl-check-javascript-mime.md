---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: 'curl -I ''https://gitlab.com/vakzz-h1/public/-/raw/master/test.js'''
tags:
  - recon
  - headers
  - mime-check
type: command
output: |-
  HTTP/2 200
  date: Thu, 02 Apr 2020 03:39:57 GMT
  content-type: application/javascript
  ...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:43.805Z'
verified: false
validated: true
submitted: true
---
# curl-check-javascript-mime

## Command

```bash
curl -I 'https://gitlab.com/vakzz-h1/public/-/raw/master/test.js'
```

## Description

This command performs a HEAD request to inspect HTTP headers of a JavaScript file hosted in a GitLab repository, verifying the content-type is application/javascript to enable CSP bypass via self-hosted scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Use HEAD method instead of GET to fetch headers only | Yes |
| URL argument | Target URL of the JS file | Yes |

## Examples

### Basic Usage

```bash
curl -I 'https://gitlab.com/vakzz-h1/public/-/raw/master/test.js'
```

### Advanced Usage

```bash
curl -I -H 'User-Agent: Mozilla/5.0' 'https://example.com/script.js'
```

## Expected Output

Description of what output to expect when the command runs successfully.

HTTP/2 200
server: nginx
content-type: application/javascript
...

## Related

- [[Related Procedure]]
