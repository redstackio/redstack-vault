---
id: cmd-curl-parse-test
data: 'curl -v "http://example.com%2Ftest" --trace-ascii -'
tags:
  - curl
  - testing
type: command
output: Trace output showing host parsing without rejection
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.294Z'
verified: false
validated: true
submitted: true
---
# curl-parse-test

## Command

```bash
curl -v "http://example.com%2Ftest" --trace-ascii -
```

## Description

Tests curl's URL parser for acceptance of percent-encoded separators in the host name, revealing CVE-2022-27780 behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `--trace-ascii` | Detailed trace | Yes |
| URL | Malformed URL with %2F in host | Yes |

## Examples

### Basic Usage

```bash
curl -v "http://example.com%2Ftest" --trace-ascii -
```

### Advanced Usage

```bash
curl -v "http://example.com%2Ftest" --trace-ascii - > parse_trace.txt
```

## Expected Output

Verbose trace indicating host parsed as example.com/test without error, showing decoding.

## Related

- [[Related Procedure]]
