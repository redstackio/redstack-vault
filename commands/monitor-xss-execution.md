---
data: tail -f /path/to/burp/logs | grep 'ks.xss.ht'
tags:
  - xss
  - monitoring
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.327Z'
id: 76884e52-19ec-4819-9c2b-78518f9945ae
verified: false
validated: true
submitted: true
---
# monitor-xss-execution

## Command

```bash
tail -f /path/to/burp/logs | grep 'ks.xss.ht'
```

## Description

Monitors proxy or log files for XHR requests indicating XSS execution to the external domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `tail -f` | Follows log file | Yes |
| `grep 'ks.xss.ht'` | Filters for domain | Yes |

## Examples

### Basic Usage

```bash
tail -f burp_logs.txt | grep 'ks.xss.ht'
```

### Advanced Usage

```bash
tail -f logs | grep -E '(ks.xss.ht|eval)'
```

## Expected Output

Lines showing GET requests to ks.xss.ht upon execution.

## Related

- [[Related Procedure]]
