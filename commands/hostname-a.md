---
id: 98c229ad-59eb-4424-bd56-6e57fae87be8
name: hostname-a
type: command
executor: bash
data: hostname -a
output: null
created_at: '2025-12-11T06:10:13.248Z'
updated_at: '2025-12-11T06:10:13.248Z'
platforms:
  - Linux
tags:
  - shell
  - info
verified: false
validated: true
submitted: true
---

# hostname-a

## Command

```bash
hostname -a
```

## Description

Displays hostname with alias names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Alias names | Yes |

## Examples

### Basic Usage

```bash
hostname -a
```

## Expected Output

web-30-sv-gprd

## Related

- [[commands/id]]
- [[procedures/Verify-Payload-Execution-and-RCE]]
