---
id: cmd-trurl-extract-001
data: 'trurl --get ''Host: {host} Zone: {zoneid}'' ''http://[fe80::1%25eth0]/'''
tags:
  - parse
  - extract
type: command
output: 'Host: [fe80::1] Zone: eth0'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.520Z'
verified: false
validated: true
submitted: true
---
# extract-url-components-with-trurl

## Command

```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

## Description

Uses trurl, a libcurl-based URL manipulation tool, to parse an IPv6 URL and extract host and zoneid components, demonstrating the separation of zone identifier.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--get` | Specify output format template | Yes |
| `'Host: {host} Zone: {zoneid}'` | Template for extracted fields | Yes |
| `'http://[fe80::1%25eth0]/'` | Input URL to parse | Yes |

## Examples

### Basic Usage

```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

### Advanced Usage

```bash
trurl -s 'http://[fe80::1%25eth0]/' --get '{host}'
```

## Expected Output

Host: [fe80::1] Zone: eth0

## Related

- [[commands/run-libcurl-parsing-test]]
