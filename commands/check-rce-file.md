---
data: ls /tmp/rce
tags:
  - verification
  - rce
type: command
output: /tmp/rce (after exploitation)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.186Z'
id: f9248a00-d1e4-4f49-8e32-b9f855a315d5
verified: false
validated: true
submitted: true
---
# check-rce-file

## Command

```bash
ls /tmp/rce
```

## Description

List contents of /tmp/rce to verify RCE by checking if the payload-executed file exists.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/rce | Path | Yes |

## Examples

### Basic Usage

```bash
ls /tmp/rce
```

## Expected Output

No such file or directory (before); /tmp/rce (after)

## Related

- [[commands/start-rails-server]]
