---
data: id
tags:
  - linux
type: command
executor: bash
platforms:
  - Linux
id: 8b4cbcf5-f699-44d4-b829-ec7a6135e11b
created_at: '2025-12-11T06:10:23.103Z'
updated_at: '2025-12-11T06:10:23.103Z'
verified: false
validated: true
submitted: true
---
# id

## Command

```bash
id
```

## Description

Displays the user ID inside a compromised container to confirm root access.

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

uid=0(root) gid=0(root) groups=0(root)

## Related

- [[commands/ls]]
- [[procedures/Gain-Root-Shell-in-Kubernetes-Containers-Using-Service-Account-Token]]
