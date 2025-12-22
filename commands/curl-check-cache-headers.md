---
id: cmd-curl-cache-headers
data: 'curl -I "https://glassdoor.com/Award/some-award" -v'
tags:
  - cache
  - headers
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.688Z'
verified: false
validated: true
submitted: true
---
# curl-check-cache-headers

## Command

```bash
curl -I "https://glassdoor.com/Award/some-award" -v
```

## Description

Inspects HTTP headers to evaluate caching rules on static-like endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Head request only | Yes |
| URL | Target endpoint | Yes |
| `-v` | Verbose | Yes |

## Examples

### Basic Usage

```bash
curl -I "https://glassdoor.com/Award/some-award" -v
```

### Advanced Usage

```bash
curl -I "https://glassdoor.com/Award/some-award?var=1" -v
```

## Expected Output

Headers like Cache-Control: public, max-age=600, no strict Vary.

## Related

- [[Related Procedure: Abuse-Relaxed-Cache-Rules-on-Static-Pages]]
