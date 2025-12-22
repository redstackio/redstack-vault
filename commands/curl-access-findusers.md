---
id: cmd-uuid-001
data: 'curl -i "http://target.com/include/findusers.php"'
tags:
  - web-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.926Z'
verified: false
validated: true
submitted: true
---
# curl-access-findusers

## Command

```bash
curl -i "http://target.com/include/findusers.php"
```

## Description

Probes the ImpressCMS findusers.php endpoint without authentication to check for access restrictions. The -i flag includes HTTP headers in output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| URL | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -i "http://target.com/include/findusers.php"
```

### Advanced Usage

```bash
curl -i -s "http://target.com/include/findusers.php" > response.txt
```

## Expected Output

HTTP/1.1 200 OK or 403 Forbidden, with body showing error or empty results.

## Related

- [[Related Procedure]]
