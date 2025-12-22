---
id: 9d2122d9-a475-4994-851f-2f0c9537aad0
name: net-localgroup-list
type: command
executor: cmd
data: net localgroup
output: null
created_at: '2023-04-06T03:56:28.626930+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - groups
verified: true
validated: true
---

# net-localgroup-list

## Command

```cmd
net localgroup
```

## Description

Lists all local groups on the system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all local groups | Yes |

## Examples

### Basic Usage

```cmd
net localgroup
```

## Expected Output

```
The request will be processed at a time chosen by the logon server.

Aliases for \\COMPUTERNAME
-------------------------------------------------------------------------------
*Administrators               *Power Users
*Backup Operators             *Remote Desktop Users
...
The command completed successfully.
```

Shows group names; use net localgroup <group> for members.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/net-localgroup-administrators]]
