---
id: cmd-curl-transpose-demo
data: 'curl -v "http://example.com%2F127.0.0.1/" --trace-ascii -'
tags:
  - curl
  - demo
type: command
output: 'Trace showing transposed URL: host example.com, path /127.0.0.1/'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.271Z'
verified: false
validated: true
submitted: true
---
# curl-transpose-demo

## Command

```bash
curl -v "http://example.com%2F127.0.0.1/" --trace-ascii -
```

## Description

Demonstrates URL host transposition due to percent-decoding in curl parser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose | Yes |
| `--trace-ascii` | Trace output | Yes |
| URL | URL with %2F before target host | Yes |

## Examples

### Basic Usage

```bash
curl -v "http://example.com%2F127.0.0.1/" --trace-ascii -
```

### Advanced Usage

```bash
curl -v "http://example.com%2F127.0.0.1/" --trace-ascii - | grep URL
```

## Expected Output

Trace with effective URL http://example.com/127.0.0.1/, host altered.

## Related

- [[Related Procedure]]
