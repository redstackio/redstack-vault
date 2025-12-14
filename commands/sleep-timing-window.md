---
data: sleep 0.5
tags:
  - timing
  - race
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.046Z'
id: 3ff9b9aa-5ab5-461b-9f6f-c215a3ac99e1
verified: false
validated: true
submitted: true
---
# sleep-timing-window

## Command

```bash
sleep 0.5
```

## Description

Pauses execution for 0.5 seconds to create a timing window for the TOCTOU swap after curl's initial handshake.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0.5` | Duration in seconds | Yes |

## Examples

### Basic Usage

```bash
sleep 0.5
```

### Advanced Usage

```bash
sleep 1
```

## Expected Output

No output; delays execution by specified time.

## Related

- [[commands/rm-ca-symlink]]
