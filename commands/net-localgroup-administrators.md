---
id: 22f6fdfb-35b7-4217-a312-5433d75893b5
name: net-localgroup-administrators
type: command
executor: cmd
data: net localgroup administrators
output: null
created_at: '2023-04-06T03:56:28.627017+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - admin
verified: true
validated: true
---

# net-localgroup-administrators

## Command

```cmd
net localgroup administrators
```

## Description

Lists members of the local Administrators group.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| administrators | Fixed group name | Yes |

## Examples

### Basic Usage

```cmd
net localgroup administrators
```

## Expected Output

```
The request will be processed at a time chosen by the logon server.

Aliases for \\COMPUTERNAME
-------------------------------------------------------------------------------
administrators members
-------------------------------------------------------------------------------
Administrator                  DOMAIN\adminuser
The command completed successfully.
```

Identifies admin users for targeting.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/net-localgroup-list]]
