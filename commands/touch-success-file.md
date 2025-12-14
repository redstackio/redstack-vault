---
data: touch /tmp/success
tags:
  - rce
  - proof-of-concept
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.471Z'
id: f9b67106-89ee-4cac-b237-255c910f10bf
verified: false
validated: true
submitted: true
---
# touch-success-file

## Command

```bash
touch /tmp/success
```

## Description

Creates an empty file at /tmp/success to demonstrate successful command injection and RCE in the Airflow exploitation scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/success` | Path to the file to create as proof | Yes |

## Examples

### Basic Usage

```bash
touch /tmp/success
```

### Advanced Usage

```bash
touch /tmp/pwned_$(date)
```

## Expected Output

File /tmp/success is created on the filesystem. Verify with `ls -l /tmp/success` showing timestamp and zero size.

## Related

- [[Related Procedure]]
