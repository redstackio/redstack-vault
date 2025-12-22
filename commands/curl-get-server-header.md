---
id: cmd-uuid-001
data: 'curl -I http://owncloud.com/'
tags:
  - recon
type: command
output: |-
  HTTP/1.1 200 OK
  Server: Apache/2.2.17 (Ubuntu)
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.989Z'
verified: false
validated: true
submitted: true
---
# curl-get-server-header

## Command

```bash
curl -I http://owncloud.com/
```

## Description

Retrieves HTTP response headers from the target to inspect the Server field for Apache version disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | Use HEAD method to fetch headers only | Yes |
| http://owncloud.com/ | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://example.com/
```

### Advanced Usage

```bash
curl -I -k https://example.com/  # For HTTPS with insecure skip
```

## Expected Output

Headers including "Server: Apache/2.2.17", confirming vulnerable version.

## Related

- [[Related Procedure]]
