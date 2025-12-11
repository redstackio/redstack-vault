---
data: id
tags:
  - enumeration
type: command
executor: bash
platforms:
  - Linux
id: cb68317d-a91d-4f1b-b46c-0be119224b4c
created_at: '2025-12-11T06:10:22.431Z'
updated_at: '2025-12-11T06:10:22.431Z'
verified: false
validated: true
submitted: true
---
# id-user-info

## Command

```bash
id
```

## Description

Displays user and group information, used in reverse shell to verify execution context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | N/A | No |

## Examples

### Basic Usage

```bash
id
```

## Expected Output

uid=500(git) gid=500(git) groups=500(git)

## Related

- [[procedures/Establish-Reverse-Shell-via-Uploaded-PoC]]
