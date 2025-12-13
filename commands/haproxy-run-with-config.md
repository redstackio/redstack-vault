---
data: ./haproxy -f haproxy.cfg -d
tags:
  - run
type: command
executor: bash
platforms:
  - Linux
id: 75e26953-2400-45d2-b0a9-2742f209e504
created_at: '2025-12-13T09:01:22.085Z'
updated_at: '2025-12-13T09:01:22.085Z'
verified: false
validated: true
submitted: true
---
# haproxy Run with Config

## Command

```bash
./haproxy -f haproxy.cfg -d
```

## Description

Runs the compiled HAProxy with a specified configuration file in debug mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Config file | Yes |
| `-d` | Debug mode | No |

## Examples

### Basic Usage

```bash
./haproxy -f haproxy.cfg -d
```

## Expected Output

HAProxy starts running, listening on port 80 with debug output.

## Related

- [[procedures/Compile-and-Setup-HAProxy-Frontend-Proxy]]
- [[tools/HAProxy]]
