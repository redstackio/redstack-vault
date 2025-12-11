---
data: hostname -a
tags:
  - enumeration
type: command
executor: bash
platforms:
  - Linux
id: 3eb953f8-b8cd-46f7-81c1-19a07d6b8dad
created_at: '2025-12-11T06:10:22.427Z'
updated_at: '2025-12-11T06:10:22.427Z'
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

Displays the hostname alias, used in reverse shell to identify the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Alias names | Yes |

## Examples

### Basic Usage

```bash
hostname -a
```

## Expected Output

web-09-sv-gprd

## Related

- [[procedures/Establish-Reverse-Shell-via-Uploaded-PoC]]
