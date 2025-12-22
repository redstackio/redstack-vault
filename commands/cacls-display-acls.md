---
id: 8f47d125-9647-4446-aaf3-a534c9e286cf
name: cacls-display-acls
type: command
executor: cmd
data: cacls $_PATH
output: null
created_at: '2023-04-06T03:56:29.436974+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
platforms:
  - Windows
tags:
  - permissions
  - acl
verified: true
validated: true
---

# cacls-display-acls

## Command

```cmd
cacls $_PATH
```

## Description

Displays ACLs for files/directories using the legacy cacls tool, alternative to icacls for permission auditing in privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH | Target file or directory (e.g., C:\\example\\file.txt) | Yes |

## Examples

### Basic Usage

```cmd
cacls C:\example\file.txt
```

## Expected Output

C:\example\file.txt BUILTIN\Users:(OI)(CI)(RX)

Shows read/execute for Users group.

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]
