---
data: hostname -a
tags:
  - enumeration
type: command
executor: bash
platforms:
  - Linux
id: d865108e-e089-4264-a128-477387d104e9
created_at: '2025-12-11T03:47:57.970Z'
updated_at: '2025-12-11T03:47:57.970Z'
verified: false
validated: true
submitted: true
---
# hostname-alias

## Command

```bash
hostname -a
```

## Description

Displays the hostname alias of the system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Display alias names | Yes |

## Examples

### Basic Usage

```bash
hostname -a
```

## Expected Output

web-09-sv-gprd

## Related

- [[procedures/Post-Exploitation-System-Enumeration]]
