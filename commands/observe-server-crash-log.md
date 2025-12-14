---
id: cmd-uuid-3
data: >-
  2021-08-11 13:23:04 -0500 Rack app ("GET ///wp1/wp-includes/wlwmanifest.xml" -
  (127.0.0.1)): #<fatal: machine stack overflow in critical region>
tags:
  - dos
  - log
type: command
output: Server crash and zombie state
executor: bash
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.495Z'
verified: false
validated: true
submitted: true
---
# Observe Server Crash Log

## Command

```bash
# Log observation (not executable, but pattern to grep)
grep -i "stack overflow" log/production.log
```

## Description

Monitors for the fatal stack overflow log entry in Puma, indicating successful DoS from recursive response mutation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| grep -i "stack overflow" | Searches logs for error | Yes |
| log/production.log | Log file path | Yes |

## Examples

### Basic Usage

```bash
tail -f log/production.log
```

### Advanced Usage

```bash
grep "machine stack overflow" log/production.log
```

## Expected Output

Log line: "Rack app ... #<fatal: machine stack overflow in critical region>".

## Related

- [[commands/send-repeated-malformed-requests]]
