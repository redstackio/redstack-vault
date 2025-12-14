---
id: cmd-curl-dot-segments
data: >-
  curl "https://glassdoor.com/Award/../List/some-list" -H "Host: glassdoor.com"
  -v
tags:
  - url-testing
  - parser
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.689Z'
verified: false
validated: true
submitted: true
---
# curl-test-dot-segments

## Command

```bash
curl "https://glassdoor.com/Award/../List/some-list" -H "Host: glassdoor.com" -v
```

## Description

Tests URL parser behavior with dot segments (/../) to detect normalization differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL with /../ | Path including dot segments | Yes |
| `-H "Host: ..."` | Explicit host header | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl "https://glassdoor.com/Award/../List/some-list" -H "Host: glassdoor.com" -v
```

### Advanced Usage

```bash
curl "https://glassdoor.com/Job/../../../Award/some-award" -H "Host: glassdoor.com" -v
```

## Expected Output

Logs indicate cache normalization and backend path processing mismatch.

## Related

- [[Related Procedure: Exploit-URL-Parser-Confusion-with-Dot-Segments]]
