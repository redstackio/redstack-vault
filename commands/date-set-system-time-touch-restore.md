---
id: new-uuid-for-date-command
name: date-set-system-time-touch-restore
type: command
executor: bash
data: |-
  ORIG_TIME=$(date)
  date -s "$_TARGET_DATE"
  touch -a -m $_FILE_NAME
  date -s "$ORIG_TIME"
output: null
created_at: '2023-04-06T03:56:17.808936+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - system-time
verified: true
validated: true
---

# date-set-system-time-touch-restore

## Command

```bash
ORIG_TIME=$(date)
date -s "$_TARGET_DATE"
touch -a -m $_FILE_NAME
date -s "$ORIG_TIME"
```

## Description

Temporarily changes system time to create or update a file with historical timestamps, then restores the original time. Requires root; use for advanced evasion in controlled environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Set system time | Built-in |
| $_TARGET_DATE | Date string (e.g., "2022-10-31 23:59:59") | Yes |
| $_FILE_NAME | File to touch | Yes |
| $ORIG_TIME | Captured original time | Derived |

## Examples

### Basic Usage

```bash
ORIG_TIME=$(date)
date -s "2022-10-31 23:59:59"
touch -a -m example
date -s "$ORIG_TIME"
```

### Advanced Usage

```bash
ORIG_TIME=$(date +%Y-%m-%d\ %H:%M:%S)
date -s "2020-01-01 00:00:00"
touch payload.sh
date -s "$ORIG_TIME"
```

## Expected Output

`date` commands output the new time briefly (e.g., `Mon Oct 31 23:59:59 UTC 2022`). File `stat` shows target time; system logs may note changes.

## Related

- [[procedures/Linux-Timestomping-Evasion]]
