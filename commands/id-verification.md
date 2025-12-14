---
id: cmd-id
data: id
tags:
  - verification
  - rce
type: command
output: uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.891Z'
verified: false
validated: true
submitted: true
---
# id-verification

## Command

```bash
id
```

## Description

Shows user and group ID information in the RCE shell to verify privileges of the compromised process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | None | No |

## Examples

### Basic Usage

```bash
id
```

## Expected Output

uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)

## Related

- [[commands/whoami-verification]]
