---
data: cat /n2
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 240224a0-9829-48f0-909a-88647a302e3e
created_at: '2025-12-14T04:08:48.008Z'
updated_at: '2025-12-14T04:08:48.008Z'
verified: false
validated: true
submitted: true
---
# Cat Netstat Output

## Command

```bash
cat /n2
```

## Description

Displays netstat results from host file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /n2 | Output file | Yes |

## Examples

### Basic Usage

```bash
cat /n2
```

## Expected Output

TCP listeners with PIDs.

## Related

- [[commands/append-netstat-to-cmd-script]]
