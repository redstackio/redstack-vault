---
id: 748a953f-e91a-416f-8e83-ba3ce6b9b015
name: cacls-grant-permission
type: command
executor: cmd
data: 'cacls $_PATH /E /G $_USER:F'
output: null
created_at: '2023-04-06T03:56:29.437035+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
platforms:
  - Windows
tags:
  - permissions
  - modification
verified: true
validated: true
---

# cacls-grant-permission

## Command

```cmd
cacls $_PATH /E /G $_USER:F
```

## Description

Grants full control permissions to a user on a file/directory using cacls, enabling write access for service modification in escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH | Target path | Yes |
| $_USER | Username (e.g., currentuser) | Yes |
| /E | Edit existing ACL | Built-in |
| /G | Grant permissions | Built-in |
| F | Full control | Built-in |

## Examples

### Basic Usage

```cmd
cacls C:\example\file.txt /E /G username:F
```

## Expected Output

Permissions updated successfully.

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]
