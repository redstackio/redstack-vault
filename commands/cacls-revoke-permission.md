---
id: 1409e61c-33c5-4078-a0b3-637472ee0f09
name: cacls-revoke-permission
type: command
executor: cmd
data: cacls $_PATH /E /R $_USER
output: null
created_at: '2023-04-06T03:56:29.437102+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
platforms:
  - Windows
tags:
  - permissions
  - modification
verified: true
validated: true
---

# cacls-revoke-permission

## Command

```cmd
cacls $_PATH /E /R $_USER
```

## Description

Revokes specified user permissions from a file/directory to clean up after granting temporary access during exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH | Target path | Yes |
| $_USER | Username to revoke | Yes |
| /E | Edit existing ACL | Built-in |
| /R | Revoke permissions | Built-in |

## Examples

### Basic Usage

```cmd
cacls C:\example\file.txt /E /R username
```

## Expected Output

Permissions revoked.

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]
