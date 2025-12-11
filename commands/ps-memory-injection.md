---
id: 320c9a1a-440c-4486-a8cd-22768d6d6e4a
name: ps-memory-injection
type: command
executor: bash
data: 'mem = `ps -o rss= -p #{pid}`'
output: null
created_at: '2025-12-11T06:10:13.188Z'
updated_at: '2025-12-11T06:10:13.188Z'
platforms:
  - Linux
tags:
  - injection
  - ruby
verified: false
validated: true
submitted: true
---

# ps-memory-injection

## Command

```bash
mem = `ps -o rss= -p #{pid}`
```

## Description

Executes ps command with interpolated pid, allowing command injection in GetProcessMem.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pid | User-controlled hash for injection | Yes |

## Examples

### Basic Usage

```bash
mem = `ps -o rss= -p #{pid}`
```

## Expected Output

Memory usage or injected command output

## Related

- [[commands/ruby-echo-inject-tmp]]
- [[procedures/Verify-Payload-Execution-and-RCE]]
