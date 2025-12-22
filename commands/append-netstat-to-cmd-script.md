---
data: echo "sudo netstat -tanp > $host_path/n2" >> /cmd
tags:
  - scripting
type: command
executor: bash
platforms:
  - Linux
id: 98fef177-7fb7-4e55-ba4e-8662478916c9
created_at: '2025-12-14T04:08:48.034Z'
updated_at: '2025-12-14T04:08:48.034Z'
verified: false
validated: true
submitted: true
---
# Append Netstat to Cmd Script

## Command

```bash
echo "sudo netstat -tanp > $host_path/n2" >> /cmd
```

## Description

Adds netstat command to script for root PID discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $host_path/n2 | Output file | Yes |

## Examples

### Basic Usage

```bash
echo "sudo netstat -tanp > $host_path/n2" >> /cmd
```

## Expected Output

Command appended.

## Related

- [[commands/create-cmd-script-shebang]]
