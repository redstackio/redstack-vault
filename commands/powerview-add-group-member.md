---
id: c064f88a-085e-4bc5-bb1a-4e5a40ed0c54
name: powerview-add-group-member
type: command
executor: powershell
data: Add-DomainGroupMember -Identity '$_GROUP' -Members '$_USER' -Credential $Cred
output: Member added successfully.
created_at: '2020-03-16T01:01:25.836298+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powerview
  - ad
verified: true
validated: true
---

# powerview-add-group-member

## Command

```powershell
Add-DomainGroupMember -Identity '$_GROUP' -Members '$_USER' -Credential $Cred
```

## Description

Adds user to AD group.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity '$_GROUP' | Group name | Yes |
| -Members '$_USER' | User | Yes |
| -Credential $Cred | Creds | No |

## Examples

### Basic Usage

```powershell
Add-DomainGroupMember -Identity 'Domain Admins' -Members 'attacker'
```

## Expected Output

Confirmation of addition.
