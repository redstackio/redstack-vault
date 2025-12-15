---
id: cmd-trurl-parse
data: 'trurl --get ''Host: {host} Zone: {zoneid}'' ''http://[fe80::1%25eth0]/'''
tags:
  - parse
  - url
  - libcurl
type: command
output: 'Host: [fe80::1] Zone: eth0'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.045Z'
verified: false
validated: true
submitted: true
---
# trurl-parse-url

## Command

```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

## Description

Uses trurl as a frontend to libcurl's CURLU API to parse a URL and extract host and zoneid components, verifying the handling of percent-encoded zone IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--get` | Specify output format template | Yes |
| `'Host: {host} Zone: {zoneid}'` | Template for extracted values | Yes |
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

> Extracts only host.

## Expected Output

Host: [fe80::1] Zone: eth0

## Related

- [[commands/run-parserbatch-test]]
