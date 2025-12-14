---
data: >-
  tail -f /var/log/nginx/access.log | grep "GET ?root:x:0:0:root:/root:/bin/bash
  HTTP/1.1" | grep "Lavf/55.48.100"
tags:
  - local-file-read
  - logging
type: command
output: 'Log entry: Malformed GET with file content in query, 400 173'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.196Z'
id: 6384a467-5bd1-47e4-87f7-109675ed39a4
verified: false
validated: true
submitted: true
---
# server-get-local-file-content

## Command

```bash
tail -f /var/log/nginx/access.log | grep "GET ?root:x:0:0:root:/root:/bin/bash HTTP/1.1" | grep "Lavf/55.48.100"
```

## Description

Monitors logs for request leaking /etc/passwd content via concat.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Log path | Access log file | Yes |

## Examples

### Basic Usage

```bash
tail -f access.log | grep "?root:x:"
```

### Advanced Usage

```bash
tail -f /var/log/nginx/access.log | grep "file:///etc/passwd" || grep "root:x:0:0"
```

## Expected Output

Log with query string containing file line, 400 status.

## Related

- [[Related Procedure: Observe-Local-File-Read]]
