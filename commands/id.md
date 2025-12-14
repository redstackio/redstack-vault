---
data: id
tags:
  - verification
  - privileges
type: command
output: uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.400Z'
id: 3ef6cd1e-18fe-432c-974a-d0eef5e88a7b
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

Prints user and group IDs to assess RCE privileges.

## Parameters

None.

## Examples

### Basic Usage

```bash
id
```

## Expected Output

uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)

## Related

- [[commands/whoami]]
