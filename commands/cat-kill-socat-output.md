---
data: cat /k2
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 24c5f34d-a6ab-43f8-87a3-279c2019e87e
created_at: '2025-12-14T04:08:48.001Z'
updated_at: '2025-12-14T04:08:48.001Z'
verified: false
validated: true
submitted: true
---
# Cat Kill Socat Output

## Command

```bash
cat /k2
```

## Description

Displays socat error logs from host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /k2 | Error file | Yes |

## Examples

### Basic Usage

```bash
cat /k2
```

## Expected Output

Any errors from kill/socat.

## Related

- [[commands/append-kill-and-socat-to-cmd-script]]
