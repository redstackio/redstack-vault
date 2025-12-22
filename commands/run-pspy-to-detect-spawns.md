---
type: command
executor: bash
data: ./pspy64 -pf -i 1000
platforms:
  - Linux
tags:
  - monitoring
  - process
  - cron
verified: true
validated: true
---

# run-pspy-to-detect-spawns

## Command

```bash
./pspy64 -pf -i 1000
```

## Description

Executes the pspy tool to monitor process and file system events at 1-second intervals, ideal for detecting cron job spawns without root access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Print process events only | No |
| -f | Print file system events | No |
| -i 1000 | Scan interval in milliseconds (1 second) | No (default 100) |

## Examples

### Basic Usage

```bash
./pspy64 -pf -i 1000
```

### Advanced Usage

Background run: nohup ./pspy64 -p > pspy.log &

## Expected Output

Real-time log of events, e.g.:
[2023-04-10 12:00:00] PID: 1234, PPID: 567, CMD: /usr/sbin/crond
[2023-04-10 12:05:00] PID: 2345, PPID: 1234, CMD: /bin/bash /etc/cron.hourly/update

## Related

- [[procedures/Linux-Privilege-Escalation-via-Scheduled-Tasks]]
- [[tools/pspy]]
