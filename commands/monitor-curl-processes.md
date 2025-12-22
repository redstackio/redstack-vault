---
data: >-
  while true;do TEST_VAR=`pgrep -l -f curl | cut -f 1 -d " "` &&  if [ -n
  "$TEST_VAR" ]; then cat /proc/$TEST_VAR/cmdline && echo ; fi; done
tags:
  - monitor
  - automation
type: command
executor: bash
platforms:
  - Linux
id: fb3e4310-2f56-44eb-abdf-d823fee1955d
created_at: '2025-12-14T17:24:19.379Z'
updated_at: '2025-12-14T17:24:19.379Z'
verified: false
validated: true
submitted: true
---
# monitor-curl-processes

## Command

```bash
while true;do TEST_VAR=`pgrep -l -f curl | cut -f 1 -d " "` &&  if [ -n "$TEST_VAR" ]; then cat /proc/$TEST_VAR/cmdline && echo ; fi; done
```

## Description

Bash loop that monitors for curl processes using pgrep, extracts PID with cut, and reads command line from /proc/<pid>/cmdline to capture arguments like --cookie-jar paths for automated exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pgrep -l -f curl | Find processes matching 'curl' with full command | Yes (internal) |
| cut -f 1 -d ' ' | Extract PID from pgrep output | Yes (internal) |
| cat /proc/$TEST_VAR/cmdline | Read null-separated args | Yes (internal) |

## Examples

### Basic Usage

```bash
# Run as-is for continuous monitoring
while true; do ... done
```

### Advanced Usage

```bash
# Add logging
while true; do ... ; echo "$(date): $output" >> curl_log.txt; done
```

## Expected Output

When curl detected: e.g., 1234curl	n--cookie-jar	a	google.com	null

## Related

- [[tools/pgrep]]
- [[procedures/Monitor-Curl-Processes-for-Automation]]
